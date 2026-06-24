# Contributing to datavidence-template-project

Thanks for improving the template. This repo is **the template itself**, not a
generated project — so the rules differ from those a generated project follows.

## Where things live

- **`template/`** — everything that gets rendered into a generated project. The
  Copier `_subdirectory` is `template`, so this is the renderable content root.
  **All template changes go here.**
- **`copier.yml`** — the questionnaire and engine settings (questions, excludes,
  tasks, messages).
- **Repo root** (`README.md`, `CONTRIBUTING.md`, `LICENSE`, `.github/`) —
  dev-facing docs and CI for the template repo. These are **not** rendered into
  generated projects.

## Golden rule: don't break the Copier variables

Inside `template/`, Copier substitutes `{{ project_name }}`, `{{ project_slug }}`,
`{{ author }}`, `{{ year }}`, `{{ license }}`, and `{{ analysis_stack }}` —
**but only in files whose name ends in `.jinja`** (the suffix is stripped on
render).

- If a file should contain rendered variables, its name **must** end in `.jinja`.
- If a file is copied verbatim, it **must not** contain `{{ ... }}` — the braces
  would appear literally in the generated project.
- The render-test guards this: `scripts/check_placeholders.py` runs against each
  rendered output and fails if unrendered placeholders leak through.

## Test your changes with the render-test

Render the template locally for each analysis stack and confirm no placeholders
leak:

```sh
uv tool install copier   # once
copier copy --defaults --data project_name=Smoke --data analysis_stack=r    . /tmp/out-r
copier copy --defaults --data project_name=Smoke --data analysis_stack=python . /tmp/out-python
copier copy --defaults --data project_name=Smoke --data analysis_stack=none  . /tmp/out-none
python /tmp/out-r/scripts/check_placeholders.py
python /tmp/out-python/scripts/check_placeholders.py
python /tmp/out-none/scripts/check_placeholders.py
```

CI (`.github/workflows/template-ci.yml`) runs the same render-test on every push
and pull request.

## What NOT to add

- **No `AGENTS.md`** anywhere. `CLAUDE.md` is the single source of prose rules.
- **No lockfiles** (`renv.lock`, `uv.lock`) committed in `template/` — generated
  projects produce them with `make setup`.
- **No duplication of the companion plugin.** Skills, hooks, and subagents live
  in [`psotobverse-utils`](https://github.com/psotob91/psotobverse-utils). The
  template references it; it never copies it.

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org):

```
feat(template): add Quarto manuscript skeleton to the R stack
fix(copier): correct project_slug validator regex
docs(readme): clarify the Cowork bridge flow
chore(ci): bump setup-uv action
```

Keep commits focused; one logical change each.

## Decisions: write an ADR

Non-trivial decisions about the template (adding a stack, changing the governance
model, restructuring policies) get an **Architecture Decision Record**. Add a new
numbered ADR under `template/docs/adr/` (the convention generated projects also
follow) describing context, decision, and consequences. This keeps the "why"
discoverable for future contributors.

## Pull requests

1. Branch from `main`.
2. Make focused changes under `template/` (or `copier.yml` / repo-root docs).
3. Run the render-test and ensure `check_placeholders.py` passes for all stacks.
4. Use Conventional Commit messages.
5. Open the PR and describe the change and its motivation; link the ADR if one
   applies.
