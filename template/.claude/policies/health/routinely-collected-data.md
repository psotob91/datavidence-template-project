# Routinely-collected data — handling & indicators

Safe, efficient construction of prevalence/incidence indicators from longitudinal
routinely-collected data (EHR, claims, surveillance, registries). Time is the easiest thing
to get wrong here, and a wrong denominator or window silently changes every rate. Pairs with
`secondary-data.md` (RECORD reporting) and `analysis/longitudinal-data.md` (repeated-measures
analysis); worked scenarios in `docs/health/indicator-scenarios.md`.

> **Prerequisite:** `health/phenotyping.md` — numerators tie to a validated phenotype.
> **Next-if:** selection-from-database flow needed → `health/study-flow.md`; reporting the study → `health/reporting-standards.md` (RECORD/RECORD-PE).

## Rules

- **Observability differs by source — never conflate.** Claims usually carry an
  **enrollment/coverage frame** (person-time even with no events); EHR shows **contacts only**
  unless a validated registration/list population exists. **A missing record ≠ absence** of
  disease, care, event, or exposure **outside approved observable time** — phrase findings as
  observed-record statements.
- **Define the denominator before the numerator.** Declare the population frame (resident /
  registered / enrolled / observed person-time / contact / point / period / …), the time
  scale, the source system, entry/exit, geography, and whether people with no records stay in
  the frame. **Never build a population denominator from an event-only table.** Compute
  person-time by **interval overlap**, not naïve `max − min`.
- **Type every window.** lookback (baseline) · washout (exclude prevalent) · clean (require no
  prior event) · confirmation (future classification) · outcome (follow-up) · risk
  (time-at-risk) · grace/gap (merge records into episodes) · eligibility (cohort membership).
  State inclusivity (`[ ]` vs `( )`).
- **Washout/lookback must sit inside observable time.** If it doesn't, **flag insufficient
  lookback** — do not silently call a case incident (standard 6–12-month washouts can still
  leave many prevalent users misclassified; Suissa). Longer washout trades sensitivity for
  specificity — choose and report it.
- **Index date is fixed; confirmation classifies, it does not move time-zero.** Shifting
  time-zero to a later confirmation date manufactures **immortal time**. Only move it if the
  estimand explicitly targets confirmed survivors.
- **Build episodes deliberately.** Sort + dedup events at the declared grain; apply allowed
  gaps, minimum duration/records, a modality hierarchy, and explicit rules for records after
  death / transfer / exit.
- **Dynamic cohorts & recurrence.** A person contributes time only while **eligible +
  observable + at-risk**. Repeated IDs can mean enrollment spells, duplicates, corrections,
  insurance transitions, or genuine re-entry — profile before collapsing. Declare the
  recurrence model: **chronic-irreversible** (one incident event ever), **recurrent-acute**
  (new events after a clean window), or **episode-based**. Re-entry is conservative: gaps are
  **non-observable**; washout does not silently span them.
- **Efficient & safe code.** Use `data.table` / DuckDB for temporal joins and windowed
  aggregation; assert no overlaps/duplicates and reconcile counts at each step
  (`analysis/data-integrity.md`, `analysis/computational-efficiency.md`). Draw the timeline **before** coding
  (`docs/health/ascii-timelines.md`); a rule you cannot draw is a rule you do not understand.
- **Numerators are observed events**, tied to a code list / phenotype (`code-mapping.md`,
  `phenotyping.md`) — not biological onset unless locally validated.

## Reporting

Report per **RECORD / RECORD-PE** (`secondary-data.md`, `reporting-standards.md`): source +
version + extraction, denominator system, numerator algorithm + validation, index/time-zero,
every window, gap/recurrence/death/censoring rules, date granularity, missingness, linkage,
and a selection flow with counts (`study-flow.md`). State the **prevalence type** (point /
period / contact) and the **incidence form** (cumulative incidence vs rate with person-time);
they are different quantities. Probe robustness to denominator, lookback, and case-definition
choices (`analysis/sensitivity-analysis.md`).

Methodological basis (citations in the template repo's
`docs/research/health-data-policies-research.md`): Bagley & Altman 2016 (EMR frequency reflects
contact, not population); Rassen et al. (Clin Epidemiol 2019; lookback choice drives estimates);
Spronk et al. 2019 (prevalence-type choice drives estimates); extended by RECORD/RECORD-PE,
ISPOR–ISPE good practices, OHDSI / DARWIN-EU `IncidencePrevalence`, and Suissa on washout /
immortal-time.
