"""
pipeline/ingest_pipeline.py — Full ingestion pipeline for Gene.

Runs all offline scripts in the correct order to go from a raw source file
(PDF or markdown) all the way to a deployed-ready webapp/data/ export.

Pipeline steps:
  1. ingest       — chunk + embed new files into data/chunks.json
  2. tag_blooms   — tag chunks with Bloom's taxonomy (Gemma + BERT)
  3. extract      — generate wiki concept/entity pages from chunks (Gemini)
  4. wiki_build   — generate stub pages + rebuild wiki/index.md
  5. export       — build FAISS indices + copy everything to webapp/data/

Usage (from project root):
  python pipeline/ingest_pipeline.py --all
  python pipeline/ingest_pipeline.py --file Vault/raw/books/new-book.md
  python pipeline/ingest_pipeline.py --all --skip-blooms
  python pipeline/ingest_pipeline.py --all --skip-gemma
  python pipeline/ingest_pipeline.py --from-step 3
  python pipeline/ingest_pipeline.py --scan
"""

import argparse
import importlib
import subprocess
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PYTHON = sys.executable

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

# (import_name, pip_install_name, needed_for_steps)
# steps: set of step numbers this package is required for.
# "blooms_full" means step 2 with Gemma (not --skip-gemma).
_DEPS: list[tuple[str, str, set]] = [
    # Step 1 — ingest
    ("dotenv",       "python-dotenv",  {1, 2, 3, 4, 5}),
    ("requests",     "requests",       {1, 3}),
    ("numpy",        "numpy",          {1, 2, 5}),
    ("fitz",         "pymupdf",        {1}),
    # Step 2 — Bloom's tagging (BERT always, Gemma only if not --skip-gemma)
    ("torch",        "torch",          {2}),
    ("transformers", "transformers",   {2}),
    ("rank_bm25",    "rank-bm25",      {2, 5}),
    # Step 2 — Gemma (heavy, GPU; skipped when --skip-gemma is set)
    ("llama_cpp",    "llama-cpp-python", {"blooms_full"}),
    # Step 4 — wiki builder
    ("anthropic",    "anthropic",      {4}),
    # Step 5 — export
    ("faiss",        "faiss-cpu",      {5}),
    ("fastembed",    "fastembed",      {5}),
]


def check_deps(active_steps: set, skip_gemma: bool) -> bool:
    """
    Try importing every package needed by the active steps.
    Prints a table of results and returns False if anything is missing.
    """
    missing = []
    checked = []

    for import_name, pip_name, needed_for in _DEPS:
        # Decide if this package is needed given the current run config.
        if "blooms_full" in needed_for:
            if 2 not in active_steps or skip_gemma:
                continue   # Gemma not needed — skip check
        elif not (needed_for & active_steps):
            continue       # Package not needed for any active step

        try:
            importlib.import_module(import_name)
            checked.append(("ok", import_name, pip_name))
        except ImportError:
            checked.append(("MISSING", import_name, pip_name))
            missing.append(pip_name)

    if not checked:
        return True

    print(f"\n{'─'*52}")
    print(f"  Dependency check ({len(checked)} packages)")
    print(f"{'─'*52}")
    for status, import_name, pip_name in checked:
        mark = "✓" if status == "ok" else "✗"
        print(f"  {mark}  {import_name:<20}  ({pip_name})")
    print(f"{'─'*52}")

    if missing:
        print(f"\n  Missing packages — install with:")
        print(f"  pip install {' '.join(missing)}\n")
        return False

    print(f"  All dependencies present.\n")
    return True


# ---------------------------------------------------------------------------
# Step runner
# ---------------------------------------------------------------------------

def run(label: str, cmd: list[str], dry_run: bool = False) -> bool:
    """Run a command, print its output live, return True on success."""
    print(f"\n{'='*60}")
    print(f"  {label}")
    print(f"  cmd: {' '.join(str(c) for c in cmd)}")
    print(f"{'='*60}")

    if dry_run:
        print("  [dry-run] skipped")
        return True

    t0 = time.time()
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)
    elapsed = time.time() - t0

    if result.returncode != 0:
        print(f"\n[FAILED] {label} exited with code {result.returncode}")
        return False

    print(f"\n[OK] {label} — {elapsed:.1f}s")
    return True


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------

def step_scan():
    return run(
        "SCAN — preview new files",
        [PYTHON, "scripts/ingest.py", "--scan"],
    )


def step_ingest(file: str | None):
    if file:
        return run(
            f"INGEST — chunk + embed: {file}",
            [PYTHON, "scripts/ingest.py", "--process", file],
        )
    return run(
        "INGEST — chunk + embed all new files",
        [PYTHON, "scripts/ingest.py", "--process-all"],
    )


