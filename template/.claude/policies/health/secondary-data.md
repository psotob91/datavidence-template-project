# Secondary / routinely-collected data (RECORD)

For studies using routinely-collected health data (EHR, claims, registries,
surveillance), report per **RECORD** (an extension of STROBE; pharmacoepidemiology:
**RECORD-PE**).

## Report (RECORD essentials)

- **Data source(s)**: each database, its **version**, the **extraction date**, coverage,
  and any **linkage** between sources with its quality/QC. Keep a **data-source table**
  in `metadata/`.
- **Code lists / phenotype algorithms** used to define exposures, outcomes, and
  covariates (include the codes or a precise reference), and how they were validated.
- **Population selection hierarchy**: how the study population was derived **from the
  database** — each step with counts (a RECORD-style selection flow; see `study-flow.md`).
- **Data cleaning** and handling of unexpected values.

## Rules

- Validate the extracted data against a contract before use (`data-contracts.md`).
- Every analysis variable's definition traces to its code list / algorithm.
- Safe, efficient handling of **longitudinal** routinely-collected data (windows,
  numerators/denominators) lives in `routinely-collected-data.md`.
