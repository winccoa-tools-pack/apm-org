---
name: create-pr
description: Guide for creating well-structured Pull Requests
---

# Create Pull Request

Guide for creating well-structured Pull Requests.

## Before You Start

- Issue is approved and assigned
- Branch follows naming convention (see [git-flow](git-flow.md))
- All commits follow [conventional commits](conventional-commits.md)
- Tests pass locally

## PR Title

Use the same format as commit messages:

```
<type>(<scope>): <description>
```

Examples:
```
feat(parser): add support for nested configs
fix(ui): resolve panel flickering on resize
docs: update installation guide
```

## Target Branch

| Your branch | PR target | Merge strategy |
|-------------|-----------|---------------|
| `feature/*` | `develop` | Squash |
| `bugfix/*` | `develop` | Squash |
| `fork:develop` / `fork:feature/*` / `fork:bugfix/*` | `develop` | Squash |
| `release/v*` | `main` | Merge commit *(created by action)* |
| `hotfix/v*` | `main` | Merge commit *(created by action)* |
| Upmerge | `develop` | Merge commit *(created by action)* |

## PR Description

Each repository has two PR templates — GitHub will prompt you to choose:

- `.github/PULL_REQUEST_TEMPLATE/feature-bugfix.md` — for feature and bugfix PRs
- `.github/PULL_REQUEST_TEMPLATE/release.md` — for release and hotfix PRs (auto-selected by the action)

Fill out the chosen template completely before requesting review.

## Checklist Before Requesting Review

- [ ] Correct target branch
- [ ] CI checks pass
- [ ] No merge conflicts
- [ ] PR description filled out
- [ ] Linked to issue

## Review & Merge

- Address all review comments before merge
- Do not merge your own PR (unless explicitly allowed)
- Maintainer merges with correct strategy (squash or merge commit per table above)
