# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). Durable
> history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-29
- **Status:** `datavidence-healthanalysis` **v0.2.0 published** (tag + GitHub release); the
  template **routes `preregister`** and documents how to install the plugin; factory bookkeeping
  + `/reflect` synthesis committed. **All clean on `main` in both repos.**

## Plugin (`datavidence-healthanalysis`) — on `main`, tagged v0.2.0
- 22 thin-verb skills (incl. `preregister`), `_shared` core, **5 hooks**
  (`guard_data_export`, `notation_check`, `sap_lock`, `attrition_log`, `variable_catalog_gate`),
  3 reviewer subagents. CI `validate-plugin` green.
- **Block 7 pre-registration enforcement:** lockable `analysis/prereg/pre-registration.yaml`
  (status:locked + content-hashed `sap_lock.json` gate), `population_cascade.yaml`,
  `log_attrition()` contract, deviations log — enforced by the 3 new hooks.
- Published: `.claude-plugin/marketplace.json` refreshed; **tag `v0.2.0`** + GitHub release.
  Install: `claude plugin marketplace add psotob91/datavidence-healthanalysis` then
  `claude plugin install datavidence-healthanalysis@datavidence-healthanalysis`.

## Template / factory (`datavidence-template-project`) — on `main`
- `preregister` routed in `knowledge-map.md.jinja` + `trigger-lexicon.md.jinja`; the
  "Install separately" note now gives the concrete install command. Verified by a health-data
  `copier` render (placeholder check OK). CI render matrix green (PR #7 merged).
- `/reflect` (2026-06-29) applied to the learning files; signal queue drained to `processed.log`.

## Deferred (per blueprint — larger, separate efforts)
- `rescue-manifest` skill → `psotobverse-utils` (migration is domain-agnostic).
- Template structure changes: human/agent `source/`-vs-`context/` split, metadata two-taxonomy.

## Notes
- Cowork is DEPRECATED for these plugins (broken server-side sync; GH #39400 et al.) — develop
  + run in Claude Code only. See `learning/STANDARDS_WATCH.md`.
- Gotchas captured this session (`learning/PLAYBOOK.md`): scripted-regex DOTALL can eat whole
  files — verify `git diff --stat`; only ONE heredoc per Bash call is reliable here.
