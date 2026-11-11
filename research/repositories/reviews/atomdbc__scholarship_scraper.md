# atomdbc/scholarship_scraper — deep static repository review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [b53d5decb4bc2ae4f603ed340adb7f606eaf80ad](https://github.com/atomdbc/scholarship_scraper/commit/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad)  
**Review state:** DEEP_REVIEW_DOCUMENTED — static source inspection; runtime tests not executed.  
**Category:** multi-source scholarship scraping prototype.  
**Verdict:** reject as-is; retain only isolated research ideas.  
**Primary risk:** unauthenticated arbitrary-URL browser scraping with destructive public API routes.

## 1. Purpose and scope

A 2024-era prototype for discovering scholarship pages from submitted URLs, classifying links, scraping page content with Playwright, extracting structured scholarship data through OpenAI, and presenting results in a Next.js dashboard. It contains a FastAPI backend, SQLAlchemy persistence, a background worker, an OpenAI-based extraction service, frontend pages and a committed SQLite database.

Latest observed commit: 19 November 2024. The tree contains 69 files. No test suite, CI workflow or license file was found. The README contains only a project heading and does not document deployment, trust boundaries or operating limits.

## 2. Architecture and dataflow

The active entry point creates a FastAPI application. API routes accept individual URLs, bulk URLs and uploaded files; create scraping tasks; expose task progress and scholarship records; export data; and provide a bulk-delete route. A worker polls pending/failed tasks, opens a Playwright browser, extracts links, classifies candidate pages, fetches scholarship pages, asks an LLM to structure the content and persists results.

The frontend includes dashboard, upload, scholarship detail and export pages. The backend data model contains scraping tasks, per-task progress, scraped links and scholarship records.

## 3. URL ingestion and browser execution

The API accepts user-supplied `HttpUrl` values and uploaded URLs. The imported `validate_url` helper only checks for a non-empty scheme and network location, and the inspected route does not call it as an admission policy. It does not enforce HTTPS, an institution allowlist, redirect validation, DNS resolution or private/link-local address blocking.

Playwright navigates submitted and discovered URLs. There is no demonstrated SSRF boundary preventing navigation to loopback, private network, cloud metadata or internal service addresses. This is a serious issue because the backend runs the browser with the server's network reachability.

Bulk URL input has no clear maximum item count. Public task creation can therefore trigger unbounded browser and model work.

## 4. API authorization and destructive operations

The inspected FastAPI entry point configures permissive CORS and mounts the API router without authentication dependencies. The task-creation, upload, status, export and deletion routes do not show a user authorization boundary.

The API includes a `DELETE /delete_all` route that deletes all scholarship records. It is not protected by an authenticated admin dependency in the inspected implementation. An exposed deployment therefore permits unauthenticated destructive requests.

The application should not be deployed to a public network in this state. CORS configuration does not replace authentication or authorization.

## 5. Worker, persistence and idempotency

The background worker processes tasks with `asyncio.gather` while sharing a synchronous SQLAlchemy session across concurrent coroutines. Session ownership is not scoped per task. The application lifespan obtains a database session through `next(get_db())` instead of managing the generator/dependency lifecycle explicitly.

The inspected persistence path creates scholarship records without a stable cross-run uniqueness contract. Repeated scraping can create duplicates. The progress model uses a one-to-one relationship without a corresponding database uniqueness constraint; retry logic creates another progress record rather than clearly resetting the existing one.

Task status and progress are not a durable, fenced job-lease design. Multiple worker processes or restarts can lead to duplicate execution or ambiguous progress state.

## 6. LLM extraction and factual quality

The AI service uses free-form JSON generation and regular-expression cleanup rather than a strict structured-output schema with field-level validation. Page text is untrusted input and is passed to the model without a robust prompt-injection boundary. The model's confidence score is not an independent verification result.

The extracted output does not preserve exact source spans or a source snapshot hash for each field. Funding and amount parsing are insufficiently typed for reliable scholarship comparisons. The code also returns an `application_url` from extraction, while the persistence preparation path reads a different `url` key with the source URL as fallback; the extracted application URL can therefore be lost and replaced with the page URL.

The resulting records cannot safely establish funding coverage, current cycle, international eligibility or an applicant's actual eligibility.

## 7. Operational and validation gaps

The project has no visible automated test suite or CI workflow, no license file and no production deployment contract. Browser execution and LLM calls have cost and timeout implications, but the inspected implementation does not demonstrate a global task budget, per-domain rate limits or durable retry scheduling.

The committed SQLite database is a local artifact, not proof of an independently validated or current scholarship dataset. No runtime, live-source, API security, SSRF, concurrency or model-output tests were run in this review.

## 8. Transfer decision for PhD Atlas

Do not reuse the service as-is. It is useful as an example of a browser-driven discovery pipeline, but the architecture needs a strict separation between untrusted URL discovery, safe fetch execution, extraction candidates and verified claims.

If rebuilding the useful pieces:
- use an allowlisted source registry and redirect/DNS/IP validation;
- isolate browser workers in a network sandbox;
- require authentication and authorization for every task and destructive endpoint;
- impose per-user, per-source and global request/model budgets;
- use typed extraction schemas and claim-level evidence spans;
- use idempotent source-observation IDs and append-only verification decisions;
- isolate each worker's database session and implement lease/fencing semantics;
- add tests for SSRF, malicious pages, prompt injection, duplicate runs, task retries and deletion authorization.

**Overall decision:** reject as a production reference. Reuse only the high-level idea of browser-based page acquisition after redesigning the security, persistence and evidence layers.

## Pinned implementation evidence

- [FastAPI entry point](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/main.py)
- [API endpoints](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/api/endpoints.py)
- [Worker](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/scraper/worker.py)
- [HTML parser](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/scraper/parser.py)
- [AI extraction service](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/services/ai.py)
- [Schemas and models](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/models/schemas.py)
- [Database session lifecycle](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/core/database.py)
- [URL helper](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/utils/utils.py)
- [Configuration](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/core/config.py)

**Validation boundary:** source files and repository metadata were inspected. No test, Playwright, OpenAI, database migration, deployment or security execution was performed.
