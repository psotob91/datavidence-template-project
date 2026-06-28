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
[2026-06-28][workflow] Percy named a standing model-routing rule (previously undocumented — grep found it nowhere): hard reasoning / planning / authoring nuanced methodology → Opus; code-execution / mechanical → Sonnet; peer-evaluation → Sonnet (generator ≠ auditor). Captured to `memory/model-routing.md` + PLAYBOOK. Applied on the health-data-policy build: Opus authored the policies; Sonnet `executor`/Explore agents did MHTML extraction + (planned) render/git + the adversarial review pass. Lesson: when the user states a working-method preference, persist it immediately — verbal rules evaporate across sessions.
[2026-06-28][token-efficiency] Reading large `.mhtml` Gemini exports (~41k lines / 2.5 MB) blew a subagent's context when parsed whole — ~95% of the file is base64 images + CSS. The conversation lives entirely in the FIRST `text/html` quoted-printable part (≈lines 13–12326). Fix that worked: Python `email` parser → take only that part → decode QP → strip script/style/tags + `data:` URIs → clean ~60–100 KB text in scratchpad → chunk → have a Sonnet subagent return a STRUCTURED digest (raw never reaches Opus). PREVENTION: for any oversized source (mhtml/pdf/transcript/dump), extract-narrow → chunk → digest-off-context; never let the raw enter the reasoning context. (Generalized into PLAYBOOK.)
[2026-06-28][copier] Copier renders the latest git TAG by default, not HEAD. This factory develops on `main` without per-change release tags, so `new-study.ps1` and the CI render matrix were silently rendering the only tag — the ancient `v0.1.0` (pre-meta-learner). CI stayed GREEN because v0.1.0 had no leaked placeholders, so "tests pass" masked "tests test the wrong thing". Caught only when a manual render came back ~55 lines (no meta-learner section) instead of ~105. Fix: `--vcs-ref=HEAD` in the generator script AND CI (CI also needs `fetch-depth: 0`). PREVENTION next time: (1) when wiring any `copier copy`, decide tag-vs-HEAD EXPLICITLY — the silent default is the latest tag; (2) read copier's `Copying from template version X` line — if X is an old tag (not `…postN.dev…+<sha>`) you're rendering stale; (3) a passing render/CI does NOT prove freshness — assert the output contains a RECENT feature, not just "no placeholders"; (4) for plain `copier copy`/`copier update` to track reality without flags, TAG releases and keep the tag current.
