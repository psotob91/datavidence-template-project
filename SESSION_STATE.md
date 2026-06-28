# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply (in the
> **terminal**; in the **desktop app** read this file yourself — see below).
> Durable history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-28
- **Branch (git local):** `main` — everything integrated **and pushed** to `origin/main`.
- **Status:** Health-data policy expansion shipped (code-mapping, phenotyping, EHR/claims
  indicators) + the prior expert-methodology corrections. All clean & pushed.

## Done (this milestone)
- **Three health-data policies** (commit `9490987`), gated by `project_profile=health-data`:
  `health/code-mapping.md` (new), `health/phenotyping.md` (new — mandatory comprehension gate
  before code), `health/routinely-collected-data.md` (stub completed). Shipped companion in
  `template/docs/health/` (ascii-timelines, phenotyping-examples, indicator-scenarios,
  checklists). Built from the `temporal-expansion-ideas/` sources + the Tsukuba EHR/claims kit
  + deep research, then Sonnet adversarial peer-review (all MUST-FIX applied). Renders clean
  for both profiles; gating + check_placeholders verified.
- **Provenance + pending plugin spec** (factory root, not shipped):
  `docs/research/health-data-policies-research.md`, `docs/plugins/datavidence-healthanalysis-blueprint.md`.
- **Learning loop:** captured model-routing (Opus reason / Sonnet execute+peer-eval) and the
  large-source-file extract→chunk→digest practice in PLAYBOOK + LEARNING_LOG + `[[model-routing]]`.
- `temporal-expansion-ideas/` distilled and **gitignored** (large .mhtml kept local only).
- Earlier this session: expert-methodology corrections to the analysis policies (commit `375807a`).

## Needs Percy's eye (flagged, handled conservatively)
- **Unverified dialysis citations:** "Lam et al. 2026 (Kidney Medicine)" and the "Tsunoda 2022"
  state-machine framing could not be confirmed — marked **provisional** in the shipped example.
  Confirm/replace DOIs before any formal use. (Gao et al. 2025 AJKD is confirmed.)

## Next steps (pending)
1. Build the `datavidence-healthanalysis` plugin from `docs/plugins/...-blueprint.md`
   (skills + hooks; currently routed-to but not installed; `methods-documentation.md`'s
   notation-check hook is marked pending until then).
2. Root `llms.txt` for the factory; extend CI to render-and-validate (beyond check_placeholders).
3. Review the remaining un-reviewed policies if desired (universal + the untouched analysis ones).
4. Optional: factory `.claude/policy/paths.allow.json` to activate the `nothing_loose` write-guard.
5. Optional: start tagging releases (e.g. `v0.2.0`) so plain `copier copy`/`update` track releases.

## Uncommitted
- None. Everything committed + pushed. (`temporal-expansion-ideas/` is gitignored, local-only.)

## Machine note
- Env cache (`~/.claude/environment.md`) on this PC reports `make` and `rg` **present**.
