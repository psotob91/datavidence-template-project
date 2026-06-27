# CLAUDE.md — datavidence template **factory** (maintainer-facing)

This file governs Claude Code when working on **the template repo itself**. It is
NOT rendered into generated projects — children are governed by
[`template/CLAUDE.md.jinja`](template/CLAUDE.md.jinja). Two `CLAUDE.md`s, two
audiences: this one is for **maintainers of the factory**; that one is for the
**analyst in a generated child**. Do not conflate them.

> Do **NOT** run `/init` — it would clobber this curated file.

## Resuming a session (read this first, in order)

The goal is to re-acquire context in seconds, not to re-read the repo:

1. **`SESSION_STATE.md`** — where we are right now + the next steps. The
   `SessionStart` hook already injects its head into your context (and warns if
   the previous session ended uncleanly — see *Meta-learner* below).
2. **`git log --oneline -8`** + `git status` — what landed and what's in flight.
3. Pull detail **on demand** only: `CHANGELOG.md` `[Unreleased]`, the newest ADR
   in `template/docs/adr/`, and the relevant `learning/sessions/<date>.md` handoff.

Do **not** preload `template/`. Retrieve, don't load.

## What this repo is

A **Copier factory**, not a project. `copier.yml` sets `_subdirectory: template`
and `_templates_suffix: .jinja`, so the master/child boundary is a **directory**:

| Location | Governs | Rendered into children? |
|---|---|---|
| repo **root** (`copier.yml`, `README.md`, `QUICKSTART.md`, `.github/`, `scripts/`, `docs/research/`, this `CLAUDE.md`, `learning/`, `SESSION_STATE.md`) | the **factory** | **No** |
| **`template/`** (everything, `.jinja` rendered) | the generated **child** | **Yes** |

A user runs `copier copy` (or `scripts/new-study.ps1`), answers the questionnaire
(`analysis_stack`, `project_profile`, `modules`, …), and gets a child whose
`*.jinja` files materialize with the suffix stripped. **Master = factory; each
child = product.** Never hand-edit generated output — edit the `.jinja` source and
re-render; the render matrix in `.github/workflows/template-ci.yml` guards it.

## Meta-learner (this factory dog-foods what it ships)

