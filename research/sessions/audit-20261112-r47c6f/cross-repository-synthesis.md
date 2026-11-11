# Cross-repository synthesis and integration proposal — audit-20261112-r47c6f

Date: 2026-11-12. Five independently assigned raw GitHub identities investigated at pinned upstream versions, with issue/PR metadata checked. No third-party runtime execution, employer-site live verification, application sending or credential use.

## Screening and unique contributions

| Identity | Proposed canonical state | Evidence-based contribution |
|---|---|---|
| dinglhmds/Search-PhD-Positions | REVIEW_RECORDED / DEEP_REVIEW_DOCUMENTED (static only) | Five-stage faculty scrape and applicant-controlled email draft; important unsafe path/HTML sinks and lack of provenance |
| DefangChen/CS_Professors | REVIEW_RECORDED / PRELIMINARY_FOCUSED | 24 hand-curated faculty research leads; not recruitment claims |
| Janjs/Web-Scraping-PhD-positions | REVIEW_RECORDED / PRELIMINARY_FOCUSED | Historical MSCA R1 researcher-stage filter; 2021 selector is not current vacancy evidence |
| heyulanKiara/django-phd-scholarship | SCREENED_EXCLUDE | Post-enrollment internal TA/RA scholarship payroll, not incoming PhD admissions; API/model drift and unsafe committed development credentials |
| D4vidHuang/PhD_scanner | SCREENED_EXCLUDE | Empty Git tree; no code/data to inspect |

## Operational synthesis

Separate **person identity** from institution, active hiring position, admission program, funding award, accepted offer, and post-matriculation teaching/research employment. Search/crawl/LLM extraction is discovery, not verification. Exact source authority, quoted span, publication date, valid cycle, applicant scope, verified_at, source hash, and reviewer decision must remain attached to every actionable statement. Unknown recruiting status, funding scope and eligibility must remain unknown rather than being turned into positive matches.

Engineering gates: canonical safe IDs for persisted artifacts; SSRF/redirect and official-host checks; reliable paginated/complete crawling; typed extraction and deterministic entity deduplication; HTML escaping and CSP; protected applicant data; authenticated, rate-limited jobs; immutable proof of submission and human authorization before contacting faculty. False-positive scholarship matches should be screened by **stage and beneficiary**, not keywords. Historical code and faculty pages remain citation leads, not 2026/27 funding evidence.

## Integration contract

This session owns only its paths under research/sessions/audit-20261112-r47c6f/. The canonical candidate CSV should mark three identities REVIEW_RECORDED and two SCREENED_EXCLUDE. A canonical review entry, if added, must reference the source-pinned session report; exclusion rows need the same evidence links. Shared state and generated indexes must be regenerated against fresh main rather than hardcoding observed totals. Do not rewrite work from other agents, and do not close issue #3 while hundreds of candidate identities remain unscreened.

The independent external source verification stage and controlled runtime benchmarks remain open. This batch does not satisfy global discovery saturation.
