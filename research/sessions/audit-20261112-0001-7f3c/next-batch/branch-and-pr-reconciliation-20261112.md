# Branch and PR reconciliation — 2026-11-12

**Canonical destination:** main, https://github.com/Armanasq/phd_application. **Coordination:** multiple sessions write concurrently; preserve all work.

## Verified PR state
At inspection, GitHub returned 21 total PRs and **zero open**. PR #12 and #14 were closed without direct merges; their source reviews or exclusions are already present on main:

- #12: dinglhmds/Search-PhD-Positions was reviewed, and heyulanKiara/django-phd-scholarship was excluded.
- #14: fsuitoal-code/phd-application-command-center was reviewed.

Reopening or merging those stale PR diffs would duplicate records and potentially overwrite newer canonical data.

## Branch-by-content comparison
All then-listed research and integration branches were inspected using GitHub compare_commits, and relevant branch SHA trees were compared file-by-file with main. Many branches are ahead in Git ancestry but contain no new canonical evidence. Differences predominantly represent older versions of research CSVs, generated indexes, README/status notes and manifests.

Branch-only documents identified:
- research/repository-audit-20261112-0001-7f3c: two session notes on siddu1998/Graduate-Admissions and simitii/CS-Grad-School-Applications-Reading-List. Canonical reports already exist; a branch-only report has inconsistent depth/tree claims. Do not overwrite canonical evidence.
- research/repository-audit-20261112-gpt6-7b61 and research/repository-audit-20261112-k5e7b: old IN_PROGRESS session manifests. Preserve history without importing stale status.
- research/session-gpt6-20261112-01: initial-investigations and old manifest; canonical investigation records were already published.

No destructive branch-level merge was justified by these content comparisons. This does not claim that every historic commit is an ancestor of main or that unsaved concurrent work is visible.

## Conflict and validation policy
1. Pull the latest main file SHA immediately before each write; update with that expected SHA.
2. Reconcile each candidate status against live data/github_discovery_candidates.csv and data/repositories.csv; do not double-count candidates or overwrite another agent's notes.
3. Rebuild research/repositories/index.md from the live registry after any review addition.
4. Validate the exact final commit in GitHub Actions. Historical green checks do not prove newer commits are valid.
5. Never force-push, delete branches, or overwrite newer main content merely to obtain a merge badge.

All commits for this session are direct, incremental main updates. Branch ownership and outstanding research tasks remain with the relevant sessions.
