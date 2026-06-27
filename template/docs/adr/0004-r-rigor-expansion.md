# 0004. R data-analysis rigor expansion (layered profile + task frameworks + modules)

Date: 2026-06-27

## Status

Accepted

## Context

The R analysis stack shipped a minimal scaffold. Reproducible biostatistics / health
research needs governance that encodes numeric rigor, data integrity, reproducibility,
reporting standards, and **task-appropriate** methods — without bloating non-health or
non-R projects, and without duplicating the companion plugin's automation. Much of this
guidance derives from published frameworks, so factual accuracy matters.

## Decision

We will expand the R stack in **layers**, gated by Copier variables:

- **Base R rigor** (`analysis_stack == 'r'`): atomic policies under
  `.claude/policies/analysis/` (numeric, data integrity/quality, contracts, onboarding,
  reproducibility, regenerables, efficiency, reporting, figures, diagrams, methods docs,
  pseudocode-first, incremental-functions, code-style, **statistical-reporting**,
  **longitudinal-data**, **regression-modeling**, IDA, model-assumptions, etc.) plus the
  `data/ metadata/ contracts/ docs/analysis/` structure, ordered `analysis/01..05` +
  `supplement`, `_targets.R` seed, Makefile `all`/`reset`, `scripts/sysinfo.py`. `renv.lock`
  is committed (absolute reproducibility).
- **Health-data profile** (`project_profile == 'health-data'`): `.claude/policies/health/`
  (reporting-standards, secondary-data/RECORD, clinical-tables, study-flow,
  routinely-collected-data) + `docs/analysis/reporting-checklist.md`.
- **Opt-in task modules** (`modules`): `causal`, `prediction`, `survey`, `spatial`,
  `synthesis` — each a scaffold under `docs/analysis/modules/` with routing.
- **Statistical guidance is organized by TASK** (descriptive / relationships / causal /
  predictive / diagnostic / synthesis), grounded in **SAMBR**, **STRATOS** (IDA,
  longitudinal, regression-without-regrets), and the **EQUATOR** family (STROBE, RECORD,
  CONSORT, TARGET, TRIPOD + PROBAST, STARD, PRISMA, REMARK), the descriptive-epidemiology
  framework, and STROBE-Equity / PROGRESS-Plus. The companion plugin
  `datavidence-healthanalysis` provides the verbs the policies route to (frozen interface).
- Framework claims were **adversarially verified** (multi-agent, source-grounded) before merge.

## Consequences

- Generated R projects ship task-aware, source-grounded governance; the profile and modules
  keep `standard` / non-R projects lean (gated via Copier `_exclude`).
- A second Copier axis (`project_profile`) plus a multiselect (`modules`) widen the CI
  render matrix; `template-ci.yml` now also renders R + health-data + all modules.
- Generated R projects gain a **reproducibility CI gate** (`make reset && make all`).
- The plugin must honor the frozen skill names; the project degrades gracefully without it.
- `health/routinely-collected-data.md` ships as a **stub**, pending a research brief.
