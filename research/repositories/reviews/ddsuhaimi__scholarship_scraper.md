# ddsuhaimi/scholarship_scraper — source-pinned historical ingestion review

- Pinned upstream commit: [f87946acd027be753dbbd11704efef8fbecfbbb3](https://github.com/ddsuhaimi/scholarship_scraper/commit/f87946acd027be753dbbd11704efef8fbecfbbb3), 2019-08-17.
- Inspection: complete three-file text corpus (`readme.md`, `scraper.py`, historical CSV), repository tree, commits and issue list. No code execution, live source retrieval or official funding verification.
- Review state: PRELIMINARY_FOCUSED; historical adapter methodology only, **not** evidence of 2026–27 scholarships.

The [scraper](https://github.com/ddsuhaimi/scholarship_scraper/blob/f87946acd027be753dbbd11704efef8fbecfbbb3/scraper.py) requests only the first plain-HTTP scholars4dev.com page and parses six fields using fixed BeautifulSoup selectors before pandas CSV export. It lacks timeout, retries, response status/content validation, source URL per award and source snapshots; bare `except` clauses silently convert structural parsing errors to nulls. The checked-in [2019 export](https://github.com/ddsuhaimi/scholarship_scraper/blob/f87946acd027be753dbbd11704efef8fbecfbbb3/export/scholarship.csv) has 12 rows spanning Bachelor's, Master's, MBA, PhD and postdoctoral awards with stale or ambiguous deadlines; it is not a PhD-only verified vacancy set.

Adapt only the idea of per-source parsing, replacing the implementation with permitted HTTPS adapters, typed extraction validation, explicit errors, cycle/timezone/country/fee-status evidence and primary-award verification. No license, tests, runnable freshness checks or applicant eligibility evidence established. [Expanded source review](../../sessions/main-20261112/2026-11-12-independent-source-audit-a9c5.md).
