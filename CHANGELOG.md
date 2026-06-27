# Changelog

Notable changes to the **datavidence template repo** (the template's own
development — generated projects carry their own `CHANGELOG.md`).
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: [SemVer](https://semver.org/).

## [Unreleased]

### Added
- `requirements-ci.txt` — pins Copier for the render-test (single source of truth).
- `.github/dependabot.yml` — monthly bumps for pip (Copier) and GitHub Actions;
  the render-test gates every bump PR.
- `scripts/new-study.ps1` — one-command bootstrap (copier + git init + commit,
  optional `make setup`) so each new study mounts without remembering the steps.
- `template/docs/SETUP.md.jinja` — short, ordered, DO/DON'T quickstart shipped
  into every project (Claude Code first, then Cowork).

### Changed
- ADR-0002: recorded the Cowork verification spike — plugin hooks DO fire in
  Cowork, but `${CLAUDE_PLUGIN_ROOT}` is not shell-expanded; documented the fix
  (shipped in `psotobverse-utils` v1.3.1) and the remaining re-test question.
- ADR-0003: Proposed → Accepted (retrieval engine is in active development as a
  separate per-project MCP; coupling is intentionally temporary).
- `template/learning/PLAYBOOK.md` and `template/_targets.R`: fixed the nonexistent
  `make pipeline` reference to `make test`; corrected the Cowork hook note.
- `.github/workflows/template-ci.yml`: install Copier from the pinned
  `requirements-ci.txt`; removed the stale "verify in Phase 4" note.
- Bumped JavaScript GitHub Actions off the deprecated Node 20 runtime:
  `actions/checkout` v4→v7, `astral-sh/setup-uv` v5/v3→v8,
  `actions/setup-python` v5→v6 (template CI and the shipped child CI). Docker
  actions (`gitleaks`, `git-cliff`) and `r-lib/actions@v2` left as-is — they
  don't use Node 20.

### Fixed
- CI render-test: `check_placeholders.py` is now passed the rendered project
  directory as its root (it defaults to `.`), so the guard scans the generated
  project instead of the template source.

## [0.1.0] - 2026-06

### Added
- Initial Claude-only template scaffold (Copier): governance layer
  (constitution + atomic policies + ADRs), R/Python/none analysis stacks,
  companion-plugin coupling, output/context contracts, CI render-test.
