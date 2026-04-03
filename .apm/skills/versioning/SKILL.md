---
name: versioning
description: Decide the correct SemVer version bump for the next release
---

# Versioning

Decide the correct [Semantic Versioning](https://semver.org/) bump when preparing a release.

## Version Bump Rules

| Change in this release | Bump | Example |
|------------------------|------|---------|
| Any `BREAKING CHANGE` footer or `!` commit | **MAJOR** | `1.2.3` → `2.0.0` |
| At least one `feat` commit | **MINOR** | `1.2.3` → `1.3.0` |
| Only `fix`, `perf`, `revert` commits | **PATCH** | `1.2.3` → `1.2.1` |
| Only `docs`, `chore`, `ci`, `build`, `style`, `refactor`, `test` | **PATCH** | `1.2.3` → `1.2.1` |

> Rule precedence: MAJOR > MINOR > PATCH. A single breaking change overrides everything else.

## How to Apply

Version bumps are applied **automatically** by the `Create Release Branch + PR` GitHub Actions workflow.  
You only need to decide the version and enter it when triggering the workflow.

**Steps:**

1. Review commits on `develop` since the last release tag
2. Apply the table above to determine the bump
3. Run workflow: `Actions` → `Create Release Branch + PR`
4. Enter the full SemVer string (e.g. `1.3.0`) — no `v` prefix in the input field

The workflow will:
- Bump `version` in `package.json`
- Create `CHANGELOG.md` section header
- Create the release branch and PR

## Pre-release Versions

Pre-release versions (`1.3.0-alpha.1`) are created automatically by the pre-release workflow for PRs to `main`. Do not set pre-release suffixes manually.

## Initial Development

During initial development (before `1.0.0`), breaking changes may bump MINOR instead of MAJOR. Once `1.0.0` is tagged, follow the rules strictly.
