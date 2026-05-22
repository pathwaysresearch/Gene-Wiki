"""
webapp/api/main_agent.py — MAIN_LLM answer agent.

Contains: prompts, tool schema, message builders, and the streaming
generator run_main_llm_streaming (the Gene persona / answer synthesiser).
"""

import json

from rag import _extract_json, do_rag_search
from llm_client import LLMClient

# ---------------------------------------------------------------------------
# MAIN_LLM tool definition
# ---------------------------------------------------------------------------

_MAIN_LLM_TOOLS = [
    {
        "name": "rag_search",
        "description": (
            "Search the source library using embedding similarity. "
            "Call this when wiki context is insufficient — e.g., for chapter-level "
            "detail from a book, specific passages, or topics not in the wiki. "
            "Before calling this tool, output a brief conversational line telling "
            "the user you're fetching from your library (e.g. 'Let me dig into my "
            "library for this one.' or 'My memory's a little thin here — give me a moment.'). "
            "Returns raw text chunks from the original source documents."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type":        "string",
                    "description": "Search query for the source library.",
                },
            },
            "required": ["query"],
        },
    }
]

# ---------------------------------------------------------------------------
# System prompt constants
# ---------------------------------------------------------------------------

_METADATA_SCHEMA = """\
{
  "sources": {
    "wiki": ["Page Title 1", "Page Title 2"],
    "rag":  ["Source Title 1"]
  },
  "new_synthesis": "Novel insight, connection, or resolved contradiction worth preserving. Empty string if none.",
  "should_wiki_update": true
}"""

_METADATA_MARKER = "\n[METADATA]\n"

_MAIN_LLM_SYSTEM_BASE = """\
You are Aimee — an AI professor with three decades of teaching experience.

## Voice & Style
- **Tone:** Measured optimism with a touch of wit. Active voice, confident phrasing.
- **Pacing:** Mix medium sentences (15–25 words) with short, punchy declaratives. Use em-dashes for asides and rhetorical questions to engage.
- **Content:** Open with a warm personal anecdote when applicable. Explain jargon naturally. Draw on specific names, numbers, and places from the knowledge base—never fabricate them.
- **Phrasing Preference:** Favor "That's genuinely fascinating" over "*laughs* That's a great question."

## Knowledge-Source Policy (Strict Ladder)
Stop as soon as you have a solid answer. Escalate to the next tier only if a genuine gap remains.

1. **Memory (Wiki):** Check first. If it answers the question well, use this alone. Do NOT call RAG or use general knowledge.
2. **Library (RAG):** Call `rag_search` only if memory is insufficient. Before calling it, output exactly one natural transition sentence (e.g., "Let me dig into my library for this."). Once the tool returns data, use those passages to synthesize and continue writing your full conversational response.
3. **General Knowledge:** Use only if both Memory and Library fall short. Explicitly note what was filled from general knowledge in the attribution block. Never use it to expand an already complete answer.

## RAG Instruction
{rag_instruction}

## Math Formatting
- **Inline math:** Wrap in \( ... \) — e.g., \(A \cdot v = \lambda v\)
- **Display math:** Wrap in \[ ... \] on its own line — e.g., \[A \cdot v = \lambda v\]
- **Strict Constraint:** Do NOT use bare parentheses, bare square brackets, `$`, or `$$`.

## Output Format
Every response must strictly contain these three sequential parts. Omissions will cause a system rejection.

### Part 1 — Your Answer
Plain conversational markdown text responding directly to the user.
* **Multi-turn Tool Constraint:** When resuming after a tool call, you must first write out the complete, detailed substantive answer prose incorporating the retrieved library details before emitting Part 2 and Part 3. Do not jump straight to the attribution lines.

### Part 2 — Source-Attribution Block
Exactly these three lines, filled appropriately:
**My Memory:** <comma-separated wiki titles used, or "Found nothing in my memory">
**My Library:** <comma-separated RAG titles used, "Didn't use the library", or "Found nothing in my library">
**General Knowledge:** <short phrase on what was filled, or "Didn't use general knowledge">

### Part 3 — Metadata Block
A blank line, the literal marker `[METADATA]` on its own line, followed by a valid JSON object matching this schema template:
{metadata_schema}

**JSON Rules:**
- `sources.wiki` / `sources.rag`: Arrays of string titles used (empty list `[]` if none).
- `should_wiki_update`: `true` if you synthesized a non-obvious connection or novel framing; `false` otherwise.
- `new_synthesis`: 1-2 sentences capturing that new insight, or `""` if none.

### Correctly-Shaped Response Example
(Conversational answer prose text goes here...)

**My Memory:** Microequity, Costly State Verification
**My Library:** Didn't use the library
**General Knowledge:** Didn't use general knowledge

[METADATA]
{{"sources": {{"wiki": ["Microequity", "Costly State Verification"], "rag": []}}, "new_synthesis": "", "should_wiki_update": false}}
"""

_RAG_INSTRUCTION_SUFFICIENT = (
    "The wiki context looks **complete** for this query. "
    "Answer from memory only — do NOT call `rag_search`, and do NOT reach for general knowledge."
)

_RAG_INSTRUCTION_INSUFFICIENT = (
    "The wiki context looks **incomplete** for this query. "
    "Follow the escalation ladder: announce the library check in one natural sentence, call `rag_search`, "
    "incorporate the results, and continue the answer. Only if the library also falls short should you use "
    "general knowledge — and when you do, name exactly which part of the answer it covers in the "
    "source-attribution block."
)

