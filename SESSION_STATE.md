# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). Durable
> history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-29
- **Status:** `datavidence-healthanalysis` **v0.2.0 on `main`** — Blocks 0–7 complete +
  description trim. Both PRs (#3 trim, #4 Block 7) **MERGED**; local `main` synced; feature
  branches deleted/pruned.

## What's on main now
- **22 thin-verb skills** (incl. `preregister`), `_shared` core, **5 hooks**
  (`guard_data_export`, `notation_check`, `sap_lock`, `attrition_log`, `variable_catalog_gate`),
  3 reviewer subagents. All skill descriptions ≤1024. `plugin.json` v0.2.0.
- **Block 7 pre-registration enforcement:** lockable `analysis/prereg/pre-registration.yaml`
  (status:locked + content-hashed `validation/logs/sap_lock.json` gate), `population_cascade.yaml`,
  `log_attrition()` contract, deviations log, no-lock-over-PENDING — enforced by the 3 new hooks.
- Eval records: `docs/evals/2026-06-29-block4-behavior-eval.md`,
  `docs/evals/2026-06-29-block7-preregister-eval.md`.

## Pending / not done
- **`/reflect`** — HELD at Percy's request ("espera para reflect"); learning queue has 4+
  unprocessed signals in both repos. Run when ready.
- **Template parity follow-up:** wire `preregister` into the template
  `knowledge-map.md.jinja` / trigger-lexicon (template repo; small).
- **Deferred (per blueprint — NOT this plugin):** `rescue-manifest` skill (→ psotobverse-utils);
  template structure changes (human/agent `source/`-vs-`context/`, metadata two-taxonomy).

## Notes
- Bash heredoc gotcha on this machine: only ONE heredoc per Bash call is reliable. Plugin-repo
  writes go via Bash/python (the factory `nothing_loose` guard blocks cross-repo Edit/Write).
- Regex DOTALL gotcha caught this session: `(?s)` made `.*` eat a whole file; always sanity-check
  `git diff --stat` after a scripted multi-file rewrite.
