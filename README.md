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

- `skills/` — Reusable AI capabilities
- `instructions/` — Context for AI agents  
- `prompts/` — Prompt templates

## Skills

| Skill | Description |
|-------|-------------|
| [conventional-commits](skills/conventional-commits.md) | Commit message format |
| [git-flow](skills/git-flow.md) | Git Flow branching workflow |
| [create-pr](skills/create-pr.md) | How to create a correct Pull Request |
