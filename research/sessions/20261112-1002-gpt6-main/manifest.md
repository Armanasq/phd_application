# Source review and evidence-based screening — 2026-11-12

**Branch:** `main`; **baseline SHA:** `f1aa1722abbb45b42653d4106214b8a577e27cbe`. Full third-party runtime validation NOT_PERFORMED.

## Deep code review
- `centrixsol/phd-applicant` [pinned upstream](https://github.com/centrixsol/phd-applicant/commit/c1b33eb17d8c57efed957c3cd33fe2ebb2355927) → [eight-section static audit](../../repositories/reviews/centrixsol__phd-applicant.md). The Next.js/Playwright integration marks offline demo and prefilled forms as submitted without portal receipts. Unauthenticated personal API paths and public document storage require redesign. No external application action executed.

## Exclusion dispositions
- `improvim/CV` — IDENTICAL_FORK: Same default commit/tree as already reviewed LimHyungTae/Awesome-PhD-CV; not independent evidence.
- `jaeminsjam/CV` — IDENTICAL_FORK: Same default commit/tree as already reviewed LimHyungTae/Awesome-PhD-CV; not independent evidence.
- `liber145/CV` — PERSONAL_CV_ARCHIVE: 2015 personal academic CV and writing samples; no reusable doctoral admissions mechanism. Private document content not extracted.
- `michaellennox/jobber` — GENERAL_JOB_CRM: 2016 Flask/Angular CRM for job hunting and Makers graduates; no doctoral-admissions or funded research opportunities.
- `sil24040/cse341-sophiesilveira1` — UNRELATED_COURSEWORK: CSE 341 contacts and temple coursework, not doctoral admissions.
- `SophiaRonquillo/SophiaRonquillo.github.io` — UNRELATED_COURSEWORK: CS 351 HTML guessing-number class projects, not admissions.
- `TIYDC/iron-jobs` — NONACADEMIC_JOBS: Job sharing for Iron Yard students and graduates, not doctoral recruitment.
- `ujjwal-kanodia/ap-project` — EMPTY_GIT_REPOSITORY: GitHub reports zero size and an empty Git repository; no inspectable project artifacts.
- `tomjackson-tech/graduate` — UNRELATED_GRADUATE_PORTFOLIO: Graduate-study project portfolio consists primarily of bank reconciliation software and spreadsheets, not doctoral admissions.
- `KieraTop/KieraLi-academic-cv` — ACADEMIC_WEBSITE_THEME: Hugo Blox academic CV website/theme example; no independent doctoral admissions or funding evidence.
- `sunjieyi/cirosantilli` — UNRELATED_TEXT_FORK: One-file fork of unrelated political text, not doctoral application resources.
- `shuijiaolou/cirosantilli` — UNRELATED_TEXT_FORK: One-file identical political-text fork, not admissions research.
- `wukun2/sunyijie-phd-application` — PRIVATE_APPLICANT_DOCUMENTS: Individual CV, university transcripts and under-review research manuscript; no reusable workflow. Educational records not extracted.

The two academic CV forks have exact upstream commit/tree parity. All screening decisions are grounded in tracked repository contents, README or GitHub metadata; no personal PDFs, transcripts or financial files copied.

## Canonical inventory
404 candidates = 166 reviews (65 deep static, 101 preliminary) + 163 excluded + 75 untriaged + 0 awaiting review. Generated index and status updated from the same candidate/review snapshot. Official funding/admissions validity remains unverified; issue #3 remains open.
