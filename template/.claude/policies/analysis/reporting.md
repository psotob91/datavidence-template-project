# Reporting

What reaches the reader is paper-ready and honest about uncertainty.

## Rules

- **Labels first.** Build a human-readable label layer (`labelled::var_label`,
  factor labels) **before** tables/figures; `gtsummary`/`gt`/`flextable` honor
  labels. What prints is legible paper labels, **never code/variable names**.
- **Always report uncertainty.** Estimates with confidence intervals — not bare
  point estimates or p-values alone.
- **No p-values in group-comparison tables** (descriptive "Table 1" of the whole
  population, or a "Table 2" comparing groups) — STROBE-aligned — **unless you
  explicitly ask** for them.
- **SMD only for causal-inference balance** in observational studies (e.g., after
  matching/weighting), not as a routine descriptive statistic.
- **Consistent rounding / significant figures** across the whole report; record
  the rule once and apply it everywhere.
