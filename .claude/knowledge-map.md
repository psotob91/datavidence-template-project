# Knowledge map — datavidence template factory

A router, not a corpus. It names the single file to open for a task. Open that
file and nothing else. (For the **child's** map, see
`template/.claude/knowledge-map.md.jinja` — different audience.)

## Read-first order

1. `.claude/constitution.md`
2. `SESSION_STATE.md` (where we are + next steps)
3. this map
4. `CLAUDE.md` (operational detail)

## Task type → consult

_Plugin skills auto-invoke by description; to call one explicitly use
`/psotobverse-utils:<name>`._

| Task type                                   | Consult / run                                                |
|---------------------------------------------|--------------------------------------------------------------|
| Resume / where are we                       | `SESSION_STATE.md`, then `git log --oneline -8`              |
| Understand a request before acting          | run `/comprehend`                                            |
| Make sure no relevant policy/file is missed | run `/coverage`                                              |
| Adversarially review a change / finding     | run `/cross-examine`                                         |
| Design a risky change                       | run `/deliberate`                                            |
| Audit coherence across the repo             | run `/reconcile`                                             |
| Organize / split oversize docs / loose files| run `/index` or `/tidy`                                      |
| Edit a child policy / structure             | `template/.claude/...` (then re-render — never hand-edit output) |
| Conditional policy routing                  | `template/.claude/policies/00-index.md.jinja` + `.../policy/routing.yml.jinja` |
| Copier questionnaire / gating               | `copier.yml`                                                 |
| Render-test / CI                            | `.github/workflows/template-ci.yml`; locally `copier copy --vcs-ref=HEAD` + `scripts/check_placeholders.py` |
| Companion-plugin development                 | `docs/plugins/datavidence-healthanalysis-blueprint.md`; the plugin repos (`[[plugin-repo-paths]]`) |
| Record a decision                           | `docs/adr/`                                                  |
| A recurring lesson                          | `learning/PLAYBOOK.md`                                       |
| A shifting Claude-Code/agent convention     | `learning/STANDARDS_WATCH.md`                                |
| Prior research / source material            | `docs/research/`                                             |

## Lazy-loading rule

Open only the target of the matching row. Do not preload `template/`, `docs/`, or
sibling rows "just in case". One row, one file.

## Regeneration recipe

`llms.txt` is a DERIVED index (git-ignored) — rebuild with
`python scripts/reindex.py`. The recipe is committed; the output is not.
