# Integration proposal — session gpt6-20261112-01

Target: main  
Source branch: research/session-gpt6-20261112-01-mainline-v3  
Base snapshot: 7a9eb79a66e06e28c69cb6fd9f23c25dee5a1da6

## Scope

This PR adds only session-owned research artifacts under `research/sessions/gpt6-20261112-01/`. It does not edit the canonical discovery inventory, repository register, generated index, shared schemas, global status or another session's files. Canonical register updates are deferred to a separately coordinated integration.

## Proposed dispositions

| Repository | Proposed disposition | Rationale |
|---|---|---|
| aditirajnish/scholarship_web_scraper | PRELIMINARY_FOCUSED | Historical Schulich-specific scraper; source review complete, runtime not tested |
| AlanWang610/academic-cv-scraper | PRELIMINARY_FOCUSED | Archived MIT CV/LLM extraction tool; privacy and identity risks |
| AliAIOps/Putting-in-for-a-PhD-and-moving-abroad | REVIEW_RECORDED | Unique fork deltas; dependent guide lineage |
| alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad | REVIEW_RECORDED | Unique fork deltas; dependent guide lineage |
| alistvt/Putting-in-for-a-PhD-and-moving-abroad | SCREENED_EXCLUDE | No substantive content delta beyond README; duplicate fork |
| centrixsol/phd-applicant | DEEP_REVIEW_DOCUMENTED | Core schema, API, automation and security paths inspected; runtime not tested |
| imranbinyounos/PhdApply | PRELIMINARY_FOCUSED | Active UI/store/model/CSV architecture inspected; full runtime validation incomplete |
| ianouhi17-ctrl/phd-application-workbench | PRELIMINARY_FOCUSED | Markdown workflow corpus reviewed; central XLSX not inspected |
| ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER | PRELIMINARY_FOCUSED | Static/localStorage UI and placeholder backend inspected |
| Khayrulbuet13/AcademicJobScraper | PRELIMINARY_FOCUSED | Single-source scraper/CLI inspected; no tests/runtime |
| JaykishanJ/PhD_Finder | PRELIMINARY_FOCUSED | Multi-omics crawler and region/funding heuristics inspected; no runtime/tests |
| ledmands/education_job_scraper | PRELIMINARY_FOCUSED | Scrape/extract/send path inspected; unsafe automatic email side effects |
| ibrar-saeed-dev/scholarship_scraper | PRELIMINARY_FOCUSED | Expo/Supabase UI and edge parser inspected; static data/provenance gaps |
| AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo | SCREENED_EXCLUDE | Java classroom calculator; SOP keyword collision |

## Ownership exclusions

Do not include or modify findings for:

- simitii/CS-Grad-School-Applications-Reading-List and siddu1998/Graduate-Admissions — already integrated through PR #6.
- Ariaeimehr/PHD-Position-Finder, arbitan/ScholarshipWebsite and archna1212/PHD-OPENINGS — already integrated through PR #7.
- chuyaowang/nl-phd-tracker, beepboopshru/scholarship-scraper, Joky02/AcademiaReach, drPod/phd-application-tracker, Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP and Atashi1990/FundBaMa — separate reports/dispositions already present on main.
- fsuitoal-code/phd-application-command-center, EydlinIlya/BlueSky-PhD-jobs, houwei1228/PhD_Fit, DataBizex/academic-positions-dashboard and Akshitha-03/Automating_PhD_Group4 — claimed by session gpt6-20261111-2031z.
- zhoujasper/phd-atlas and zxcgzx/phd-application-tracker — claimed by session 20261112-0031z-gpt6-a.
- The ten repositories in session 2cabbe82 — already integrated through PR #6.

## Canonical inventory follow-up

After ownership reconciliation, a separate coordinated change should:

1. Re-read the latest canonical inventory and all merged review files.
2. Confirm repository identities and fork lineage.
3. Add only the session's unique repository dispositions with stable IDs and source snapshot SHAs.
4. Regenerate indexes and run the repository integrity checks.
5. Reconcile all status counts; do not promote preliminary reviews to deep review.

## Merge condition

Merge only if this PR's diff contains only the session directory, no duplicate report exists on main or another active PR, the branch is based on the current mainline, conflicts are resolved, and available CI checks pass. This proposal is not evidence that a merge has occurred.