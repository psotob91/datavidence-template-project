# Reporting

What reaches the reader is paper-ready and honest about uncertainty.

## Rules

- **Labels first.** Build a human-readable label layer (`labelled::var_label`,
  factor labels) **before** tables/figures; `gtsummary`/`gt`/`flextable` honor
  labels. What prints is legible paper labels, **never code/variable names**.
- **Always report uncertainty.** Estimates with confidence intervals — not bare
  point estimates or p-values alone.
- **Prefer standardized differences (SMD) over p-values for baseline balance.**
  p-values in descriptive ("Table 1") comparisons are usually inappropriate (they
  test a hypothesis you don't have) — omit them in RCTs and use with caution
  elsewhere.
- **Consistent rounding / significant figures** across the whole report; record
  the rule once and apply it everywhere.
