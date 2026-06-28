# Longitudinal data (repeated measures)

IDA and analysis for repeated-measures / longitudinal data. Basis: STRATOS
longitudinal IDA (Lusa et al., STRATOS TG3, PLOS ONE 2024, `pone.0295726`).

> **Prerequisite:** `analysis/initial-data-analysis.md` — IDA (repeated-measures branch) precedes this.
> **Next-if:** estimand is marginal/population-average → `analysis/correlated-data.md` (GLS/GEE choice); MAR dropout in continuous endpoints or dynamic-vs-fixed-time prediction → `analysis/missingness.md`.

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

- Use a method that respects the correlation structure, matched to the task and the
  **estimand**; **pre-specify** it and **declare the missingness mechanism**
  (MCAR/MAR/MNAR). **Mixed / MMRM** fits **subject-specific** targets or **MAR-dropout
  continuous endpoints** (MMRM handles MAR dropout without explicit imputation). When the
  estimand is **marginal / population-average**, prefer **GLS** (continuous, serial
  outcome — see `correlated-data.md`) or **GEE** (binary/count). See `missingness.md`.
- Keep reshaping/derivation (long↔wide, windows) in `R/`+`targets`, reproducible (see
  `regenerables.md`). For routinely-collected longitudinal sources (EHR/claims/...),
  see the health profile's `routinely-collected-data.md`.

## By analysis goal

The longitudinal toolkit differs by task — never import one goal's method into another
(e.g., reading a prediction model's coefficients causally).

- **Causal** (effect of a time-varying treatment): when a confounder is **time-varying
  and itself affected by prior treatment** (confounder *and* mediator), standard
  regression is biased *either way you turn* — adjusting blocks part of the effect and
  opens a collider path; not adjusting leaves confounding. Use **g-methods**:
  parametric **g-formula**, **marginal structural models via IPTW** (stabilized weights;
  check/trim extremes), or **g-estimation**; frame the contrast as **sustained
  strategies / dynamic treatment regimes**, not a single coefficient. Basis: Robins;
  Hernán & Robins, *Causal Inference: What If* (2020); Naimi, Cole & Kennedy, *Int J
  Epidemiol* 2017; Daniel et al., *Stat Med* 2013.
- **Prediction**: distinguish **fixed-time (baseline)** from **dynamic** prediction.
  For fixed prediction, use **only predictors measured at or before the prediction time
  origin (startpoint)** — using any later value leaks the future (immortal-time / data
  leakage). For prediction that updates over follow-up, use **landmarking** (van
  Houwelingen & Putter, 2012) or **joint longitudinal–survival models** (Rizopoulos,
  2012; `JM`/`JMbayes`); report time-dependent discrimination **and** calibration. Do
  not interpret predictor coefficients causally.
- **Description**: start with **spaghetti / mean-profile plots** and the 5-domain IDA
  above; for population-average change a **mixed-effects growth model or GEE** is often
  enough. Trajectory-clustering (**GBTM / LCGA / GMM**) is a *descriptive* device only —
  **classes are over-extracted** (fit indices favour more classes than are real), so
  report BIC/entropy/min class size, sensitivity-test the class count, and never reify
  classes as real subgroups (contested: Nagin & Odgers 2010; van der Nest et al. 2020).
