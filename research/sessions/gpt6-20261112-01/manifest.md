# Research session manifest

- Session: gpt6-20261112-01
- Started: 2026-11-12
- Canonical repository: https://github.com/Armanasq/phd_application
- Baseline: main@c33758e2373e8726ed4d4ba58aaab736d83c43de
- Isolated branch: research/session-gpt6-20261112-01
- Worktree: unavailable in this execution environment; repository reads/writes use branch-scoped GitHub operations.
- Main policy: main is the sole integration target and remains read-only until a reviewed pull request is ready. A PR necessarily requires this isolated source branch and main as base.
- No direct commits to main; no force-push, reset, destructive checkout, or edits to another session's files.

## Coordination audit

Published branch inspection found concurrent sessions after the initial baseline:

| Branch | Published scope | Overlap / handling |
|---|---|---|
| research/repository-audit-20261112-0001-7f3c | simitii reading list; siddu Graduate-Admissions | Claims both initially screened-in repositories; do not duplicate or modify its artifacts |
| research/repository-audit-20261112-0031z-gpt6-a | simitii; siddu; zhoujasper PhD Atlas; zxcgzx tracker | Duplicate claims on first two; separate claims on PhD Atlas and tracker |
| research/repository-audit-gpt6-20261111-2031z | simitii; siddu; fsuitoal; BlueSky; PhD_Fit; DataBizex; Akshitha | Duplicate claims on first two; avoid all assigned repositories, including Akshitha |
| research/repository-audit-20261112-2cabbe82 | branch at baseline commit; no published artifacts | Scope unknown; do not assume no private work |

Unpublished/private work in other conversations remains unobservable. Published branch claims are treated as active ownership until reconciled by their owners.

## Scope correction

- Withdrawn from active scope due overlapping claims: simitii/CS-Grad-School-Applications-Reading-List; siddu1998/Graduate-Admissions; Akshitha-03/Automating_PhD_Group4.
- Existing preliminary reconnaissance for those repositories remains in the session's initial-investigations.md as historical work, but will not be submitted as a competing canonical review.
- Current independent scope: aditirajnish/scholarship_web_scraper; AlanWang610/academic-cv-scraper; AliAIOps/Putting-in-for-a-PhD-and-moving-abroad; alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad; alistvt/Putting-in-for-a-PhD-and-moving-abroad.
- The three Farsi repositories are derivative forks of Fatemeh-J/Putting-in-for-a-PhD-and-moving-abroad. Compare unique blobs only; do not count them as independent applicant experiences.
- Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad is byte-identical at the tree/blob level to the Fatemeh-J upstream and already has a preliminary review in the canonical corpus.

## Current repository investigation status

| Repository | Status |
|---|---|
| aditirajnish/scholarship_web_scraper | Preliminary source review completed; MIT license; historical Schulich-only scraper; runtime not executed |
| AlanWang610/academic-cv-scraper | Preliminary source review completed; archived MIT project; CV discovery, extraction and author-name resolution inspected statically; runtime not executed |
| AliAIOps/Putting-in-for-a-PhD-and-moving-abroad | Fork-difference review in progress; unique content inspected; source lineage established |
| alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad | Fork-difference review in progress; unique content inspected |
| alistvt/Putting-in-for-a-PhD-and-moving-abroad | Fork comparison in progress; README-only content delta relative to upstream |

## Integration policy

- All new findings stay under research/sessions/gpt6-20261112-01/ on this branch.
- Canonical inventory, generated indexes, global status, shared schemas, other session manifests and issues remain untouched until coordinated integration.
- A pull request will target main. Before creating it, fetch the latest main, compare the complete diff, verify that no other session has already integrated equivalent findings, run relevant repository integrity checks, and resolve any conflicts on this branch.
- Do not merge until the PR diff has been reviewed, all conflicts are resolved, and available CI checks pass. Use a non-force update; preserve upstream and other sessions' commits.
- If a conflict involves semantic disagreement or overlapping findings, reconcile source evidence; do not choose a side mechanically.

## Evidence and safety

- Pin upstream repository commit/tree/blob SHAs.
- Record exact inspected paths, metadata, issues/PRs, source history, license, security/privacy risks, limitations and uninspected scope.
- Distinguish verified source facts, interpretation, recommendations and unknowns.
- No untrusted code or crawlers are executed with credentials; no live Firebase/database access.
- Do not reproduce personal CVs, recommendation letters, passport/immigration details, or other sensitive applicant material.
- No third-party runtime validation is claimed unless performed and recorded.

## Outstanding

- Complete the unique fork-delta audit and classify duplicate forks accurately.
- Continue through the remaining untriaged candidate inventory in disjoint batches.
- Inspect current published branches before each new assignment.
- Produce a session-specific cross-repository synthesis.
- Prepare and validate a PR into main; do not claim a merge until GitHub confirms it.