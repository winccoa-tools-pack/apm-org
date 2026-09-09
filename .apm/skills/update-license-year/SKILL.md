---
name: update-license-year
description: Update copyright years and license headers across a repository
---

# Update License Year

This skill updates copyright years in source files and headers across a repository. It replaces single-year headers (e.g. `Copyright (c) 2025`) and end-years in ranges (e.g. `2018-2025`) with a target year.

## Usage

Run the helper script from the repository root (or specify `--root`). By default the script uses the current year as the target year.

```bash
python .apm/skills/update-license-year/update_license_year.py --root . --year 2026
```

## What it changes

- `Copyright (c) 20XX` → updates to the specified year.
- `Copyright 2018-20XX` → updates the end year to the specified year.
- Handles common variations (case-insensitive, © symbol).

## Dry run

Use `--dry-run` to preview changes without modifying files.

## Implementation

A small Python script is included at `.apm/skills/update-license-year/update_license_year.py`.
