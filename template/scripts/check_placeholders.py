#!/usr/bin/env python3
"""Fail if any unrendered copier placeholders remain in the tree.

Used as a guard after `copier copy` / `copier update` and in CI: a generated
project must not contain the template's literal placeholder name or an
un-rendered copier variable. Walks the WHOLE tree (including dot-directories such
as .claude and .github) but skips VCS/dependency/build dirs.

IMPORTANT: this does NOT flag every `{{ ... }}` / `{% ... %}`. Files such as
`cliff.toml` (git-cliff Tera templates) and GitHub Actions workflows
(`${{ secrets.* }}`) legitimately contain brace syntax that MUST survive into the
generated project. We flag only the literal sentinel and unrendered *copier*
variables. If `copier.yml` gains a new question, add it to COPIER_VARS.

Usage:
    python scripts/check_placeholders.py [ROOT]   # default ROOT = "."

Exit status:
    0  clean
    1  one or more placeholders found (offending file:line printed to stderr)

Standard library only — no third-party dependencies.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Directories never worth scanning (VCS, virtualenvs, caches, deps).
EXCLUDED_DIRS = {".git", ".venv", "venv", "renv", "node_modules", "__pycache__"}

# Literal sentinel: the canonical template placeholder name.
LITERAL_NEEDLES = ("__project_name__",)

# Copier questions declared in copier.yml. An unrendered copier variable means a
# file was templated wrong (e.g. a verbatim .md that should have been .jinja).
COPIER_VARS = (
    "project_name", "project_slug", "author", "year", "license",
    "analysis_stack", "knowledge_retrieval",
)
# Match a {{ ... }} or {% ... %} construct that contains a copier variable.
# This deliberately ignores git-cliff / GitHub-Actions braces (no copier var).
COPIER_VAR_RE = re.compile(r"{[{%][^}]*\b(?:" + "|".join(COPIER_VARS) + r")\b")

# This script itself legitimately mentions the needles above; skip it.
SELF_NAME = Path(__file__).name


def is_probably_text(path: Path) -> bool:
    """Cheap binary sniff: a NUL byte in the first chunk means binary."""
    try:
        with path.open("rb") as fh:
            return b"\x00" not in fh.read(4096)
    except OSError:
        return False


def iter_files(root: Path):
    """Yield files under root, pruning EXCLUDED_DIRS."""
    for path in root.rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def scan_file(path: Path) -> list[tuple[int, str]]:
    """Return [(lineno, offending_text), ...] for every offending line in path."""
    hits: list[tuple[int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return hits
    for lineno, line in enumerate(text.splitlines(), start=1):
        for needle in LITERAL_NEEDLES:
            if needle in line:
                hits.append((lineno, needle))
        m = COPIER_VAR_RE.search(line)
        if m:
            hits.append((lineno, m.group(0)))
    return hits


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    if not root.exists():
        print(f"check_placeholders: root does not exist: {root}", file=sys.stderr)
        return 1

    found = False
    for path in iter_files(root):
        if path.name == SELF_NAME:
            continue
        if not is_probably_text(path):
            continue
        for lineno, offending in scan_file(path):
            found = True
            rel = path.relative_to(root) if path.is_relative_to(root) else path
            print(f"{rel}:{lineno}: unrendered placeholder {offending!r}", file=sys.stderr)

    if found:
        print("\ncheck_placeholders: FAILED - unrendered placeholders above.", file=sys.stderr)
        return 1
    print("check_placeholders: OK - no unrendered placeholders found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
