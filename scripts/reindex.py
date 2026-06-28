#!/usr/bin/env python3
"""Regenerate llms.txt — a navigable, derived index of this repository.

llms.txt is a flat map of the project: one line per file, each showing the
path and a short descriptor (the first heading or first non-empty line). It is
DERIVED — never edit it by hand; run this recipe to rebuild it.

Usage:
    python scripts/reindex.py            # rewrite llms.txt
    python scripts/reindex.py --check    # exit 1 if llms.txt is stale (CI)
    python scripts/reindex.py --root DIR --out FILE

Constraints:
    * Standard library only.
    * Skips dot-directories (.git, .claude, .github, ...), virtualenvs, renv,
      node_modules and other noise.
    * Output kept under MAX_BYTES (~10 KB); truncated with a notice if larger.

Exit status:
    0  index written (or, with --check, already up to date)
    1  with --check: llms.txt is missing or out of date
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

OUT_NAME = "llms.txt"
MAX_BYTES = 10 * 1024  # keep the index small and context-friendly

# Names of directories to prune. Dot-dirs are pruned generically (see walk()).
EXCLUDED_DIRS = {".venv", "venv", "renv", "node_modules", "__pycache__", "renv"}

# Files that are not worth indexing.
EXCLUDED_FILES = {OUT_NAME, ".gitkeep", ".DS_Store"}

HEADER = (
    "# Derived index — regenerate with: python scripts/reindex.py. "
    "Do not edit by hand.\n"
)

# Extensions we try to read a descriptor from; others get a bare path line.
TEXT_SUFFIXES = {
    ".md", ".markdown", ".txt", ".qmd", ".rmd",
    ".py", ".r", ".toml", ".yml", ".yaml", ".json", ".cfg", ".ini",
    ".sh", ".mk", "", ".jinja",
}


def is_excluded_dir(name: str) -> bool:
    return name.startswith(".") or name in EXCLUDED_DIRS


def walk(root: Path):
    """Yield indexable files under root, pruning dot-dirs and noise dirs."""
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            entries = sorted(current.iterdir(), key=lambda p: p.name.lower())
        except OSError:
            continue
        for entry in entries:
            if entry.is_dir():
                if not is_excluded_dir(entry.name):
                    stack.append(entry)
            elif entry.is_file() and entry.name not in EXCLUDED_FILES:
                yield entry


def descriptor(path: Path) -> str:
    """Best-effort one-line summary: first Markdown heading or first line."""
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return ""
    try:
        with path.open("r", encoding="utf-8", errors="replace") as fh:
            first_nonempty = ""
            for raw in fh:
                line = raw.strip()
                if not line:
                    continue
                if line.startswith("#"):
                    return line.lstrip("#").strip()
                if not first_nonempty:
                    first_nonempty = line
                    # For code/config, the first comment or line is enough.
                    break
            return first_nonempty
    except OSError:
        return ""


def build_index(root: Path) -> str:
    lines = [HEADER, "\n"]
    body: list[str] = []
    for path in sorted(walk(root), key=lambda p: str(p.relative_to(root)).lower()):
        rel = path.relative_to(root).as_posix()
        desc = descriptor(path)
        body.append(f"- {rel}" + (f" — {desc}" if desc else ""))

    text = "".join(lines) + "\n".join(body) + "\n"

    if len(text.encode("utf-8")) > MAX_BYTES:
        # Truncate conservatively, keeping whole lines.
        notice = "\n# … index truncated (exceeded 10 KB); narrow the tree.\n"
        budget = MAX_BYTES - len(notice.encode("utf-8"))
        encoded = text.encode("utf-8")[:budget]
        text = encoded.decode("utf-8", errors="ignore")
        text = text[: text.rfind("\n") + 1] + notice
    return text


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Regenerate llms.txt index.")
    parser.add_argument("--root", default=".", help="Repository root (default: .)")
    parser.add_argument("--out", default=None, help="Output path (default: ROOT/llms.txt)")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if llms.txt is missing or stale.",
    )
    args = parser.parse_args(argv[1:])

    root = Path(args.root)
    out = Path(args.out) if args.out else root / OUT_NAME

    generated = build_index(root)

    if args.check:
        existing = out.read_text(encoding="utf-8") if out.exists() else ""
        if existing != generated:
            print(
                f"reindex: STALE — {out} is out of date. Run: python scripts/reindex.py",
                file=sys.stderr,
            )
            return 1
        print(f"reindex: OK — {out} is up to date.")
        return 0

    out.write_text(generated, encoding="utf-8")
    print(f"reindex: wrote {out} ({len(generated.encode('utf-8'))} bytes).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
