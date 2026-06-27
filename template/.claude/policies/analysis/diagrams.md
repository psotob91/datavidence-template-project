# Diagrams

Harmonized, readable diagrams for methods and results.

## Rules

- **Result / participant flow (CONSORT / cohort).** Build with the `flowchart`
  package (from the dataframe, reproducible). **Sketch first:** a text/line mock
  with the box words and connections only — **no numbers** — agree it, then code
  the real counts.
- **Process / method flowcharts → mermaid with ISO 5807 nomenclature.**
  process = rectangle, decision = diamond, data = parallelogram, **database =
  cylinder `[( )]`**, terminator = stadium, predefined process/subroutine =
  `[[ ]]`, document = document shape. A **distinct shape per kind** +
  differentiated colorblind-safe colors + a consistent legend.
- **Physical ER diagrams → mermaid `erDiagram`** (tables, keys, cardinality),
  tied to `contracts/` + `metadata/`.
- **Timelines → mermaid `timeline` / `gantt`** (enrollment, follow-up windows,
  milestones).
