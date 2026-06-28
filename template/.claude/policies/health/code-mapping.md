# Clinical code mapping (diagnoses, drugs, procedures, labs)

Mapping and grouping clinical codes (ICD, SNOMED, RxNorm/ATC, CPT/PCS, LOINC) is data
processing that silently decides what every downstream count means. Treat code sets as
**versioned, validated inputs**, not constants typed into a script.

> **Prerequisite:** `health/secondary-data.md` — RECORD code-list reporting frames this.
> **Next-if:** codes define a condition/state → `health/phenotyping.md` (comprehension gate before code).

## Rules

- **Provenance & versioning.** Every code set carries its **source + version + extraction
  date**, and is **frozen** for the study (e.g. "AHRQ Elixhauser 2026; phecodeX v1.0; pulled
  2026-06-28"). Store the list in `metadata/` and reference it from each variable's definition
  (`secondary-data.md`). Never inline an unsourced vector like `c("E11","I10")`.
- **Don't operationalize the *same* construct two ways.** Pick one grouping per variable by
  goal: **comorbidity index** (Charlson / Elixhauser) for confounding/casemix;
  **phecodes / phecodeX** (Wei Lab) for phenotype-wide grouping of ICD; **OMOP concept sets**
  (OHDSI Standardized Vocabularies) for multi-site harmonization. Using different systems for
  *different* variables in one study is fine (e.g. Elixhauser for casemix + phecodes for the
  exposure phenotype); what breaks comparability is defining one variable two ways or
  switching systems mid-pipeline.
- **Crosswalks are directional and lossy.** ICD-9↔ICD-10 GEMs, vocabulary maps, and
  national adaptations are not bijections — state the direction and **quantify the loss**
  (unmapped %, one-to-many). Re-map at the source level; don't chain lossy maps.
- **Clean in a fixed sequence** (order matters): force **character** type (never numeric) →
  trim + uppercase → ICD-9 zero-padding (**never** for ICD-10) → split WHO dagger/asterisk
  (etiology/manifestation) → handle terminal `X` carefully: in ICD-10-CM the `X` in positions
  4–6 is a **structural placeholder** holding the slot for a meaningful **7th character**
  (encounter type **A/D/S** = initial/subsequent/sequela), so **preserve all characters and
  validate against the official tabular list** rather than stripping from the right; only
  WHO-ICD-10 admin placeholder `X` (e.g. some national extracts) is safe to drop → cascade-
  truncate to the 3-char header only when a full match fails.
- **Validate before use (gates).** Report **% orphan** (unmapped), **% unspecified** (`.9`),
  **% truncated**; set WARN/FAIL thresholds and block on FAIL (`data-contracts.md`). Keep a
  transformation log (raw → clean) for reproducibility.
- **Use maintained packages — verify status, never assume.** Tool maintenance changes;
  confirm on CRAN / the upstream repo at use. As of 2026-06: the R **`icd`** package is
  **archived — avoid it**; use **`medicalcoder`** or **`comorbidity`** for Charlson/Elixhauser,
  the **`PheWAS`** package (GitHub, not CRAN) for phecode/phecodeX grouping, and OHDSI
  packages (`CDMConnector`, `FeatureExtraction`) for OMOP. **Pin versions** (`renv.lock` /
  `requirements.txt`). phecodeX codes are character-prefixed — keep them as strings.
- **Local code systems need explicit handling.** Some systems have no package (e.g. Japanese
  DPC / K-codes / YJ-codes) — build documented join tables against the official reference
  (MHLW, KEGG, UMLS); don't approximate with a foreign vocabulary.

Pairs with `secondary-data.md` (RECORD code-list reporting), `phenotyping.md` (codes feed
phenotypes), `analysis/data-contracts.md`, and `analysis/reproducibility.md`. Provenance of
these recommendations: the template repo's `docs/research/health-data-policies-research.md`.
