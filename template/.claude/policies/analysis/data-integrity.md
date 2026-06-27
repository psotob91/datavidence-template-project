# Data integrity

Protect the data from silent corruption between `data/raw` and analysis.

## Rules

- **Raw is immutable.** Never edit source data in place. Every change is code in
  the pipeline (`data/raw` → `data/derived`), reproducible from scratch.
- **Declare and verify join cardinality.** State the expected relationship
  (1:1, 1:m) at every join and assert row counts before/after. Silent row
  multiplication from a bad key is a top source of invisible error.
- **Control types explicitly.** Set factor levels deliberately; parse dates with
  an explicit format (`clock` / `lubridate`). Never rely on silent coercion.
- **Range & key checks.** Validate plausible bounds and allowed levels on key
  variables, and uniqueness of keys assumed unique, before analysis.
