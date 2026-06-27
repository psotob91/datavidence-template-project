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
