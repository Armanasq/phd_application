# Repository audit session — 20261112-gpt6-7b61

- Session identifier: `20261112-gpt6-7b61`
- Target: `Armanasq/phd_application` / `main`
- Base `main` commit: `27cf5b9568dd528d468a970b9053d87ceb270248`
- Isolated remote branch: `research/repository-audit-20261112-gpt6-7b61`
- Workspace: branch-scoped GitHub API; no shared working directory or local worktree is touched
- Progress: IN_PROGRESS
- Intended integration: reviewable PR into `main`, guarded against concurrent updates

## Published coordination check

At assignment, `main` contained 404 discovery candidates, 88 canonical review records (18 deep static, 70 preliminary), 294 untriaged and 22 screened exclusions. PR #6 and PR #7 were merged; no PR was open. Active branch manifests were inspected for `20261112-0031z-gpt6-a`, `20261112-nima-go2phd-8c24`, `audit-20261112-r47c6f`, `gpt6-20261111-2031z`, `gpt6-20261112-01` and `2cabbe82`. No published overlapping claim for the five repository identities below was found. Other sessions' unpublished state cannot be seen.

## Independent assigned repository identities

| Canonical repository ID | Starting disposition | Source scope |
| --- | --- | --- |
| `Lukas-Vasionis/PhD_Positions` | UNTRIAGED | University-specific Swiss/Norwegian/TUM PhD vacancy adapters, processing, SQL data model, CLI/UI, error handling and provenance |
| `Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor` | UNTRIAGED | Scholarship monitor skill, core runtime, evidence/eligibility verification, dedup, state, tests and scheduled workflow |
| `mdsazzathossain1/GradResearch_AI` | UNTRIAGED | Professor discovery, research matching, email generation, execution/security/privacy; do not display or use committed credentials |
| `dhcoders/JobsACUK-WebScraper` | UNTRIAGED | Bounded source-level review of academic vacancy scraper and history |
| `mgoar/mtt-phd-filter` | UNTRIAGED | Verify keyword false-positive/irrelevance; do not confuse PHD multi-target filtering with doctoral degrees |

## Ownership and modification boundaries

- Only create files under `research/sessions/20261112-gpt6-7b61/` on this branch.
- Do not update global candidate/review registers, schemas, generated indexes, issue ownership, another session's files or branches.
- Capture exact upstream commit SHAs, inspected files, evidence, implementation-versus-claim differences, tests/run limits, verification gaps and transferability.
- Use separate reports and a session-local proposed inventory delta rather than editing shared records.
- Before merge, re-fetch `main`, branch/PR ownership state, inspect every changed file, confirm source-specific evidence, and check available CI. Reject accidental overlap or conflicts. Do not force-push or rewrite any branch.

## Verification constraints

Static source inspection via GitHub is not runtime validation. No third-party credentials, automated outreach, application submissions, personal applicant content or secret values will be processed or reproduced. Upstream executables are not run against production sources.
