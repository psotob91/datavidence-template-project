# Standards Watch — Anthropic / Claude Code agent-building conventions

A **living radar** of the conventions this factory relies on for building
AI-supported artifacts: skills, plugins, MCP servers, hooks, RAG, and
agentic repos. This space **changes fast** (weeks, not years). The point of this
file is not to freeze a dogma but to make our assumptions **explicit, dated, and
falsifiable**, so drift is visible.

## Epistemic rules (read before adding/trusting an entry)

1. **Every entry is provisional.** It carries an `as-of` date, a `confidence`,
   and a `re-verify` trigger. An entry past its trigger is *suspect*, not law.
2. **Source-anchored, not authority-anchored.** Prefer the official docs
   (`docs.claude.com` / `code.claude.com`) or a first-party changelog over blog
   posts. Record the source.
3. **No dogmatism.** When a convention is contested or moving, say so in *Notes*
   and keep the alternative visible. Flag, don't enforce.
4. **Escalate, don't silently adopt.** When `/reflect` detects that a convention
   we depend on may have changed, it should **ask the user** and recommend a
   re-verification, not rewrite the template unilaterally.
5. **Fast-change ≠ rebuild constantly.** Only act on a change when it affects a
   file we ship. A new shiny pattern that doesn't touch our artifacts goes to
   *Watching*, not *Adopted*.

## Adopted (we depend on these today)

| Topic | Current understanding | as-of | Confidence | Re-verify | Source |
|---|---|---|---|---|---|
| Hooks events | `SessionStart`, `UserPromptSubmit`, `Stop`, `SubagentStop`, `SessionEnd`, `PreToolUse`, `PostToolUse`, `PreCompact`, `Notification`; JSON on stdin; `SessionStart` can inject `additionalContext` | 2026-06-28 | High | when a hook silently stops firing, or every ~2 mo | code.claude.com/docs/en/hooks |
| Plugin layout | `.claude-plugin/plugin.json` manifest; `hooks/`, `skills/`, `agents/`, `commands/` dirs; `${CLAUDE_PLUGIN_ROOT}` not shell-expanded everywhere → read env by name (ADR-0002) | 2026-06-28 | High | on next plugin SDK release | code.claude.com/docs/en/plugins |
| Skills | `SKILL.md` with YAML frontmatter (`name`, `description`); description drives triggering; progressive disclosure (don't preload bodies) | 2026-06-28 | High | every ~2 mo | code.claude.com/docs/en/skills |
| Memory / CLAUDE.md | root `CLAUDE.md` re-read after `/compact`; nested/conversation-only instructions are NOT auto-re-injected → persist durable state to disk | 2026-06-28 | High | every ~2 mo | code.claude.com/docs/en/memory |
| Machine index | `llms.txt` per llmstxt.org (single H1, blockquote summary, H2 link sections, a literal `## Optional` section) | 2026-06-28 | Med | when render-validation lands | llmstxt.org |

## Watching (may matter soon — do NOT act yet)

| Topic | Signal | as-of | Why it might matter | Recommended check |
|---|---|---|---|---|
| AGENTS.md ecosystem | Cross-agent `AGENTS.md` gaining adoption; Claude Code still reads only `CLAUDE.md` | 2026-06-28 | If children must support multiple agents, bridge (import/symlink) rather than duplicate | Re-check whether Claude Code reads AGENTS.md natively |
| RAG retrieval | Hybrid (BM25 + dense + rerank) is the safe default; GraphRAG/LazyGraphRAG only if multi-hop is proven (ADR-0003) | 2026-06-28 | The companion retrieval MCP is in active dev | Re-verify before committing to a graph approach |
| Cowork plugin delivery | Server-side marketplace sync is broken (serves stale versions; GH #39400/#38008/#39274/#40600). DECISION: deprecate Cowork for our plugins; develop+run in Claude Code (terminal) only. | 2026-06-29 | Cowork could silently run an old plugin version | Re-check GH #39400 before re-targeting Cowork |

## Contested / be measured (no single right answer)

- **Whether to auto-wire reflection as a hook vs. a manual ritual.** We chose a
  hybrid (hook captures, human gates synthesis). Some setups auto-edit; we judged
  that too risky (silent drift). Keep the gate unless evidence says otherwise.

<!-- /reflect appends here from the signal queue. Keep entries dated and sourced. -->
