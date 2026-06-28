# Factory policy (enforced layer)

Repo-level rules the companion plugin enforces at tool time on **this factory repo**.
They complement the prose charter (`.claude/constitution.md`); these are the
machine-checked guardrails.

## What is enforced

- **Write allowlist.** Writes are permitted only under the paths listed in
  `paths.allow.json` (`allow_write`). A new loose file elsewhere is denied — this is
  the "nothing loose" guard (constitution rule 8).
- **Secret protection.** The plugin's `env_protect` hook blocks `.env`, keys, PEM, and
  `id_*` regardless of the allowlist.

## How

The installed `psotobverse-utils` `nothing_loose` PreToolUse hook reads this
`paths.allow.json` via `$CLAUDE_PROJECT_DIR` and applies the rules. If the file is
absent or unreadable, the hook **FAILS OPEN** (writes proceed) — so keep it present and
valid. Note (safe-edit): a write whose path resolves **outside** this repo is denied by
`nothing_loose`, so cross-repo edits (e.g. the plugin source repos) require a session
rooted in that repo — see each plugin's "Safe-edit protocol".
