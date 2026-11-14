# Integration proposal — session gpt6-20261112-01

Target: `main`  
Source branch: `research/session-gpt6-20261112-01-integration`  
Base snapshot: `ccbd518c8e036d4dca8de881e25be8de97f22648`

## Scope

This PR proposes only additive session-owned research artifacts. It does not edit `data/github_discovery_candidates.csv`, `data/repositories.csv`, generated indexes, global status, schemas or other session directories. Canonical inventory changes are deferred to a separately coordinated integration after all parallel ownership claims are reconciled.

## Proposed dispositions

| Repository | Proposed disposition | Rationale |
|---|---|---|
| aditirajnish/scholarship_web_scraper | `PRELIMINARY_FOCUSED` | MIT historical source-specific scraper; source review complete, runtime not tested |
| AlanWang610/academic-cv-scraper | `PRELIMINARY_FOCUSED` | Archived MIT CV/LLM extraction tool; privacy and identity risks; runtime not tested |
| AliAIOps/Putting-in-for-a-PhD-and-moving-abroad | `REVIEW_RECORDED` | Unique fork deltas; dependent guide lineage |
| alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad | `REVIEW_RECORDED` | Unique fork deltas; dependent guide lineage |
| alistvt/Putting-in-for-a-PhD-and-moving-abroad | `SCREENED_EXCLUDE` | No substantive content delta beyond README; duplicate fork |
| centrixsol/phd-applicant | `DEEP_REVIEW_DOCUMENTED` | Core schema, API, automation and security paths inspected; runtime not tested |
| chuyaowang/nl-phd-tracker | `DEEP_REVIEW_DOCUMENTED` | Extension, token flow, local API and persistence path inspected; runtime not tested |
| Joky02/AcademiaReach | `DEEP_REVIEW_DOCUMENTED` | Search, compose, review, SMTP/IMAP, data and deployment paths inspected; tests inspected but not executed |
| Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP | `DEEP_REVIEW_DOCUMENTED` | Core source and DB paths inspected; committed private binaries deliberately excluded |
| imranbinyounos/PhdApply | `PRELIMINARY_FOCUSED` | Active UI/store/model/CSV architecture inspected; full view and runtime validation incomplete |
| ianouhi17-ctrl/phd-application-workbench | `PRELIMINARY_FOCUSED` | Markdown workflow corpus reviewed; central XLSX not inspected |
| drPod/phd-application-tracker | `PRELIMINARY_FOCUSED` | Supabase hooks, storage, auth and tests inspected; RLS config absent |
| ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER | `PRELIMINARY_FOCUSED` | Static/localStorage UI and placeholder backend inspected |
| Khayrulbuet13/AcademicJobScraper | `PRELIMINARY_FOCUSED` | Single-source scraper/CLI inspected; no tests/runtime |
| JaykishanJ/PhD_Finder | `PRELIMINARY_FOCUSED` | Multi-omics crawler and region/funding heuristics inspected; no runtime/tests |
| ledmands/education_job_scraper | `PRELIMINARY_FOCUSED` | Scrape/extract/send path inspected; unsafe automatic email side effects |
| ibrar-saeed-dev/scholarship_scraper | `PRELIMINARY_FOCUSED` | Expo/Supabase UI and edge parser inspected; static data/provenance gaps |
| beepboopshru/scholarship-scraper | `PRELIMINARY_FOCUSED` | Skeleton scraper modules inspected; incomplete selectors and data model |
| Atashi1990/FundBaMa | `SCREENED_EXCLUDE` | Static marketing/information site, no operational opportunity database |
| AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo | `SCREENED_EXCLUDE` | Java classroom calculator; SOP keyword collision |

## Ownership exclusions

Do not include or modify findings for:

- simitii/CS-Grad-School-Applications-Reading-List and siddu1998/Graduate-Admissions — already integrated through PR #6.
- Ariaeimehr/PHD-Position-Finder, arbitan/ScholarshipWebsite and archna1212/PHD-OPENINGS — claimed in session audit-20261112-0001-7f3c's integration branch.
- Akshitha-03/Automating_PhD_Group4, fsuitoal-code/phd-application-command-center, EydlinIlya/BlueSky-PhD-jobs, houwei1228/PhD_Fit and DataBizex/academic-positions-dashboard — claimed by session gpt6-20261111-2031z.
- zhoujasper/phd-atlas and zxcgzx/phd-application-tracker — claimed by session 20261112-0031z-gpt6-a.
- All ten repositories in session 2cabbe82 are already represented by its merged reports in main.

## Required checks before canonical inventory update

1. Re-read the latest main inventory and all merged session reports.
2. Check current branches and open PRs for later ownership claims.
3. Resolve candidate identity/fork lineage; do not count derivative copies as independent sources.
4. Update candidate and repository registers in one coordinated change with stable IDs and correct review states.
5. Regenerate indexes with repository scripts and run schema/integrity tests.
6. Verify all source links and preserve uninspected scope.
7. Do not change global status totals until the canonical CSV and generated index reconcile.

## Merge condition

Merge this session-artifact PR only if the source branch is based on current main, the PR diff contains only this session's directory, no duplicate report exists in main or another active PR, and GitHub reports the PR mergeable with required checks passing. This proposal is not evidence that a merge has occurred.