# Blueprint — `datavidence-healthanalysis` plugin (IN PROGRESS)

**Status: in progress (2026-06-28).** Implementation started: `skills/_shared/health-principles.md`
and the exemplar `skills/phenotype-gate/SKILL.md` are built (pattern locked); the rest is specced
below. This file is the **single implementable spec** for the whole portfolio. It lives at the
template-repo root (not rendered into children).

## Why a plugin (vs more policies)

The `health/` policies (`code-mapping.md`, `phenotyping.md`, `routinely-collected-data.md`) +
the `docs/health/` companion are the **methodology** (human source of truth, shipped to
children). The plugin adds the **mechanism**: skills that scaffold/validate the same rules,
versioned and DRY — exactly as `psotobverse-utils` carries the meta-learner mechanism. Generic
MECHANISM → plugin; DATA + CONFIG + routing stays local (the meta-learner-refactor lesson).

## Already shipped generically — do NOT rebuild

The routing / comprehension / recall **mechanism is generic** and lives in `psotobverse-utils`
(≥ v1.7.0). This plugin **consumes** it; it must not reimplement it:

- **Conditional routing** — `policy_router.py` reads the child's `.claude/policy/routing.yml`. The
  health edges (codes → code-mapping → phenotyping → routinely-collected-data; the data→causal fork)
  are **data rows** there, not plugin code.
- **`timeline-before-pseudocode`** — delivered by the generic `comprehension_gate.py` driven by the
  `phenotype-timeline-gate` rule in `routing.yml` (mode `block`). The plugin does NOT rebuild this.
- **Comprehension gate (explain-back) + recall** — `/comprehend`, `/coverage` are generic.
- **Adversarial review** — `/cross-examine` is generic.

So the plugin surface is: **domain validating skills + domain hooks + reviewer subagents**.

## Name

Use **`datavidence-healthanalysis`** (referenced by `methods-documentation.md`'s `notation-check`
hook). The older `datavidence-healthdata` is drift; standardize on `datavidence-healthanalysis`.

## Portfolio (reconciled 2026-06-28)

Decided by a **280-judge self-consistency vote** (40 policies × 7 Sonnet replicas) under the
EQUATOR/STRATOS framing — these frameworks ARE health-methodology, so they live here, not in
`psotobverse-utils`. Raw verdicts: `docs/plugins/evidence/skill-hook-portfolio-vote.json`.

**Naming reconciliation (this revision).** The vote's **consolidated names are CANONICAL**. The
template's older routed names (`data-contract`, `missingness-report`, `eda`, `table1`, `cohort-flow`,
`process-diagram`) and `DEVELOPMENT_GUIDE.md` §2 are **aligned to these in the cableado block**
(rewrite the `knowledge-map.md.jinja` rows, the 3 policy skill-refs, and §2). Two skills the template
routes but the vote dropped are **kept and built** so no route dangles: `numeric-check`, `method-audit`.
Old→new map: `data-contract`→`validate-data-contract` · `missingness-report`→`assess-missingness` ·
`eda`→`run-ida` · `table1`+`cohort-flow`+RECORD→`scaffold-reporting` (by type) · `process-diagram`→`draft-diagram`.

### Skill conventions (how to build each)

Skills are **markdown-only thin verbs** — no bundled R scripts. Each `SKILL.md` says WHAT to do, in
order, and delegates math/compute to **R (via the `executor` subagent)** or **WolframAlpha MCP**. The
**policy file carries the full rules**; the `SKILL.md` carries the *interface*: trigger phrases (third
person, auto-invoke, disjoint from siblings), the scope boundary, the gate spine, and the output
artifact. Body ≤ 250 lines. **Exemplar:** `skills/phenotype-gate/SKILL.md`. **Shared invariants:**
`skills/_shared/health-principles.md` (math-by-tool, claim→evidence, PENDING_LOCAL_DECISION,
comprehension-before-code, generator≠auditor). Reference the child-relative gates
(`docs/health/checklists.md`, `docs/health/ascii-timelines.md`); never bundle them.