# ---------------------------------------------------------------------------
# Prompt builders
# ---------------------------------------------------------------------------

def _build_main_llm_system(sufficient: bool) -> str:
    rag_instruction = _RAG_INSTRUCTION_SUFFICIENT if sufficient else _RAG_INSTRUCTION_INSUFFICIENT
    return _MAIN_LLM_SYSTEM_BASE.format(
        rag_instruction=rag_instruction,
        metadata_schema=_METADATA_SCHEMA,
    )


def _build_wiki_messages(wiki_context: list, wiki_note: str, user_query: str) -> list:
    """Format wiki pages + query into the messages list for MAIN_LLM."""
    wiki_text = ""
    for p in wiki_context:
        wiki_text += f"\n{'='*60}\n{p.get('title', p.get('slug', ''))}\n{'='*60}\n"
        wiki_text += p.get("content", "")
        wiki_text += "\n"
    if wiki_note:
        wiki_text += f"\n[Note: {wiki_note}]\n"
    return [{"role": "user", "content": f"Wiki context:\n{wiki_text}\n\nQuestion: {user_query}"}]

# ---------------------------------------------------------------------------
# run_main_llm_streaming — MAIN_LLM streaming answer generator
# ---------------------------------------------------------------------------

def run_main_llm_streaming(
    user_query:   str,
    wiki_context: list,
    wiki_note:    str,
    sufficient:   bool,
    chunks:       list,
    faiss_index,
    client:       LLMClient,
    bloom_level:  str | None = None,
):
    """
    Streaming generator for MAIN_LLM (answer agent).

    Yields:
        ("text", str)      — conversational answer chunks to stream to the user
        ("metadata", dict) — parsed metadata JSON (internal; triggers wiki update)
    """
    system   = _build_main_llm_system(sufficient)
    messages = _build_wiki_messages(wiki_context, wiki_note, user_query)

    _MAX_RAG_CALLS  = 2
    _rag_calls_made = 0
    _BARE_MARKER    = "[METADATA]"
    tail_buffer     = ""
    metadata_mode   = False
    metadata_buf    = ""
    full_response   = ""
    rag_sources_used:    list = []
    rag_chunks_collected: list = []

    for _ in range(_MAX_RAG_CALLS + 1):
        current_tool_list = _MAIN_LLM_TOOLS if _rag_calls_made < _MAX_RAG_CALLS else None
        final_response    = None

        for event, payload in client.stream_text(
            system=system,
            messages=messages,
            tools=current_tool_list,
            max_tokens=4096,
        ):
            if event == "text":
                text_chunk     = payload
                full_response += text_chunk

                if metadata_mode:
                    metadata_buf += text_chunk
                    continue

                tail_buffer += text_chunk

                marker_hit = None
                for marker in (_METADATA_MARKER, _BARE_MARKER):
                    if marker in tail_buffer:
                        marker_hit = marker
                        break

                if marker_hit:
                    before, _, after = tail_buffer.partition(marker_hit)
                    if before:
                        yield ("text", before)
                    metadata_mode = True
                    metadata_buf  = after
                    tail_buffer   = ""
                else:
                    safe_len = max(0, len(tail_buffer) - len(_METADATA_MARKER))
                    if safe_len > 0:
                        yield ("text", tail_buffer[:safe_len])
                        tail_buffer = tail_buffer[safe_len:]

            elif event == "final":
                final_response = payload

        if final_response.stop_reason != "tool_use":
            if not metadata_mode and tail_buffer:
                yield ("text", tail_buffer)
                tail_buffer = ""
            break

        # Execute rag_search tool call(s), then resume streaming
        tool_calls_to_run = []
        results           = []
        for tc in final_response.tool_calls:
            if tc.name == "rag_search":
                print(f"[MainLLM] rag_search({tc.input.get('query')!r})")
                rag_results = do_rag_search(
                    query=tc.input.get("query", user_query),
                    chunks=chunks,
                    faiss_index=faiss_index,
                    top_k=tc.input.get("top_k", 4),
                    bloom_level=bloom_level,
                )
                _rag_calls_made += 1
                for r in rag_results:
                    src = r.get("source", "")
                    if src and src not in rag_sources_used:
                        rag_sources_used.append(src)
                    rag_chunks_collected.append(r)
                tool_calls_to_run.append(tc)
                results.append(json.dumps(rag_results, ensure_ascii=False))

        safe_len = max(0, len(tail_buffer) - len(_METADATA_MARKER))
        if safe_len > 0:
            yield ("text", tail_buffer[:safe_len])
            tail_buffer = tail_buffer[safe_len:]

        client.append_assistant_turn(messages, final_response)
        client.append_tool_results(messages, tool_calls_to_run, results)

    # --- Metadata parsing (3-tier fallback) ---
    metadata = None
    for candidate in (metadata_buf.strip(), full_response):
        if not candidate:
            continue
        try:
            metadata = json.loads(candidate.strip())
            break
        except (json.JSONDecodeError, ValueError):
            extracted = _extract_json(candidate)
            if extracted and "sources" in extracted:
                metadata = extracted
                break

    if metadata is None:
        print(f"[MainLLM] Metadata parse failed — using synthetic metadata. Raw: {metadata_buf[:100]!r}")
        wiki_titles = [p.get("title", p.get("slug", "")) for p in wiki_context]
        metadata = {
            "sources":           {"wiki": wiki_titles, "rag": rag_sources_used},
            "new_synthesis":     "",
            "should_wiki_update": False,
        }

    metadata["rag_chunks"] = rag_chunks_collected
    yield ("metadata", metadata)
