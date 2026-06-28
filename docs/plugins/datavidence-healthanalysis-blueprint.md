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

| Hook (event) | Does |
|---|---|
| code-provenance (PreToolUse on edits) | Flags hardcoded code vectors (e.g. `c("E11","I10")`) lacking a `# source/version/date` provenance comment. |
| timeline-before-pseudocode (PreToolUse) | When a phenotype pseudocode/code file is being written, require an accompanying ASCII timeline + decision diagram (the comprehension gate) to exist first. |
| denominator/numerator-integrity (Stop / pre-commit) | Run the `docs/health/checklists.md` items as yes/no gates; warn on any "no/unknown". |
| `notation-check` (already referenced) | The existing methods-documentation hook: flags methods text whose math symbols are absent from the notation registry. |

## Reuse the agent-index retrieval pattern

The Tsukuba kit (`methodology-policy-kits/ehr-claims-longitudinal/agent_index/`) is the model
for cheap agent navigation of heavy content: `AGENT_ENTRYPOINT.md` + `routing.yml`
(intent → 1–3 files) + `lookup_cards.yml` (guardrails) + `scenario_router.yml` (load scenario
IDs, not whole corpora). If the plugin ships a large reference/scenario corpus, generate this
index with a script (don't hand-write JSON/YAML "for the agent") and keep the machine layer
**derived, separate, and deletable** from the human methodology.

## Build order (when picked up)

1. Read `docs/research/health-data-policies-research.md` + the three `health/` policies + the
   `docs/health/` companion (the contract the plugin must enforce).
2. Scaffold the plugin (`.claude-plugin/plugin.json`, `skills/`, `hooks/`) like
   `psotobverse-utils`; make hooks opt-in via a project config so they no-op elsewhere.
3. Implement skills as thin verbs over the policies; implement hooks fail-open, stdlib-only.
4. Wire `methods-documentation.md`'s `notation-check` to the real hook.
5. Version, changelog, marketplace; update `template/CLAUDE.md.jinja`'s plugin notes.