def step_tag_blooms(skip_gemma: bool, reset: bool):
    cmd = [PYTHON, "scripts/tag_blooms.py"]
    label = "BLOOM'S — tag chunks with Bloom's taxonomy"
    if reset:
        cmd.append("--reset")
        label += " (reset)"
    elif skip_gemma:
        cmd.append("--skip-gemma")
        label += " (BERT only, no Gemma)"
    return run(label, cmd)


def step_extract_entities(source: str | None):
    cmd = [PYTHON, "scripts/extract_entities.py", "--all"]
    label = "EXTRACT — generate wiki concept/entity pages"
    if source:
        cmd = [PYTHON, "scripts/extract_entities.py", "--source", source]
        label += f" (source: {source})"
    return run(label, cmd)


def step_wiki_build():
    return run(
        "WIKI BUILD — generate stubs + rebuild index.md",
        [PYTHON, "scripts/auto_wiki_builder.py", "--all"],
    )


def step_export():
    return run(
        "EXPORT — build FAISS indices → webapp/data/",
        [PYTHON, "scripts/export_for_web.py"],
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

STEP_NAMES = {
    1: "ingest",
    2: "tag_blooms",
    3: "extract",
    4: "wiki_build",
    5: "export",
}


def main():
    parser = argparse.ArgumentParser(
        description="Full ingestion pipeline: raw file → webapp/data/",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument("--all",  action="store_true", help="Process all new files in Vault/raw/")
    source_group.add_argument("--file", metavar="PATH",      help="Process a single file")
    source_group.add_argument("--scan", action="store_true", help="Preview new files only (no processing)")

    parser.add_argument("--skip-blooms",  action="store_true", help="Skip step 2: Bloom's tagging (no GPU needed)")
    parser.add_argument("--skip-gemma",   action="store_true", help="Step 2: use BERT only, skip Gemma goal extraction")
    parser.add_argument("--reset-blooms", action="store_true", help="Step 2: strip all bloom tags and re-tag from scratch")
    parser.add_argument("--skip-extract", action="store_true", help="Skip step 3: entity/concept extraction")
    parser.add_argument("--skip-wiki",    action="store_true", help="Skip step 4: stub + index.md generation")
    parser.add_argument("--source",       metavar="NAME",      help="Step 3: only extract from this source name")
    parser.add_argument("--from-step",    type=int, metavar="N", choices=range(1, 6),
                        help="Resume from step N (1=ingest, 2=blooms, 3=extract, 4=wiki, 5=export)")

    args = parser.parse_args()

    if not (args.all or args.file or args.scan or args.from_step):
        parser.print_help()
        sys.exit(0)

    # Scan-only mode
    if args.scan:
        step_scan()
        return

    from_step = args.from_step or 1

    # Build the set of step numbers that will actually run.
    active_steps: set = set()
    if from_step <= 1:
        active_steps.add(1)
    if from_step <= 2 and not args.skip_blooms:
        active_steps.add(2)
    if from_step <= 3 and not args.skip_extract:
        active_steps.add(3)
    if from_step <= 4 and not args.skip_wiki:
        active_steps.add(4)
    active_steps.add(5)

    if not check_deps(active_steps, skip_gemma=args.skip_gemma):
        sys.exit(1)

    failed_step = None
    t_start = time.time()

    print(f"\nGene ingestion pipeline — starting from step {from_step} ({STEP_NAMES[from_step]})")
    if args.file:
        print(f"Source file: {args.file}")

    steps = []

    # Step 1 — ingest
    if from_step <= 1:
        steps.append(("1. Ingest",      lambda: step_ingest(args.file)))

    # Step 2 — Bloom's tagging
    if from_step <= 2 and not args.skip_blooms:
        steps.append(("2. Tag Bloom's", lambda: step_tag_blooms(args.skip_gemma, args.reset_blooms)))

    # Step 3 — entity/concept extraction
    if from_step <= 3 and not args.skip_extract:
        steps.append(("3. Extract",     lambda: step_extract_entities(args.source)))

    # Step 4 — stub + index.md
    if from_step <= 4 and not args.skip_wiki:
        steps.append(("4. Wiki build",  lambda: step_wiki_build()))

    # Step 5 — export (always last)
    if from_step <= 5:
        steps.append(("5. Export",      lambda: step_export()))

    for name, fn in steps:
        ok = fn()
        if not ok:
            failed_step = name
            break

    total = time.time() - t_start
    print(f"\n{'='*60}")
    if failed_step:
        print(f"  PIPELINE FAILED at: {failed_step}")
        print(f"  Fix the error above, then resume with --from-step <N>")
    else:
        print(f"  PIPELINE COMPLETE — {total:.1f}s total")
        print(f"  webapp/data/ is ready. Commit + push to deploy.")
    print(f"{'='*60}\n")

    if failed_step:
        sys.exit(1)


if __name__ == "__main__":
    main()
