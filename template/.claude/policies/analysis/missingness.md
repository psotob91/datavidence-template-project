# Missing data

Missingness is a finding, not a nuisance to silently drop.

> **Next-if:** longitudinal continuous endpoint with MAR dropout (MMRM), or dynamic-vs-fixed-time prediction (immortal-time) → `analysis/longitudinal-data.md`.

## Rules

- **Account for every row.** Report N at each pipeline stage and explain every
  dropped or excluded record (a reconciled flow, not a vanishing count).
- **Detect → inspect → reason → handle, in that order.** Inspect patterns
  (e.g. `naniar`) and state the assumed mechanism (MCAR / MAR / MNAR) explicitly
  before choosing a treatment.
- **No silent listwise deletion; match the method to the mechanism.** Default to
  **multiple imputation** (`mice`, **M ≥ 20** — the package default of 5 is too few;
  `pmm` for non-normal variables); reserve complete-case for **confirmed MCAR with
  minimal loss**. For **longitudinal continuous** endpoints, **MMRM** handles MAR
  dropout without explicit imputation. **LOCF / BOCF / WOCF are deprecated — do not use.**
- **MNAR ⇒ pre-specified sensitivity.** When MNAR is plausible, pre-specify a sensitivity
  analysis (reference-based MI or tipping-point); best-/worst-case single imputation is
  deprecated.
- **Show it.** Report missingness in descriptive output; never hide it.

## By analysis goal

The handling rule follows the estimand.

- **Causal:** the imputation model must be **congenial / compatible with the substantive
  model** — include the exposure, outcome, all confounders, and any interactions /
  non-linear terms in the same form (prefer **SMC-FCS** when the analysis has
  interactions or splines). **Impute missing confounders** rather than dropping them
  (complete-case discards adjustment and can bias the effect); impute the outcome with
  caution ("impute then delete") and run an **MNAR sensitivity analysis** — MAR-based MI
  is never sufficient evidence of robustness. Basis: Sterne et al., *BMJ* 2009; White,
  Royston & Wood, *Stat Med* 2011; Bartlett et al. (SMC-FCS), *Stat Methods Med Res* 2015.
- **Prediction:** development-time and **deployment-time** missingness differ — the
  deployed model must return a prediction for a **single new patient** with missing
  predictors, without using the outcome or any post-baseline info. Use **pattern
  submodels** or **deployment-ready conditional imputation** (re-applicable to one
  record), and keep development and deployment handling matched (else calibration
  drifts). **Contested — the missing-indicator method:** discouraged etiologically (biases
  effects) but **defensible in prediction** *iff* the missingness mechanism is stable
  between development and deployment; if it shifts, it degrades calibration. Basis:
  Hoogland et al., *Stat Med* 2020; Sisk et al., *Stat Methods Med Res* 2023; Steyerberg 2019.
- **Description:** for estimands meant to **generalize** (prevalence/incidence/means),
  use **MI or survey/IP weighting**, not complete-case (unbiased only under MCAR); report
  completeness (n/% missing, by subgroup) and, where feasible, the estimate both
  complete-case and after MI/weighting. Basis: Sterne et al., *BMJ* 2009; Carpenter &
  Kenward 2013.
