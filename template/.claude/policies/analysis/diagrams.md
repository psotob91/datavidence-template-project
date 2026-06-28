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
- **ER diagrams → mermaid `erDiagram`** (tables, keys, cardinality), tied to
  `contracts/` + `metadata/`. Default to **Crow's Foot / Information Engineering
  notation** (what `erDiagram` renders) — the most readable, text-renderable,
  version-controllable option; there is **no single ISO ER notation**. If you
  specifically want an ISO-backed notation, use a **UML class diagram** (ISO/IEC 19505);
  reserve **IDEF1X** (ISO/IEC/IEEE 31320-2) for formal contractual schemas. Don't mix
  notations within a project.
- **Timelines / Gantt → mermaid `timeline` / `gantt`** (enrollment, follow-up windows,
  milestones), **code-generated**. **No ISO notation standard exists** for Gantt /
  timelines (ISO 21500/21502 cover PM *process*, not chart notation) — follow the
  convention: one clearly-labeled, monotonic time axis; **tasks as bars, milestones as
  diamonds, dependencies as arrows**; **ISO 8601 dates** (YYYY-MM-DD).
