# Blueprint — `datavidence-healthanalysis` plugin (PENDING, not built)

**Status: pending.** This is a spec for a future companion plugin, to be built in a later
session by an agent that consults this repo. Nothing here is installed or wired yet. It lives
at the template-repo root (not rendered into children).

## Why a plugin (vs more policies)

The `health/` policies (`code-mapping.md`, `phenotyping.md`, `routinely-collected-data.md`) +
the `docs/health/` companion are the **methodology** (human source of truth, shipped to
children). A plugin would add the **mechanism**: skills that scaffold/validate, and hooks that
enforce, the same rules — versioned and DRY, exactly as `psotobverse-utils` carries the
meta-learner mechanism. Generic MECHANISM → plugin; DATA + CONFIG + routing stays local
(the lesson from the meta-learner refactor — see `learning/LEARNING_LOG.md`).

## Already shipped generically — do NOT rebuild (updated 2026-06-28)

The routing / comprehension / recall **mechanism is now generic** and lives in
`psotobverse-utils` (≥ v1.7.0). This plugin **consumes** it; it must not reimplement it:

- **Conditional routing** — `policy_router.py` (additive reminders) reads the child's
  `template/.claude/policy/routing.yml` (already shipped). The health routing edges
  (codes → code-mapping → phenotyping → routinely-collected-data; the data→causal fork)
  are **data rows** there, not plugin code.
- **`timeline-before-pseudocode`** — delivered by the generic `comprehension_gate.py`
  driven by the `phenotype-timeline-gate` rule in `routing.yml` (mode `block`: asks before
  writing `*phenotype*` code when no sibling timeline/decision artifact exists). The plugin
  does **not** need its own version of this hook — see the revised hooks table.
- **Comprehension gate (explain-back) + recall** — `/comprehend` and `/coverage` are
  generic commands; `coverage` is benchmarked (`eval/coverage/`: union recall 1.00).
- **Adversarial review** — `/cross-examine` is generic.

So this plugin's real surface shrinks to: **domain validating skills + domain-specific
hooks the generic engine cannot cover + `routing.yml` data** (the data already ships from
the factory). DATA + CONFIG stay in the factory/child; only domain MECHANISM lives here.

## Name

