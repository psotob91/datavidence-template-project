# Changelog

Notable changes to the **datavidence template repo** (the template's own
development — generated projects carry their own `CHANGELOG.md`).
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: [SemVer](https://semver.org/).

## [Unreleased]

### Added
- **Meta-learner + maintainer `CLAUDE.md`** (the master/builder repo now dog-foods
  what it ships). The learning-loop MECHANISM was hoisted into the
  `psotobverse-utils` plugin (≥ v1.4.0) — versioned and DRY — and each repo OPTS IN
  via a `.claude/meta-learner.json` config (presence activates the plugin's session
  hooks here; absent ⇒ they no-op, so unrelated repos are untouched). That config
  carries the repo's domain signal patterns and the consensus-radar filename.
  - Factory: root `CLAUDE.md` (factory-vs-child map + fast-resume recipe + plugin
    routing), `.claude/meta-learner.json` (agent-building patterns →
    `learning/STANDARDS_WATCH.md`), `learning/` scaffold, `SESSION_STATE.md`.
  - Template (children get a *working* loop, not an inert scaffold):
    `template/.claude/meta-learner.json` (methodological patterns →
    `template/learning/CONSENSUS_WATCH.md`), `CONSENSUS_WATCH.md` (EQUATOR/GRADE/
    Cochrane/regulators with explicit epistemic caveats — consensus lag, Table-2
    fallacy, confounder≠prognostic, MCID/Bayesian as *contested*; non-dogmatic,
    ask-the-user gate), constitution **rule 9** ("Close the learning loop"), a
    WRITE-trigger section in `CLAUDE.md.jinja`, a REFLECTOR consensus lane, and a
    `SESSION_STATE.md.jinja` seed.
  - The loop (`SessionStart` crash-detect + fast resume, `UserPromptSubmit` signal
    capture, `SessionEnd` handoff) + `/psotobverse-utils:reflect` and
    `/psotobverse-utils:audit-report` skills now ship from the plugin. Tested
    end-to-end (opt-in gate, lifecycle, crash detection) and via a Copier render.
- **`docs/audits/` convention** (factory + template) + the `/audit-report` skill:
  multi-agent audits write a small indexed `00-summary.md` with raw maps as
  referenced sidecars — never an unindexed mega-blob that blows context. The
  2026-06-28 factory audit is preserved under `docs/audits/`.
- **R data-analysis rigor expansion** (branch `feat/r-rigor-expansion`, layered):
  - Base-rigor folders (R stack): `data/{raw,derived}`, `metadata/`, `contracts/`,
    `docs/analysis/` (with `notation.md`), `config.example.yml` (portable data
    connection); `copier.yml` flags `project_profile` + `modules`.
  - 22 atomic policies under `.claude/policies/analysis/` (R-gated) covering numeric
    rigor, data integrity/quality, contracts, onboarding, reproducibility,
    regenerables, reporting (STROBE), figures, diagrams, model assumptions
    (frequentist + Bayesian MCMC/INLA), methods documentation, pseudocode-first,
    incremental-functions gate, and more; conditional `00-index`.
  - Stack: ordered tutorial notebooks `analysis/01_ingest…05_report` + `supplement`,
    `_targets.R` with deterministic seed, `Makefile` `all`/`reset`,
    `scripts/sysinfo.py` (capacity probe). `renv.lock` is committed (absolute repro).
  - Routes to the companion **`datavidence-healthanalysis`** plugin (frozen
    interface); the project still works without it.
- `QUICKSTART.md` — a 5-minute, recipe-style guide with a real worked example
  (*Anemia Infantil Puno*), plugin install, and a paste-ready **start prompt**
  that makes Claude Code give a panorama and ask for the minimum needed to begin.
  Linked prominently at the top of `README.md`.
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
