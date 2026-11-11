# dhcoders/JobsACUK-WebScraper — source-pinned static audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/dhcoders/JobsACUK-WebScraper  
**Pinned commit:** [cdff22fd58c1542dbda23690f4c1ebe37e46fab8](https://github.com/dhcoders/JobsACUK-WebScraper/commit/cdff22fd58c1542dbda23690f4c1ebe37e46fab8)  
**Repository ID:** 764164602  
**Review state:** DEEP_REVIEW_DOCUMENTED (complete single-file static review; runtime NOT_TESTED).  
**Disposition:** Reject as operational vacancy infrastructure; retain only the concept of a narrow Jobs.ac.uk source adapter.

## 1. Purpose and actual scope

This is a command-line polling script for a user-provided Jobs.ac.uk search-results URL. It scrapes the visible first page and prints job title, institution, salary text and deadline. It does not support multiple source adapters, PhD-only qualification, nationality/tuition eligibility, source lineage, or an application workflow. It cannot establish that a vacancy is funded or still open.

## 2. Architecture and complete source inventory

The pinned repository tree contains two files: .gitattributes and jobscraping.py. The Python source imports requests, BeautifulSoup and lxml; takes a URL and desired refresh interval from input(); fetches HTML through requests.get(); selects job-card and date elements using CSS class names; prints text; and sleeps in a while True loop. No README, package requirements, tests, CI workflow, application database, or LICENSE file appears in the tree.

Source: [jobscraping.py at pinned commit](https://github.com/dhcoders/JobsACUK-WebScraper/blob/cdff22fd58c1542dbda23690f4c1ebe37e46fab8/jobscraping.py).

## 3. Data flow and parsing contract

Input: one external search-results URL and one integer specified as hours. The script makes one HTTP GET per loop, parses elements with classes j-search-result__text, j-search-result__date-span and related classes, then extracts a title, employer and salary text from each job result. It separately collects all deadline nodes from the entire page. Output is printed to stdout only; no job URL, employer ID, query timestamp, source snapshot, row identity, funding classification, eligibility claim, or timezone is persisted.

## 4. Source-verified correctness defects

- **Interval unit:** The requested interval is described as hours, but refresh = int(refresh_raw) * 60 is passed directly to time.sleep(), which expects seconds. A requested one-hour delay becomes 60 seconds, 60 times more frequent than requested.
- **Deadline misassociation:** Every job card iterates over the complete page-level deadline list and overwrites duedate repeatedly. Consequently, each job is printed with the last deadline on the page, not its own closing date.
- **Unbound data:** When the HTTP status is not 200, jobshtml remains undefined and HTML parsing continues. If deadline nodes are absent, duedate remains undefined.
- **Missing child nodes:** Calls such as ads.find('a').text and ads.find('div', class_=...).text assume required descendants exist; malformed cards fail rather than producing explicit missing fields.
- **No bounded request controls:** requests.get(url) has no explicit timeout, retry/backoff, rate-limit awareness, or exception recovery; the infinite loop can terminate on network or parser errors.
- **No temporal semantics:** The deadline is an unparsed string with no locale, timezone or cut-off information. It is not a verified application deadline.

These are direct static observations. Live selector compatibility has not been verified.

## 5. Quality, provenance and maintenance

GitHub metadata reports a 2024 repository with a small two-file history. At inspection, no issues or pull requests were returned. No dependency lockfile, test fixtures, versioning, release pipeline, license, or maintainer source-policy documentation was found. Selector drift, link redirects, expired posts and duplicate vacancy listings are unhandled.

## 6. Security, privacy and operational risks

The CLI accepts an arbitrary URL but is not a multi-tenant network service, so it is not appropriate to classify this script as an exposed SSRF API. Its principal risks are wrong deadlines, uncontrolled polling and repeated output, with possible provider rate-limit or terms-of-use violations. It neither stores personal applicant data nor sends messages. Missing funding, fee and location verification blocks automated admissions decisions.

## 7. Comparison and reusable method

Compared with a multi-source crawler, this script has a simpler extraction surface but no evidence model or durable state. Reuse only a source-specific adapter boundary: input as a typed search request; extract one job card atomically with its own closing date and canonical link; normalize the date into a timezone-aware value; persist source revision, fetch time and selector version; add deduplication and a bounded retry budget. Validate with recorded HTML fixtures and a mock HTTP transport before running against a live board.

## 8. Disposition and limits

**Decision:** DEEP_REVIEW_DOCUMENTED, reject as-is for PhD Atlas. One source file was fully inspected, but upstream code was not executed; no runtime, current Jobs.ac.uk page, live position, provider permission or deadline was verified. Retain the report for source-adapter failure-mode design, not as evidence of available funded doctoral positions.
