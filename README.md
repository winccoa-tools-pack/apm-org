# apm-org

Organization-wide APM (Agent Package Manager) configuration for winccoa-tools-pack.

## Overview

This package contains AI agent skills, prompts, and instructions that are **shared across ALL repositories** in the organization.

## Setup

### 1. Install APM (once per machine)

**Windows (PowerShell):**
```powershell
irm https://aka.ms/apm-windows | iex
```

**macOS / Linux:**
```bash
curl -sSL https://aka.ms/apm-unix | sh
```

> For alternative install methods (Homebrew, Scoop, pip) see the official guide:  
> https://microsoft.github.io/apm/getting-started/quick-start/

### 2. After cloning any repository

```bash
apm install
```

This syncs skills, instructions, and prompts from `apm.yml` into `.github/`, `.claude/`, `.cursor/` — the native directories your AI tools read automatically.

### 3. Keeping up to date

Re-run `apm install` when `apm.yml` or `apm.lock.yaml` changes (e.g. after `git pull`).

## Usage in repositories

Add to your `apm.yml`:

```yaml
dependencies:
  apm:
    - winccoa-tools-pack/apm-org
```

## Contents

- `.apm/skills/` — Reusable AI capabilities
- `.apm/instructions/` — Context for AI agents  
- `.apm/prompts/` — Prompt templates

## Skills

| Skill | Description |
|-------|-------------|
| [conventional-commits](.apm/skills/conventional-commits/SKILL.md) | Commit message format |
| [git-flow](.apm/skills/git-flow/SKILL.md) | Git Flow branching workflow |
| [create-pr](.apm/skills/create-pr/SKILL.md) | How to create a correct Pull Request |
| [versioning](.apm/skills/versioning/SKILL.md) | Decide the correct SemVer version bump |
| [changelog](.apm/skills/changelog/SKILL.md) | Write and maintain CHANGELOG.md entries |
