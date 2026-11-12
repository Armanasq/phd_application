# Deep static audit — Scholars4Scholars/ScholarshipScraper

**Pinned Git tree:** `cf6fcd7e378aa499c6a2f13214b89f60e120db22` ([immutable inventory](https://api.github.com/repos/Scholars4Scholars/ScholarshipScraper/git/trees/cf6fcd7e378aa499c6a2f13214b89f60e120db22)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Funding/eligibility:** NOT_VERIFIED.

## 1. Objective and relevance

Assess source implementation and reusability for PhD discovery/application, without claiming actual admission or current offers.

## 2. Source architecture and execution

Entire scraper.py uses Python 2 xrange, old HTTP Fastweb IDs and positional dt/dd pairing; writes random named JSON batches. Does not verify official scholarship status, dates or eligibility.

## 3. Algorithms and data contracts

Source modules inspected: [scraper.py](https://github.com/Scholars4Scholars/ScholarshipScraper/blob/main/scraper.py). The tree was inventoried, but external endpoints and binary resources were not exercised. Source metadata/links or user-defined status fields do not independently prove eligibility, scholarship funding or submission.

## 4. Confirmed code-level risks

**P2: HTTP_PYTHON2_UNVERIFIED_SCHOLARSHIP_METADATA.** Entire scraper.py uses Python 2 xrange, old HTTP Fastweb IDs and positional dt/dd pairing; writes random named JSON batches. Does not verify official scholarship status, dates or eligibility. The finding concerns inspected code; actual live-service exposure or exploitation remains untested.

## 5. Provenance and verification limits

A future implementation must preserve original issuer URL, crawl time, exact quoted claim, intake cycle, deadline timezone, funding coverage and eligibility status. Treat missing confirmation as UNKNOWN, not OPEN or FULLY_FUNDED.

## 6. Interconnections and transferable methods

Separate data ingestion, candidate matching, human review and applicant private state. Comparable reviewed systems show that crawled opportunities and editable application status fields are not authoritative source facts. Any reusable architecture requires evidence and security hardening.

## 7. Recommendation and priority

**P2 — do not adopt unmodified.** Address HTTP_PYTHON2_UNVERIFIED_SCHOLARSHIP_METADATA, restrict external network access and add source/identity validation before migration into the PhD research workflow.

## 8. Required tests and closure conditions

Not run: source snapshot comparison, live provider checks, runtime tests, auth/permission tests, network attack reproduction, multiuser isolation and deadline verification. Add unit tests for the specific defect, incomplete source responses, false openings, concurrent updates, exact IDs and authorization.
