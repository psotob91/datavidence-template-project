# Reporting standards (EQUATOR, by design / task)

Pick the EQUATOR guideline by study **design + analysis task**; record the choice and
fill its checklist in `docs/analysis/reporting-checklist.md`. Source of truth:
equator-network.org (download the official checklist; **do not copy copyrighted text** —
reference item numbers).

## Choose the guideline

- **Observational** (cohort / case-control / cross-sectional): **STROBE**; for
  routinely-collected / secondary data add **RECORD** (pharmacoepi: **RECORD-PE**) —
  see `secondary-data.md`.
- **Randomized trial**: **CONSORT**; trials on routinely-collected data: **CONSORT-ROUTINE**.
- **Causal from observational** (target trial emulation): **TARGET** statement (+ STROBE/RECORD).
- **Prediction model** (development / validation): **TRIPOD** (+ TRIPOD-AI); risk of
  bias with **PROBAST**.
- **Prognostic factor / biomarker**: **REMARK** (+ PROGRESS-2).
- **Diagnostic accuracy**: **STARD** (+ QUADAS-2).
- **Systematic review / meta-analysis**: **PRISMA** (+ AMSTAR-2 / ROBIS). *(module `synthesis`)*
- **Protocols**: **SPIRIT** (trials).

## Descriptive & equity

- **Descriptive**: the descriptive-epidemiology framework (Lesko et al., 2022) —
  population (person/place/time), outcome/state, measure of occurrence. **PROGRESS-1**
  for simple comparisons / documenting gaps.
- **Equity / disparities**: **STROBE-Equity** (10 items) + **PROGRESS-Plus** equity
  factors (place, race/ethnicity, occupation, gender/sex, religion, education, SES,
  social capital + intersections).

## Rules

- Reporting expectations follow the TASK (see `analysis/statistical-reporting.md`).
- Every reported result maps to a checklist item; unmet items are flagged, not hidden.
