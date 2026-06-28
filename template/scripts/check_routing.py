#!/usr/bin/env python3
"""Check that the machine routing (.claude/policy/routing.yml) does not drift from
the human routing table in .claude/policies/00-index.md.

The index "Conditional routing" table is the human source of truth; routing.yml is
the enforced subset read by the `policy_router` hook. This guard asserts that every
policy a routing.yml rule points to (`next_policy`) is also documented in the index
routing section — so an enforced edge can never be undocumented.

Standard library only (no PyYAML): both files are parsed with regexes. This is a
drift tripwire, not a full schema validator.

Usage:
    python scripts/check_routing.py            # report, exit 0/1
    python scripts/check_routing.py --root DIR

Exit status:
    0  in sync (or nothing to check — files absent / no rules)
    1  drift: routing.yml references a policy the index routing table omits
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

INDEX_REL = ".claude/policies/00-index.md"
ROUTING_REL = ".claude/policy/routing.yml"

# Policy-ish path references, e.g. analysis/foo.md, health/bar.md, docs/analysis/modules/causal.md
POLICY_RE = re.compile(r"(?:docs/analysis/modules/|analysis/|health/|universal/)[\w./-]+\.md")
NEXT_RE = re.compile(r"^\s*next_policy:\s*[\"']?([^\"'\s]+)", re.MULTILINE)


def _read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def index_routing_targets(text: str) -> set[str]:
    """Policies referenced inside the '## Conditional routing' section of the index."""
    start = text.find("## Conditional routing")
    if start == -1:
        return set()
    # Section runs until the next top-level '## ' or EOF.
    rest = text[start + len("## Conditional routing"):]
    nxt = rest.find("\n## ")
    section = rest if nxt == -1 else rest[:nxt]
    return set(POLICY_RE.findall(section))


def routing_yml_targets(text: str) -> set[str]:
    return set(m.strip() for m in NEXT_RE.findall(text))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Check routing.yml vs the index routing table.")
    ap.add_argument("--root", default=".", help="Project root (default: .)")
    args = ap.parse_args(argv[1:])
    root = Path(args.root)

    routing = _read(root / ROUTING_REL)
    if not routing.strip():
        print("check_routing: no routing.yml (or empty) — nothing to check.")
        return 0

    enforced = routing_yml_targets(routing)
    if not enforced:
        print("check_routing: routing.yml has no rules — nothing to check.")
        return 0

    documented = index_routing_targets(_read(root / INDEX_REL))
    missing = sorted(enforced - documented)
    if missing:
        print(
            "check_routing: DRIFT — routing.yml points to policies the index "
            "'Conditional routing' table does not document:",
            file=sys.stderr,
        )
        for m in missing:
            print(f"  - {m}", file=sys.stderr)
        print("Reconcile routing.yml with .claude/policies/00-index.md.", file=sys.stderr)
        return 1

    print(f"check_routing: OK — {len(enforced)} enforced edge(s) all documented in the index.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
