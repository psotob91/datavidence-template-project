# Reproducibility

A fresh clone plus `make all` must rebuild every result from input + code alone.

## Rules

- **Seeds via the pipeline.** Set `tar_option_set(seed = N)` so each target gets a
  deterministic seed; don't rely on a single top-level `set.seed()`. For parallel
  work use `RNGkind("L'Ecuyer-CMRG")` + `future`/`furrr` with `seed = TRUE`. Seed
  CV / bootstrap too.
- **Pin the environment.** `renv.lock` is **committed**; record the R version. Fix
  `TZ` and `LC_COLLATE` (deterministic dates & sorting); use UTF-8.
- **Capture `sessioninfo`** with every output bundle.
- **Provenance stamp.** Stamp each output with the commit SHA, the input data
  hash, and a timestamp.
