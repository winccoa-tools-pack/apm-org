---
name: labels
description: Apply and roll out the correct org-wide labels to repositories
---

# Labels

All labels across the organization are defined in a single source of truth.  
**Never create ad-hoc labels directly in a repository** — use the rollout workflow instead.

## Source of Truth

[`winccoa-tools-pack/.github` → `labels/labels.yml`](https://github.com/winccoa-tools-pack/.github/blob/main/labels/labels.yml)

Full documentation: [`docs/LABELS.md`](https://github.com/winccoa-tools-pack/.github/blob/main/docs/LABELS.md)

## Available Labels

| Category | Examples |
|----------|---------|
| Priority | `priority/critical`, `priority/high`, `priority/medium`, `priority/low` |
| Type | `enhancement`, `bug`, `documentation`, `breaking-change`, `dependencies` |
| Component | `core`, `api`, `testing`, `quality`, `configuration`, `integration` |
| Status | `needs-triage`, `status/in-progress`, `status/review`, `status/blocked`, `status/ready` |
| Special | `good-first-issue`, `help-wanted`, `security`, `performance`, `area/build` |

## Roll Out Labels to Repositories

### All repos at once

1. Go to [`winccoa-tools-pack/.github`](https://github.com/winccoa-tools-pack/.github) → **Actions**
2. Run workflow **"Fan-out labels to repositories"**
3. Start with `dry-run: true` to preview — then re-run with `dry-run: false`
4. Use `strict: true` to also delete labels not in `labels.yml`

### Single repo

1. Run workflow **"Run single-target label sync"**
2. Set `target-repo` to `winccoa-tools-pack/<repo-name>`

### Add a new repo to the rollout

Edit [`repos.txt`](https://github.com/winccoa-tools-pack/.github/blob/main/repos.txt) in the `.github` repo — one `org/repo` per line.

## Add or Change a Label

1. Edit `labels/labels.yml` in `winccoa-tools-pack/.github`
2. Commit and push to `main`
3. Run the fan-out workflow to apply across all repos

## Quick Fix via CLI (one-off)

```bash
# Create a missing label in one repo
gh label create "priority/high" --color "eb6420" --description "Important for milestone success" --repo winccoa-tools-pack/<repo>

# Edit an existing label
gh label edit "needs-triage" --color "FBCA04" --repo winccoa-tools-pack/<repo>
```

> Quick fixes do not update `labels.yml`. Always follow up with a proper edit to keep the source of truth in sync.

## Required Secret

The rollout workflows require the org secret `ORG_LABELS_PAT` (scope: `repo`).
