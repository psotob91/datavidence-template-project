# `docs/analysis/` — methodological documentation (survives agent sessions)

Decisions and methods that must outlive any single session live here, in human
language. These are **not** agent scratchpads (those are disposable, in
`_agent_cache/` / `_agent_private/`).

Typical contents (added as the project needs them):

- `analysis-plan.md` — question, estimand, cohort, outcomes, covariates, phases.
- `notation.md` — the **mathematical notation registry** (LaTeX); methods text
  must not break this notation.
- `variable-derivation.md` — how each derived variable is constructed.
- `assumptions.md`, `table-shells.md` — pre-results plans.
- *(health-data profile)* a Statistical Analysis Plan (SAP) and EQUATOR
  reporting checklists (STROBE / CONSORT / TRIPOD).

## Relationship to other folders

- **Methods narrative** (extended, journal-appendix style) is written
  continuously alongside the analysis; the long-form supplement lives in
  `analysis/supplement.qmd`.
- Machine-readable dictionaries/indices live in `../metadata/`; data
  prerequisites live in `../contracts/`.
