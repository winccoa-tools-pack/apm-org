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

- `instructions/` — Context for AI agents
- `skills/` — Reusable AI capabilities  
- `prompts/` — Prompt templates

## Structure

```
apm-org/
├── apm.yml
├── README.md
├── instructions/
├── skills/
└── prompts/
```
