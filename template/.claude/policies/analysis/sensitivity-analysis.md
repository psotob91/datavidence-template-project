# Sensitivity analysis

Show that conclusions survive reasonable alternative choices.

## Rules

- **Pre-specify the key ones:** alternative definitions, inclusion criteria,
  missing-data and outlier handling, and modeling choices.
- **Reuse the pipeline.** Organize data and code so an alternative analysis
  re-runs the pipeline with different parameters — not a copy-paste fork.
- **Use principled methods for missing data.** Under plausible MNAR, use reference-based
  MI or tipping-point (see `missingness.md`); LOCF/BOCF and best-/worst-case single
  imputation are deprecated even as sensitivity analyses.
- **Report alongside the primary.** Agreement strengthens the result; divergence
  is disclosed, not buried.

## By analysis goal

- **Causal:** stress the *unverifiable identifying assumptions*. Run **quantitative bias
  analysis (QBA)** for unmeasured confounding, **misclassification**, and **selection
  bias** (prefer probabilistic over single-value; Lash, Fox et al. 2021). Report the
  **E-value** (VanderWeele & Ding, *Ann Intern Med* 2017) at **both the point estimate
  and the CI limit nearest the null** — but **as a screening device, not a verdict**:
  it is a near-monotone transform of the estimate, has no "large enough" threshold, and
  ignores non-confounding bias (critique: Ioannidis, Tan & Blum 2019). Add **negative
  controls** (Lipsitch et al. 2010) and **tipping-point** analyses that **name the
  plausible confounders**, not "residual confounding" in the abstract.
- **Prediction:** show performance is not a pipeline artifact. Quantify optimism by
  **bootstrap correction** (not a single split); test transportability with
  **internal–external (cluster / temporal / geographic) validation**; vary predictor /
  outcome definitions, modeling method, and **missing-data handling**; report
  **calibration stability** (slope/intercept, curve) and **subgroup / fairness**
  robustness. Basis: Steyerberg 2019; Steyerberg & Harrell, *J Clin Epidemiol* 2016;
  TRIPOD+AI (Collins et al., *BMJ* 2024).
- **Description:** re-estimate under alternative **case / exposure definitions and
  inclusion criteria**; show sensitivity to **standardization and weighting** choices
  (alternative standard populations; direct vs indirect); treat **sample-vs-target
  divergence** as a quantifiable bias (generalize / transport), and probe **MNAR /
  tipping-point** for missingness. Basis: Lesko, Fox & Edwards, *Am J Epidemiol* 2022.
