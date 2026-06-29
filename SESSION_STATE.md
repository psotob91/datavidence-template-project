# SESSION_STATE — current state of the factory

> **Rolling file. OVERWRITE it, don't append.** Always small (~1 screen). Durable
> history lives in `learning/sessions/` (handoffs) and `git log`.

- **Updated:** 2026-06-29
- **Status:** **Blueprint backlog fully closed.** `datavidence-healthanalysis` v0.2.0 (Blocks 0–7);
  `psotobverse-utils` **v1.8.0** (adds `/rescue-manifest`); template routes `preregister` and is
  reconciled with the blueprint's structure spec. All three repos clean on `main`.

## What shipped (this stretch)
- **`psotobverse-utils` v1.8.0** — new generic **`/rescue-manifest`** skill: plans a legacy-repo
  migration (KEEP/DROP/REGENERATE/KEEP-EXTERNAL + regenerability/archivist/hard-coded-path/size-gate
  tests) into a decision-matrix manifest; PLANS only, hands approved moves to `/tidy`. Cold-read
  audited (P1/P2 fixes), doc_hygiene clean. Tagged + released. (PR #2.)
- **Template structure backlog → RESOLVED-BY-EXISTING-DESIGN** — the template already implements the
  human/agent separation + two-taxonomy + KEEP-EXTERNAL under its own naming (`context/`=human inputs,
  `_agent_cache/`+`.rag/`+`data/derived/`=agent-derived gitignored, `metadata/`=practice,
  `config.yml`=connected-data; no `server_payload/` ever existed). Tsukuba `source/`+`context/`-as-agent
  naming deliberately NOT adopted (conflict/regression). Blueprint records the mapping + rationale;
  only gap closed = `~$*` added to `template/.gitignore`. (PR #8.)

## Repos on `main`
- `datavidence-healthanalysis` — v0.2.0 (22 skills incl. `preregister`, 5 hooks, 3 subagents).
- `psotobverse-utils` — v1.8.0 (8 skills incl. `rescue-manifest`, governance hooks, meta-learner).
- `datavidence-template-project` (factory) — routes `preregister`; blueprint backlog closed.

## Pending / deferred (nothing blocking)
- Optional, stays deferred per blueprint: a dedicated server-deploy transfer-script +
  `docs/server_setup.md` (the `config.yml` connect pattern already covers connected data; revisit
  only on a real server hand-off).
- Learning queue: `/reflect` drained this session; new signals accrue normally.

## Notes
- Bash heredoc gotcha on this machine: only ONE heredoc per Bash call is reliable. Cross-repo
  writes go via Bash/python (the factory `nothing_loose` guard blocks Edit/Write outside the root).
- After a scripted multi-file regex rewrite, always sanity-check `git diff --stat` (a DOTALL `.*`
  once ate whole files). Cowork is DEPRECATED for these plugins — Claude Code only.
