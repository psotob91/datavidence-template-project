#!/usr/bin/env python3
"""Fail if any unrendered template placeholders remain in the tree.

Used as a guard after `copier copy` / `copier update` and in CI: a generated
project must not contain the template's literal placeholder name or any
un-rendered Jinja markup. Walks the WHOLE tree (including dot-directories such
as .claude and .github) but skips VCS/dependency/build dirs.

Usage:
    python scripts/check_placeholders.py [ROOT]   # default ROOT = "."

Exit status:
    0  clean
    1  one or more placeholders found (offending file:line printed to stderr)

Standard library only — no third-party dependencies.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Directories never worth scanning (VCS, virtualenvs, caches, deps).
EXCLUDED_DIRS = {".git", ".venv", "venv", "renv", "node_modules", "__pycache__"}

# Literal needles that indicate an unrendered template.
LITERAL_NEEDLES = ("__project_name__",)
# Jinja markers that must never survive into a rendered project.
JINJA_NEEDLES = ("{{", "}}", "{%")

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
    """Yield files under root, pruning EXCLUDED_DIRS in place."""
    for path in root.rglob("*"):
        # Skip anything living inside an excluded directory.
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def scan_file(path: Path) -> list[tuple[int, str]]:
    """Return [(lineno, needle), ...] for every offending line in path."""
    hits: list[tuple[int, str]] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return hits
    for lineno, line in enumerate(text.splitlines(), start=1):
        for needle in (*LITERAL_NEEDLES, *JINJA_NEEDLES):
            if needle in line:
                hits.append((lineno, needle))
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
        for lineno, needle in scan_file(path):
            found = True
            rel = path.relative_to(root) if path.is_relative_to(root) else path
            print(f"{rel}:{lineno}: unrendered placeholder {needle!r}", file=sys.stderr)

    if found:
        print(
            "\ncheck_placeholders: FAILED — unrendered placeholders above.",
            file=sys.stderr,
        )
        return 1
    print("check_placeholders: OK — no unrendered placeholders found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