The learning-loop MECHANISM lives in the `psotobverse-utils` plugin (≥ v1.5.0),
versioned and DRY; this repo OPTS IN via [`.claude/meta-learner.json`](.claude/meta-learner.json)
(its presence activates the plugin's session hooks here; absent ⇒ they no-op).
That config also holds this repo's domain signal patterns (agent-building terms)
and routes durable consensus signals to `learning/STANDARDS_WATCH.md`.

- **`SessionStart`** — injects `SESSION_STATE.md` + the last handoff so you resume
  cheaply, **detects an unclean exit** via a dirty-bit (`.claude/state/session.json`:
  arms `status=active`; `SessionEnd` flips it to `clean_exit`; an `active` bit at
  the next start ⇒ the previous session crashed), and runs a **once-per-machine
  environment probe** (shell + available CLIs + OS quirks → cached at
  `~/.claude/environment.json` / `.md`) whose summary it injects every session, so
  you know what this machine has — and what to avoid (e.g. PowerShell 5.1 `&&`) —
  without re-checking.
- **`UserPromptSubmit`** — cheap, crash-safe, append-only capture of **correction**
  and **consensus/standards** signals to `learning/queue/signals.jsonl`.
- **`SessionEnd`** — writes one deterministic, forward-looking **handoff** to
  `learning/sessions/` (only when the tree is dirty or signals were captured).
- **`/psotobverse-utils:reflect`** — the human-gated synthesis step: turns the
  signal queue into **proposed diffs** for the learning files. Never auto-edits.
- **`/psotobverse-utils:audit-report`** — structures multi-agent audit output as a
  small indexed `docs/audits/<date>-<slug>/` instead of a context-blowing blob.

> Requires the plugin at **≥ 1.5.0**. If only 1.3.x is installed, the session
> hooks and these two skills are absent (the repo still works); update with
> `claude plugin marketplace update psotobverse-utils` then
> `claude plugin update psotobverse-utils@psotobverse-utils` (restart to apply).

### Terminal tooling on this machine
The `SessionStart` env probe caches this machine's shell + CLIs at
`~/.claude/environment.md` — read it instead of re-checking. Notes:
- Prefer the **Grep tool** over raw `rg` (Claude Code already wraps ripgrep).
- This repo's own work is **copier + python + git/gh** (no `make`). When you
  **test a generated child's pipeline**, the R/Quarto/`make` idioms — and the
  make-less equivalents to use when `make` is absent — live in
  [`template/docs/running-from-terminal.md.jinja`](template/docs/running-from-terminal.md.jinja).

### The learning ritual (WRITE triggers, not just reads)
At a natural checkpoint, or when `SessionStart` reports queued signals, **run
`/reflect`**. It routes each signal to:

| File | Holds |
|---|---|
| `learning/LEARNING_LOG.md` | append-only, dated facts ("what happened") |
| `learning/PLAYBOOK.md` | distilled, proven-reusable lessons |
| `learning/REFLECTOR.md` | triage board (Now / Defer+TRIGGER / Optional / Discard) |
| `learning/WATCHLIST.md` | open TODOs / anomalies (prune on resolution) |
| `learning/STANDARDS_WATCH.md` | Anthropic/Claude-Code conventions we depend on — dated, falsifiable, **non-dogmatic** |

`STANDARDS_WATCH.md` exists because agent-building conventions change in **weeks**.
Its rule: when a convention we ship may have changed, **re-verify against the
official docs and ASK the user** — never silently adopt or rewrite the template.

## Persistence model (survives `/compact` and crashes)

- **Stable rules** → this `CLAUDE.md` (re-read after `/compact`).
- **Durable lessons** → `learning/*.md` (committed).
- **Transient state** → `SESSION_STATE.md` (rolling) + `learning/sessions/` (handoffs)
  + `git` (finished work). Anything that must survive a crash lives on disk, never
  only in the conversation.

## Testing / verifying the meta-learner
The hook scripts live in the plugin (`$CLAUDE_PLUGIN_ROOT/hooks/`); test them
there by piping simulated stdin (stdlib, no venv, fail-open). To confirm THIS repo
is opted in, check that `.claude/meta-learner.json` exists and `enabled` is true —
without it the plugin's session hooks no-op here.

## Companion plugin (`psotobverse-utils`)

Generic guardrails and thin-verb skills come from the `psotobverse-utils` plugin
(installed once at machine/user scope — there is no per-project binding; once
installed its skills are available in every session). The factory **uses** them;
route generic capabilities to the plugin's namespaced skills:

| Generic capability | Plugin skill |
|---|---|
| Repo organization / index / split oversize docs | `/psotobverse-utils:index` |
| Content coherence / docs-vs-code audit | `/psotobverse-utils:reconcile` |
| Relocate loose / misplaced files | `/psotobverse-utils:tidy` |
| Design before a risky change | `/psotobverse-utils:deliberate` |
| Goal-directed multi-step execution | `/psotobverse-utils:goal` |
| Capture lessons (learning loop) | `/psotobverse-utils:reflect` |
| Organize audit / diagnostic output | `/psotobverse-utils:audit-report` |

Skills auto-trigger by description (just describe the task); to call one
explicitly, prefix the plugin name. Its **hooks** fire at USER scope (write-guard,
`.env` protection, doc hygiene, stop reminder) — the factory meta-learner above is
additive and project-scoped. The plugin's `nothing_loose` write-guard fails open
here (no `.claude/policy/paths.allow.json` at the factory root) — by design for now.

## Conventions
- Conventional Commits; record significant decisions as ADRs in `template/docs/adr/`.
- Keep factory ↔ template **parity**: every factory improvement useful to the
  child belongs in `template/`, and every template improvement that applies to the
  factory belongs here. The learning loop, `/reflect`, and `/audit-report` exist in
  both for this reason.