Use **`datavidence-healthanalysis`** (this is what `template/.claude/policies/analysis/
methods-documentation.md`'s `notation-check` hook already references). The older
`temporal-expansion-ideas/datavidence_integrated_final/` docs call it `datavidence-healthdata`
— that is drift; standardize on `datavidence-healthanalysis` when building.

## Skill & hook portfolio (decided 2026-06-28)

Decided by a **280-judge self-consistency vote** (40 policies × 7 Sonnet replicas) under the
EQUATOR/STRATOS framing — these analysis frameworks ARE health-methodology, so they live here,
not in `psotobverse-utils`. Raw verdicts: `docs/plugins/evidence/skill-hook-portfolio-vote.json`.
Result: 17 skill / 2 hook / 21 policy-only. Granularity = **consolidated** (same-shape scaffolders
merged): the original 3-skill list was a large undercount.

### Skills — MUST (10)

| Skill | Does | Covers policy/-ies | Vote |
|---|---|---|---|
| `onboard-data` | Connect/copy data per the taxonomy; portable config; minimal provenance docs. | data-onboarding | 1.00 |
| `validate-data-contract` | Validate raw + analysis-ready data at the gates; block on failure; record results. | data-contracts | 1.00 |
| `run-ida` | Scaffold + run STRATOS initial data analysis; **longitudinal mode** for the 5-domain repeated-measures IDA. | initial-data-analysis **+** longitudinal-data | 1.00 (merged) |
| `frame-study` | Scaffold the analysis plan/SAP: pre-specify the estimand/outcome, classify the task→methods (STRATOS/SAMBR), and select the EQUATOR reporting guideline. | pre-specification **+** statistical-reporting **+** reporting-standards | 0.71–1.00 (merged) |
| `validate-assumptions` | Generate the right residual/assumption diagnostics per model; graphics-first. | model-assumptions | 1.00 |
| `assess-missingness` | Profile missingness, reason about mechanism (MCAR/MAR/MNAR), propose handling (MI/MMRM) + sensitivity. | missingness | 0.57† |
| `map-clinical-codes` | Validate a code set: provenance/version stamp, cleaning sequence, orphan/unspecified/truncated gates, archived-package flag. *(absorbs the old `code-provenance` check.)* | code-mapping | 0.71 |
| `phenotype-gate` | Generate the phenotype-spec with comprehension-gate sections (restate, ≥2 examples/counter-examples, ASCII decision+timeline), then pseudocode + test-fixture stubs — code withheld until sign-off. | phenotyping | 0.71 |
| `design-indicator` | Scaffold/review a denominator→numerator→window→episode design against the integrity checklists; returns findings or `PENDING_LOCAL_DECISION`. *(absorbs the old `denominator/numerator-integrity` checks.)* | routinely-collected-data | 0.86 |
| `scaffold-reporting` | Produce an EQUATOR-aligned reporting artifact, by **type**: RECORD data-source table (secondary-data) · Table 1/2 with gtsummary (clinical-tables) · CONSORT/STROBE/PRISMA participant-flow diagram (study-flow). | secondary-data **+** clinical-tables **+** study-flow | 0.86 (merged) |

### Skills — OPTIONAL
- `specify-regression` (regression-modeling, 0.86 / priority optional) — scaffold a regression spec
  (no dichotomizing; splines; penalize sparse-data/separation).
- *Deferred (panel split):* `specify-sensitivity-plan` (sensitivity-analysis, 0.57†). *Panel said
  policy-only (mostly):* `review-outliers` (outliers), `big-data-triage` (computational-efficiency),
  `draft-diagram` (diagrams) — revisit only if real need appears.

### Hooks

| Hook (event) | Does | Vote |
|---|---|---|
| `guard-data-export` (PreToolUse) | Ask/flag on a write that would send identifiable data outside the project (egress guard). **New — strongly endorsed.** | 0.86, must |
| `notation-check` (PostToolUse/edit) | Flag methods text whose math symbols are absent from the notation registry; wire `methods-documentation.md` to it. | 0.71, optional |

**Reclassified / not built as separate hooks:** `code-provenance` → folded into `map-clinical-codes`;
`denominator/numerator-integrity` → folded into `design-indicator`; `timeline-before-pseudocode` →
already generic (`routing.yml` + `comprehension_gate.py`). †`assess-missingness` an optional hook may
follow later; the panel split skill vs skill+hook.

## Reuse the agent-index retrieval pattern

The Tsukuba kit (`methodology-policy-kits/ehr-claims-longitudinal/agent_index/`) is the model
for cheap agent navigation of heavy content: `AGENT_ENTRYPOINT.md` + `routing.yml`
(intent → 1–3 files) + `lookup_cards.yml` (guardrails) + `scenario_router.yml` (load scenario
IDs, not whole corpora). If the plugin ships a large reference/scenario corpus, generate this
index with a script (don't hand-write JSON/YAML "for the agent") and keep the machine layer
**derived, separate, and deletable** from the human methodology.

## Build order (when picked up)

Repo state as of 2026-06-28: the plugin repo exists at `C:\workspace\datavidence-healthanalysis`
(remote `github.com/psotob91/datavidence-healthanalysis`), **scaffolded + self-hardened** (its own
`.claude/` governance, hygiene, CI, safe-edit protocol) but still **v0.0.1 with no domain skills/
hooks**. So steps 1–2 below are largely done; start at 3.

1. Read `docs/research/health-data-policies-research.md` + the three `health/` policies + the
   `docs/health/` companion (the contract the plugin must enforce).
2. ~~Scaffold~~ (done) — the plugin skeleton, manifest, governance, and CI are in place.
3. Implement the **10 must-build skills** + the `guard-data-export` hook from the portfolio above
   (thin verbs over the policies; fail-open, stdlib-only). Do NOT build routing/comprehension/
   timeline/recall (generic, already shipped). Suggested order: `phenotype-gate`,
   `map-clinical-codes`, `design-indicator` (the 3 highest-danger health verbs) → `frame-study`,
   `run-ida`, `validate-assumptions`, `assess-missingness` (the STRATOS analysis core) →
   `onboard-data`, `validate-data-contract`, `scaffold-reporting` → `guard-data-export` hook.
4. Add `notation-check` (optional hook) and wire `methods-documentation.md` to it; consider
   `specify-regression` (optional skill).
5. Version, changelog, marketplace; update `template/CLAUDE.md.jinja`'s plugin notes.

## Backlog — enforcement & structure (from the tsukuba audit, 2026-06-28)

Source: `docs/audits/2026-06-28-tsukuba-audit/`. The portfolio above is *policies→skills*;
this is the **enforcement layer** (the owner's "mandatory pre-registration" paradigm) + the
**human/agent + metadata structure**. Spec only — not built.

### New hooks (enforcement — the "mandatory" gates)
| Hook (event) | Does | Pattern |
|---|---|---|
| `sap-lock` (PreToolUse on cleaning/analysis writes) | Block/ask if the canonical pre-registration is not `status: locked` (no `validation/logs/sap_lock.json`). The owner's core requirement. | File-existence gate (like their reliable `data_lock.json`). Additive to reads; only gates writes. |
| `attrition-log` (PostToolUse on filtering scripts) | Flag a script that drops rows but doesn't call `log_attrition(step, n_in, n_out, excludes_target_population, reason)`. | Makes flow-diagram inputs accumulate **from the start**. |
| `variable-catalog-gate` (PreToolUse on productive scripts) | Block a script that references a variable whose `variable_spec_catalog.yaml` `status: unknown`. | Their `<<PENDING_CONFIRMATION_Qn>>` would correctly block. |

### New artifacts (the pre-registration paradigm — next design block)
- **One canonical, lockable pre-registration artifact** (a single file aggregating the
  mandatory fields: population/estimand, index date, exposures, outcomes, objectives,
  model, pre-specified adjustments, sensitivity list, **deviations log**), fillable from
  arbitrary inputs (drop protocol/annexes → harmonize) with **PENDING markers** allowed.
  Becomes the methods appendix; `status: locked` is the gate.
- **`population_cascade.yaml`** (target → accessible → sampled → study, counts per level)
  + the standardized **`excludes_target_population`** boolean in the attrition log.
- (Deferred — Stage 2) publish pre-registration + SAP + modifications + deviations to an
  open registry (track/justify deviations).

### New generic skill
- **`rescue-manifest`** (likely `psotobverse-utils` — migration is domain-agnostic):
  harmonize an arbitrary source repo into the template layout (KEEP/DROP/REGENERATE/
  KEEP-EXTERNAL), with the archivist test + regenerability test + hard-coded-path audit +
  size gate. Rehearsed example: `docs/audits/2026-06-28-tsukuba-audit/rescue-manifest.md`.

### Template structure changes (factory backlog, not this plugin)
- **Human/agent separation:** human-canonical `source/`; agent-derived under `context/`
  (regenerable, gitignored); routing sends human-only on request, human+AI by default.
- **Metadata two-taxonomy:** `metadata/` = practice (archivist test); `context/` = agent.
- **`.gitignore` for regenerables** (`~$*`, `**/derived/**` extractions, `*.jsonl` indexes,
  large `**/worklists/*.csv`) + a named gitignored scratch dir for private profiling notes.
- **Drop the `server_payload/` pattern:** transfer script + `config/paths.local.yml` +
  symlink/junction to the data root + one `docs/server_setup.md`.
