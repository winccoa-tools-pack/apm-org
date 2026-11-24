---
name: labels
description: Apply and roll out the correct labels to a repository
---

# Labels

Each repository defines its labels in `.github/labels.yml` and syncs them with
`.github/workflows/sync-labels.yml`
([crazy-max/ghaction-github-labeler](https://github.com/crazy-max/ghaction-github-labeler)).
**Never create ad-hoc labels in the GitHub UI** — edit `labels.yml` instead.

The org-wide label list and its descriptions are in
[`winccoa-tools-pack/.github` → `labels/labels.yml`](https://github.com/winccoa-tools-pack/.github/blob/main/labels/labels.yml)
and [`docs/LABELS.md`](https://github.com/winccoa-tools-pack/.github/blob/main/docs/LABELS.md).
The per-repo `.github/labels.yml` from the template is the file that is actually applied.

> The old fan-out workflows (`Fan-out labels to repositories`, `Run single-target label sync`)
> and the secret `ORG_LABELS_PAT` no longer exist.

## How it works

- Repos created from `template-npm-shared-library` already contain both files.
- The workflow runs on a push to `develop` that changes `.github/labels.yml`, every Monday 06:00 UTC, and manually.
- It uses `GITHUB_TOKEN` (`issues: write`), no PAT is needed.
- Automatic runs never delete labels (`skip-delete`). Only a manual run with `skip_delete: false` removes labels that are not in `labels.yml`.

## New repository

After "Use this template", run **Actions → Sync labels → Run workflow** once.
Start with `dry_run: true` to preview, then run again with `dry_run: false`.

```bash
gh workflow run sync-labels.yml --repo winccoa-tools-pack/<repo> -f dry_run=false
gh label list --repo winccoa-tools-pack/<repo> --limit 100
```

## Add or change a label

1. Edit `.github/labels.yml` (`name`, `color` without `#`, `description` up to 100 characters).
2. Merge to `develop`. The workflow applies the change.

## Labels used by automation

| Label | Used by |
|-------|---------|
| `breaking-change` | Release planner: major bump |
| `enhancement` | Release planner: at least minor bump |
| `release`, `chore` | Release PRs |
| `merge-in-3-days-without-review`, `merge-in-2-days-without-review`, `merge-in-1-day-without-review`, `merged-without-review` | `auto-approve-owner-prs.yml` countdown |
| `dependencies`, `size/small`, `area/build`, `dependabot/patch` | `dependabot.yml` |
| `source`, `cli`, `ci`, `docs`, `tests`, `config` | `labeler.yml` (actions/labeler) |

Keep these in `labels.yml`, with names identical to the ones in `dependabot.yml` and `labeler.yml`.
Create the countdown labels before the first owner PR that should use the countdown (the sync workflow does this).

## Existing repository or other template

Copy `.github/labels.yml` and `.github/workflows/sync-labels.yml` from
[template-npm-shared-library](https://github.com/winccoa-tools-pack/template-npm-shared-library)
and run the workflow once.
