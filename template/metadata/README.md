# `metadata/` — machine-readable, neutral reproducibility metadata

Neutral, shareable, agent-independent metadata that lets a human (or machine)
understand and reproduce the analysis. Recommended files:

- `data_dictionary.csv` — the **machine-readable codebook** (always present):
  one row per variable with `variable, label, type, unit, allowed_values,
  missing_codes, source, derivation, notes`.
- `data_sources.yml` — provenance of each raw input: source, date, **checksum**,
  access (copied vs. connected), license/limitations.
- `variable_index.yml`, `table_index.yml`, `figure_index.yml` — indices linking
  artifacts back to the code that produced them.

## Two codebooks, on purpose

- **Machine-readable** (here, `data_dictionary.csv`) — for reproducibility and
  tooling. Always maintained.
- **Didactic human codebook** — a rich, readable view of the data structure,
  generated on demand (e.g. `summarytools::dfSummary`). Different artifact,
  different audience.

## Rule

If something is needed for a human to **understand, reproduce, or audit** the
analysis, it belongs here (or in `../docs/analysis/`, `../contracts/`, `R/`,
`tests/`, `outputs/`) — **never only** in an agent cache (`_agent_cache/`).
