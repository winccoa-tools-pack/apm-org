---
name: git-flow
description: Navigate the Git Flow branching workflow correctly
---

# Git Flow

Navigate the Git Flow branching workflow correctly.

## Branch Types

| Branch | Source | Target | Created By |
|--------|--------|--------|------------|
| `feature/*` | `develop` | `develop` | Manual |
| `bugfix/*` | `develop` | `develop` | Manual |
| `release/v*` | `develop` | `main` | GitHub Actions |
| `hotfix/v*` | `main` | `main` | GitHub Actions |

## Quick Reference

### Feature
```bash
git checkout develop && git pull
git checkout -b feature/my-feature
# work...
# PR → develop
```

### Bugfix
```bash
git checkout develop && git pull
git checkout -b bugfix/fix-issue
# work...
# PR → develop
```

### Release (via GitHub Actions)

**Do NOT create release branches manually.**

Use the workflow: `Actions` → `Create Release Branch + PR`

1. Go to repository → Actions → "Create Release Branch + PR"
2. Click "Run workflow"
3. Select:
   - **kind**: `release`
   - **version**: SemVer (e.g. `1.2.0`)
   - **base_branch**: `develop`
   - **target_branch**: `main`
4. Workflow automatically:
   - Creates `release/v1.2.0` branch
   - Bumps package version
   - Updates CHANGELOG
   - Creates pre-release (release candidate for testing)
   - Tags the repository
   - Creates PR to `main`
5. You may push additional CHANGELOG edits to the release branch
6. After PR merge: upmerge to `develop` is created automatically

**Note:** Release branches are protected and cannot be deleted.

### Hotfix (via GitHub Actions)

**Do NOT create hotfix branches manually.**

Use the workflow: `Actions` → `Create Release Branch + PR`

1. Go to repository → Actions → "Create Release Branch + PR"
2. Click "Run workflow"
3. Select:
   - **kind**: `hotfix`
   - **version**: SemVer (e.g. `1.2.1`)
   - **base_branch**: `main` (auto-adjusted for hotfix)
   - **target_branch**: `main`
4. Workflow automatically:
   - Creates `hotfix/v1.2.1` branch
   - Bumps package version
   - Updates CHANGELOG
   - Creates pre-release (release candidate for testing)
   - Tags the repository
   - Creates PR to `main`
5. You may push additional CHANGELOG edits to the hotfix branch
6. After PR merge: upmerge to `develop` is created automatically

**Note:** Hotfix branches are protected and cannot be deleted.

## Merge Strategies

| PR Type | Merge Strategy | Reason |
|---------|---------------|--------|
| Feature/Bugfix → develop | **Squash** | Clean history, single commit per feature |
| Release/Hotfix → main | **Merge commit** | Preserve history, avoid upmerge conflicts |
| Upmerge (main → develop) | **Merge commit** | Preserve history, avoid merge conflicts |

### Upmerge PRs

After release/hotfix merges to `main`, an action automatically creates a PR to upmerge changes back to `develop`. This PR contains:
- `package.json` (version bump)
- `package-lock.json` (for npm/vscode projects)
- `CHANGELOG.md` updates

**Important:** Always use **merge commit** for upmerge PRs, never squash. Squashing breaks history and causes merge conflicts in future releases.

## Rules

1. **Feature/Bugfix**: Branch from `develop`, merge to `develop` (manual, **squash**)
2. **Release/Hotfix**: Create via GitHub Actions workflow (automated, **merge commit**)
3. **Upmerge PRs**: Auto-created after release/hotfix, use **merge commit**
4. Release/Hotfix branches are protected (cannot be deleted)
5. Use conventional commit messages

## Branch Naming

### Manual branches (feature/bugfix)
```
<type>/<short-description>
```
- Lowercase, use hyphens
- Examples: `feature/add-export`, `bugfix/fix-config-parsing`
- Optional: include issue number `feature/123-add-export`

### Automated branches (release/hotfix)
```
<type>/v<semver>
```
- Created by workflow, always includes version
- Examples: `release/v1.2.0`, `hotfix/v1.2.1`

## Contributing via Forks

External contributors can use forks to submit PRs.

### Fork Workflow

1. Fork the repository
2. Create branch from your fork's `develop`
3. Make changes following conventional commits
4. Create PR: `fork:develop` → `upstream:develop`

### Fork Rules

| Allowed | Not Allowed |
|---------|-------------|
| `fork:develop` → `develop` | `fork:main` → `main` |
| `fork:feature/*` → `develop` | Any PR to `main` from fork |
| `fork:bugfix/*` → `develop` | |

**Important:** 
- PRs from forks must always target `develop`, never `main`
- Only release/hotfix workflows (run by maintainers) can merge to `main`
- Fork PRs use **squash** merge
