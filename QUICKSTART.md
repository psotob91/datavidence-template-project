# QUICKSTART — mount a new study in ~5 minutes

A direct, copy-paste recipe. We use one real example all the way through:

> **Example study:** *Anemia Infantil Puno* — a childhood-anemia cohort in Puno,
> R stack. Replace the name/paths with your own as you go.

You do **not** just clone a folder — you generate a **named, configured** project
and let Claude Code orient you on what to fill in before you start.

---

## 0. One time per machine (skip if already done)

```powershell
# Copier (the project generator)
uv tool install copier        # or: pipx install copier

# The companion plugin (skills + governance hooks). Once, machine-global.
claude plugin marketplace add psotob91/psotobverse-utils
claude plugin install psotobverse-utils@psotobverse-utils
claude plugin list            # expect: psotobverse-utils  ✔ enabled
```

> After any `claude plugin` change, start a **fresh** `claude` session so the
> hooks load.

---

## 1. Generate the project (this is where you give it a title)

Interactive — Copier asks you a short questionnaire, so the project is **named and
configured**, not just copied:

```powershell
copier copy gh:psotob91/datavidence-template-project C:\workspace\anemia-infantil-puno
```

Answer like this (our example):

| Question         | What you type for the example      | Notes                                  |
| ---------------- | ---------------------------------- | -------------------------------------- |
| `project_name`   | `Anemia Infantil Puno`             | the human title; shows in README/docs  |
| `project_slug`   | *(press Enter)* → `anemia_infantil_puno` | auto-derived; valid R/Python name |
| `author`         | *(press Enter)* → `Percy Soto-Becerra` |                                    |
| `year`           | *(press Enter)* → `2026`           |                                        |
| `license`        | *(press Enter)* → `MIT`            |                                        |
| `analysis_stack` | `r`                                | R + {targets} + Quarto                 |
| `project_profile` | `health-data`                     | adds EQUATOR reporting + clinical tables/flows (use `standard` for non-clinical) |
| `modules`         | *(optional)* e.g. `causal`         | task packs (space to select); leave empty if unsure |
| `knowledge_retrieval` | `none`                        | leave as none unless you need RAG      |

Then turn it into a git repo:

```powershell
cd C:\workspace\anemia-infantil-puno
git init -b main; git add -A; git commit -m "chore: init Anemia Infantil Puno from datavidence template"
```

> **Shortcut (if you cloned this template repo):** one command does generate +
> git init + commit:
> ```powershell
> .\scripts\new-study.ps1 -Name "Anemia Infantil Puno" -Dest "C:\workspace\anemia-infantil-puno"
> ```

---

## 2. Open it in Claude Code

```powershell
cd C:\workspace\anemia-infantil-puno
claude
```

Claude Code auto-loads `CLAUDE.md` + `.claude/`. **Do NOT run `/init`** — a curated
governance setup already ships here; `/init` would clobber it.

---

## 3. Paste the START PROMPT (orientation)

This is the important part. Paste this as your **first message**. It makes Claude
read the rules, give you a **panorama** of what you have, and tell you the
**minimum** it needs from you to begin — then offer to set up your `PROJECT_BRIEF`.

```text
You are starting a fresh project generated from the datavidence template.
First, read these in order (only what you need): .claude/constitution.md →
.claude/policies/00-index.md → .claude/knowledge-map.md → CLAUDE.md →
PROJECT_BRIEF.md.

Then do THREE things, briefly:

1) PANORAMA — in <10 bullet points, tell me what this project already gives me:
   the governance rules in force (what will be blocked/allowed), the analysis
   stack and how to run it, where inputs go (context/), where outputs go
   (outputs/), and which files are still empty placeholders I must fill.

2) WHAT YOU NEED FROM ME — list the MINIMUM I must provide to start real work,
   as a short checklist. At least: the study goal/question, the population and
   setting, the main outcome(s) and exposure(s), the data source(s), the audience,
   success criteria, key constraints, and any deadline. Ask me for these now.

3) NEXT STEP — once I answer, propose the exact diff to fill PROJECT_BRIEF.md
   from my answers (apply only after I confirm), and tell me the single next
   prompt I should send to begin the analysis.

Rules: do not invent facts or data; if something isn't in my answers or the repo,
say "unknown" and ask. Mark uncertainty. Ask before irreversible actions. Put all
deliverables under outputs/.
```

Claude will reply with the panorama + a short checklist of what to tell it. You
answer in plain language; it fills `PROJECT_BRIEF.md` for you (you approve the
diff). That's your project configured — not just a copied folder.

---

## 4. Restore the analysis environment

```powershell
make setup     # R: restores renv  |  Python: uv sync
make test      # runs the {targets} pipeline (R) / pytest (Python)
```

Lockfiles (`renv.lock` / `uv.lock`) are generated here and intentionally **not**
committed by the template.

---

## 5. (Optional) Use it in Cowork too

In the Claude Code session, generate the bridge once:

```text
/psotobverse-utils:sync-cowork
```

It writes `.claude/COWORK_INSTRUCTIONS.md`. In Cowork → Projects → + → **Use an
existing folder** → select the project → paste that file into **Instructions**.

> Note: Cowork governs via a server-synced plugin that may lag behind the latest
> plugin version. Claude Code is the runtime of record; see
> [`template/docs/adr/0002-cowork-plugin-verification-spike.md`](template/docs/adr/0002-cowork-plugin-verification-spike.md).

---

## What you have now (the panorama, in one glance)

| You get | Where |
| --- | --- |
| Charter + atomic policies (the rules Claude follows) | `.claude/constitution.md`, `.claude/policies/` |
| Write-guard + secret-protection hooks | companion plugin (auto, in Code) |
| Single source of intent (you fill this) | `PROJECT_BRIEF.md` |
| Your input materials (read-only) | `context/` |
| Your deliverables (self-contained) | `outputs/<slug>/` |
| Scratch (ephemeral) | `tmp/` |
| Decisions log | `docs/adr/` |
| Lessons that proved reusable | `learning/PLAYBOOK.md` |

More detail per project: [`docs/SETUP.md`](template/docs/SETUP.md.jinja) (short
card) and [`docs/ACTIVATION.md`](template/docs/ACTIVATION.md.jinja) (full).

---

## Recipe TL;DR

```powershell
# once per machine
uv tool install copier
claude plugin marketplace add psotob91/psotobverse-utils
claude plugin install psotobverse-utils@psotobverse-utils

# per study
copier copy gh:psotob91/datavidence-template-project C:\workspace\<your-study>
cd C:\workspace\<your-study>; git init -b main; git add -A; git commit -m "chore: init"
claude            # paste the START PROMPT from step 3, then answer its checklist
make setup
```
