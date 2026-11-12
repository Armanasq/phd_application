# wijayantoap/scholarship-scraper — focused original-source review

**Source:** https://github.com/wijayantoap/scholarship-scraper. **Pinned Git tree SHA:** `400d6b14cf21d1abfab311e9aecb53559568c2cd` ([tree](https://api.github.com/repos/wijayantoap/scholarship-scraper/git/trees/400d6b14cf21d1abfab311e9aecb53559568c2cd)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Official current opening, eligibility and funding:** UNKNOWN.

## 1. Files actually inspected

[server.js](https://github.com/wijayantoap/scholarship-scraper/blob/main/server.js), [scholars4DevPost.js](https://github.com/wijayantoap/scholarship-scraper/blob/main/scholars4DevPost.js), [indbeasiswaPost.js](https://github.com/wijayantoap/scholarship-scraper/blob/main/indbeasiswaPost.js). Other source and binary files were inventoried but not exhaustively read. This is PRELIMINARY_FOCUSED, not evidence of passing tests.

## 2. Findings and scope

2021 Express server exposes Scholars4Dev and Indbeasiswa list/post/category/sitemap routes with query-supplied URL passed to scraper module and no explicit host allowlist, authentication or error handling in server.js. SSRF exploitability depends on uninspected downstream functions.

## 3. Cross-repository transfer

Treat templates, personal historical cases and front-end forms separately from source-backed scholarship policy. Preserve provenance and do not reuse personal data as if it were public program facts.

## 4. Missing confirmation

**UNVALIDATED_FETCH_URL_PARAMS_AND_NO_ERROR_BOUNDARY (P1).** No live tests, official current-cycle funding verification, admissions outcome independent verification, or complete binary document analysis was performed.
