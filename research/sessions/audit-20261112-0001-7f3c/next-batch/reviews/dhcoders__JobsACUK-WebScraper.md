# dhcoders/JobsACUK-WebScraper — single-file implementation review

- Repository ID: 764164602
- Default branch: main
- Inspected revision: cdff22fd58c1542dbda23690f4c1ebe37e46fab8
- Tree: two entries (.gitattributes and jobscraping.py)
- Review state: DEEP_REVIEW_DOCUMENTED (complete static review of the only source file; runtime NOT_TESTED)
- Confidence: High for code-level defects; no live Jobs.ac.uk response verified

## 1. Purpose and workflow

The script is a local polling utility for a user-supplied Jobs.ac.uk search URL. It requests the page, parses job cards with BeautifulSoup, prints title/employer/salary/deadline fields, and repeats after a user-selected refresh interval. It is not a reusable academic vacancy platform: the URL, CSS selectors, output fields, and parsing assumptions are site-specific.

## 2. Implementation findings

- The script requests a refresh interval in hours but calculates refresh = input * 60 and passes that value to time.sleep(), which expects seconds. The actual interval is one-sixtieth of the requested duration in hours (for example, a requested 1-hour interval becomes 60 seconds).
- It collects all deadline elements from the page, then loops over every deadline inside each job-card loop. The due date is overwritten repeatedly, so each job is assigned the final deadline found on the page rather than its own deadline.
- If no deadline elements exist, duedate is never assigned before it is printed.
- If the HTTP response is not 200, jobshtml is never assigned, but parsing continues and references it.
- requests.get() has no explicit timeout, retry/backoff, status raise, or connection policy.
- CSS selectors are hard-coded to the current Jobs.ac.uk markup and have no parser fixtures or fallback selectors.
- The script does not extract a canonical job URL, description, institution country, funding evidence, supervisor, eligibility, or application deadline timezone.
- There is no canonical deduplication, persistent state, new/changed detection, alert delivery, or source provenance. The same page is reprinted each loop.
- The infinite loop has no structured shutdown, logging, or error recovery.
- The code imports BeautifulSoup and lxml but the repository has no requirements file or environment instructions.

## 3. Maintenance and disposition

The repository contains no README, license, tests, CI, configuration, or deployment instructions. The full source file was inspected; no runtime execution was performed.

**Disposition:** retain as a historical single-source scraper example only. Do not adopt its refresh scheduling, deadline association, HTTP handling, or data model. A modern adapter should use per-card parsing, timezone-aware dates, bounded HTTP retries/timeouts, fixtures, canonical job identity, and evidence-backed funding/location fields.

Evidence:
- [Repository](https://github.com/dhcoders/JobsACUK-WebScraper)
- [Complete script](https://github.com/dhcoders/JobsACUK-WebScraper/blob/cdff22fd58c1542dbda23690f4c1ebe37e46fab8/jobscraping.py)
