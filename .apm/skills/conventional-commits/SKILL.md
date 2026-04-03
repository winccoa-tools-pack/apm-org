---
name: conventional-commits
description: Generate and validate commit messages following Conventional Commits
---

# Conventional Commits

Generate and validate commit messages following [Conventional Commits](https://www.conventionalcommits.org/).

## Format

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

## Types

| Type | Description | Version Bump |
|------|-------------|--------------|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `docs` | Documentation only | - |
| `style` | Formatting, no code change | - |
| `refactor` | Code change, no feature/fix | - |
| `perf` | Performance improvement | PATCH |
| `test` | Adding/updating tests | - |
| `build` | Build system changes | - |
| `ci` | CI configuration | - |
| `chore` | Maintenance | - |
| `revert` | Revert previous commit | PATCH |

## Rules

1. Type is **required**, lowercase
2. Scope is optional, in parentheses
3. Description is **required**, lowercase start, no period
4. Header max **72 characters**
5. Breaking changes: add `!` after type or `BREAKING CHANGE:` footer

## Examples

**Simple:**
```
feat: add dark mode support
```

**With scope:**
```
fix(parser): handle empty config files
```

**Breaking change:**
```
feat(api)!: change return type to Promise

BREAKING CHANGE: getProject() now returns Promise<Project>
```

**With body:**
```
fix(config): resolve path handling on Windows

Paths with backslashes were not normalized correctly
when reading pvssInst.conf on Windows systems.

Fixes #123
```
