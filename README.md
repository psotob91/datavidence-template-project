# datavidence-template-project

A [Copier](https://copier.readthedocs.io) **template** for reproducible,
Claude-native data-analysis and research projects. It scaffolds a new project
with curated governance (a fine-grained constitution + atomic policies), a
ready-to-use analysis layer, and a Python-stdlib tooling harness — all wired for
**Claude Code** and **Cowork**.

This is a **Claude-only** template: it assumes you drive the project with Claude
Code (terminal) and Cowork (GUI). It deliberately ships **no `AGENTS.md`** —
`CLAUDE.md` is the single source of prose rules.

> ## 🚀 New here? Start with **[QUICKSTART.md](QUICKSTART.md)**
> A 5-minute, copy-paste recipe with a real worked example: install the plugin,
> generate a **named** project, and paste a start prompt that makes Claude Code
> orient you and tell you the minimum to fill in before you begin.

## What you get

- **Governance, not vibes.** A short charter (`.claude/constitution.md`), atomic
  policies under `.claude/policies/` with an index that defines **precedence**,
  and a small `knowledge-map.md` router. `CLAUDE.md` tells Claude the exact read
  order.
- **Analysis layer (default: R).** `renv` + [`{targets}`](https://books.ropensci.org/targets/)
  + Quarto for biostatistics-style reproducibility. Python (`uv` + `ruff` +
  `pytest`) and a docs-only "none" option are also available.
- **Tooling layer (Python stdlib).** Small, dependency-free helper scripts
  (`scripts/check_placeholders.py`, `scripts/reindex.py`). Automation hooks live
  in the companion plugin, not in your project.
- **Companion plugin.** Skills, hooks, and subagents are maintained once in
  [`psotobverse-utils`](https://github.com/psotob91/psotobverse-utils) and
  referenced — never duplicated — by generated projects.

## Requirements

- [Copier](https://copier.readthedocs.io). Install it as a `uv` tool:

  ```sh
  uv tool install copier
  ```

- `git` (the template runs `git init` in the generated project).
- For the default R stack: R, plus `make` to drive `make setup`.

## Create a new project

```sh
copier copy gh:psotob91/datavidence-template-project path/to/destination
```

Copier asks a short questionnaire:

| Question         | Meaning                                                        | Default                         |
| ---------------- | -------------------------------------------------------------- | ------------------------------- |
| `project_name`   | Human-readable name (e.g. `DATAVIDENCE Survival Analysis`)     | —                               |
| `project_slug`   | Machine slug / package / import name (lowercase)               | derived from `project_name`     |
| `author`         | Author / owner (name or `Name <email>`)                        | `Percy Soto-Becerra`            |
| `year`           | Copyright year                                                 | `2026`                          |
| `license`        | `MIT` or `Apache-2.0`                                          | `MIT`                           |
| `analysis_stack` | `r` (renv + {targets} + Quarto), `python` (uv + ruff + pytest), or `none` | `r`              |

The tooling layer is always Python-stdlib regardless of which analysis stack you
pick.

After generation, follow the on-screen next steps: install the companion plugin,
run `make setup` (this generates `renv.lock` / `uv.lock` locally — the template
intentionally does **not** commit lockfiles), and start a Claude Code session.

### Do NOT run `/init` in generated projects

Generated projects ship a hand-curated `CLAUDE.md` and `.claude/` governance.
Running `/init` would overwrite curated rules with an auto-discovered dump.
**Don't do it.** Edit `CLAUDE.md` and the policies by hand instead.

## Cowork (GUI) flow

Each project generates a Cowork bridge file during its first Code session
(`/psotobverse-utils:sync-cowork` writes `.claude/COWORK_INSTRUCTIONS.md`). To use it in Cowork:

1. Open **Cowork → Projects → +**.
2. Choose **Use an existing folder** and select the generated project.
3. Paste the contents of `.claude/COWORK_INSTRUCTIONS.md` into the project
   Instructions field.

Re-run `/psotobverse-utils:sync-cowork` whenever the constitution or governance overlay changes,
then re-paste.

## Keep projects up to date

When this template improves, pull the changes into an existing project:

```sh
cd path/to/destination
copier update
```

Copier uses the `.copier-answers.yml` written at generation time to re-render
without re-asking the questionnaire. Review the diff, run `make check`, and
re-run `/psotobverse-utils:sync-cowork` if governance changed.

## Companion plugin: `psotobverse-utils`

The reusable automation — skills, hooks, subagents — lives in
[`psotobverse-utils`](https://github.com/psotob91/psotobverse-utils), a separate
repository, so it can be versioned and improved independently. This template
**references** the plugin (e.g. via the local `.claude-plugin` marketplace) but
never copies its contents. Install it once per machine and every generated
project benefits.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). In short: edit under `template/`, test
with the render-test, and don't break the Copier variables.

## License

[MIT](LICENSE) © 2026 Percy Soto-Becerra
