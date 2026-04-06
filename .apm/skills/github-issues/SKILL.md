---
name: github-issues
description: Where to create issues, how to organize them, and how to transfer misplaced ones
---

# GitHub Issues

Follow these rules to keep the issue backlog clean and navigable across the organization.

## Where to Create Issues

| Issue type | Repository |
|-----------|-----------|
| Org-wide vision, epic, cross-repo initiative | `winccoa-tools-pack/.github` |
| APM lockfile automation, label rollout, org DevOps | `winccoa-tools-pack/apm-org` |
| VS Code extension skills, CI publish workflow | `winccoa-tools-pack/apm-vscode-extension` |
| npm package skills, exports conventions | `winccoa-tools-pack/apm-npm-package` |
| Bug or feature in a specific tool | That tool's own repository |

**Rule:** `.github` issues are for **vision and cross-repo planning only**. Implementation sub-issues always live in the repository that will do the work.

## Transferring a Misplaced Issue

```bash
gh issue transfer <issue-number> <target-owner>/<target-repo> --repo <source-owner>/<source-repo>
```

Example — move issue #58 from `.github` to `apm-vscode-extension`:

```bash
gh issue transfer 58 winccoa-tools-pack/apm-vscode-extension --repo winccoa-tools-pack/.github
```

The issue gets a new number in the target repo. GitHub automatically redirects the old URL.

## Epics and Sub-issues

- Create the epic in `.github` with a checklist linking sub-issue numbers
- Create each sub-issue directly in the implementation repo
- Reference sub-issues in the epic body as `owner/repo#number` (cross-repo) or `#number` (same repo)

Example epic checklist:

```markdown
- [ ] winccoa-tools-pack/apm-vscode-extension#2 — publishing skill
- [ ] winccoa-tools-pack/apm-npm-package#2 — dev-setup skill
- [ ] winccoa-tools-pack/apm-org#2 — auto-update lockfiles
```

## Issue Labeling

Use org-wide labels. See the `labels` skill for the full list and rollout workflow.

Key labels for APM/skills work:
- `enhancement` — new skill or feature
- `documentation` — docs-only change
- `area/build` — CI/CD workflow changes
