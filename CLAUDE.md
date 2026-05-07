# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

**Danny** — a dual-LLM knowledge chatbot for a domain expert (currently Prof. Deepa Mani, ISB). Two Claude agents collaborate on every query: one navigates and maintains the wiki (WIKI_LLM, Sonnet), one synthesises the answer (MAIN_LLM, Opus). Source knowledge lives in two tiers: a structured wiki (`Vault/wiki/`) and a FAISS-backed RAG database (`data/chunks.json`).

Deployed as: **Flask backend on Google Cloud Run** + **static frontend on Vercel**.

---

## Commands

### Local dev server
```bash
pip install -r requirements.txt
cp .env.example .env          # fill ANTHROPIC_API_KEY, GEMINI_API_KEY, GITHUB_TOKEN
python webapp/api/index2.py --serve
# Open http://localhost:5001
```

### Interactive REPL (no browser)
```bash
python webapp/api/index2.py
```

### Single query
```bash
python webapp/api/index2.py --query "What is microequity?"
```

### Rebuild graph / wiki index
```bash
python webapp/api/index2.py --rebuild-graph
python webapp/api/index2.py --build-wiki-index
```

### Ingest workflow (run in order when adding new source material)
```bash
python scripts/ingest.py --scan                         # preview new files
python scripts/ingest.py --process-all                  # chunk + embed into data/chunks.json
python scripts/tag_blooms.py                            # tag new chunks (skips already-tagged)
python scripts/extract_entities.py --all                # LLM-generate wiki concept/entity pages
python scripts/auto_wiki_builder.py --all               # generate stub pages + rebuild index.md
python scripts/export_for_web.py                        # build FAISS indices → webapp/data/
```

`export_for_web.py` is **always the last step** before committing — it builds everything the Docker image needs.

### Graph CLI
```bash
python scripts/graph.py --build
python scripts/graph.py --stats
python scripts/graph.py --traverse <slug>
```

### Bloom's taxonomy tagging
```bash
python scripts/tag_blooms.py                  # tag only untagged chunks
python scripts/tag_blooms.py --reset          # strip all bloom tags, re-tag from scratch
python scripts/tag_blooms.py --rethreshold    # recompute labels from stored confidences
                                              # (no inference — instant; edit BLOOMS_TUNED_THRESHOLDS first)
```

### Docker (local)
```bash
cd webapp
docker build -t danny-backend .
docker run -p 8080:8080 -e ANTHROPIC_API_KEY=... -e GEMINI_API_KEY=... -e GITHUB_TOKEN=... danny-backend
```

---

## Architecture

### Two-Tier Knowledge System

| Tier | Location | Contents |
|------|----------|---------|
| **Wiki** | `webapp/Vault/wiki/` | Markdown pages with YAML frontmatter: ~420 concepts, ~200 entities, 8 persona pages, stubs, synthesized pages |
| **RAG** | `data/chunks.json` + `webapp/data/chunks.faiss` | ~1200-word chunks from books/papers, 3072-dim Gemini embeddings |

The wiki is the primary knowledge source. RAG is the fallback for verbatim/deep source retrieval. The wiki grows at query time via async `update_wiki`.

### Query Pipeline

```
User query
  → Hybrid BM25 (30%) + MiniLM cosine (70%) over wiki pages → top-5 candidates
  → WIKI_LLM (Claude Sonnet): reads index.md + top-5 pages
      tools: read_page(slug), graph_traverse(slug, hops, max_nodes)
      output: { sufficient, selected_slugs, note }
  → MAIN_LLM (Claude Opus): reads selected wiki pages
      tool: rag_search(query, top_k) — FAISS + optional Bloom's filter
      output: SSE stream of answer chunks + structured metadata
                { sources, new_synthesis, should_wiki_update }
  → answer streamed to user via SSE
  → if should_wiki_update=true → async update_wiki (fire-and-forget)
        → writes synthesized/slug.md, patches _graph.json,
          rebuilds BM25 index, pushes to GitHub
```

### File Roles (webapp/api/)

