# apm-org

Organization-wide APM (Agent Package Manager) configuration for winccoa-tools-pack.

## Overview

This package contains AI agent skills, prompts, and instructions that are **shared across ALL repositories** in the organization.

## Usage

Add to your repository's `apm.yml`:

```yaml
dependencies:
  apm:
    - winccoa-tools-pack/apm-org
```

Then run:

```bash
apm install
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
