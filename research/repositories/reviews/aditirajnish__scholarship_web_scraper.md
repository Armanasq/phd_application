# aditirajnish/scholarship_web_scraper — source-pinned deep static review

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/aditirajnish/scholarship_web_scraper | **Pinned source:** [`4786fa11d7871e37f78003babd7de5abe82d2c0f`](https://github.com/aditirajnish/scholarship_web_scraper/commit/4786fa11d7871e37f78003babd7de5abe82d2c0f) | **State:** DEEP_REVIEW_DOCUMENTED (static code) | **Verdict:** historical scholarship recipient extraction only; reject unsafe HTTP/TLS practices.

## 1. Purpose and data grain

A 2020 Python/Requests/BeautifulSoup scraper for the Schulich Leaders university award recipient archive, **not** a current doctoral-funding vacancy discovery system. The tracked tree has 10 entries including main.py, verify.py, requirements.txt, README, MIT LICENSE, and four emitted example text files for university/year combinations (2019–2020). It extracts names, program text and selected university from profiles of scholarship recipients, rather than offer eligibility/deadline/tuition terms.

## 2. Pipeline

`verify.py` contains fixed Canadian participating-university names and years 2012–2020 plus an empty all-year option. `main.py:get_link_suffixes()` fetches `/scholars/{year}`, selects HTML `span.field-content a` anchors, and builds scholar-profile paths. `get_page_info()` fetches each profile, selects the `person--selected-by` university, `person--title` recipient and `person--program`; it filters by university, returns a simple text block, and `write_file()` saves a per-institution/year file.

This is an ETL example for a historic *recipient cohort*. Award recipients are outcomes; they are not a denominator of qualified applicants and cannot establish a success rate, stipend offer, or scholarship available to this user.

## 3. Transport-integrity and fetch faults

Both Requests calls use `verify=False`, disabling TLS certificate verification. This permits undetected transport interception or content substitution; it is not a safe production source-ingestion pattern. Calls also omit timeouts, retry/backoff, content-type/size checks and final-URL allowlisting.

`get_page_info()` dereferences `university_div.text` without a null check. A changed HTML template or missing profile field can abort the batch. Link suffixes are concatenated directly to the base domain and require validation; no safe relative-URL normalization contract is demonstrated.

## 4. Data quality and identity

University matching is an exact case-sensitive string comparison against a static configured label. Name variants, bilingual names, redirects and unstructured program labels can silently cause missing rows. `write_file()` overwrites the annual file with no version history or source revision metadata. No stable scholar ID, source URL per row, extraction confidence, fetch status, timestamp or provenance span is persisted.

The examples consist of names/programs only; no scholarship amount, program level, funding duration, donor eligibility or official current policy. Scraping award winners is conceptually distinct from seeking open awards and raises separate data-minimization considerations.

## 5. Temporal and institutional boundary

`verify_year()` only accepts 2012–2020; the committed hardcoded example uses 2020 and University of British Columbia. GitHub's repository history was last observed in 2020. Do not label any extracted student as a current scholarship recipient or infer a funded 2026/27 PhD opportunity from this archive.

Schulich Leaders is a specific Canadian award program; its recipient-page HTML format and degree focus cannot be generalized to global doctoral employer postings.

## 6. Security, ethics and reproducibility

Requirements pin the 2020-era Requests/BeautifulSoup dependencies. The code contains no test suite, CI, schema migration, official-source policy, retention rules or personal-data permission assessment. It writes recipient names into plain text. Publicly listed scholarship recipients can be legitimate research subjects in some contexts, but permission/terms, purpose limitation and individual privacy still apply; these names are unnecessary for this PhD research, so none are reproduced.

The optional all-year mode may require its own source-page schema; no runtime tests or live provider access were performed.

## 7. Transferable abstractions

Retain only the source-specific adapter structure and an explicit university/year selection gate. For source-backed funding research, rebuild with HTTPS verification, allowed hosts, redirects and bounded requests; source URL and snapshot IDs per observation; validated extraction schemas; normalized institutions and degree types; clear distinction between award winner and currently available funded doctoral role; and tests against captured authorized HTML fixtures.

No third-party recipient lists or proprietary source data should be copied into the canonical opportunity register without justification.

## 8. Pinned evidence and validation

- [README](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/README.md)
- [Collector and TLS configuration](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/main.py)
- [University/year selection](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/verify.py)
- [Dependencies](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/requirements.txt)
- [Historical output example path](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/schulich_text_files/schulich_university_of_british_columbia_2020.txt)

**DEEP_REVIEW_DOCUMENTED — source-level only.** The complete small Python implementation and repository inventory were inspected, without executing network calls, independently verifying current provider rules, reusing personal identities or testing TLS failures.
