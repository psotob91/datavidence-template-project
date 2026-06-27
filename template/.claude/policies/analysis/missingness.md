# Missing data

Missingness is a finding, not a nuisance to silently drop.

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
