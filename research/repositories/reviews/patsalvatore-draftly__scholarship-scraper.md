# patsalvatore-draftly/scholarship-scraper — Go crawler and HTTP control-plane audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/patsalvatore-draftly/scholarship-scraper  
**Repository ID:** 947007040  
**Pinned commit:** [053c315c81437c4ced52a11c6f1a89de581a70a7](https://github.com/patsalvatore-draftly/scholarship-scraper/commit/053c315c81437c4ced52a11c6f1a89de581a70a7)  
**Review state:** DEEP_REVIEW_DOCUMENTED — complete 387-line main.go inspected statically; HTTP exposure and upstream execution NOT_TESTED.  
**Verdict:** BLOCK operational reuse due to unauthenticated SQL/control endpoints.

## 1. Purpose and scope
A small Go/Colly/SQLite service for fetching Next.js page JSON from an internal list of College Board BigFuture scholarship URLs. It retains an URL/status queue and scraped page content in SQLite; it does not have a PhD admissions eligibility parser, PhD funding/fee classifier, or corroborated opportunity dataset.

## 2. Source and architecture
The pinned repository contains eight files (Go module/lock, one main.go, Docker/Fly deployment configuration and GitHub Actions workflow). main.go configures SQLite WAL with a single connection and two tables: urls and scraped_data. The scrape coroutine enumerates queued URLs, visits each via Colly, and extracts text from a Next.js data script. One callback wraps inserting data and marking a URL complete in a SQL transaction. It uses a Colly delay/random jitter and context cancellation. An HTTP chi router exposes /sql, /backfill, /start and /stop in addition to a root health response.

Evidence: [main.go](https://github.com/patsalvatore-draftly/scholarship-scraper/blob/053c315c81437c4ced52a11c6f1a89de581a70a7/main.go), [Dockerfile](https://github.com/patsalvatore-draftly/scholarship-scraper/blob/053c315c81437c4ced52a11c6f1a89de581a70a7/Dockerfile).

## 3. Critical trust-boundary failures
- **Raw SQL execution endpoint:** GET /sql accepts the query-string parameter q and passes it directly into db.Query(q). No authentication, authorization, query language restriction, or statement allowlist appears in the inspected router. SQL statements can access database contents and potentially alter state depending on driver and query semantics. This is an immediate block for any network-exposed deployment.
- **Unprotected control plane:** GET /start and GET /stop schedule or cancel scraping, and GET /backfill imports local JSON files into the DB. These state-changing endpoints are unauthenticated GET operations, allowing unauthorized process-control actions and violating safe HTTP method semantics.
- **Concurrent-state race:** isRunning and _cancel are shared globals modified by handlers, the scraper goroutine and error callbacks without consistently using a mutex or atomic primitives. Repeated starts/stops may race, even though a mutex guards some SQLite writes.
- **Unbounded database results:** /sql collects full result sets in memory for JSON response, with no enforced row/query size limit.
- **Fixed service port:** main.go obtains an environment PORT value but constructs http.Server with a hardcoded 8080, so runtime port configuration is ignored.
- **Source fidelity:** INSERT OR IGNORE means an already-scraped URL will not automatically replace stale text. The status row is marked complete without field-level proof of a valid deadline or current eligibility.

## 4. Data and audit gaps
The DB retains URL, scraped script content, status code, timestamp and processing status, but lacks document identity, version hash, scholarship title/award amount/deadline, funding restrictions, international eligibility or source authority. Backfill imports JSON's programTitleSlug field and prepends a fixed BigFuture path. The external source cannot be assumed to cover funded doctoral research positions or international applicants.

## 5. Execution and maintainability
The Go module imports chi, Colly and go-sqlite3; a Docker/Fly deployment path exists but runtime compatibility, network isolation and access control were not tested. No test files, security lint or e2e fixtures were present in the eight-file tree. Several error paths use log.Fatal in code serving HTTP requests, which may terminate the whole process rather than fail an individual job. Cancellation is not passed into the scraper SQL transaction, which uses context.Background.

## 6. Relative merits
Transactionally recording URL payload + status is stronger than a plain CSV append, and low-concurrency crawler design is practical for respectful polling. However, the exposure of arbitrary SQL and mutable control endpoints is unacceptable for a hosted service.

## 7. Transfer rules
For PhD Atlas, decouple crawler workers from a private control API; require authenticated RBAC and CSRF-safe methods, and remove arbitrary SQL from HTTP entirely. Use a typed queue with retry/lease semantics, canonical source URL and immutable document revisions, idempotent claim extraction, bounded results and safe cancellation. Separate source observation from verified scholarship eligibility, date and award terms. Test hostile query/control requests in an isolated fixture environment before deployment.

## 8. Review decision
**DEEP_REVIEW_DOCUMENTED — BLOCK.** Whole main.go and repository file tree inspected. Not performed: compile, Docker/Fly deploy, live crawl, SQL endpoint probing, concurrency/race test, upstream database-content access or any application action. Findings describe static source design, not a confirmed exposed service.
