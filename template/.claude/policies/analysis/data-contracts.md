# Data contracts

Prerequisites a dataset must meet to enter the pipeline. Pairs with `contracts/`
and the `/datavidence-healthdata:data-contract` skill. See also `data-integrity.md`:
contracts validate **at the gates**; integrity guards **in-pipeline** joins and
transforms.

## Rules

- **Validate at the gates.** Check raw data against its contract **before**
  cleaning; check analysis-ready data **before** modeling (e.g. `pointblank`).
- **Record results.** Write validation output to `outputs/validation/`.
- **Block on failure.** A failed contract stops the analysis unless the exception
  is explicitly documented and accepted in `docs/adr/`.
- **Contracts state prerequisites, not methods.** Keys, types, allowed values,
  required-non-missing, join cardinality — yes. Methodological choices belong in
  `docs/analysis/`, not here.
