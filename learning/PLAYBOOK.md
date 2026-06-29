# Factory Playbook

**Distilled, read before a task.** Curated, high-signal guidance for maintaining
the **template factory** (this repo), not the analysis work inside a child. Keep
it short; if a line stops being true, fix it and log the correction in
`LEARNING_LOG.md`.

## What this repo is

- This repo is a **Copier factory**, not a project. `copier.yml` sets
  `_subdirectory: template`, so **everything under `template/` is the rendered
  CHILD**; everything at the root governs the **factory itself** and is NOT
  rendered. Master = factory; each generated child = product.
- Never hand-edit generated output. Edit the `.jinja` source under `template/`,
  then re-render. Verify with the render matrix (`.github/workflows/template-ci.yml`).

## Patterns that work

- Two `CLAUDE.md` files, different audiences: the **root `CLAUDE.md`** (this
  layer) is for template MAINTAINERS; **`template/CLAUDE.md.jinja`** governs
  generated children. Do not conflate them.
- Hooks are Python stdlib, no venv, and use the portable bootstrapper
  (`python -c` reading `CLAUDE_PROJECT_DIR` from `os.environ`, fail-open). Test a
  hook by piping simulated stdin JSON to the script before wiring it.
- Keep the meta-learner hybrid: cheap append-only capture during the session
  (`UserPromptSubmit`), a deterministic skeleton on `SessionEnd`, and a
  **human-gated** `/reflect` for synthesis. Never let a hook silently edit a
  learning file.
- **Model routing (Percy's standing rule):** hard reasoning / planning / authoring
  nuanced methodology → **Opus**; code-execution / mechanical → **Sonnet**;
  peer-evaluation / adversarial review → **Sonnet** (generator ≠ auditor). In the main
  session keep authoring on Opus and spawn Sonnet agents (`model: sonnet`, e.g.
  `psotobverse-utils:executor`) for extraction/render/git and for review passes.
- **Big source files (mhtml/pdf/transcripts/dumps): extract narrow → chunk → digest
  off-context.** An MHTML "Save page" export is ~95% base64 images + CSS; the real
  content is the FIRST `text/html` quoted-printable part (in a Gemini export ≈lines
  13–12326 of ~41k). Pull only that part with Python's `email` parser, decode QP, strip
  `<script>/<style>/<tags>` + `data:` URIs → clean ~60–100 KB text in scratchpad. Then
  hand the chunks to a Sonnet subagent that returns a STRUCTURED digest, so the raw
  never enters the Opus context. If the main session must read, use `Read` offset/limit
  ranges — never the whole file. (This is `token-efficiency.md` applied to binaries.)

## Gotchas

- Do NOT run `/init`; this curated `CLAUDE.md` is authoritative and `/init` would
  clobber it.
- The `psotobverse-utils` plugin hooks fire at USER scope (every session). The
  write-guard `nothing_loose` FAILS OPEN here because the factory root has no
  `.claude/policy/paths.allow.json` — add one only if you want write-allowlisting
  at the factory level (it will start checking your writes immediately).
- `template/llms.txt` is the CHILD's index; the factory has its own root
  `llms.txt`. Regenerate the child's with `make reindex` inside a render.
- **Copier renders the latest git TAG by default, not HEAD.** We develop on `main`
  without per-change release tags, so any `copier copy` without `--vcs-ref=HEAD`
  renders the stale `v0.1.0` snapshot. `new-study.ps1` and CI now pass
  `--vcs-ref=HEAD` (CI: `fetch-depth: 0`). When wiring/reading any render: decide
  tag-vs-HEAD explicitly, check copier's `Copying from template version X` line
  (an old tag, not `…dev…+<sha>`, means stale), and don't trust a green render —
  it can pass against the wrong version. If you ever want plain `copier copy` /
  `copier update` to track reality, start tagging releases.

- **Scripted regex rewrites: no DOTALL on bounded matches; verify with `git diff --stat`.**
  A `(?s)`/DOTALL flag makes `.*` cross newlines and run to EOF -- a bounded "frontmatter
  block" rewrite ate whole files. Match line-bounded blocks WITHOUT DOTALL; for
  whitespace-flexible text, tokenize and join with `\s+` (`re.escape` escapes spaces, so
  `.replace(' ', r'\s+')` is wrong). After any scripted multi-file rewrite, read
  `git diff --stat` BEFORE committing -- a wildly asymmetric insert/delete count (e.g. 26/465)
  is the tell that the regex over-matched.
- **One heredoc per Bash call on this machine.** Git Bash here fails to parse a single command
  containing multiple heredocs ("unexpected EOF"); write one file per call. Cross-repo/plugin
  writes go via Bash/python (the factory `nothing_loose` guard blocks Edit/Write outside the
  project root).

## Optimal disclosure (read order for a new session)

1. Root `CLAUDE.md` → 2. `SESSION_STATE.md` (current state) →
3. `git log --oneline -8` → 4. pull detail on demand from `CHANGELOG.md`,
the relevant ADR, and `learning/sessions/` handoffs. Do not preload `template/`.
