# Rescue manifest (rehearsed on the tsukuba study)

A worked example of "salvage only what matters into a fresh template-based project",
used to design a generic `rescue-manifest` skill/policy. Decisions: KEEP · DROP
(regenerable) · KEEP-EXTERNAL (never in repo).

## Raw data — KEEP-EXTERNAL (never in repo)

The harmonized claims bundle (~27 GB) lives at `C:\tsukuba-internship-coding\claims_harmonization`
(`TSUKUBA_DATA_ROOT`). procedure.csv 11.8 GB, drug.csv 8.2 GB, diagnosis.csv 6.0 GB,
+ patient/geography/facility/checkup. **Never copy into the repo** — register the path
in `metadata/provenance.yaml`; connect via env var + symlink/junction.

## KEEP (carry to the new project)

| Item | Class | Destination |
|---|---|---|
| `metadata/provenance.yaml`, `data_dictionary.csv`, `phenotype_code_lists.yaml`, `charlson_quan2011_map.csv`, `reporting_guideline_map.yml`, `r_package_registry.yml` | practice | `metadata/` |
| `dictionaries/tsukuba_claims/external/` (KEGG, WHO ICD-10 zip), `translation_maps/who_icd10_2019_verified.csv`, `manual/…`, registries, `README.md` | practice | `metadata/dictionaries/…` |
| `analysis-plan/` (sap, estimand, objectives, data-prep, qc, missing-data, sensitivity, decision-matrix, spatial) | practice | `analysis-plan/` |
| `protocol/source/*.docx` | practice (human-canonical) | `protocol/source/` |
| `analysis/{decision_log, assumption_register, bias_risk_register, attrition_log, claims}` | practice (living records) | `analysis/records/` |
| `policies/` (the 11 governance files) | governance | mostly superseded by template policies — mine for any gaps |
| `validation/*.R`, `scripts/{generate_data_lock,audit_reproducibility,protocol_*}.R/.py` | code | `scripts/`, `validation/` |
| `questionnaires/*` (unresolved-questions workbook) | practice | `docs/open-questions/` |
| `papers-methods-reference/*/source/` (PDFs) | reference | `context/papers/…/source/` |

## DROP (regenerable — rebuild in the new project)

`protocol/derived/{chunks,index,logs,md,tables/*.html,*.json}`, `papers/*/rag/`,
`_index/*.jsonl`, `metadata/repo_file_index.csv`, `dictionaries/.../derived/*`,
empty `.gitkeep` stubs, `~$*.docx`, **all of `server_payload/`**.

## Scrub before copy

`dictionary_manifest.json`, `config/project.yml`, `provenance.yaml` embed hard-coded
absolute paths (`C:\data-tsu\…`, `C:\tsukuba-internship-coding\…`) → parameterize.

## Metadata taxonomy (the two classes, kept separate)

- **(a) practice** — travels in a data-deposit package: dictionaries, code lists,
  provenance, codebooks, external reference downloads, verified translation maps.
  → `metadata/`.
- **(b) agent** — for AI navigation, regenerable: `knowledge_index.yml`,
  `repo_file_index.csv`, chunked text, RAG/GraphRAG indexes, protocol-derived specs.
  → `context/` (gitignored where regenerable).

## Seeds for a generic `rescue-manifest` skill/policy

1. **Required fields per entry:** `item`, `class` (raw / metadata-practice /
   metadata-agent / code / document / derived), `decision` (KEEP / DROP / REGENERATE /
   KEEP-EXTERNAL), `destination` (template slot), `why` (irreversibility/regenerability),
   `flag` (large-binary / sensitive / hard-coded-path / stale-on-copy / needs-update).
2. **Regenerability test:** if it rebuilds from in-repo sources in <30 min without human
   judgement → DROP/REGENERATE, don't carry.
3. **Archivist test (for metadata):** would a data archivist include it in a deposit
   package? yes → `metadata/` (practice); no → `context/` (agent).
4. **Hard-coded-path audit:** grep every config/manifest for absolute paths before
   copying; flag `needs-update`.
5. **Size gate:** any class-agent file > 1 MB requires an explicit `justification` or
   auto-proposes DROP.
