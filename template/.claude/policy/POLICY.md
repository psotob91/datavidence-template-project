# Project policy (enforced layer)

Project-level rules the companion plugin enforces at tool time. These complement
the prose charter; they are the machine-checked guardrails.

## What is enforced

- **Write allowlist.** Writes are permitted only under the paths listed in
  `paths.allow.json` (`allow_write`). Anything outside is denied.
- **Secret protection.** Paths matching `protect` (`.env`, keys, PEM, `id_*`)
  are never writable, even if they sit under an allowed directory.
- **Nothing-loose.** Generated artifacts must land in their designated
  directories (notably `outputs/`), not scattered across the tree.

## How

The companion plugin's `nothing_loose` PreToolUse hook reads
`paths.allow.json` via `$CLAUDE_PROJECT_DIR` and applies these rules. If that
file is absent or unreadable, the hook FAILS OPEN (writes proceed) — so keep the
file present and valid.
