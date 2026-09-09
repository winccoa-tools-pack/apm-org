"""Dependabot PR scanner

Scans repositories for open Dependabot PRs and reports status/possible fixes.

Usage:
  - set env var GITHUB_TOKEN
  - python dependabot_scan.py --repo owner/repo
  - python dependabot_scan.py --repos-file repos.txt

This is intentionally conservative: it only reads data and prints a report.
"""

import os
import sys
import argparse
import requests
import time
import csv
import json

# Minimal GitHub API helper
GITHUB_API = "https://api.github.com"

def gh_get(path, token, params=None):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    r = requests.get(GITHUB_API + path, headers=headers, params=params)
    if r.status_code == 401:
        raise SystemExit("Unauthorized: check GITHUB_TOKEN")
    if r.status_code >= 400:
        raise SystemExit(f"GitHub API error {r.status_code}: {r.text}")
    return r.json()

def list_dependabot_prs(owner_repo, token):
    owner, repo = owner_repo.split("/")
    prs = []
    page = 1
    while True:
        params = {"state": "open", "per_page": 100, "page": page}
        path = f"/repos/{owner}/{repo}/pulls"
        batch = gh_get(path, token, params=params)
        if not batch:
            break
        for pr in batch:
            author = pr.get("user", {}).get("login", "")
            labels = [l.get("name") for l in pr.get("labels", [])]
            if author.lower().startswith("dependabot") or any("dependabot" in (s or "") for s in labels):
                prs.append(pr)
        page += 1
        if len(batch) < 100:
            break
    return prs

def analyze_pr(pr, token):
    owner_repo = "/".join([pr["base"]["repo"]["owner"]["login"], pr["base"]["repo"]["name"]])
    number = pr["number"]
    owner, repo = owner_repo.split("/")

    # Mergeable state (may be null if not calculated)
    pr_detail = gh_get(f"/repos/{owner}/{repo}/pulls/{number}", token)
    mergeable = pr_detail.get("mergeable")
    mergeable_state = pr_detail.get("mergeable_state")

    # Reviews
    reviews = gh_get(f"/repos/{owner}/{repo}/pulls/{number}/reviews", token)
    approved = any(r.get("state") == "APPROVED" for r in reviews)

    # Check runs / statuses
    checks = gh_get(f"/repos/{owner}/{repo}/commits/{pr['head']['sha']}/check-runs", token)
    check_runs = checks.get("check_runs", [])
    failing_checks = [c for c in check_runs if c.get("conclusion") not in ("success", "neutral", "skipped", None)]

    # Combined status
    status = gh_get(f"/repos/{owner}/{repo}/commits/{pr['head']['sha']}/status", token)
    state = status.get("state")

    # Conflicts
    conflict = mergeable_state == "dirty" or (mergeable is False)

    issues = []
    suggestions = []
    if failing_checks:
        issues.append("failing_checks")
        suggestions.append("Investigate failing CI; re-run or fix tests in the dependency or fork.")
    if not approved and pr_detail.get("draft") is False and pr_detail.get("maintainer_can_modify"):
        issues.append("no_approval")
        suggestions.append("Request an approver or enable auto-approval for dependabot if policy allows.")
    if conflict:
        issues.append("merge_conflict")
        suggestions.append("Rebase or update branch to resolve conflicts; consider triggering auto-rebase.")
    if state == "pending":
        issues.append("checks_pending")
        suggestions.append("Wait or re-run checks; investigate flaky checks.")

    return {
        "repo": owner_repo,
        "number": number,
        "title": pr.get("title"),
        "url": pr.get("html_url"),
        "mergeable": mergeable,
        "mergeable_state": mergeable_state,
        "conflict": conflict,
        "status_state": state,
        "failing_checks_count": len(failing_checks),
        "issues": issues,
        "suggestions": suggestions,
    }

def run_scan(repos, token, out_json=None, out_csv=None):
    results = []
    for r in repos:
        print(f"Scanning {r}...")
        try:
            prs = list_dependabot_prs(r, token)
        except SystemExit as e:
            print(f"Error scanning {r}: {e}")
            continue
        for pr in prs:
            try:
                res = analyze_pr(pr, token)
            except SystemExit as e:
                print(f"Error analyzing PR {pr.get('html_url')}: {e}")
                continue
            results.append(res)
        # Respect rate limits lightly
        time.sleep(0.5)

    if out_json:
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
    if out_csv:
        fieldnames = ["repo", "number", "title", "url", "mergeable", "mergeable_state", "conflict", "status_state", "failing_checks_count", "issues", "suggestions"]
        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in results:
                row = {k: json.dumps(v) if isinstance(v, (list, dict)) else v for k, v in r.items()}
                writer.writerow(row)

    # Print a concise summary
    print("\nScan complete. Summary:")
    for r in results:
        issues = ",".join(r.get("issues", [])) or "ok"
        print(f"- {r['repo']}#{r['number']}: {issues} -> {r['url']}")

    return results

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--repo", help="Single repo in OWNER/REPO format")
    p.add_argument("--repos-file", help="Path to file with OWNER/REPO per line")
    p.add_argument("--out-json", help="Write full JSON report")
    p.add_argument("--out-csv", help="Write CSV report")
    return p.parse_args()

def main():
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Set GITHUB_TOKEN in environment with appropriate scopes (repo, repo:status)")
        sys.exit(1)

    repos = []
    if args.repo:
        repos = [args.repo]
    elif args.repos_file:
        with open(args.repos_file, "r", encoding="utf-8") as f:
            repos = [l.strip() for l in f if l.strip() and not l.strip().startswith("#")]
    else:
        print("Provide --repo or --repos-file")
        sys.exit(1)

    run_scan(repos, token, out_json=args.out_json, out_csv=args.out_csv)

if __name__ == "__main__":
    main()
