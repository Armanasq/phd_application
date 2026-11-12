# syedpeera/Phd-Admissions-NITPY — deep static code audit

**Source:** https://github.com/syedpeera/Phd-Admissions-NITPY. **Pinned Git tree SHA:** `932bc5fc88bc822edca5ea73bb07f5badced2b68` ([tree](https://api.github.com/repos/syedpeera/Phd-Admissions-NITPY/git/trees/932bc5fc88bc822edca5ea73bb07f5badced2b68)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Official current opening, eligibility and funding:** UNKNOWN.

## 1. Scope and objective

Inspect concrete source-level implementation and determine its fit for PhD evidence and applicant workflows.

## 2. Implementation architecture

2019/20 NIT Puducherry PHP portal gathers application, eligibility and uploaded documents. `connection.php` embeds DB access information; `home.php` interpolates many applicant-controlled values into SELECT/INSERT SQL and includes a hardcoded SMTP password. Do not reproduce credential values or individual records. Requires prepared SQL, authenticated roles and secret rotation.

## 3. Source and dataflow

Inspected [connection.php](https://github.com/syedpeera/Phd-Admissions-NITPY/blob/master/connection.php), [index.php](https://github.com/syedpeera/Phd-Admissions-NITPY/blob/master/index.php), [home.php](https://github.com/syedpeera/Phd-Admissions-NITPY/blob/master/home.php). The snapshot is source level; no live service testing performed.

## 4. Confirmed correctness/security risks

**INLINE_SQL_INTERPOLATION_AND_PUBLISHED_SERVICE_SECRETS (P0).** 2019/20 NIT Puducherry PHP portal gathers application, eligibility and uploaded documents. `connection.php` embeds DB access information; `home.php` interpolates many applicant-controlled values into SELECT/INSERT SQL and includes a hardcoded SMTP password. Do not reproduce credential values or individual records. Requires prepared SQL, authenticated roles and secret rotation. Statements about authentication and errors apply to inspected code; deployed rule configurations and exploitability were not tested.

## 5. Verification and external-authority constraints

Extracted scholarship records, self-reported applicant states and program pages do not establish a current official funded offer. Preserve issuer URL, source excerpt, collection timestamp, intake cycle and formal deadline/eligibility checks.

## 6. Cross-repository transferable methods

Separate source collection from candidate-eligibility verification and personal applicant state. Repository supplies useful workflow concepts only after authorization, typed claim evidence and integrity controls.

## 7. Verdict

**P0: adopt no production code until INLINE_SQL_INTERPOLATION_AND_PUBLISHED_SERVICE_SECRETS corrected.** Preserve privacy of applicant artifacts and never infer current funding from old metadata.

## 8. Tests and open questions

No CI execution, source owner contact, candidate document read, live scraping or adversarial tests performed. Add tests for authentication, conflicting source deadlines, data replacement, dedup, persistent state, empty/incomplete HTTP pages and precision of extraction.
