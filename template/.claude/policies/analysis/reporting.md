# Reporting

What reaches the reader is paper-ready and honest about uncertainty.

## Rules

- **Labels first.** Build a human-readable label layer (`labelled::var_label`,
  factor labels) **before** tables/figures; `gtsummary`/`gt`/`flextable` honor
  labels. What prints is legible paper labels, **never code/variable names**.
- **Match uncertainty to the quantity, by reporting task.** Report **confidence
  intervals for the estimands of interest** (effects, associations, predictions) —
  never bare point estimates or p-values alone. A **descriptive baseline /
  comparison table characterizes the study SAMPLE** and does not need inferential
  CIs or p-values for that purpose (it is describing who was studied, not estimating
  a population parameter).
  - **Exception — descriptive epidemiology:** when a descriptive quantity *is* the
    estimand and is meant to **generalize to a target population** (a prevalence /
    incidence), it carries sampling uncertainty → **report its CI** (Lesko, Fox &
    Edwards, *Am J Epidemiol* 2022). The rule is "match uncertainty to
    sample-description vs population-estimand", not "tables never get CIs".
- **No p-values in baseline/comparison tables** unless you ask. In **RCTs** this is
  required (CONSORT 2025 — testing chance imbalance after randomization is incoherent);
  in **observational** tables prefer **standardized differences (SMD)**. This is
  methodological consensus, **not** a STROBE rule.
- **Use SMD for balance** in any baseline/comparison table (RCT or observational;
  especially after matching/weighting) — not a p-value.
- **No bare "(non-)significant" dichotomies.** Report the estimate + CI and the exact
  p-value; interpret the magnitude, not a 0.05 threshold (ASA 2019).
- **Consistent rounding / significant figures** across the whole report; record
  the rule once and apply it everywhere.
