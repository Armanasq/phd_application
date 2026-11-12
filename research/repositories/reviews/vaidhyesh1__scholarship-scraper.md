# vaidhyesh1/scholarship-scraper — deep static code audit

**Source:** https://github.com/vaidhyesh1/scholarship-scraper. **Pinned Git tree SHA:** `9f5f258b29e7a7a71ac8c82df91cf3dd0f905a06` ([tree](https://api.github.com/repos/vaidhyesh1/scholarship-scraper/git/trees/9f5f258b29e7a7a71ac8c82df91cf3dd0f905a06)). **Inspected:** 2026-11-12. **Runtime:** NOT_TESTED. **Official current opening, eligibility and funding:** UNKNOWN.

## 1. Scope and objective

Inspect concrete source-level implementation and determine its fit for PhD evidence and applicant workflows.

## 2. Implementation architecture

Python Selenium scrapes CollegeScholarships.org listing/detail pages with fixed female filter, brittle XPath and two browser processes. It writes a wholesale MongoDB replace_one on collected rows; no browser cleanup or complete-source marker in inspected script and an HTTP first-party issuer check is absent.

## 3. Source and dataflow

Inspected [scraper.py](https://github.com/vaidhyesh1/scholarship-scraper/blob/main/scraper.py), [categorize.py](https://github.com/vaidhyesh1/scholarship-scraper/blob/main/categorize.py). The snapshot is source level; no live service testing performed.

## 4. Confirmed correctness/security risks

**SINGLE_SOURCE_BIASED_FILTER_AND_UNBOUNDED_BROWSER (P1).** Python Selenium scrapes CollegeScholarships.org listing/detail pages with fixed female filter, brittle XPath and two browser processes. It writes a wholesale MongoDB replace_one on collected rows; no browser cleanup or complete-source marker in inspected script and an HTTP first-party issuer check is absent. Statements about authentication and errors apply to inspected code; deployed rule configurations and exploitability were not tested.

## 5. Verification and external-authority constraints

Extracted scholarship records, self-reported applicant states and program pages do not establish a current official funded offer. Preserve issuer URL, source excerpt, collection timestamp, intake cycle and formal deadline/eligibility checks.

## 6. Cross-repository transferable methods

Separate source collection from candidate-eligibility verification and personal applicant state. Repository supplies useful workflow concepts only after authorization, typed claim evidence and integrity controls.

## 7. Verdict

**P1: adopt no production code until SINGLE_SOURCE_BIASED_FILTER_AND_UNBOUNDED_BROWSER corrected.** Preserve privacy of applicant artifacts and never infer current funding from old metadata.

## 8. Tests and open questions

No CI execution, source owner contact, candidate document read, live scraping or adversarial tests performed. Add tests for authentication, conflicting source deadlines, data replacement, dedup, persistent state, empty/incomplete HTTP pages and precision of extraction.