**Output-artifact convention (portfolio-wide, from the iteration-2 eval).** A sizeable spec follows
`skills/_shared/spec-artifact.md`: when it exceeds the doc-hygiene limit (~300 lines) **split** it into an
indexed `<spec-dir>/` (`comprehension/00-overview…08-pending-decisions.md` + a `README.md` router) instead
of one wall of text — the `04-decision-diagram.md` + `05-timelines.md` + `comprehension/` names satisfy the
`phenotype-timeline-gate` for free. For the **human view**, copy the child scaffold
`template/analysis/_spec-template.qmd` + `_assets/spec-theme.scss` (shipped only when `analysis_stack == r`)
into the spec dir and `quarto render` an **academic + executive** HTML: an always-visible executive summary
(status badge · one-paragraph restatement · decision diagram · open PENDING checklist) above a
`panel-tabset` of the academic detail. The scaffold lives in the **child** (presentation = child;
orthogonality); skills stay markdown-only and just point to it.

The render is **chaptered** (`## Comprensión` / `## Hacia el código` / `## Validación`, each a tabset)
and the spec carries two coding-bridge sections: a **`variable-catalog.yaml`** (the tsukuba
`variable_spec_catalog` schema — input/derived/uncertain, `status: unknown` + `<<PENDING_CONFIRMATION_Qn>>`
for variables it cannot confirm against `metadata/data_dictionary.csv`) and **implementable, language-agnostic
pseudocode** (`build/pseudocode.md`, per `analysis/pseudocode-first.md`). This **pulls the
`variable-catalog-gate` artifact forward** from Block 7 into the artifact format — the gate now has a
`variable-catalog.yaml` to enforce. Included section files use `####`+ headings only (a `##`/`###` inside an
include leaks a stray tab — the bug that made the first render look crowded).

### Build clusters (= plan blocks)

| Block | Skills / components |
|---|---|
| 1 PRIORITY (EHR/claims · codes · denominators) | `phenotype-gate` (exemplar — DONE) · `map-clinical-codes` · `design-indicator` |
| 2 STRATOS core | `frame-study` · `run-ida` · `validate-assumptions` · `assess-missingness` · `numeric-check` |
| 3 data + reporting | `onboard-data` · `validate-data-contract` · `scaffold-reporting` |
| 4 optional | `specify-regression` · `specify-sensitivity-plan` · `review-outliers` · `big-data-triage` · `draft-diagram` |
| 5 hooks + panel | hooks `guard-data-export`, `notation-check` · subagents `methodologist`, `statistician`, `reporting-reviewer` · panel skill `method-audit` |
| modules (opt-in, module-gated) | `dag-causal` · `prediction-validation` · `survey-design` · `spatial` |

### Skills — interface spec (one stanza each: policy · triggers · scope boundary · output)

**Block 1 — PRIORITY**
- **phenotype-gate** — `health/phenotyping.md`. Triggers: define cases, computable phenotype, identify
  patients by algorithm, case definition. Scope: consumes a code set, feeds an indicator; NOT code-set
  assembly, NOT denominators. Output: phenotype-spec (10-section comprehension gate) → pseudocode +
  fixtures. **DONE (exemplar).**
- **map-clinical-codes** — `health/code-mapping.md`. Triggers: ICD/CIE-10, ICD-9, SNOMED, RxNorm, ATC,
  CPT, LOINC, diagnosis/medication code list, crosswalk, GEM, phecode, comorbidity index. Scope: assemble
  & validate a **code set**; NOT grouping into a yes/no label (→ phenotype-gate). Output: a validated
  code-set manifest (source+version+extraction date; one-grouping; crosswalk direction + loss %; cleaning
  sequence char→trim/upper→ICD-9 zero-pad→dagger/asterisk→terminal-X→cascade-truncate; gates %orphan /
  %unspecified / %truncated vs thresholds; archived-`icd`-package flag; pinned versions). Returns
  PENDING_LOCAL_DECISION for unmade grouping/threshold choices.
- **design-indicator** — `health/routinely-collected-data.md`. Triggers: incidence, prevalence,
  denominator, person-time, episode, washout, lookback window, rate. Scope: denominator→numerator→
  window→episode design for routinely-collected data; NOT the case label itself (→ phenotype-gate).
  Output: an indicator design doc — denominator before numerator; population frame; person-time by
  interval overlap (not max−min); every window typed (lookback/washout/clean/confirmation/outcome/risk/
  grace/eligibility); index fixed (no immortal time); episode + recurrence model; states prevalence type
  (point/period) and incidence form (cumulative vs rate). Runs `checklists.md` denominator + numerator
  gates; PENDING_LOCAL_DECISION on unmade frames.

