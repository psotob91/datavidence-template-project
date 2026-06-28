# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). The
> `SessionStart` hook injects its head so a new session resumes cheaply (in the
> **terminal**; in the **desktop app** read this file yourself — see below).
> Durable history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-28
- **Branch (git local):** `feat/routing-hardening` in **3 repos** — **committed, NOT pushed**
  (awaiting Percy's push OK). Factory +9, `psotobverse-utils` +7, `datavidence-healthanalysis` +1.
- **Status:** Routing-hardening + recall-safety-net + plugin-hardening effort **complete locally**.
  Benchmark green (union recall 1.00, 46/46 off-route caught). Plan:
  `~/.claude/plans/quizzical-roaming-sonnet.md`.

## Done (this effort — all on `feat/routing-hardening`)
- **Factory:** per-policy Prerequisite/Next-if headers + 7 reciprocal xrefs + GLS↔MMRM-by-estimand;
  hub "Conditional routing" table + **Invariant 0** (additive-never-subtractive) + `routing.yml.jinja`
  + `check_routing.py` (in CI); `trigger-lexicon.md.jinja`; full generic port to repo root
  (`.claude/constitution.md`, `.claude/knowledge-map.md`, hygiene, `llms.txt`+reindex, `docs/adr/`);
  `eval/coverage/` benchmark. Render matrix **green** (4 profiles).
- **psotobverse-utils v1.7.0:** `/coverage` (recall panel) + `coverage_sentinel`; `/comprehend`;
  `/cross-examine`; `policy_router` + `comprehension_gate` (+ `routing_util`) — all opt-in, fail-open,
  Invariant-0-safe, tested; self-hardened (own `.claude/` governance, CI, safe-edit protocol).
- **datavidence-healthanalysis:** remote wired, `temporal-expansion-ideas/` gitignored, self-hardened
  (governance + CI + safe-edit). **Features still blueprint-only** (v0.0.1 skeleton).
- **Blueprint** (`docs/plugins/...`) enriched: routing/comprehension/timeline/recall now generic;
  domain surface shrunk to 3 skills + 3 hooks.

## Next steps (pending Percy)
1. **Push** the 3 `feat/routing-hardening` branches + merge to `main` (propose-then-confirm).
2. After merge: `claude plugin update psotobverse-utils@psotobverse-utils` (restart) to activate the
   new commands/hooks in live sessions (source edits are inert until update — by design).
3. Build the 3 `datavidence-healthanalysis` domain skills + 3 hooks from the enriched blueprint
   (still pending; routing/recall/comprehension are already generic — don't rebuild).
4. **M4b done:** factory `.claude/policy/paths.allow.json` now activates the `nothing_loose` guard.

## Needs Percy's eye
- **Benchmark labels** (`eval/coverage/fixtures.json`): expert validation welcome — re-scoring is free
  (nominations frozen in `results.json`).
- **Unverified dialysis citations** (pre-existing): "Lam et al. 2026 (Kidney Medicine)" and the
  "Tsunoda 2022" framing — confirm DOIs before formal use (Gao et al. 2025 AJKD confirmed).

## Uncommitted
- None (this file is the last factory commit alongside M4b).

## Machine note
- Plugin source repos on this PC: `C:\workspace\psotobverse-utils`,
  `C:\workspace\datavidence-healthanalysis` (both git-backed). Env cache:
  `~/.claude/environment.md` (`make`/`rg`/`copier`/`uv` present).
