# Study flow diagrams (by design)

A reproducible participant/selection flow, generated from data, with reconciled counts.

## By design

- **RCT**: CONSORT 2025 flow (per-timepoint counts; analysis populations) — `consort` / `flowchart`.
- **Cohort / observational selection**: participant flow — **`flowchart`** (bruigtp),
  built from the dataframe.
- **Routinely-collected / secondary data**: a RECORD-style **selection-from-database**
  flow (records in DB → after each criterion → analytic cohort), each box traceable to
  its source/step — `flowchart`. See `secondary-data.md`.
- **Systematic review**: PRISMA flow — **`PRISMA2020`**. *(module `synthesis`)*

## Rules

- **Sketch first (approval gate):** a plain-text mock (boxes + connections, **no
  numbers**) → get the user's OK → then code the real counts (see `analysis/diagrams.md`).
- Every box has a source; counts **reconcile** (in = out + excluded, at each step).
