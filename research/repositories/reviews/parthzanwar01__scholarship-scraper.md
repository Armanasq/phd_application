# Deep static audit — ParthZanwar01/scholarship-scraper

**Pinned Git tree:** `138b638d0b7f29acae456fc724be583a777cefcf` ([immutable inventory](https://api.github.com/repos/ParthZanwar01/scholarship-scraper/git/trees/138b638d0b7f29acae456fc724be583a777cefcf)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Funding/eligibility:** NOT_VERIFIED.

## 1. Objective and relevance

Assess source implementation and reusability for PhD discovery/application, without claiming actual admission or current offers.

## 2. Source architecture and execution

FastAPI scraper/enrichment/create/delete routes have no auth in the inspected module. README publishes access credential material, withheld here. Celery Beat runs repeated polling and enrichment; scraper does not establish current official funding.

## 3. Algorithms and data contracts

Source modules inspected: [scholarship_scraper/app/main.py](https://github.com/ParthZanwar01/scholarship-scraper/blob/main/scholarship_scraper/app/main.py), [scholarship_scraper/app/tasks.py](https://github.com/ParthZanwar01/scholarship-scraper/blob/main/scholarship_scraper/app/tasks.py), [scholarship_scraper/orchestrator.py](https://github.com/ParthZanwar01/scholarship-scraper/blob/main/scholarship_scraper/orchestrator.py). The tree was inventoried, but external endpoints and binary resources were not exercised. Source metadata/links or user-defined status fields do not independently prove eligibility, scholarship funding or submission.

## 4. Confirmed code-level risks

**P0: EXPOSED_CREDENTIAL_MATERIAL_AND_PUBLIC_MUTATION_ENDPOINTS.** FastAPI scraper/enrichment/create/delete routes have no auth in the inspected module. README publishes access credential material, withheld here. Celery Beat runs repeated polling and enrichment; scraper does not establish current official funding. The finding concerns inspected code; actual live-service exposure or exploitation remains untested.

## 5. Provenance and verification limits

A future implementation must preserve original issuer URL, crawl time, exact quoted claim, intake cycle, deadline timezone, funding coverage and eligibility status. Treat missing confirmation as UNKNOWN, not OPEN or FULLY_FUNDED.

## 6. Interconnections and transferable methods

Separate data ingestion, candidate matching, human review and applicant private state. Comparable reviewed systems show that crawled opportunities and editable application status fields are not authoritative source facts. Any reusable architecture requires evidence and security hardening.

## 7. Recommendation and priority

**P0 — do not adopt unmodified.** Address EXPOSED_CREDENTIAL_MATERIAL_AND_PUBLIC_MUTATION_ENDPOINTS, restrict external network access and add source/identity validation before migration into the PhD research workflow.

## 8. Required tests and closure conditions

Not run: source snapshot comparison, live provider checks, runtime tests, auth/permission tests, network attack reproduction, multiuser isolation and deadline verification. Add unit tests for the specific defect, incomplete source responses, false openings, concurrent updates, exact IDs and authorization.
