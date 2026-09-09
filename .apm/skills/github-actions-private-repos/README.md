GitHub Actions: Private repository limitations
===========================================

Summary
-------

Some GitHub Actions workflows and automation that rely on public repository visibility, GitHub Apps (marketplace apps), or organization-level automation may not run or will be restricted when the repository is private. The practical remedies are:

- Change the repository visibility to **public** so the automation can run as intended, or
- Accept that the automation will not run in a private repo and perform the affected steps manually.

Identified affected workflows
-----------------------------

These workflows have been identified as likely not working in a private GitHub repository (investigate each if you plan to keep the repo private):

- `.github/workflows/apply-settings-and-rulesets.yml`
- `.github/workflows/auto-approve-owner-prs.yml`
- `.github/workflows/dependabot-auto-merge.yml`

Notes & guidance
----------------

- There may be additional workflows or actions affected beyond the three listed above — audit workflows that rely on third-party GitHub Apps, marketplace actions, or org-level automation.
- Check repository settings under *Settings → Actions* and *Settings → Secrets and variables* to ensure required permissions and secrets exist.
- If you need automation but cannot make the repo public, consider implementing manual scripts or scheduled tasks outside GitHub Actions (CI runner, local scripts, or a small server) to perform the same operations.

Next steps
----------

- Decide whether to change repository visibility to public or accept manual processes.
- If keeping private, create a short checklist for manual steps that replace the disabled workflows.
- Optionally, run a scan of `.github/workflows/*.yml` to find other workflows referencing marketplace apps or org-level automation.

Contact
-------

If you want, I can:

- Open a PR adding this note into the repo documentation.
- Scan existing workflows to produce a fuller list of likely-affected workflows.
