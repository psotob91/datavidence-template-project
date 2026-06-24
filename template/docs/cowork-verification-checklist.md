# Cowork verification checklist (one-time, per machine)

Claude Code and Cowork are different runtimes. The companion plugin
`psotobverse-utils` is the only carrier of guardrails into Cowork (a project's
`.claude/settings.json` hooks do NOT fire there). Two assumptions behind that
design are unverified until you check them on your machine (see
`docs/adr/0003-...` and the project's `docs/adr/0002-cowork-plugin-verification-spike.md`):

1. plugin-bundled hooks actually fire in Cowork, and
2. `$CLAUDE_PROJECT_DIR` resolves to the selected folder inside Cowork's VM
   (so `nothing_loose` can read this project's `.claude/policy/paths.allow.json`).

Run this once after installing the plugin in Cowork. Record the outcome in
`docs/adr/0002-...`.

## Setup

1. Claude Desktop → **Cowork → Customize → Plugins** → add marketplace
   `psotob91/psotobverse-utils` → install **psotobverse-utils** (machine-global).
2. In a Claude **Code** session in this project, run `/sync-cowork` to generate
   `.claude/COWORK_INSTRUCTIONS.md`.
3. Cowork → **Projects → + → Use an existing folder** → select this project.
   Paste `.claude/COWORK_INSTRUCTIONS.md` into the project **Instructions**, and
   add `context/` as **Context**.

## Checks

| # | Ask Cowork to… | Expected | If it fails |
|---|----------------|----------|-------------|
| A | Write a file **outside** the allowlist, e.g. `loose.txt` at the repo root | **Blocked** by `nothing_loose` | Hooks are NOT firing in Cowork → record in ADR-0002; rely on `COWORK_INSTRUCTIONS` rules only |
| B | Read `.env` | **Blocked** by `env_protect` | As above |
| C | Write `R/scratch.R` (inside the allowlist) | **Allowed** | If also blocked → over-blocking; check `paths.allow.json` |
| D | Both A (blocked) and C (allowed) hold | `$CLAUDE_PROJECT_DIR` resolves + allowlist is read correctly | If everything is allowed regardless → `nothing_loose` is failing open (safe, but no enforcement in Cowork) → record in ADR-0002 |
| E | "audit this for coherence" → `/reconcile` | Skill engages; can spawn the `explorer` auditor | Subagents not available → record |
| F | "tidy up the loose files" → `/tidy` | Skill **proposes** moves, does not auto-move | — |

## Record

Update `docs/adr/0002-cowork-plugin-verification-spike.md`: set **Status:
Accepted** if A–D pass, or note exactly which assumption failed and that
`nothing_loose` fail-open keeps Cowork safe (no enforcement) until resolved.
