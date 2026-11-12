# Khayrulbuet13/AcademicJobScraper — deep static Python academic-job adapter audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/Khayrulbuet13/AcademicJobScraper | **Pinned revision:** [`13981e7dd13cab8a56a566b677833959b99f440f`](https://github.com/Khayrulbuet13/AcademicJobScraper/commit/13981e7dd13cab8a56a566b677833959b99f440f) | **State:** DEEP_REVIEW_DOCUMENTED (static source) | **Decision:** adapt source-specific extraction interface after adding source, security, lifecycle and tests.

## 1. What it implements

A pip-installable Python package (`academicjobscraper`) with a CLI that scrapes an academicjobsonline.org listing URL and each detected job-detail link, extracts organization, job title and description, and filters descriptions for user-supplied research keywords. README provides import and CLI examples; the package publishes `job_links.csv`, `jobs_data.json` and `relevant_jobs.csv`. The tracked tree contains package code, packaging files, an example, notebook, built wheel/tarball and documentation graphics. Last observed GitHub update: 2025-02-09. MIT license present.

The tool does **not** implement official 2026/27 scholarship validation, local candidate eligibility, applications or a verified funded-PhD feed.

## 2. Extraction and classification dataflow

`AcademicJobScraper.scrape(url)` fetches the given listing page, collects anchor `href` values containing `/ajo/jobs/`, omits `/apply` links, writes the links to CSV, sequentially fetches detail pages with a one-second pause, and persists title/institute/description/canonical link as JSON. `_filter_jobs()` scans each description for case-insensitive substring matches of provided keywords and emits a three-field CSV of title/company/link.

The crawler's notion of relevance is substring presence in a job description. It does not distinguish a tenure-track faculty position from a doctoral employment offer, a historical posting from an open position, or paid salary from unfunded graduate admission.

## 3. URL and fetch security boundaries

The CLI accepts an arbitrary initial `url` and follows unvalidated hyperlinks. No public-HTTPS requirement, hostname restriction, redirect/DNS/IP validation, content-size bound or URL normalization is enforced before `requests.get`. For a server-side web service this would constitute an SSRF risk; here it remains an unsafe fetch surface in a local user-launched scraper.

Both initial and detail `requests.get` calls omit an explicit timeout; hangs can stall an entire crawl indefinitely. There is no bounded retry/backoff, rate-limit interpretation or robots/terms gating. The code uses exact CSS/DOM structures that can change without warning.

## 4. Data identity, deduplication and temporal accuracy

The collector deduplicates URLs inside a single page by string equality, not by normalized canonical opportunity ID. `_extract_job_details` may take the page's canonical link element, which can point to a general site URL if the source template changes. The dataset overwrites output files on each run and has no first/last seen timestamps, cycle, current status, source snapshot hashes or historical revisions.

No deadline, posted date, timezone, salary/stipend, international fee, contract type, source-claim span or official recruitment approval is extracted. A keyword hit cannot be promoted to `OPEN_VERIFIED` or `FUNDED`. Repeated full scans also cannot detect whether a missing result means a closed job versus pagination/API failure.

## 5. Packaging and deployment quality

`cli.py` accepts required URL and keywords and optional filenames; `setup.py` declares setuptools entry point, Python >=3.6 and Requests/BeautifulSoup requirements. But setup metadata still contains placeholder author email, project URL and author name, which reduces package provenance confidence. The repository commits built `.whl` and `.tar.gz` artifacts, but their reproducibility against source was not verified.

No dedicated test suite, CI run or deployment contract was found. The notebook and examples are usage references rather than empirical source parser tests.

## 6. Failure and output behavior

The detail fetch handler catches broad exceptions, logs to stdout and silently skips failed pages, making a partial scrape appear as an ordinary list of results. The CLI process reports counts of “relevant” jobs without preserving failed source counts or an explicit completeness ratio. The raw JSON has no crawl run identity to trace which opportunities were missed.

The `_filter_jobs()` code only scans `job['description']`; a relevant position with a sparse description and informative title can be missed. Conversely, generic “AI” in a faculty posting can be accepted despite not being a PhD.

## 7. Transfer into research framework

Useful: explicit source adapter, separate raw and filtered output, keyword filters, CLI parity and simple job-detail extraction. Required for research-grade use:
1. Restrict approved source domains, HTTPS and redirects, and honor terms/rate limits.
2. Capture per-page fetch metadata, source revision/hash, and current-cycle exact evidence.
3. Distinguish `faculty`, `postdoc`, `PhD employed`, `scholarship`, `unfunded admission`.
4. Implement stable official posting identity, canonical dedup and historical change tracking.
5. Extract exact deadline/funding/eligibility claims with official employer confirmation.
6. Add regression fixtures, missing-field guards, fetch failure logs, source completeness and bounded retries.
7. Test packaging metadata and versioned reproducible builds before installing built distributions.

## 8. Pinned source references and validation limits

- [README](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/README.md)
- [Actual scraper and filter](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/academicjobscraper/scraper.py)
- [Command-line wrapper](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/academicjobscraper/cli.py)
- [Setuptools and package metadata](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/setup.py)
- [Example](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/example.py)
- [Packaged requirements](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/requirements.txt)

**DEEP_REVIEW_DOCUMENTED — static.** No source web pages were scraped, no package installed, no wheel verified, no live academic vacancies checked, and no CI/security execution performed.
