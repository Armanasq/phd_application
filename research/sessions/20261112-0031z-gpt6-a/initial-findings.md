# Initial source findings — 20261112-0031z-gpt6-a

**Date:** 2026-11-12  
**State at capture:** INITIAL_SCOUTING; superseded by the two deep source reports and the previously merged historical-resource investigations.  
**Isolation:** session-specific branch and directory only.

> This document is retained as an initial investigation log, not the authoritative final review status. The two mature implementation reviews are [`zhoujasper-phd-atlas.md`](zhoujasper-phd-atlas.md) and [`zxcgzx-phd-application-tracker.md`](zxcgzx-phd-application-tracker.md). The reading-list and SOP-corpus reviews were already merged through [PR #6](https://github.com/Armanasq/phd_application/pull/6); redundant drafts from this session were removed.

## 1. `simitii/CS-Grad-School-Applications-Reading-List`

- Upstream default branch: `master`.
- Commit SHA: `189be53b9299ded95d7a6517b6d5760d4286df70`; Git tree SHA: `37244a3594d1cb04b5466655106a432bf4e2de08`; one tree entry.
- README blob: `58d7aef8ea0692802fb83e42444e61a27624bdbe`.
- The only tracked file is a curated 2019-era CS graduate admissions reading list.
- Topics include general application strategy, admissions reflections, statement-of-purpose writing, historical successful statements, CS rankings, and questions to ask prospective advisers.
- The listed references span approximately 2007–2020; this is a secondary-source bibliography, not a maintained vacancy or admissions-policy database.
- Research value: source discovery and historical triangulation for research-fit narrative, SOP structure, advisor evaluation, and applicant decision-making.
- Risks: temporal obsolescence, link rot, US/CS selection bias, survivorship bias in successful-essay examples, and unclear representativeness.
- Not inspected yet: individual linked sources, source freshness, upstream commit history, issues/PRs, license, and claim-level verification.
- Status: PRELIMINARY_SOURCE_INSPECTION.

## 2. `siddu1998/Graduate-Admissions`

- Upstream default branch: `main`.
- Commit SHA: `71d1750175b1cca2bca78fe738765b0c42c58c0a`; Git tree SHA: `afbf0d99adafecb942326c5f3f646e8bd34694f9`; 40 entries.
- README blob: `38f25942a1fa6fd1203e7caee0b0dbb4667df95e`.
- Contains university-specific statement-of-purpose PDFs for Brown, CMU, Columbia, Cornell, EPFL, Imperial, MIT, Oxford, Purdue, UBC, UCSC, UIUC, UMCP, UNC-Chapel Hill, and USC.
- Includes multiple MS/PhD examples and application-cycle references to 2020 and 2021.
- Also contains recommendation-letter documents and supporting media links.
- Research value: longitudinal comparison of narrative adaptation across institutions and degree levels; can support analysis of research-fit specificity, narrative continuity, and program-specific tailoring.
- Risks: historic admissions requirements, survivorship bias, no verified outcomes in README, personal-data exposure in recommendation letters and applicant documents, and possible copyright/privacy constraints.
- No recommendation-letter content is reproduced in this public report.
- Not inspected yet: PDF contents, provenance/author permissions, commits, issues/PRs, license, and external resource validity.
- Status: PRELIMINARY_SOURCE_INSPECTION.

## 3. `zhoujasper/phd-atlas`

- Upstream default branch: `main`.
- Commit SHA: `8f4318eda901020b61d91abfc82411943200c70f`; Git tree SHA: `47be03f3fb1ca14dfc95dc2cc6a252ac964c9f96`; 1,961 recursive entries, not truncated.
- README blob: `2ca9cac2683264cfdacb0f2ea5bc1f5ed880c49f`.
- README describes a self-hosted, personal-only PhD application workspace. It explicitly says team collaboration is not part of the public distribution.
- Declared stack: React 19, TypeScript 6, Vite 8, Express 5, Zod, SQLite by default, optional MySQL/MariaDB, PostgreSQL and SQL Server, Vitest, Testing Library, and Playwright.
- Product domains documented: application pipeline, program discovery, supervisor dossier, document checklist/versioning, funding, tasks/deadlines, correspondence, mail integration, profile library, share links, exports, calendar, backups, admin, and desktop/PWA operation.
- Tree shows dedicated desktop Electron code, deployment artifacts, Codex plugin/skill, Claude MCP package, localization, CI, release pipelines, test suites, benchmark tools, and large CLI implementation.
- README documents user-approved device authorization, bounded scopes, expiry, revocation, account permissions, and credential storage outside downloadable plugin bundles.
- Research value: a broad implementation comparator for local-first admissions case management, typed backend contracts, multi-database persistence, auditable workflows, exports/backups, and scoped agent integration.
- Risks/questions requiring source validation: whether README feature claims are implemented and tested at the pinned revision; authorization enforcement at every route; database adapter parity; import/export integrity; offline conflict handling; release supply-chain security; and scope/version compatibility.
- Not inspected yet: detailed backend/domain modules, schema/migrations, auth middleware, API routes, integration CLI, desktop boundary, CI/test results, commit history, issues/PRs, and execution.
- Status: DEEP_REVIEW_IN_PROGRESS.

## 4. `zxcgzx/phd-application-tracker`

- Upstream default branch: `main`.
- Commit SHA: `8826e96755f4d76854e00725226ff92fed59af18`; Git tree SHA: `51db6bdf919b700bc48bad40dbba61b32d36371e`; 84 recursive entries.
- README blob: `6261924ff1c515d0ca19c6c3c300b9f7301fc961`.
- Architecture includes configurable university scrapers, a two-level crawler, Supabase synchronization, PostgreSQL schema/RLS, frontend professor management, import, filters, statistics, timelines, and scheduled/manual GitHub Actions.
- Inspected `crawler/scrapers/base_scraper.py`: request sessions, timeout/retry/delay, apparent-encoding detection, BeautifulSoup/lxml parsing, keyword/sibling extraction, CSS and regex extraction, and research-area normalization/filtering.
- Inspected `database/schema.sql` and `database/fix_rls_policies.sql`: multiple application/professor/follow-up tables and policies granting broad read/write access with `USING (true)` and `WITH CHECK (true)`.
- The existing project risk register identifies credential-like service-role fallback material in `crawler/database/supabase_sync.py`. This audit does not reproduce secrets or attempt authentication.
- Research value: configurable institution-specific extraction, supervisor entity management, crawling telemetry, and explicit synchronization diagnosis.
- Risks: credential handling, permissive multi-user RLS, selector brittleness, stale source data, parser quality, retry/rate-limit behavior, duplicate professor resolution, and frontend/backend consistency.
- Safety: static inspection only for credential-bearing integration; no live DB access or secret use.
- Not inspected yet: full sync implementation, config, two-level scraper, frontend import/state management, all SQL scripts, tests, commit history, issues/PRs, and runtime.
- Status: DEEP_REVIEW_IN_PROGRESS.

## Cross-repository synthesis — preliminary

1. The two reading-list/SOP repositories are knowledge artifacts, not operational source-of-truth systems. Their claims need a provenance layer, date, and official-source recheck before being used for current admissions decisions.
2. PhD Atlas and the tracker represent two different product scopes: broad personal application lifecycle management versus university-supervisor discovery and data ingestion.
3. A mature integrated design should separate discovery records from verified opportunity records, source evidence from extracted claims, and application readiness from actual submission/offer events.
4. Supervisor discovery should never imply current recruiting or funding. Scraped professor interests are not evidence of open funded positions.
5. The tracker’s broad RLS policies and credential fallback are direct counterexamples for secure applicant-private data design. Do not copy these patterns.
6. The PhD Atlas authorization model is promising at the documented level but must be checked against actual route-level enforcement and tests before adopting it.

## Evidence classification

- Verified: repository metadata, tree sizes/SHAs, listed paths, README text, and contents of the explicitly inspected source files at the pinned upstream revisions.
- Interpretation: applicability and architectural comparisons above.
- Unknown: runtime behavior, test pass status, production security, current upstream activity, external admissions validity, and completeness of source inspection.

This historical first-pass note does not certify completeness. Subsequent deep reviews for PhD Atlas and the supervisor tracker are separately documented; the historical-reading-list review and PDF-corpus inventory are already on `main` via PR #6.
