# Longitudinal data (repeated measures)

IDA and analysis for repeated-measures / longitudinal data. Basis: STRATOS
longitudinal IDA (Huebner et al., PLOS ONE 2023, `pone.0295726`).

## Initial data analysis — 5 domains, BEFORE any outcome association

- **Participation profile**: timing, number of measurements per subject, planned vs
  actual measurement times.
- **Missingness**: distinguish **non-enrollment / intermittent / drop-out / death**;
  item-level missingness; compare complete vs incomplete responders; patterns and
  predictors.
- **Univariate**: summarize baseline **and** time-varying variables.
- **Multivariate**: associations among explanatory + structural variables; stratify by
  structural variables. **Do NOT explore explanatory–outcome associations in IDA.**
- **Longitudinal aspects**: within- vs between-subject variation; **serial
  correlation**; cohort and period effects. Visualize (spaghetti / lasagna plots).

## Analysis

- Use a method that respects the correlation structure (mixed models / GEE / etc.)
  matched to the task; **pre-specify** it. Account for the dropout/missingness mechanism.
- Keep reshaping/derivation (long↔wide, windows) in `R/`+`targets`, reproducible (see
  `regenerables.md`). For routinely-collected longitudinal sources (EHR/claims/...),
  see the health profile's `routinely-collected-data.md`.