| File | Role |
|------|------|
| `kb.py` | Path/env constants, `KnowledgeBase` singleton (loaded once at startup), `WikiSearchIndex` (hybrid BM25+MiniLM) |
| `pipeline.py` | Wires WIKI_LLM and MAIN_LLM together; `query_streaming()` is the main entrypoint |
| `wiki.py` | `run_wiki_llm()` — WIKI_LLM agent loop + `update_wiki_async()` |
| `main_agent.py` | `run_main_llm_streaming()` — MAIN_LLM agent loop, streams answer |
| `rag.py` | Gemini embedding + FAISS cosine search + Bloom's level filter |
| `graph.py` | YAML frontmatter parsing, graph queries, `save_graph()` |
| `llm_client.py` | Provider-agnostic client normalising Anthropic + OpenAI-compatible APIs |
| `pdf_utils.py` | PDF upload handling (base64 → text) |
| `index2.py` | Flask app, routes, singletons, CLI entry point |

### Scripts (offline pipeline — not deployed)

| Script | Purpose |
|--------|---------|
| `ingest.py` | PDF/MD → chunks → Gemini embeddings → `data/chunks.json` |
| `chunker.py` | 3-tier PDF extraction (PyMuPDF → Gemini OCR → Gemini direct) + chunking library |
| `export_for_web.py` | Builds FAISS indices + copies to `webapp/data/` (always run last before deploy) |
| `graph.py` | Builds `_graph.json` from wiki YAML frontmatter |
| `tag_blooms.py` | Orchestrates Bloom's tagging (Gemma + BERT) |
| `chunk_blooms_tagger.py` | BERT multilabel classifier; edit `BLOOMS_TUNED_THRESHOLDS` here |
| `gemma_goal_extractor.py` | Gemma 4 GGUF learning goal extractor (GPU offload via llama_cpp) |
| `extract_entities.py` | Gemini 2.5 Pro → wiki concept/entity pages from RAG chunks |
| `auto_wiki_builder.py` | Generates stub pages + rebuilds `wiki/index.md` |

### Wiki Page Format

```markdown
---
type: concept          # concept | entity | persona | stub | synthesized
aliases: [Alias 1, A1]
relationships:
  - target: other-slug
    type: related_to   # proposed_by | discussed_in | related_to | includes | contrasts_with | part_of | applied_to
tags: [strategy, technology]
---

# Page Title

Body text...

## Relationships
- **related_to**: [[other-slug|Other Page]]
```

`wiki/index.md` is **always injected** into the WIKI_LLM system prompt — keep it concise and well-structured.

### Data Flow: Local vs Deployed

- `data/chunks.json` — full chunks with 3072-dim embeddings (local only, ~19 MB, not in Docker)
- `webapp/data/chunks.json` — text only, no embeddings (baked into Docker image)
- `webapp/data/chunks.faiss` — FAISS index (baked into Docker image)
- `webapp/Vault/wiki/` — wiki pages (baked into Docker image, also live-updated via GitHub push)

### Environment Variables

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | Claude API (both LLMs) |
| `GEMINI_API_KEY` | Gemini embeddings (`gemini-embedding-2-preview`, 3072-dim) |
| `GITHUB_TOKEN` + `GITHUB_REPO` | Auto-push wiki updates after synthesis |
| `ALLOWED_ORIGIN` | CORS — set to Vercel frontend URL |
| `WIKI_LLM_MODEL` / `MAIN_LLM_MODEL` | Override default models (Sonnet / Opus) |
| `WIKI_LLM_PROVIDER` / `MAIN_LLM_PROVIDER` | `claude` or `nebius` |

---

## LLM Roles (Strict Separation)

### WIKI_LLM (Sonnet — navigation + maintenance)
- Never talks to the user.
- Given BM25 top-5 pages + `index.md` + user query: decides if context is sufficient or calls tools.
- Tools: `read_page(slug)`, `graph_traverse(slug, hops, max_nodes)`
- When `should_wiki_update: true` from MAIN_LLM: calls `update_wiki` asynchronously.

### MAIN_LLM (Opus — answer synthesis)
- Talks to the user exclusively.
- Escalation ladder (stops as soon as solid): wiki pages only → `rag_search` → general knowledge.
- Always emits structured metadata at end of stream: `{ sources, new_synthesis, should_wiki_update }`.
- Tool: `rag_search(query, top_k)`

---

## Coding Guidelines

### Think Before Coding
- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, push back.

### Simplicity First
- Minimum code that solves the problem. No speculative features.
- No abstractions for single-use code. No error handling for impossible scenarios.

### Surgical Changes
- Touch only what you must. Match existing style.
- Don't refactor adjacent code. Mention (don't delete) unrelated dead code.
- Remove only imports/variables that **your** changes made unused.
