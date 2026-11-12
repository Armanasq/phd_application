# Deep static audit — vsvarapriya/phd_admissions_portal

**Pinned Git tree:** `a29b544673e16d84d34d1c34b4a3e404d64b6b5e` ([immutable inventory](https://api.github.com/repos/vsvarapriya/phd_admissions_portal/git/trees/a29b544673e16d84d34d1c34b4a3e404d64b6b5e)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Funding/eligibility:** NOT_VERIFIED.

## 1. Objective and relevance

Assess source implementation and reusability for PhD discovery/application, without claiming actual admission or current offers.

## 2. Source architecture and execution

AdminLogin.php includes plaintext database access credentials and interpolates supplied identity/password in SQL; Application.php also builds SQL from session email. Original sample documents are not read or reproduced.

## 3. Algorithms and data contracts

Source modules inspected: [AdminLogin.php](https://github.com/vsvarapriya/phd_admissions_portal/blob/main/AdminLogin.php), [Application.php](https://github.com/vsvarapriya/phd_admissions_portal/blob/main/Application.php), [README.md](https://github.com/vsvarapriya/phd_admissions_portal/blob/main/README.md). The tree was inventoried, but external endpoints and binary resources were not exercised. Source metadata/links or user-defined status fields do not independently prove eligibility, scholarship funding or submission.

## 4. Confirmed code-level risks

**P0: HARDCODED_DATABASE_SECRET_AND_AUTH_QUERY_INJECTION.** AdminLogin.php includes plaintext database access credentials and interpolates supplied identity/password in SQL; Application.php also builds SQL from session email. Original sample documents are not read or reproduced. The finding concerns inspected code; actual live-service exposure or exploitation remains untested.

## 5. Provenance and verification limits

A future implementation must preserve original issuer URL, crawl time, exact quoted claim, intake cycle, deadline timezone, funding coverage and eligibility status. Treat missing confirmation as UNKNOWN, not OPEN or FULLY_FUNDED.

## 6. Interconnections and transferable methods

Separate data ingestion, candidate matching, human review and applicant private state. Comparable reviewed systems show that crawled opportunities and editable application status fields are not authoritative source facts. Any reusable architecture requires evidence and security hardening.

## 7. Recommendation and priority

**P0 — do not adopt unmodified.** Address HARDCODED_DATABASE_SECRET_AND_AUTH_QUERY_INJECTION, restrict external network access and add source/identity validation before migration into the PhD research workflow.

## 8. Required tests and closure conditions

Not run: source snapshot comparison, live provider checks, runtime tests, auth/permission tests, network attack reproduction, multiuser isolation and deadline verification. Add unit tests for the specific defect, incomplete source responses, false openings, concurrent updates, exact IDs and authorization.
