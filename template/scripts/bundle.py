#!/usr/bin/env python3
"""Build a clean transfer bundle, or verify connected-data paths before a run.

Two modes (Python stdlib only; the one external dependency is `git`):

  python scripts/bundle.py            Build dist/<project>-<shortsha>.tar.gz via
                                      `git archive HEAD` -- a snapshot of the COMMITTED
                                      tree only, so everything gitignored (config.yml,
                                      .env, data/derived/, _targets/, caches) is excluded
                                      automatically. Use it to hand a project to a server
                                      that has no git/internet. See docs/server_setup.md.

  python scripts/bundle.py --verify   Read config.yml's data_sources[*].path and check that
                                      each exists. Run it on a new machine BEFORE `make all`
                                      to catch a mis-pointed data path early. Read-only;
                                      never prints secrets. (Checksums are recorded in
                                      metadata/data_sources.yml -- verify those there.)
"""
from __future__ import annotations
import os, re, subprocess, sys
from pathlib import Path


def _repo_root() -> Path:
    try:
        out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, check=True).stdout.strip()
        return Path(out)
    except Exception:
        return Path.cwd()


def _short_sha(root: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "nogit"


def build() -> int:
    root = _repo_root()
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / (root.name + "-" + _short_sha(root) + ".tar.gz")
    try:
        subprocess.run(["git", "-C", str(root), "archive", "--format=tar.gz",
                        "-o", str(out), "HEAD"], check=True, capture_output=True, text=True)
    except Exception as e:
        print("[bundle] git archive failed: " + str(e), file=sys.stderr)
        print("[bundle] commit your work first -- git archive snapshots the committed tree.",
              file=sys.stderr)
        return 1
    print("[bundle] wrote %s (%.2f MB)" % (out.relative_to(root), out.stat().st_size / 1e6))
    print("[bundle] EXCLUDED (gitignored/untracked -- set up on the target per "
          "docs/server_setup.md): config.yml, .env, data/derived/, _targets/, caches.")
    print("[bundle] On the target: unpack, then cp config.example.yml config.yml + edit, "
          "cp .env.example .env + edit, create the data junction, then `make setup && make all`.")
    return 0


_NAME_RE = re.compile(r'^\s{2}([A-Za-z0-9_.-]+)\s*:\s*$')
_PATH_RE = re.compile(r'^\s{4,}path\s*:\s*(.+?)\s*$')


def _strip_value(raw: str) -> str:
    raw = raw.strip()
    if raw[:1] in ('"', "`") or raw[:1] == "'":
        q = raw[0]
        end = raw.find(q, 1)
        return raw[1:end] if end != -1 else raw[1:]
    return raw.split("#", 1)[0].strip()


def _config_paths(cfg: Path):
    """Best-effort scan of config.yml data_sources[*].path (stdlib, no PyYAML)."""
    items, cur, in_ds = [], None, False
    for line in cfg.read_text(encoding="utf-8", errors="replace").splitlines():
        if re.match(r'^data_sources\s*:', line):
            in_ds = True
            continue
        if in_ds and re.match(r'^\S', line):
            in_ds = False
        if not in_ds:
            continue
        mn = _NAME_RE.match(line)
        if mn:
            cur = mn.group(1)
            continue
        mp = _PATH_RE.match(line)
        if mp and cur:
            items.append((cur, _strip_value(mp.group(1))))
    return items


def verify() -> int:
    root = _repo_root()
    cfg = root / "config.yml"
    if not cfg.exists():
        print("[verify] no config.yml yet -- copy config.example.yml -> config.yml and fill in the "
              "machine-specific data paths first (nothing to verify).")
        return 0
    sources = _config_paths(cfg)
    if not sources:
        print("[verify] config.yml lists no data_sources paths (nothing to verify).")
        return 0
    failed = 0
    for name, path in sources:
        if Path(path).exists():
            print("[verify] OK    %s: exists (%s)" % (name, path))
        else:
            print("[verify] FAIL  %s: path does not exist -> %s" % (name, path))
            failed += 1
    print("[verify] %d/%d data source(s) present. "
          "(Checksums: see metadata/data_sources.yml.)" % (len(sources) - failed, len(sources)))
    return 1 if failed else 0


def main() -> int:
    args = sys.argv[1:]
    if any(a in ("-h", "--help") for a in args):
        print(__doc__)
        return 0
    if "--verify" in args:
        return verify()
    return build()


if __name__ == "__main__":
    sys.exit(main())
