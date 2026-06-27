# `data/` — the data taxonomy

This folder separates **inputs** (persistent, versioned) from **derived data**
(regenerable, never versioned). The rule that makes the project portable and
auditable: **only inputs + code go to git; everything else regenerates.**

## `data/raw/` — inputs (immutable, persistent)

Original source data. **Never edited in place** — every transformation happens
in code. Two ways data gets here:

- **Copied** (light datasets): the file lives in `data/raw/` and is committed.
- **Connected** (heavy or private/external data): the file stays at its origin
  and the project points to it through `config.yml` (git-ignored) — see
  `../config.example.yml`. Move the project to another machine → fix the path in
  `config.yml` → everything reruns. **Never hardcode absolute paths.**

Record provenance (source, date, checksum) for each raw input in `../metadata/`.

> Inputs you (or the agent acting as an expert) author as part of the analysis —
> coding schemes, mapping tables, curated reference inputs — are **also inputs**:
> they persist, are committed, and travel with the repo. They are *not* derived.

## `data/derived/` — intermediates & processed outputs (regenerable)

Built by the pipeline (`{targets}`). **Git-ignored**; rebuilt from raw + code
with `make reset && make all`. Do **not** commit anything here and do **not**
keep `_v` copies — provenance is a checksum in `../metadata/`, not a duplicate.

## Why this matters

Cloning the repo on any PC and running `make all` must reproduce every derived
artifact from `data/raw/` + code alone. `make reset` (`tar_destroy()` + clean
derived) lets you rebuild from zero to verify full reproducibility.
