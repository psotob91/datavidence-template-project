# Missing data

Missingness is a finding, not a nuisance to silently drop.

## Rules

- **Account for every row.** Report N at each pipeline stage and explain every
  dropped or excluded record (a reconciled flow, not a vanishing count).
- **Detect → inspect → reason → handle, in that order.** Inspect patterns
  (e.g. `naniar`) and state the assumed mechanism (MCAR / MAR / MNAR) explicitly
  before choosing a treatment.
- **No silent listwise deletion.** Choose handling deliberately — justified
  complete-case or multiple imputation (`mice`) — and document why.
- **Show it.** Report missingness in descriptive output; never hide it.
