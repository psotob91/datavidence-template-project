# Initial data analysis (IDA)

Check the data is fit for purpose before modeling — without peeking at the
exposure–outcome association.

## Rules

- **Run the STRATOS 6-phase IDA** before modeling: metadata setup → data cleaning →
  **data screening** (missing values; univariate & multivariate descriptions;
  sample-size / subgroup adequacy; influential observations) → initial data reporting →
  refine the analysis plan → document. (Functional-form and collinearity screening of
  predictors **is** IDA; only outcome-model checks — residual diagnostics, PH tests —
  belong to the modeling phase.)
- **Never look at explanatory–outcome associations during IDA.** That is the line
  that separates IDA from data dredging.
- **IDA ≠ EDA.** IDA checks fitness-for-purpose; it does not hunt for findings.
- **Pre-specify an IDA plan**, separate it from inference, and produce a
  **reproducible IDA report**; fold any resulting changes into the SAP with
  justification.
- For repeated-measures data, follow `longitudinal-data.md` (5 longitudinal domains).
