Dependabot monitoring skill
===========================

Purpose
-------

Provide a lightweight skill to detect stalled or failing Dependabot pull requests (PRs), analyse their status (CI checks, merge conflicts, approvals), and propose corrective actions.

What it does
------------

- Scans one or more repositories for open PRs created by Dependabot (or labeled accordingly).
- For each PR, fetches mergeable state, review status, and check-run conclusions.
- Produces a report describing why a PR may be blocked and suggests likely fixes (e.g., rebase, add reviewers, update base branch, fix failing tests).

Files
-----

- `dependabot_scan.py` — Python script to query the GitHub API and produce a CSV/JSON report.
- `requirements.txt` — Python requirements for the script.

Usage
-----

1. Create a GitHub token with `repo` and `repo:status` scopes (or org-level read access for multiple repos). Export it as `GITHUB_TOKEN`.

2. Run the scanner for the current repository:

```powershell
python .apm/skills/dependabot-monitor/dependabot_scan.py --repo OWNER/REPO
```

3. To scan multiple repos, provide `--repos-file repos.txt` where each line is `OWNER/REPO`.

Notes
-----

- The script cannot run without a valid `GITHUB_TOKEN` in the environment.
- Running across many repositories may be rate-limited — consider using an org-level token or add caching.
- The scanner makes suggestions, not automatic fixes. Some fixes (e.g., merging major updates) require human review.

Next steps I can take
--------------------

- Open a PR adding this skill to the repo docs.
- Run the scanner against a list of repos you provide (you'll need to supply `GITHUB_TOKEN`).
- Add automation to open issues or notify maintainers when stalled PRs are detected.