**Block 2 — STRATOS core**
- **frame-study** — `analysis/pre-specification.md` + `analysis/statistical-reporting.md` +
  `health/reporting-standards.md`. Triggers: analysis plan, SAP, estimand, pre-specify outcome, which
  reporting guideline. Scope: frames the plan up front; NOT running the analysis. Output: a SAP skeleton
  — pre-specified estimand/outcome, task→method classification (STRATOS/SAMBR), and the selected EQUATOR
  guideline; flags post-hoc.
- **run-ida** — `analysis/initial-data-analysis.md` + `analysis/longitudinal-data.md`. Triggers: initial
  data analysis, IDA, EDA, data screening; longitudinal mode for repeated measures. Scope: STRATOS IDA
  before modeling; NOT model diagnostics (→ validate-assumptions). Output: an IDA report (5 STRATOS
  domains; longitudinal mode adds the repeated-measures structure scan).
- **validate-assumptions** — `analysis/model-assumptions.md`. Triggers: check assumptions, residual
  diagnostics, model diagnostics, proportional hazards. Scope: post-fit diagnostics, graphics-first; NOT
  pre-fit screening. Output: the right residual/assumption diagnostics per model (`performance`, `car`,
  `DHARMa`, `survival::cox.zph`; Bayesian `bayesplot`/`loo`), with "violation ≠ invalid" framing.
- **assess-missingness** — `analysis/missingness.md`. Triggers: missing data, NA, imputation, MICE, MAR,
  MNAR. Scope: profile + mechanism + handling plan; NOT generic data validation (→ validate-data-contract).
  Output: a missingness profile (pattern via `naniar`), mechanism reasoning (MCAR/MAR/MNAR), handling
  proposal (MI via `mice` / MMRM) + sensitivity; never silent listwise deletion.
- **numeric-check** — `analysis/numeric-computation.md`. Triggers: verify this number, recompute,
  check the percentage/total/CI. Scope: verify a specific numeric claim by re-deriving it in code; NOT
  authoring a table (→ scaffold-reporting). Output: a recomputation (R via executor, or WolframAlpha for
  symbolic) anchored to script+output; flags any model-computed number.

**Block 3 — data + reporting**
- **onboard-data** — `analysis/data-onboarding.md`. Triggers: connect data, import dataset, set up the
  data folder, where does the data live. Scope: connect/copy + portable config + minimal provenance; NOT
  schema validation (→ validate-data-contract). Output: `data/README.md` + `config.example.yml`
  (`rio`/`here`), copy-light/connect-heavy per the taxonomy, minimal provenance docs.
- **validate-data-contract** — `analysis/data-contracts.md` (+ `analysis/data-integrity.md`). Triggers:
  validate data, data contract, schema check, data quality gate. Scope: gate raw + analysis-ready data;
  block on failure. Output: a `pointblank` contract + run results (types, ranges, join cardinality,
  uniqueness); records pass/fail; blocks downstream on FAIL.
- **scaffold-reporting** — `health/secondary-data.md` + `health/clinical-tables.md` +
  `health/study-flow.md`. Triggers: Table 1, baseline characteristics table, participant flow,
  CONSORT/STROBE/PRISMA, RECORD data-source table. Scope: produce an EQUATOR-aligned reporting artifact
  **by type**; begins with the sketch-first approval gate (plain-text mock, no numbers) from the
  `diagrams` policy. Output (by type): RECORD data-source table (secondary-data) · Table 1/2 via
  `gtsummary`, no p in comparison tables, SMD + missingness (clinical-tables) · CONSORT/STROBE/PRISMA
  participant-flow diagram via `flowchart` (study-flow).

**Block 4 — optional**
- **specify-regression** — `analysis/regression-modeling.md`. Triggers: regression spec, model the
  outcome, adjust for confounders. Scope: spec a regression; NOT diagnostics (→ validate-assumptions).
  Output: a model spec — no dichotomizing, splines for non-linearity, no stepwise, penalize
  sparse-data/separation; respects `collinearity.md` (VIF is a flag, never drop a confounder for it).
- **specify-sensitivity-plan** — `analysis/sensitivity-analysis.md`. Triggers: sensitivity analysis,
  robustness check, E-value. Scope: pre-specify sensitivity analyses reusing the primary pipeline.
  Output: a sensitivity plan listed alongside the primary estimand (pre-specified, not post-hoc).
