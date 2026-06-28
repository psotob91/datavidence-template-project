# Audit — `geographic-variation-dyalisis-tsukuba` (Codex-era repo)

Date: 2026-06-28 · Read-only audit (3 Sonnet explorers) of
`C:\tsukuba-internship-coding\geographic-variation-dyalisis-tsukuba`
(maintenance-dialysis geographic-variation study, Tsukuba claims; built with Codex).
`methodology-policy-kits/` excluded (already used for the RAG).

Purpose: mine the repo for (i) lessons to improve the template / skills / hooks,
(ii) what to **salvage** into the new template-based project (see
[`rescue-manifest.md`](rescue-manifest.md)), and (iii) what to **avoid**.

## Headline

The owner's instincts were sound; the repo had the right *ideas* but lacked
**enforcement** and **clean separation**. The wins to carry forward are mechanisms,
not content.

## Lessons → proposals (policy / skill / hook)

| Finding (what the repo did) | Gap | Proposal |
|---|---|---|
| Pre-registration exists but **distributed** across `sap.md` + `estimand.yaml` + `objectives.yaml` + a 1,600-line decision matrix; no single lockable artifact. | No canonical, lockable pre-registration; nothing blocks analysis before it's set. | **One lockable pre-registration artifact** + skill `frame-study`/`prespecify-estimand` (already in portfolio) to harmonize arbitrary inputs into it + **new hook `sap-lock`** (file-existence gate like their `data_lock.json` — the most reliable gate they had). |
| `attrition_log.csv` already carries an **`excludes_target_population`** boolean (= the target/accessible/sampled/study cascade; gives the two-branch STROBE flow). | No mechanism forces each filter to log its counts; flow diagram is retrospective. | Skill `emit-attrition-step` (R fn + testthat fixture) + **hook**: a script that filters rows but doesn't call `log_attrition()` is flagged. Standardize `excludes_target_population`. Flow inputs accumulate *from the start*. |
| Population cascade present but not a named schema. | Not machine-tracked. | `population_cascade.yaml` (counts per level) + a policy; light hook checks both branches exist. |
| `variable_spec_catalog.yaml` schema is excellent (variable_id, analytic_role, source, grain, derivation, qc, status, provenance) but a **stub**. | Productive scripts can use unmapped variables. | Skill to populate it + **hook** blocking scripts that reference `status: unknown` variables (their `<<PENDING_CONFIRMATION_Q3>>` nephrology gap would correctly block). |
| `source/`(human .docx) vs `derived/`(agent) is the right model; uses `<<PENDING_CONFIRMATION_Qn>>` anti-hallucination sentinels. | `protocol/derived/` sits *inside* `protocol/` and looks paper-ready; `sap.md` mixes PI prose with agent reformulations → contamination. | Template structure: human-canonical `source/`; agent-derived under `context/` (regenerable, gitignored); **routing** that sends human-only on request, human+AI by default. Keep the PENDING sentinels. |
| Two metadata classes **mixed**: agent nav (`knowledge_index.yml`, `repo_file_index.csv`) sit in `metadata/` next to practice metadata (`data_dictionary.csv`, `provenance.yaml`). | Can't tell practice from agent at a glance. | Separate: `metadata/` = practice; `context/`/`docs/nav` = agent. Heuristic = **the archivist test**: "would a data archivist include this in a deposit package?" yes→metadata, no→context. |
| `data_lock.json` "no modeling before this file exists" is the **one hard, machine-checkable gate** and the most reliable thing in the system. | — (validate) | Replicate the file-existence-gate pattern for `sap_lock.json`, `variable_catalog` completeness, etc. |

## Anti-patterns to avoid (and template gaps to close)

- **`server_payload/` = 8 docs, zero code** — over-engineered offline-transfer scaffold.
  Replace with: a transfer script that strips agent dirs + `config/paths.local.yml`
  (gitignored) + a **symlink/junction to the data root** + one `docs/server_setup.md`.
  (Confirms the owner's simplification.)
- Committed regenerables (protocol table HTML/CSV/JSON, `*.jsonl` indexes), an 8 MB
  worklist CSV, duplicate `.docx` at root+`source/`, `~$*.docx` lock files, a `src/`
  tombstone dir, **7 overlapping navigation surfaces**, dual `.claude`/`.codex` agent
  defs needing manual sync.
- **Template `.gitignore` should ship** rules for: `~$*`, `**/derived/**` table/jsonl
  extractions, large `**/worklists/*.csv`, generated indexes. A clearly-named
  gitignored **scratch/agent-context** dir for private profiling notes (row counts).

## What this adds beyond the portfolio vote

The 280-judge vote decided *policies→skills*. This audit adds the **enforcement
layer** (the owner's "mandatory" paradigm) + **structure**, folded into the blueprint
backlog: hooks `sap-lock` / `attrition-log` / `variable-catalog-gate`; the canonical
lockable pre-registration artifact + `population_cascade.yaml` + the
`excludes_target_population` standard; a generic `rescue-manifest` skill; and the
human/agent + metadata-taxonomy structure changes.

Next block (owner-chosen): **design the pre-registration system** (the lockable
artifact + `sap-lock` hook + fill-from-arbitrary-inputs).
