# ledmands/education_job_scraper — deep static ETL and alerting audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/ledmands/education_job_scraper | **Pinned commit:** [`9304bc99e92eb68dfe3c7ef8c655f48090c61ab3`](https://github.com/ledmands/education_job_scraper/commit/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3) | **State:** DEEP_REVIEW_DOCUMENTED (static) | **Decision:** reference staged extraction/notification architecture, reject code as a reliable doctoral vacancy feed.

## 1. Scope and intent

A 2025 Python project to scrape three U.S.-centered education/academic job boards—AcademicJobsOnline, Chronicle of Higher Education Jobs and NAAEE—into separate SQLite tables, extract fresh rows into plaintext files and send those summaries by SMTP. README specifies a manual database setup and `run.py` imports `scrape.py`, `extract.py` and `send.py`. The repository is a general academic employment monitor, not limited to funded doctoral vacancies, scholarships or official campus admission decisions.

The tree includes small parsers, a SQLite database and local mail configuration placeholders; no automated tests or CI workflow was identified.

## 2. Actual data flow and model

`scrape.py` parses board-specific HTML; it writes separate tables `AcademicJobsOnlineJobs`, `ChronicleHigherEducationJobs` and `NaaeeJobs`, with URL duplicates prevented by comparing incoming URLs to previously loaded table values. It sets AcademicJobsOnline incremental freshness using the most recent `PostedDate`, and the Chronicle module paginates a fixed number of pages.

`extract.py` reads rows newer than a rolling seven-day cutoff, formats them as text per source; `send.py` mails the three text files through SMTP_SSL, using local sender/recipient/password files. `run.py` orchestrates scrape→extract→send with configuration of 10 Chronicle pages and the seven-day report window.

The architecture cleanly separates acquisition, persistence, report formatting and outbound delivery, but **posting date is not application deadline** and a job board hit is not proof of a funded PhD slot.

## 3. Deterministic AJO date parsing defect (P0)

Inside `scrape_academic_jobs_online()`, the fallback cutoff is the literal string `"20250301"` when the table is empty; if rows exist, the query result is a one-element tuple converted with `str(cutoff_date)`. In either case, the code then applies `cutoff_date = cutoff_date[1:9]` and parses with `datetime.strptime(..., "%Y%m%d")`.

For the empty database the slice discards the first digit, returning seven characters `"0250301"`. For a tuple string such as `"('20250301',)"` the slice begins with a quote. Neither matches an eight-digit `YYYYMMDD` string. Thus the AJO source path can fail before processing any postings, rather than correctly establishing a date boundary. Store a typed YYYYMMDD integer/string, use tuple element `row[0]`, and parse after explicit format validation.

## 4. Additional correctness and resilience issues

- The Chronicle parser obtains `listing_response` for each detail URL but checks the **parent listing page's `response.status_code`** in the detail error branch. Failed detail requests can flow into HTML parsing and unpredictable empty fields.
- Pagination mutates the Chronicle URL by slicing `url[0:42]` and appending page numbers, depending on a fixed-length URL string rather than `urljoin` or query parameters.
- AJO and Chronicle requests have no explicit timeout, backoff or bounded retry and parse class names that can drift.
- Broad `except:` clauses suppress parse errors and can write incomplete records. Existing URL sets are not refreshed after inserts during one crawl, creating within-run duplicate attempts; no globally unique opportunity/edition ID exists.
- The SQLite tables do not record last-verified timestamp, source hash, official vacancy status, degree, funding, international eligibility or recruitment cycle. There is no per-source completeness marker, so partial crawler failures cannot be distinguished from zero new opportunities.

## 5. Delivery, secrets and applicant-state boundary

Mail credentials are read from local plaintext files. They are intended for a designated recipient, but the inspected source does not document secure secret storage, mail-sending authorization gates, retry/idempotency or recipient allowlisting. The script sends whatever rows were extracted regardless of their official funding or current opportunity relevance.

A researcher should not infer any applicant submission, PI approval, offered scholarship, or contact permission from a notification email. For a private workspace, email delivery should use explicit user opt-in, safe credentials and durable sent-message receipts.

## 6. Deployment and evidence limitations

The README supplies SQL table creation instructions rather than a versioned migration or schema validator. There are no automated regression fixtures for date parsing, altered HTML, empty source results, paging or failed SMTP sends. The project code is sufficient to identify the critical date-slicing and wrong-status-response errors without executing live board requests.

The jobs span education employment categories; filtering must distinguish postdoctoral/faculty postings, doctoral employment, assistantships and ordinary professional jobs before counting available funded PhD roles.

## 7. Transfer and corrective architecture

Retain a staged source-adapter→SQLite→report→notification design, but:
1. Parse cutoff and posted dates through typed source fields and test initial empty databases.
2. Enforce response status checks on the correct HTTP response, timeouts and safe URL/redirect policies.
3. Use per-source unique IDs and lifecycle snapshots; do not infer closure from missing rows on partial runs.
4. Store actual application-deadline and applicant eligibility separately from posted date.
5. Capture official employer URL, funding terms and verification state before generating action-worthy alerts.
6. Use securely stored mail credentials, recipient consent, idempotent deliveries and audit events.
7. Add fixtures for DOM drift, incomplete pages, duplicate retries and date ambiguity.

## 8. Pinned implementation evidence

- [README and source-specific schema](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/README.md)
- [Three scrapers and cutoff defect](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/scrape.py)
- [Database to text export](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/extract.py)
- [Email delivery and TLS SMTP](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/send.py)
- [Orchestration and fallback cutoff](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/run.py)

**DEEP_REVIEW_DOCUMENTED — static only.** Source-level correctness defects and architecture were inspected at the pinned revision. No live scraping, external job validation, email send, database execution, source-terms assessment or security exploit was performed.