- **review-outliers** — `analysis/outliers.md`. Triggers: outliers, extreme values, implausible values.
  Scope: detect→inspect→document→sensitivity; never silent removal. Output: an outlier report + a
  with/without sensitivity plan.
- **big-data-triage** — `analysis/computational-efficiency.md`. Triggers: big data, on-disk, out of
  memory, slow query, millions of rows. Scope: pick the engine + pattern; NOT the statistics. Output: a
  triage note (`data.table`/`duckdb`/`arrow`; vectorize; cache/freeze long runs).
- **draft-diagram** — `analysis/diagrams.md`. Triggers: process diagram, flowchart, method diagram.
  Scope: process/method diagrams (Mermaid + ISO 5807); cohort/participant flow lives in
  scaffold-reporting. Begins with the sketch-first gate. Output: a Mermaid process diagram.

**Block 5 — panel skill**
- **method-audit** — `analysis/verification-effort.md`. Triggers: audit the methods, review the analysis
  (methods not results), is this analysis sound. Scope: a **fan-out voting panel** (the skill orchestrates;
  it is not itself a subagent) over the three reviewer subagents; depth by stakes (light 1 / standard 3 /
  deep 5 + synthesis, anti-sycophancy concede-at-≥4). Output: a structured verdict (finding · severity ·
  evidence · recommendation), every number tool-computed. Reuses generic `/cross-examine` machinery.

**Modules (opt-in, only when the project enables the module — never forced)**
- **dag-causal** (`dagitty`/`ggdag`, causal module) · **prediction-validation** (`rms`/`pmsampsize`,
  TRIPOD/PROBAST, prediction module) · **survey-design** (`survey`/`srvyr`, survey module) · **spatial**
  (`sf`/`terra`/`stars`, spatial module). Same thin-verb conventions; each pairs with its
  `docs/analysis/modules/<m>.md`. Build last; gate on real need.

### Hooks (fail-open, stdlib-only, registered in `hooks/hooks.json` — never in `plugin.json`)

| Hook (event) | Does | Vote |
|---|---|---|
| `guard-data-export` (PreToolUse) | Ask/flag on a write that would send identifiable data (real ID columns, PII) outside the project — to git, `outputs/`, `context/`, or the prompt — unless the user asked; propose drop/anonymize or documented perturbation. Egress guard. | 0.86, must |
| `notation-check` (PostToolUse/edit) | Flag methods text whose math symbols are absent from the child's `docs/analysis/notation.md`; wire `methods-documentation.md` + `supplement.qmd.jinja` to it. | 0.71, optional |

Use the `psotobverse-utils` `python -c` bootstrapper verbatim (resolve `CLAUDE_PLUGIN_ROOT` by name;
fail-open `sys.exit(0)` if unresolved). Do NOT redefine the generic `nothing_loose`/`env_protect` guards.
Reclassified (not separate hooks): `code-provenance` → folded into `map-clinical-codes`;
`denominator/numerator-integrity` → folded into `design-indicator`; `timeline-before-pseudocode` →
already generic. (`provenance-stamp` from the old guide: deferred — not voted in.)

### Subagents (`agents/<role>.md`, model tier per role)

`methodologist` (design validity) · `statistician` (statistical correctness) · `reporting-reviewer`
(EQUATOR/reporting adherence) — all **sonnet** (judge tier), read-only tools, cold-read + refute,
structured verdicts, math delegated. Reuse `executor`/`explorer` from `psotobverse-utils`. A
`SubagentStop` hook may later enforce non-negotiables (no secrets/data in output; numbers tool-computed).

## Reuse the agent-index retrieval pattern

The Tsukuba kit (`methodology-policy-kits/ehr-claims-longitudinal/agent_index/`) is the model for cheap
agent navigation of heavy content: `AGENT_ENTRYPOINT.md` + `routing.yml` (intent → 1–3 files) +
`lookup_cards.yml` (guardrails) + `scenario_router.yml`. If the plugin ships a large reference/scenario
corpus, **generate** this index with a script and keep the machine layer derived, separate, deletable.

## Build order (= plan blocks; checkpoint + commit each)

