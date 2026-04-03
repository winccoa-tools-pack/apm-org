---
name: changelog
description: Write and maintain CHANGELOG.md entries correctly before a release
---

# Changelog

Write and maintain `CHANGELOG.md` following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## When to Update

The `Create Release Branch + PR` workflow creates the version section header in `CHANGELOG.md` automatically.  
**You are responsible for filling in the content** on the release/hotfix branch before the PR is merged.

```
## [1.3.0] - 2026-04-04   ← created by workflow

### Added
### Changed
### Fixed
```

Push your edits directly to the release branch:

```bash
git checkout release/v1.3.0
# edit CHANGELOG.md
git add CHANGELOG.md
git commit -m "docs: update changelog for v1.3.0"
git push
```

## Format

```markdown
## [<version>] - <YYYY-MM-DD>

### Added
- Short description of new feature (#PR)

### Changed
- Short description of change (#PR)

### Fixed
- Short description of fix (#PR)

### Removed
- Short description of removal (#PR)
```

## Section Rules

| Section | Use for |
|---------|---------|
| `Added` | New features (`feat`) |
| `Changed` | Changes to existing behavior (`refactor`, `perf`, `deps`) |
| `Fixed` | Bug fixes (`fix`, `revert`) |
| `Removed` | Deleted features |
| `Deprecated` | Soon-to-be-removed features |
| `Security` | Vulnerability fixes |

Only include sections that have entries. Omit the rest.

## Entry Style

- Start with a capital letter
- No trailing period
- Reference the PR number in parentheses: `(#42)`
- One entry per logical change — do not paste raw commit messages
- Group dependency bumps: `deps: bump eslint and related packages (#78, #79, #80)`

## Example

```markdown
## [1.3.0] - 2026-04-04

### Added
- Support dark mode via `winccoa.theme` setting (#101)

### Changed
- deps: bump eslint from 8.x to 9.x (#98, #99)

### Fixed
- Resolve path handling on Windows with backslash separators (#103)
```

## What NOT to Do

- Do not leave the section headers empty before merging
- Do not copy raw commit messages (e.g. `feat: add dark mode`) — rewrite for end-users
- Do not add a `[Unreleased]` section (the workflow manages this)
