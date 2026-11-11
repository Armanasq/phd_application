# abolfazl-yousefi/Academic-Job-Scraper-Project — notebook implementation review

**Date:** 2026-11-11 · **Commit:** [848eee97b2ea917fa4e03c9469947d1339c29fcd](https://github.com/abolfazl-yousefi/Academic-Job-Scraper-Project/commit/848eee97b2ea917fa4e03c9469947d1339c29fcd) · **State:** PRELIMINARY_FOCUSED

**Verdict:** REJECT AS-IS; retain the source-discovery concept only. **Risk:** tls_verification_disabled_brittle_parsers_and_broken_notebook.

## Repository and source coverage

Three tracked files: `.DS_Store`, a minimal README and one Jupyter notebook. The notebook contains three adapters:
- ScholarshipDB: category/program/keyword/date-window search, pagination and detail-page extraction.
- FindAPhD: keyword search with a `non-eu-students` filter; attempts to extract title, university, department, country, supervisor and body.
- EURAXESS: keyword search and extraction of title, institute, deadline, country and body.

The source list is a useful historical discovery lead, but the notebook does not distinguish an aggregator listing from the original employer/university announcement.

## HTTP and parser implementation

The shared `open_page` helper calls `requests.get(url, verify=False)`, parses HTML and sleeps for a fixed interval. It disables TLS certificate verification and suppresses warnings globally. It does not set a timeout, check HTTP status, validate redirects, use a stable user-agent, implement retry/backoff or preserve response metadata.

The ScholarshipDB path relies on positional selectors such as `ul.list-unstyled[4]` and assumes a nested anchor structure. These selectors are brittle under site redesign. The source-specific extraction is limited to a few display fields; funding terms, fee coverage, citizenship rules and source evidence are not normalized.

## Static execution defects

The notebook is not executable end-to-end as committed:
- FindAPhD and EURAXESS cells contain invalid assignments with a trailing colon, e.g. `soup = open_page(url, time_sleep):`.
- A later cell calls `extract_job_defintion_from_result`, but no definition exists in the notebook.
- That cell calls `open_page(url)` although the helper requires both `url` and `time_sleep`.
- Output columns are declared but not consistently populated; no reproducible dependency file or tests exist.

These are static findings; the scraper was not executed.

## Missing production capabilities

No persistent store, canonical identity, deduplication, source snapshots, audit trail, stale-record lifecycle, applicant eligibility, international tuition coverage or structured funding verification. The notebook prints some details but does not create a durable, reviewable opportunity dataset.

## Transfer and decision

The three-source adapter idea is reusable only after redesign. A mature replacement needs isolated source adapters, fixture-based parser tests, safe HTTP/TLS, stable IDs, original employer links, source timestamps, claim-level evidence, deduplication, funding/eligibility gates and human review for conflicts.

**Evidence:** [repository](https://github.com/abolfazl-yousefi/Academic-Job-Scraper-Project) · [notebook](https://github.com/abolfazl-yousefi/Academic-Job-Scraper-Project/blob/848eee97b2ea917fa4e03c9469947d1339c29fcd/Academic%20Job%20Scraper.ipynb).