# Audit summary — datavidence factory (2026-06-28)

**Method:** 11-agent workflow (7 subsystem mappers + 2 web-research dossiers →
cross-referenced diagnosis → cold-read adversarial verifier). **All 13 verified
claims confirmed, zero refutations.**
**Raw:** workflow run `wf_83d659c4-793` (per-agent maps + research) in the session
transcript dir; not committed (large). This summary is the durable record.

## What the repo is
A **Copier factory**, not a project: `copier.yml` sets `_subdirectory: template`,
so everything under `template/` is the rendered **child**; everything at the root
governs the **factory** and is not rendered. Master = factory; each generated
child = product.

## Key findings (severity)
1. **[HIGH] Meta-learner had no trigger.** The `learning/` system was
   architecturally complete but mechanically inert: `constitution.md` had zero
   learning mentions; `CLAUDE.md.jinja` referenced learning only as a passive read
   pointer; no hook/policy fired at a session boundary. Empty is correct for a
   fresh child, but nothing would ever fill it.
2. **[HIGH] The factory had no learning layer at all** — no root `.claude/`, no
   `CLAUDE.md`, no `learning/` — so the sessions building the template could not
   dog-food the meta-learner it ships.
3. **[MED] The only session-boundary automation was wrong.** Plugin
   `stop_reminder.py` is a `Stop` hook (fires every turn, not per session) and only
   prints a nudge — it writes nothing.
4. **[MED] `nothing_loose` write-guard fails open** at the factory root (no
   `.claude/policy/paths.allow.json`).
5. **[MED] `temporal-expansion-ideas/`** is untracked, un-gitignored, unindexed,
   reachable only from a stub; its `datavidence_integrated_final` proposal is
   superseded by the merged design.
6. **[MED] `datavidence-healthanalysis` plugin referenced but not installed** —
   `data-onboarding.md` + module docs route children to skills that don't exist.
7. **[LOW] False positives corrected:** `supplement.qmd.jinja` and
   `config.example.yml` exist; `llms.txt` does index the learning files.

Also missing: a root developer `CLAUDE.md`, a root `llms.txt`. The audit itself
exposed an 8th issue → a 112 KB result blob blew context and was unindexed (fixed
by the `/audit-report` convention).

## Decisions taken this session
- Built + **tested** the **factory meta-learner**: `.claude/hooks/`
  (SessionStart crash-detect, UserPromptSubmit signal capture, SessionEnd handoff)
  + `.claude/settings.json` + `learning/` (incl. `STANDARDS_WATCH.md`) + `/reflect`
  + root `CLAUDE.md`.
- **Patched the template meta-learner**: mirrored hooks into `template/.claude/`,
  added `learning/CONSENSUS_WATCH.md` (EQUATOR/GRADE/Cochrane + epistemic caveats,
  non-dogmatic), made the learning ritual a WRITE trigger (constitution rule 9 +
  `CLAUDE.md.jinja`), added child `/reflect`.
- Added the **`/audit-report`** skill + `docs/audits/` convention (factory + template).

## Pending (from the diagnosis, not yet done)
- Resolve `temporal-expansion-ideas/` (prose-ify briefs into `docs/research/` or
  archive + gitignore; finish the `routinely-collected-data.md` stub).
- Fix the `datavidence-healthanalysis` plugin reference (ship it, repoint, or mark planned).
- Add a root `llms.txt` for the factory; extend CI to render-and-validate, not just check placeholders.
- Decide whether to add a factory `.claude/policy/paths.allow.json` (activate the write-guard).
- Consider consolidating the learning-loop hooks into the plugin (versioned inheritance).
