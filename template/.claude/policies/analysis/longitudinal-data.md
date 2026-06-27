# Longitudinal data (repeated measures)

IDA and analysis for repeated-measures / longitudinal data. Basis: STRATOS
longitudinal IDA (Lusa et al., STRATOS TG3, PLOS ONE 2024, `pone.0295726`).

## Initial data analysis — 5 domains, BEFORE any outcome association

- **Participation profile**: timing, number of measurements per subject, planned vs
  actual measurement times.
- **Missing values**: distinguish **non-enrollment / intermittent / drop-out / death**;
  item-level missingness; compare complete vs incomplete responders; patterns and
  predictors.
- **Univariate descriptions**: summarize baseline **and** time-varying variables.
- **Multivariate descriptions**: associations among explanatory + structural variables; stratify by
  structural variables. **Do NOT explore explanatory–outcome associations in IDA.**
- **Longitudinal aspects**: within- vs between-subject variation; **serial
  correlation**; cohort and period effects. Visualize (spaghetti / lasagna plots).

## Analysis

- Use a method that respects the correlation structure, matched to the task;
  **pre-specify** it and **declare the missingness mechanism** (MCAR/MAR/MNAR). For
  **continuous endpoints, MMRM** handles MAR dropout without explicit imputation; GEE for
  population-average (binary/count) targets. See `missingness.md`.
- Keep reshaping/derivation (long↔wide, windows) in `R/`+`targets`, reproducible (see
  `regenerables.md`). For routinely-collected longitudinal sources (EHR/claims/...),
  see the health profile's `routinely-collected-data.md`.
