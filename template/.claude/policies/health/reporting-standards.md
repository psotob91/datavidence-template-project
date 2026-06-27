# Reporting standards (EQUATOR, by design / task)

Pick the EQUATOR guideline by study **design + analysis task**; record the choice and
fill its checklist in `docs/analysis/reporting-checklist.md`. Source of truth:
equator-network.org (download the official checklist; **do not copy copyrighted text** —
reference item numbers). Reporting guidelines, risk-of-bias tools, and methodological
frameworks are **distinct** — keep them straight.

## Reporting guidelines (by design)

- **Observational** (cohort / case-control / cross-sectional): **STROBE** (general
  observational reporting); for routinely-collected / secondary data add **RECORD**
  (pharmacoepidemiology: **RECORD-PE**, an *extension* of RECORD) — see `secondary-data.md`.
- **Randomized trial**: **CONSORT**; trials on routinely-collected data: **CONSORT-ROUTINE**.
- **Causal from observational** (target trial emulation): **TARGET**, on top of STROBE/RECORD.
- **Prediction model** (development / validation): **TRIPOD** (+ TRIPOD-AI).
- **Prognostic factor / biomarker**: **REMARK** (tumour-marker prognostic; generalizes to
  prognostic factors).
- **Diagnostic accuracy**: **STARD**.
- **Systematic review / meta-analysis**: **PRISMA**. *(module `synthesis`)*
- **Protocols**: **SPIRIT** (trials).

## Risk-of-bias / appraisal tools (NOT reporting guidelines)

- Prediction models → **PROBAST**. Diagnostic accuracy → **QUADAS-2**. Systematic
  reviews → **ROBIS** (risk of bias) and **AMSTAR-2** (methodological-quality appraisal).

## Methodological frameworks (NOT reporting guidelines)

- Prognosis Research Strategy: **PROGRESS-1** (fundamental/overall prognosis),
  **PROGRESS-2** (prognostic factors), **PROGRESS-3** (prognostic models).

## Descriptive & equity

- **Descriptive** (occurrence/distribution): descriptive-epidemiology framework (Lesko
  et al., 2022) — population (person/place/time), outcome/state, measure of occurrence.
- **Equity / disparities**: **STROBE-Equity** + **PROGRESS-Plus** — the 8 PROGRESS factors
  (place, race/ethnicity, occupation, gender/sex, religion, education, SES, social capital)
  **plus** age, disability, sexual orientation, homelessness, substance misuse.

## Rules

- Reporting expectations follow the TASK (see `analysis/statistical-reporting.md`).
- Every reported result maps to a checklist item; unmet items are flagged, not hidden.
