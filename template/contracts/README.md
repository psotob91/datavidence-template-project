# `contracts/` — data contracts (prerequisites for entering the pipeline)

A contract declares what a dataset **must satisfy** before it is allowed into the
analysis. Contracts are validation artifacts (e.g. with
[`pointblank`](https://rstudio.github.io/pointblank/)) — **not** a place to bury
methodological decisions (those live in `../docs/analysis/`).

Recommended files:

- `raw_<dataset>.yml` — checks for raw data **before** cleaning.
- `analysis_<dataset>.yml` — checks for analysis-ready data **before** modeling.

Each contract should state: name, purpose, source, primary key, unit of
observation, variables + types, allowed values, required-non-missing, date rules,
and **expected join cardinality** (1:1, 1:m).

## Rules

- Validate **raw** data before cleaning; validate **analysis-ready** data before
  modeling. Write validation results to `outputs/validation/`.
- **Block** analysis on a failed contract unless the exception is explicitly
  documented and accepted (record it in `docs/adr/`).
- Verify join cardinality at every join — silent row multiplication is a top
  source of invisible bugs.