Repo state 2026-06-28: skeleton scaffolded + self-hardened; **Block 0 done** (`_shared` + `phenotype-gate`
exemplar + this spec). Then:

1. **Block 1 (PRIORITY):** `map-clinical-codes`, `design-indicator` (the EHR/claims/codes/denominator core).
2. **Block 2:** `frame-study`, `run-ida`, `validate-assumptions`, `assess-missingness`, `numeric-check`.
3. **Block 3:** `onboard-data`, `validate-data-contract`, `scaffold-reporting`.
4. **Block 4:** `specify-regression`, `specify-sensitivity-plan`, `review-outliers`, `big-data-triage`, `draft-diagram`.
5. **Block 5:** hooks `guard-data-export` + `notation-check` (wire `methods-documentation.md`); subagents
   `methodologist`/`statistician`/`reporting-reviewer`; panel skill `method-audit`.
6. **Block 6 (cableado + release):** reconcile cold-read; align template (`knowledge-map.md.jinja` rows,
   the 3 policy skill-refs, `DEVELOPMENT_GUIDE.md` §2) to the canonical names; `claude plugin validate .`;
   render-a-child smoke test; CHANGELOG + version bump; update `template/CLAUDE.md.jinja` plugin notes.
7. **Block 7 (stretch, gated):** the tsukuba enforcement layer below.

Per-block method: Sonnet drafters (1/skill, follow the exemplar, read 1 policy + `checklists.md`) →
Sonnet cold-read auditor (refute vs policy + checklists) → Opus integrates + validates. Drafters/integrator
write to the plugin repo via Bash heredoc (the factory `nothing_loose` guard denies cross-repo
Write/Edit; Bash is not intercepted). Opt-in module skills build last, gated on need.

## Backlog — enforcement & structure (from the tsukuba audit, 2026-06-28) — Block 7, specced-but-staged

Source: `docs/audits/2026-06-28-tsukuba-audit/`. The portfolio above is *policies→skills*; this is the
**enforcement layer** (the "mandatory pre-registration" paradigm) + the human/agent + metadata structure.
**Spec only — not built; needs the pre-registration artifact designed first.**

### New hooks (the "mandatory" gates)
| Hook (event) | Does | Pattern |
|---|---|---|
| `sap-lock` (PreToolUse on cleaning/analysis writes) | Block/ask if the canonical pre-registration is not `status: locked` (no `validation/logs/sap_lock.json`). | File-existence gate (like their `data_lock.json`); additive to reads; gates writes only. |
| `attrition-log` (PostToolUse on filtering scripts) | Flag a script that drops rows but doesn't call `log_attrition(step, n_in, n_out, excludes_target_population, reason)`. | Makes flow-diagram inputs accumulate from the start. |
| `variable-catalog-gate` (PreToolUse on productive scripts) | Block a script referencing a variable whose `variable_spec_catalog.yaml` `status: unknown`. | `<<PENDING_CONFIRMATION_Qn>>` would correctly block. |

### New artifacts (the pre-registration paradigm — design block)
- **One canonical, lockable pre-registration artifact** (population/estimand, index date, exposures,
  outcomes, objectives, model, pre-specified adjustments, sensitivity list, **deviations log**),
  fillable from arbitrary inputs with **PENDING markers**; `status: locked` is the gate; becomes the
  methods appendix.
- **`population_cascade.yaml`** (target → accessible → sampled → study, counts per level) + the
  standardized **`excludes_target_population`** boolean in the attrition log.
- (Deferred — Stage 2) publish pre-registration + SAP + modifications + deviations to an open registry.

### New generic skill (likely `psotobverse-utils` — migration is domain-agnostic)
- **`rescue-manifest`** — harmonize an arbitrary source repo into the template layout
  (KEEP/DROP/REGENERATE/KEEP-EXTERNAL), with the archivist test + regenerability test + hard-coded-path
  audit + size gate. Rehearsed: `docs/audits/2026-06-28-tsukuba-audit/rescue-manifest.md`.

### Template structure changes (factory backlog, not this plugin)
- Human/agent separation (human-canonical `source/`; agent-derived `context/`, regenerable, gitignored).
- Metadata two-taxonomy (`metadata/` = practice; `context/` = agent). `.gitignore` for regenerables.
- Drop the `server_payload/` pattern: transfer script + `config/paths.local.yml` + junction + one
  `docs/server_setup.md`.
