# Initial data analysis (IDA)

Check the data is fit for purpose before modeling — without peeking at the
exposure–outcome association.

## Rules

- **Run a structured IDA** (STRATOS framework) before modeling: metadata + data
  cleaning, then data screening (integrity, structure, missingness, univariate and
  multivariate distributions) and the assumptions the planned analysis needs.
- **Never look at explanatory–outcome associations during IDA.** That is the line
  that separates IDA from data dredging.
- **IDA ≠ EDA.** IDA checks fitness-for-purpose; it does not hunt for findings.
- **Pre-specify an IDA plan**, separate it from inference, and produce a
  **reproducible IDA report**; fold any resulting changes into the SAP with
  justification.
- For repeated-measures data, follow `longitudinal-data.md` (5 longitudinal domains).
