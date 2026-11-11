# Deep static review — Janjs/Web-Scraping-PhD-positions

## 1. Repository identification
- **Repository:** https://github.com/Janjs/Web-Scraping-PhD-positions
- **Pinned revision:** `429a7761f34bfd4b1d69de125cefe39dc1922d01`, 2021-10-03; inspected 2026-11-12. Git tree contains one Python source file, no README, package metadata, license or test suite. GitHub API returned no issues or PRs in the inspected snapshot.
- **Scope:** historical one-source doctoral-vacancy scraper for the former EU Marie Curie job-page layout. All tracked source content was inspected; **not executed**, and the 2021 endpoint was not tested for current availability.

## 2. Problem and assumptions
The script targets positions marked `Computer science` and `First Stage Researcher (R1)` on a single historical European job-search HTML page, then emails extracted fragments. Assumes a locally installed Selenium Chrome driver with a developer-specific absolute path, stable HTML CSS classes, a valid Gmail SMTP password entered interactively and that the first loaded page contains all relevant entries. A listed job is not proof of a current MSCA-funded doctoral contract, international applicant eligibility or an open application window.

## 3. Implementation and actual data flow
The entire [single-file implementation](https://github.com/Janjs/Web-Scraping-PhD-positions/blob/429a7761f34bfd4b1d69de125cefe39dc1922d01/webScrapingMarieCuriePhDs.py) defines `webScrap` and `sendEmail`. `webScrap` opens the historical EU job page with `webdriver.Chrome`, sleeps a fixed two seconds, parses browser HTML with BeautifulSoup and `lxml`, selects `div` classes starting `jobOp views-row`, then indexes the first two `p.jobField` values to extract discipline and R1 status. Matching blocks are kept as HTML elements rather than normalizing title, employer, location, deadline, stipend or source URL. `sendEmail` concatenates `prettify()` HTML into an email and uses SMTP_SSL on port 465 with manually entered password and fixed sender/recipient addresses. The main block runs scraping immediately followed by sending.

## 4. Defects, security and operational failures
1. A hard-coded user-machine Selenium driver path prevents portable or containerized execution. No driver management, browser version handling, headless mode, retries, page limits, or test fixtures.
2. `job_types[0].strong.text` and `job_types[1].strong.text` assume both fields and `strong` children always exist; a small HTML change raises an exception. Fixed `time.sleep(2)` does not ensure page or AJAX completion.
3. No pagination, stable vacancy identity, deduplication, date extraction, salary/funding checks, posted-versus-deadline distinction, provenance snapshots or official employer link verification.
4. SMTP addresses are hard-coded; the password is requested via `input()` rather than non-echoing credential capture, and SMTP errors are not isolated from the crawl. **Do not copy source addresses or use user credentials for reproductions.**
5. A fixed legacy page target and 2021 source snapshot make current vacancy and employer claims unreliable. No source tests, CI, releases or open issues/PRs were observed through inspected GitHub metadata. Absence of issues is not proof of correct behavior.

## 5. Applicability to a 2026/27 research pipeline
Only the simple concept of category-specific discovery is transferable. Rebuild with official contemporary portal/API discovery, enforce TLS, explicit robots/Terms review, deterministic HTML/API fixtures, schema-validated canonical fields, stable source IDs, temporal confidence, source-to-employer verification and separate authorized notification. A vacancy can be surfaced as an unverified **lead**; do not infer a funded award or accepted application.

## 6. Comparison and lineage
[PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker) has broader multi-board parameterization but its reviewed implementation includes TLS-validation and unsafe `eval` defects. [Academic Job Digest](https://github.com/BaseLayerAI/academic-job-digest) provides more advanced adapter/persistence designs but similarly cannot certify eligibility. The present legacy script is only a one-page Selenium extraction example, **not independent evidence** of current MSCA opportunities. No derivative-code relationship to these comparators was established.

## 7. Verdict
**REJECT AS AN OPERATIONAL SOURCE; retain as historical scraper anti-pattern.** High confidence in source-level parsing, hard-coded path, missing schema/expiry/retry, and password-handling issues because the full single-file implementation was read. Current page availability, exploitation and vacancy accuracy were not tested. Source code has no observed license grant; do not copy it.

## 8. Evidence, validation gap and next checks
Primary proof is the immutable [2021 source](https://github.com/Janjs/Web-Scraping-PhD-positions/blob/429a7761f34bfd4b1d69de125cefe39dc1922d01/webScrapingMarieCuriePhDs.py) and [commit history](https://github.com/Janjs/Web-Scraping-PhD-positions/commits/429a7761f34bfd4b1d69de125cefe39dc1922d01). The file is the complete tree at `429a7761f34bfd4b1d69de125cefe39dc1922d01`. No runtime, live site access, SMTP execution, messages or secrets were used. Any modern replacement requires official EU/MSCA source discovery, source authorization, synthetic tests for missing fields and pagination, and independent institutional funding/deadline checks. This review is a **full-tree static report, not runtime certification**.
