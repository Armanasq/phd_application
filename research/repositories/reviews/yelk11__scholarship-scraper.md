# Deep static audit — Yelk11/scholarship_scraper

**Pinned Git tree:** `2c884d2e3a222b266438d6907aa29b190442ed9a` ([immutable inventory](https://api.github.com/repos/Yelk11/scholarship_scraper/git/trees/2c884d2e3a222b266438d6907aa29b190442ed9a)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Funding/eligibility:** NOT_VERIFIED.

## 1. Objective and relevance

Assess source implementation and reusability for PhD discovery/application, without claiming actual admission or current offers.

## 2. Source architecture and execution

Python crawler builds a SQLite URL queue. Validator.validate returns a percentage; crawler treats any nonzero result as valid. Loader lacks explicit HTTP timeout/raise_for_status, so error pages can enter extraction.

## 3. Algorithms and data contracts

Source modules inspected: [crawler.py](https://github.com/Yelk11/scholarship_scraper/blob/main/crawler.py), [validator.py](https://github.com/Yelk11/scholarship_scraper/blob/main/validator.py), [loader.py](https://github.com/Yelk11/scholarship_scraper/blob/main/loader.py). The tree was inventoried, but external endpoints and binary resources were not exercised. Source metadata/links or user-defined status fields do not independently prove eligibility, scholarship funding or submission.

## 4. Confirmed code-level risks

**P1: KEYWORD_PERCENT_TREATED_AS_BOOLEAN.** Python crawler builds a SQLite URL queue. Validator.validate returns a percentage; crawler treats any nonzero result as valid. Loader lacks explicit HTTP timeout/raise_for_status, so error pages can enter extraction. The finding concerns inspected code; actual live-service exposure or exploitation remains untested.

## 5. Provenance and verification limits

A future implementation must preserve original issuer URL, crawl time, exact quoted claim, intake cycle, deadline timezone, funding coverage and eligibility status. Treat missing confirmation as UNKNOWN, not OPEN or FULLY_FUNDED.

## 6. Interconnections and transferable methods

Separate data ingestion, candidate matching, human review and applicant private state. Comparable reviewed systems show that crawled opportunities and editable application status fields are not authoritative source facts. Any reusable architecture requires evidence and security hardening.

## 7. Recommendation and priority

**P1 — do not adopt unmodified.** Address KEYWORD_PERCENT_TREATED_AS_BOOLEAN, restrict external network access and add source/identity validation before migration into the PhD research workflow.

## 8. Required tests and closure conditions

Not run: source snapshot comparison, live provider checks, runtime tests, auth/permission tests, network attack reproduction, multiuser isolation and deadline verification. Add unit tests for the specific defect, incomplete source responses, false openings, concurrent updates, exact IDs and authorization.
