# Research session manifest — mainline integration

- Session ID: gpt6-20261112-01
- Canonical repository: https://github.com/Armanasq/phd_application
- Base commit: ccbd518c8e036d4dca8de881e25be8de97f22648 (latest main at branch creation)
- Source branch: research/session-gpt6-20261112-01-integration
- Integration target: main
- Working mode: branch-scoped GitHub operations because no local worktree is available. No direct main-branch writes.
- Pull-request rule: all changes are proposed against main; merge only after diff review, conflict resolution, and available checks pass.

## Mainline and parallel-session reconciliation

- PR #6 from session 2cabbe82 is merged. Its ten supplemental repository reports and synthesis are already in main under research/sessions/2cabbe82/.
- Session 2cabbe82 already covers simitii/CS-Grad-School-Applications-Reading-List and siddu1998/Graduate-Admissions. Do not duplicate these reports.
- Session audit-20261112-0001-7f3c has a separate integration branch with reports for Ariaeimehr/PHD-Position-Finder, arbitan/ScholarshipWebsite, and archna1212/PHD-OPENINGS. Treat all three as owned by that session; do not duplicate or modify its files.
- Session gpt6-20261111-2031z retains claims for fsuitoal-code/phd-application-command-center, EydlinIlya/BlueSky-PhD-jobs, houwei1228/PhD_Fit, DataBizex/academic-positions-dashboard, and Akshitha-03/Automating_PhD_Group4. Do not investigate or integrate competing reports for these.
- Latest mainline also contains supplemental reports for chuyaowang/nl-phd-tracker, beepboopshru/scholarship-scraper, aluminium5/ScholarshipScraper, arunrathi9/Data-Science-Scholarships, atomdbc/scholarship_scraper, borekda/phd-list and chinasaokolo/csGraduateApps. Treat these as already reviewed; do not duplicate them.
- Session 20261112-0031z-gpt6-a claims zhoujasper/phd-atlas and zxcgzx/phd-application-tracker, and has overlapping early claims on simitii/siddu. Do not duplicate these.
- Branch research/repository-audit-20261112-2cabbe82 has been merged as PR #6. Its work is part of main.
- Other sessions' unpublished/private activity remains unobservable. Published claims are treated as active ownership.

## Superseded work

- The earlier branch research/session-gpt6-20261112-01 was created from an older main snapshot and contains preliminary notes overlapping with simitii, siddu1998, Akshitha, and Ariaeimehr.
- That branch is intentionally not being merged. Its work is superseded by mainline reconciliation and published session claims.
- The current branch was created directly from latest main to prevent stale-base and duplicate-content integration.

## Independent active scope

| Repository | Scope | Current assessment |
|---|---|---|
| aditirajnish/scholarship_web_scraper | Source-level scraper review | Preliminary review completed |
| AlanWang610/academic-cv-scraper | CV discovery, parsing and identity-resolution review | Preliminary review completed |
| AliAIOps/Putting-in-for-a-PhD-and-moving-abroad | Fork-delta review against Fatemeh-J upstream | Unique content inspected |
| alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad | Fork-delta review against same upstream | Unique content inspected |
| alistvt/Putting-in-for-a-PhD-and-moving-abroad | Fork-delta review against same upstream | README-only delta; duplicate content |
| centrixsol/phd-applicant | Admissions CRM and browser automation | Deep static review completed |
| Joky02/AcademiaReach | Supervisor discovery, research, outreach and reply workflow | Deep static review completed |
| Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP | Opportunity scraping and resume matching | Deep static review completed; personal artifacts not inspected |
| imranbinyounos/PhdApply | GradKit Pro local application workspace | Structured source review completed |
| ianouhi17-ctrl/phd-application-workbench | Applicant planning templates and workbook | Markdown corpus reviewed; binary workbook not inspected |
| drPod/phd-application-tracker | Supabase application/document tracker | Preliminary source review completed |
| ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER | LocalStorage application and job tracker | Preliminary source review completed |
| Khayrulbuet13/AcademicJobScraper | AcademicJobsOnline scraper | Preliminary source review completed |
| JaykishanJ/PhD_Finder | Multi-omics focused multi-source crawler | Preliminary source review completed |
| ledmands/education_job_scraper | Academic-job scraper and automatic emailer | Preliminary source review completed |
| ibrar-saeed-dev/scholarship_scraper | Expo/Supabase scholarship directory | Preliminary source review completed |
| Atashi1990/FundBaMa | Scholarship/education website | Screened as static marketing site, not an implemented opportunity system |
| AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo | Keyword collision | Excluded: unrelated Java classroom exercise |

## Source lineage and deduplication

- AliAIOps, alirezazolanvari, and alistvt are forks of Fatemeh-J/Putting-in-for-a-PhD-and-moving-abroad. They are derivative versions of one underlying firsthand guide, not independent applicant samples.
- Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad is blob-identical to the Fatemeh-J upstream and already has a preliminary review in the canonical corpus.
- AliAIOps contains several unique edits to the post-admission, immigration, relocation and job-search guidance.
- alirezazolanvari contains a separate set of edits and an accommodation section.
- alistvt differs from the upstream only in README content at the inspected tree snapshot.
- archna1212/PHD-OPENINGS shares identical implementation blobs with the already-reviewed Aghababaei/PhD-Seeker and is owned by another active session's duplicate-screening report.

## Research integrity and safety

- Upstream commit SHAs and inspected paths are recorded in the session reports.
- Static inspection is not runtime validation. No third-party code has been executed in this session.
- No private PDFs, recommendation letters, resumes, passports, or committed database contents are reproduced or inspected.
- No live Firebase/Supabase/MongoDB access, credential use, application submission, or email sending was performed.
- All findings distinguish verified source facts, interpretations, risks, recommendations and unknowns.

## Integration controls

- All artifacts remain under research/sessions/gpt6-20261112-01/ on this branch.
- Do not edit canonical inventory, generated indexes, shared schemas, global status or other session directories in this PR.
- Before PR creation, compare the complete branch diff against latest main and all published session artifacts.
- Resolve conflicts only in this branch, preserving all mainline changes. No force-push, reset or destructive file operations.
- Merge only after the PR is non-duplicative, the final diff is reviewed, and available CI checks pass.

## Completion status

- Independent repository investigations documented: 17 relevant or adjacent repositories/fork variants plus one false-positive exclusion.
- Deep static reviews: centrixsol, chuyaowang, Joky02, Gurudev517.
- Structured source reviews: imranbinyounos, ianouhi17-ctrl.
- Preliminary reviews: aditirajnish, AlanWang610, drPod, ATULPANDEYIITR, Khayrulbuet13, JaykishanJ, ledmands, ibrar-saeed-dev, beepboopshru.
- Remaining: extend the 330-candidate untriaged queue in disjoint batches; complete PDF/workbook limitations where safe; validate cross-source claims; prepare PR.