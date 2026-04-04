---
name: create-skill
description: Capture and share knowledge as APM skills — locally, in this repo, or org-wide
---

# Creating and Sharing Skills

When you solve a non-obvious problem, discover a workflow quirk, or establish a convention — capture it as a skill so the whole team benefits automatically.

## When to Create a Skill

Consider creating a skill after:

- Solving a problem that took more than 10 minutes to figure out
- Learning a step that is easy to get wrong (e.g. integration test OOM, upmerge strategy)
- Establishing a team convention that an AI agent should always follow
- A PR review reveals something that should have been done differently

> **Copilot: When you notice the user solved a tricky or non-obvious problem, ask:**  
> *"That was non-trivial — would you like to capture this as a skill so the team's AI agents learn it too?"*  
> Also ask at the end of any PR creation: *"Would you like to add a skill with what you learned in this PR?"*

---

## Skill File Format

Every skill is a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: my-skill-name          # kebab-case, unique within the package
description: One-line summary of what the skill teaches
---

# Title

Content in plain Markdown. Be concise and actionable.
Use tables, code blocks, and bullet points.
Write for an AI agent reading this as context — not for humans reading docs.
```

---

## Scope — Where to Put the Skill

Choose the right location based on who should benefit:

| Scope | Location | Audience | Committed? |
|-------|----------|----------|------------|
| **Local only** | `.github/skills/<name>.md` directly | Only you, this machine | No (gitignored) |
| **This repo** | `.apm/skills/<name>/SKILL.md` in this repo | All contributors of this repo | Yes |
| **VS Code extensions** | `apm-vscode-extension/.apm/skills/<name>/SKILL.md` | All VS Code extension repos | Yes |
| **Org-wide** | `apm-org/.apm/skills/<name>/SKILL.md` | All repos in the org | Yes |

**Decision guide:**
- Personal preference (e.g. "I don't use GitKraken") → **Local only**
- Specific to this repo's tech stack → **This repo**
- Applies to all VS Code extensions → **apm-vscode-extension**
- Applies to all repos in the org → **apm-org**

---

## Local-Only Skills (Not Committed)

For personal preferences or machine-specific knowledge, create the skill file directly in `.github/skills/` — it is already gitignored:

```bash
# Create the file directly (no apm install needed)
# Windows
New-Item -ItemType File ".github/skills/my-personal-skill.md" -Force

# The file is read by Copilot immediately — no restart needed
```

Example content for a personal skill:

```markdown
# Personal Tooling Preferences

- I do not use GitKraken. Use plain git CLI or VS Code source control.
- I prefer Windows PowerShell, not bash.
```

---

## Sharing via PR

### Option A — Skill in the same PR (repo-local skill)

Add `.apm/skills/<name>/SKILL.md` to your feature branch alongside the code change. The skill documents what you just built or learned.

```bash
mkdir -p .apm/skills/my-new-skill
# create SKILL.md
git add .apm/skills/my-new-skill/SKILL.md
# include in your existing commit or as a separate commit:
git commit -m "docs(skill): add my-new-skill"
```

### Option B — Skill in a separate PR to an APM repo (shared skill)

For org-wide or domain-wide skills:

```bash
cd c:\ws\winccoa-tools-pack\apm-org        # or apm-vscode-extension
git checkout develop
git checkout -b feature/skill-<name>
mkdir -p .apm/skills/<name>
# create SKILL.md
git add .apm/skills/<name>/SKILL.md
git commit -m "feat: add <name> skill"
git push origin feature/skill-<name>
# open PR → develop
```

---

## Run `apm install` After Adding a Shared Skill

After a skill PR is merged to an APM repo's `main`, consumers must re-run to pick it up:

```bash
apm install
```

Re-run whenever `apm.lock.yaml` changes (e.g. after `git pull`).

---

## Content Tips

- Write for an AI agent, not a human reader — be explicit, not narrative
- Lead with the rule, follow with the reason
- Include concrete examples and commands
- Keep it short — one concept per skill
- Avoid duplicating what is already in another skill; reference it instead
