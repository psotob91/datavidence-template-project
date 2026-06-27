# Factory Learning Log

Append-only journal of concrete lessons learned **building the template factory**
(not the analysis work inside a generated child — that has its own log shipped in
`template/learning/`). Newest at the bottom. **Never edit or delete past entries**;
if a lesson is later proven wrong, append a correcting entry.

Distilled, reusable conclusions graduate into `PLAYBOOK.md`; raw candidate
improvements are triaged in `REFLECTOR.md`; emerging Anthropic agent-building
conventions are tracked in `STANDARDS_WATCH.md`.

## Format

```
[YYYY-MM-DD][topic] lesson — what happened, what we learned, what to do next time.
```

`topic` is a short tag (e.g. `hooks`, `copier`, `audit`, `plugin`, `meta-learner`).

## Entries

[2026-06-28][meta-learner] The master/factory repo had no `.claude/`, no `CLAUDE.md`, and no learning layer, so the sessions that BUILD the template could not dog-food the meta-learner the template ships. Added a factory-scoped meta-learner (SessionStart/UserPromptSubmit/SessionEnd hooks + `/reflect`). Lesson: a template that preaches a practice must dog-food it at the factory level, or the practice rots untested.
[2026-06-28][hooks] Session diaries belong on `SessionEnd`, not `Stop` — `Stop` fires after every assistant turn (wrong cadence). Crash detection uses a dirty-bit: SessionStart arms `status=active`; SessionEnd flips to `clean_exit`; an `active` bit at next start ⇒ unclean exit. Verified by running the hooks directly with simulated stdin before trusting them.
[2026-06-28][audit] A multi-agent audit wrote a single 112 KB JSON blob to a temp file, which blew context and was unindexed (drift/hallucination risk). Lesson: audits must emit a SMALL indexed summary (diagnosis + verdict) to a known path and keep the raw maps separate and referenced — never inline a mega-artifact. (See the audit-output policy/skill.)
[2026-06-28][plugin] First-built the meta-learner mechanism LOCALLY (factory + template), then refactored it INTO the psotobverse-utils plugin (v1.4.0) because the mechanism is generic/orthogonal — duplicating it into the factory + N children violated DRY. Lesson: generic MECHANISM → plugin (versioned, fix-once); only DATA + CONFIG + routing stays local. Made the plugin hooks OPT-IN via `.claude/meta-learner.json` so they no-op in unrelated repos (a user-scope hook that WRITES into every project would litter them).
