# Research session manifest — reconciled mainline v3

- Session ID: gpt6-20261112-01
- Canonical repository: https://github.com/Armanasq/phd_application
- Base commit: 7a9eb79a66e06e28c69cb6fd9f23c25dee5a1da6 (main at branch creation)
- Source branch: research/session-gpt6-20261112-01-mainline-v3
- Integration target: main
- Working mode: branch-scoped GitHub operations; no direct writes to main.
- Pull-request rule: propose only unique session artifacts against main; merge after diff review, conflict resolution and available checks.

## Parallel-session reconciliation

- PR #6 (session 2cabbe82) is merged. Its ten supplemental repository reports are already in main.
- PR #7 (session audit-20261112-0001-7f3c) is merged. Its Ariaeimehr, Arbitan and Archna investigations are already in main.
- Mainline now also contains reviews/dispositions for chuyaowang/nl-phd-tracker, beepboopshru/scholarship-scraper, aluminium5/ScholarshipScraper, arunrathi9/Data-Science-Scholarships, atomdbc/scholarship_scraper, borekda/phd-list, chinasaokolo/csGraduateApps, Joky02/AcademiaReach, drPod/phd-application-tracker, Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP and Atashi1990/FundBaMa. These are excluded from this PR.
- Session gpt6-20261111-2031z retains claims for fsuitoal-code/phd-application-command-center, EydlinIlya/BlueSky-PhD-jobs, houwei1228/PhD_Fit, DataBizex/academic-positions-dashboard and Akshitha-03/Automating_PhD_Group4. Do not duplicate.
- Session 20261112-0031z-gpt6-a retains claims for zhoujasper/phd-atlas and zxcgzx/phd-application-tracker. Do not duplicate.
- Other sessions' unpublished/private work remains unobservable. Published branch and mainline records are treated as authoritative ownership signals.

## Superseded branches

- research/session-gpt6-20261112-01 was created from an older main snapshot and contained exploratory notes overlapping with other sessions. It is not being merged.
- research/session-gpt6-20261112-01-integration was based on a stale main snapshot and is superseded.
- research/session-gpt6-20261112-01-mainline-v2 was based on a main snapshot that became stale while parallel work continued. It is superseded.
- This v3 branch was created from the latest observed main commit and carries only non-duplicative session artifacts.

## Independent scope retained for this PR

| Repository | Assessment |
|---|---|
| aditirajnish/scholarship_web_scraper | Preliminary source review |
| AlanWang610/academic-cv-scraper | Preliminary source review; archived |
| AliAIOps/Putting-in-for-a-PhD-and-moving-abroad | Unique fork-delta review |
| alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad | Unique fork-delta review |
| alistvt/Putting-in-for-a-PhD-and-moving-abroad | Duplicate fork; README-only delta |
| centrixsol/phd-applicant | Deep static review |
| imranbinyounos/PhdApply | Structured source review |
| ianouhi17-ctrl/phd-application-workbench | Structured document/workflow review; workbook uninspected |
| ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER | Preliminary source review |
| Khayrulbuet13/AcademicJobScraper | Preliminary source review |
| JaykishanJ/PhD_Finder | Preliminary source review |
| ledmands/education_job_scraper | Preliminary source review |
| ibrar-saeed-dev/scholarship_scraper | Preliminary source review |
| AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo | False-positive exclusion |

Counts: 12 relevant/adjacent repository identities, including two unique Farsi-guide fork variants; one duplicate-fork exclusion; one keyword-collision false-positive exclusion. The upstream Farsi guide is one dependent applicant-experience source, not multiple independent cases.

## Evidence and safety

- Upstream commit SHAs and inspected paths are pinned in the individual reports.
- No third-party code was executed. No live database, Firebase, Supabase or SMTP account was accessed.
- No email, application submission or external action was performed.
- Private résumé PDFs, recommendation letters, transcripts, passports and committed database contents were not opened or reproduced.
- Static review is not runtime validation. Tests were inspected where available but not executed.
- Findings distinguish verified source facts, interpretation, risk, recommendation and unknown.

## Integration controls

- All artifacts are under research/sessions/gpt6-20261112-01/ on this branch.
- This PR does not modify the canonical discovery CSV, repository register, generated index, shared schema or global status.
- Before merge, compare the entire diff with latest main and all open branches/PRs.
- Resolve conflicts only in this branch. Preserve all mainline commits; no force-push, reset or destructive file operations.
- Merge only if the PR is non-duplicative, mergeable, and available CI checks pass.

## Remaining work

- Continue the 319-candidate untriaged inventory in disjoint batches after checking new parallel ownership.
- Deepen preliminary reviews where the implementation warrants it.
- Complete the binary workbook inspection only if it can be obtained and safely inspected.
- Perform independent source rechecks and runtime validation in an isolated sandbox where feasible.
- Coordinate canonical inventory updates in a separate change after review ownership is reconciled.