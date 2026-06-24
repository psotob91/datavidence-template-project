# Cowork verification checklist (one-time, per machine)

Confirms the companion plugin's guardrails actually work in **Cowork**. Two
assumptions behind the plugin-primary design need an empirical check on your
machine (see `docs/adr/0002-cowork-plugin-verification-spike.md`):

1. plugin-bundled hooks/subagents fire in Cowork, and
2. `$CLAUDE_PROJECT_DIR` resolves to the selected folder inside Cowork's VM
   (so `nothing_loose` can read this project's `.claude/policy/paths.allow.json`).

## Before you start — read this first

- **Two different runtimes.** *Claude Code* (terminal) auto-reads `CLAUDE.md` +
  `.claude/`. *Cowork* (Claude Desktop GUI) does **not** — you paste the rules
  into its **Instructions** field. The plugin is the only thing that carries
  hooks/skills/subagents into Cowork (a project's `settings.json` hooks do NOT
  fire there).
- **Use a GENERATED project, not this template repo.** Run these steps in a
  project you made with `copier copy` (it has `.claude/constitution.md` and
  `.claude/policy/paths.allow.json` at its root, which the checks rely on). The
  template repo itself has no `.claude/` at its root, so the checks won't work
  there. A throwaway generated project is fine.
- **You do NOT need to run any slash command to set up.** Every generated
  project already ships a usable `.claude/COWORK_INSTRUCTIONS.md` **stub** — you
  can paste it as-is. (Optional upgrade below.)

## Part A — Setup (Cowork GUI, one time)

1. **Install the plugin (once per machine):** Claude Desktop → **Cowork →
   Customize → Plugins** → add marketplace `psotob91/psotobverse-utils` →
   install **psotobverse-utils**.
2. **Open the project:** **Cowork → Projects → + → Use an existing folder** →
   select your generated project's folder.
3. **Paste the rules:** open `.claude/COWORK_INSTRUCTIONS.md`, copy everything
   between `[PASTE FROM HERE]` and `[END]`, and paste it into the project's
   **Instructions** field.
4. **Add context:** add the `context/` folder as the project **Context**.

> **Optional — full instructions instead of the stub.** In a **terminal**
> `claude` session inside the project (NOT the Cowork GUI, and NOT an embedded
> IDE chat), run `/psotobverse-utils:sync-cowork`. It regenerates
> `.claude/COWORK_INSTRUCTIONS.md` from the constitution + overlay (approve the
> `.claude/` write when asked), then re-paste. The shipped stub already works
> without this.

## Part B — Verify (type these as prompts INSIDE Cowork)

| # | Ask Cowork to…                                            | Expected                                  |
|---|-----------------------------------------------------------|-------------------------------------------|
| 1 | "Create a file `loose.txt` at the project root, text: hi" | **Blocked** by `nothing_loose`            |
| 2 | "Create `R/scratch.R` with a comment"                     | **Allowed** (inside the allowlist)        |
| 3 | "Read the `.env` file"                                    | **Blocked** by `env_protect`              |
| 4 | "Tidy up the loose files"                                 | `tidy` **proposes** moves, never auto-moves |
| 5 | "Audit this project for coherence"                        | `reconcile` engages (may spawn `explorer`)  |

**Pass criteria:** #1 **blocked** AND #2 **allowed** → hooks fire in Cowork AND
`$CLAUDE_PROJECT_DIR` resolves correctly. If *everything* is allowed regardless,
the hooks aren't firing (or no allowlist was found): `nothing_loose` fails open,
so you're safe but with **no enforcement** in Cowork — record that.

## Record

Update `docs/adr/0002-cowork-plugin-verification-spike.md`: set **Status:
Accepted** if #1/#2 pass, or note which assumption failed and that
`nothing_loose` fail-open keeps Cowork safe (no enforcement) until resolved.

## Troubleshooting

- **`Unknown command: /psotobverse-utils:sync-cowork`** — you typed it in an
  embedded IDE chat, or in a terminal session started *before* the plugin was
  installed. Plugin commands are namespaced and only load in a fresh terminal
  `claude`. Fix: restart `claude` / run `/reload-plugins`, or just skip it and
  paste the shipped stub.
- **Plugin not listed** — run `/reload-plugins` (or restart). Confirm with
  `claude plugin list` (Status should be `✔ enabled`).
- **Skills don't auto-fire** — describe the task in natural language
  ("audit this", "tidy the loose files"); to call one explicitly use
  `/psotobverse-utils:<name>`.
