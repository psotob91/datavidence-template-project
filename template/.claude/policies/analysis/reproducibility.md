# Reproducibility

A fresh clone plus `make all` must rebuild every result from input + code alone.

## Rules

- **Seeds via the pipeline.** Set `tar_option_set(seed = N)` so each target gets a
  deterministic seed; don't rely on a single top-level `set.seed()`. For parallel
  work use `RNGkind("L'Ecuyer-CMRG")` + `future`/`furrr` with `seed = TRUE`. Seed
  CV / bootstrap too.
- **Pin the environment.** `renv.lock` is **committed** (it pins packages, not R itself or
  system libraries); for bit-level reproducibility pin R too via a Docker image (e.g.,
  `rocker/r-ver` by **SHA-256 digest**, not a floating tag). Fix `TZ` and `LC_COLLATE`
  (deterministic dates & sorting); use UTF-8.
- **Capture `sessioninfo`** with every output bundle.
- **Provenance stamp.** Stamp each output with the commit SHA, the input data
  hash, and a timestamp.
