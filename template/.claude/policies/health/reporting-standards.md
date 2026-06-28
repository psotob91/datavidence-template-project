# Reporting standards (EQUATOR, by design / task)

Pick the EQUATOR guideline by study **design + analysis task**; record the choice and
fill its checklist in `docs/analysis/reporting-checklist.md`. Source of truth:
equator-network.org (download the official checklist; **do not copy copyrighted text** —
reference item numbers). Reporting guidelines, risk-of-bias tools, and methodological
frameworks are **distinct** — keep them straight.

> **Prerequisite:** `health/secondary-data.md` — RECORD reporting feeds the guideline choice.
> **See also (always):** `analysis/pre-specification.md` — TARGET pairs with the pre-specified causal estimand for target-trial emulation.

## Reporting guidelines (by design)

- **Observational** (cohort / case-control / cross-sectional): **STROBE** (general
  observational reporting); for routinely-collected / secondary data add **RECORD**
  (pharmacoepidemiology: **RECORD-PE**, an *extension* of RECORD) — see `secondary-data.md`.
- **Randomized trial**: **CONSORT 2025** (supersedes CONSORT 2010); trials on
  routinely-collected data: **CONSORT-ROUTINE**.
- **Causal from observational** (target trial emulation): **TARGET** (JAMA 2025) — state
  the causal estimand and identifying assumptions, and align eligibility/start to avoid
  immortal-time bias — on top of STROBE/RECORD.
- **Prediction model** (development / validation): **TRIPOD+AI (2024)** (supersedes
  TRIPOD 2015; covers regression and ML).
- **Prognostic factor / biomarker**: **REMARK** (tumour-marker prognostic; generalizes to
  prognostic factors).
- **Diagnostic accuracy**: **STARD (2015)**; for AI-based tests add **STARD-AI (2025)**.
- **Systematic review / meta-analysis**: **PRISMA**. *(module `synthesis`)*
- **Protocols**: **SPIRIT** (trials).

## Risk-of-bias / appraisal tools (NOT reporting guidelines)

- Prediction models → **PROBAST+AI (2025)** (supersedes PROBAST 2019). Diagnostic
  accuracy → **QUADAS-2**. Systematic reviews → **ROBIS** (risk of bias) and **AMSTAR-2**
  (methodological-quality appraisal).

## Methodological frameworks (NOT reporting guidelines)

- Prognosis Research Strategy: **PROGRESS-1** (fundamental/overall prognosis),
  **PROGRESS-2** (prognostic factors), **PROGRESS-3** (prognostic models).

## Descriptive & equity

- **Descriptive** (occurrence/distribution): descriptive-epidemiology framework (Lesko
  et al., 2022) — population (person/place/time), outcome/state, measure of occurrence.
- **Equity / disparities**: **STROBE-Equity** (2025; 10 equity items added to STROBE) +
  **PROGRESS-Plus** — the 8 PROGRESS factors
  (place, race/ethnicity, occupation, gender/sex, religion, education, SES, social capital)
  **plus** age, disability, sexual orientation, homelessness, substance misuse.

## Rules

- Reporting expectations follow the TASK (see `analysis/statistical-reporting.md`).
- Every reported result maps to a checklist item; unmet items are flagged, not hidden.
