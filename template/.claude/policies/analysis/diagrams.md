# Diagrams

Harmonized, readable diagrams for methods and results.

## Rules

- **Result / participant flow (CONSORT 2025 / cohort; PRISMA 2020 for reviews).** Build
  with the `flowchart` package (from the dataframe, reproducible). **Sketch first (approval gate):**
  write a plain-text mock (in `docs/analysis/` or the script header) with box
  words and connections only — **no numbers** — and **get the user's OK**; only
  then code the real counts.
- **Process / method flowcharts → mermaid with ISO 5807 nomenclature.**
  process = rectangle, decision = diamond, data = parallelogram, **database =
  cylinder `[( )]`**, terminator = stadium, predefined process/subroutine =
  `[[ ]]`, document = document shape. A **distinct shape per kind** + colorblind-safe
  colors (Okabe-Ito) paired with the shapes (redundant encoding) + a consistent legend.
- **Physical ER diagrams → mermaid `erDiagram`** (tables, keys, cardinality),
  tied to `contracts/` + `metadata/`.
- **Timelines → mermaid `timeline` / `gantt`** (enrollment, follow-up windows,
  milestones); use **ISO 8601 dates** (YYYY-MM-DD).
