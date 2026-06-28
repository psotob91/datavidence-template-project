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

## Candidate skills

| Skill | Does | Enforces policy |
|---|---|---|
| `phenotype-scaffold` | Generates a phenotype-spec doc pre-filled with the comprehension-gate sections (restate, ≥2 examples, ≥2 counter-examples, ASCII decision + temporal diagram stubs), then a pseudocode skeleton + test-fixture stub — gated so code is withheld until human sign-off. | `phenotyping.md` |
| `code-list-validate` | Takes a code set, checks provenance/version stamp, runs the cleaning sequence, reports orphan/unspecified/truncated gates, flags archived packages (`icd`). | `code-mapping.md` |
| `indicator-review` | Reviews a denominator/numerator/window/episode design against the integrity checklists; returns findings or `PENDING_LOCAL_DECISION`. | `routinely-collected-data.md` |

## Candidate hooks

| Hook (event) | Does | Status |
|---|---|---|
| code-provenance (PreToolUse on edits) | Flags hardcoded code vectors (e.g. `c("E11","I10")`) lacking a `# source/version/date` provenance comment. | **domain — build here** (generic engine can't know what a "code vector" is) |
| ~~timeline-before-pseudocode~~ | — | **DONE generically:** the `phenotype-timeline-gate` rule in `routing.yml` + `comprehension_gate.py`. Do not rebuild. |
| denominator/numerator-integrity (Stop / pre-commit) | Run the `docs/health/checklists.md` items as yes/no gates; warn on any "no/unknown". | **domain — build here** |
| `notation-check` (already referenced) | The existing methods-documentation hook: flags methods text whose math symbols are absent from the notation registry. | **domain — build here**; wire `methods-documentation.md` to it |

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
3. Implement the **three domain skills** (thin verbs over the policies) and the **three domain
   hooks** (`code-provenance`, `denominator/numerator-integrity`, `notation-check`) — fail-open,
   stdlib-only. Do NOT build routing/comprehension/timeline/recall (generic, already shipped).
4. Wire `methods-documentation.md`'s `notation-check` to the real hook.
5. Version, changelog, marketplace; update `template/CLAUDE.md.jinja`'s plugin notes.
