# atomdbc/scholarship_scraper — full-stack implementation audit

- Repository ID: 293971225
- Default branch: main
- Inspected commit: b53d5decb4bc2ae4f603ed340adb7f606eaf80ad
- Repository tree: 92 entries
- Review state: DEEP_REVIEW_DOCUMENTED (static; runtime NOT_TESTED)
- Confidence: High for inspected source and architecture; no live scraping, database execution, or deployment validation

## 1. Problem and intended users

The project is a general scholarship-discovery platform. It accepts seed URLs or uploaded URL files, crawls pages, classifies links with an LLM, extracts scholarship fields, stores results in SQLite, and exposes a FastAPI API consumed by a Next.js dashboard.

The repository is not specifically a PhD admissions system. The five seed URLs in schools.csv are heterogeneous and include general student scholarship sources alongside a graduate-research route. The product does not enforce doctoral-level eligibility or distinguish a salaried doctoral employment contract from a scholarship, tuition waiver, stipend, or one-time award.

## 2. Architecture and data flow

### Backend

- FastAPI application and router in main.py and app/api/endpoints.py.
- SQLAlchemy models and SQLite database in app/models/schemas.py and app/core/database.py.
- Alembic initial migration for scraping tasks, progress, scraped links, and scholarships.
- Playwright-based dynamic browser worker in app/scraper/worker.py.
- Link parsing in app/scraper/parser.py.
- Async OpenAI link classification and GPT-4 scholarship extraction in app/services/ai.py.
- URL and file helpers in app/utils/utils.py.
- A long-running polling worker started during FastAPI lifespan.

### Frontend

- Next.js 13 application with dashboard, scholarship detail, URL upload, CSV upload, and export pages.
- API client in frontend/lib/api.ts.
- Dashboard components for status cards, scholarship table, and filters.
- The frontend API base URL is hard-coded to an HTTP endpoint rather than configured through a deployment environment variable.

### Intended flow

User URL or CSV upload -> ScrapingTask -> polling worker -> Playwright page -> link extraction -> LLM relevance classification -> Playwright detail-page visit -> HTML extraction -> LLM structured extraction -> SQLAlchemy Scholarship row -> dashboard API -> Next.js UI.

The design separates ingestion, persistence, and presentation. However, important state transitions and data mappings are incomplete.

## 3. Critical startup and dependency defects

- worker.py imports playwright.async_api, but requirements.txt does not declare Playwright. main.py imports the worker at application import time. A clean installation from the declared requirements can therefore fail before the API starts.
- No Playwright browser-install step, Dockerfile, docker-compose file, or reproducible deployment guide is present.
- README.md contains only a short project heading and does not document setup, required services, environment variables, browser installation, or worker operation.
- The project has no test directory or CI workflow.
- A SQLite database file is committed to the repository. Its binary contents were not opened; its freshness, provenance, and suitability as a reproducible seed are unknown.
- output.txt contains an older repository-tree snapshot and refers to a different migration layout from the current tree. It is stale development output, not a reliable architecture document.

## 4. Worker orchestration and state defects

- The worker polls every 60 seconds and selects pending/failed tasks. On success it sets next_run to a future time but also changes status to completed; completed tasks are not selected by the polling query, so the configured periodic re-scrape does not occur.
- On failure the task is marked failed, but next_run is not advanced. The same failed task can therefore be retried every polling interval without a bounded backoff.
- Settings such as MAX_RETRIES, RETRY_DELAY, SCRAPING_INTERVAL, SCRAPER_RATE_LIMIT, and WORKERS are declared but not consistently used by the worker. The actual retry and polling behavior is hard-coded.
- One SQLAlchemy Session is shared by concurrent scrape_url coroutines created with asyncio.gather. A synchronous SQLAlchemy Session is not safe for concurrent task use.
- The long-running worker obtains its DB session with next(get_db()) but does not retain the generator. Generator finalization can close the session immediately, leaving the worker to reuse a session outside the intended dependency lifecycle. Use an explicit sessionmaker/context per worker task. If startup fails before worker_task is assigned, the lifespan finally block can also reference an unbound local and mask the original startup exception.
- The ScrapedLink row is inserted before classification/extraction, but processed is never set True. If processing fails after insertion, a later run finds the existing URL and skips it, with no explicit retryable state.
- The worker visits each extracted scholarship link using the same Playwright page. After processing the links, it calls page.content() again to parse the main page; the page is now at the last visited detail URL, not the original task URL. This can cause the final detail page to be parsed as if it were the source landing page.
- There is no task claim/lease or row-level locking before work starts. Multiple application replicas can select and process the same pending task concurrently.

Positive patterns include a distinct task/progress model, dynamic browser rendering, a polling worker, and separate API/UI layers. They need correct state semantics and per-task session ownership.

## 5. SSRF, authorization, and resource boundaries

- The API has no authentication or authorization dependency on task creation, URL upload, scholarship deletion, or task deletion endpoints.
- CORS is configured broadly with wildcard origins and credentials. The app also binds to 0.0.0.0.
- URL validation checks for an HTTP(S) scheme and a network location but does not resolve or reject loopback, link-local, RFC1918, or cloud-metadata addresses.
- The worker uses Playwright to navigate user-supplied URLs and extracted links. There is no private-IP denylist, redirect revalidation, DNS-rebinding defense, or domain allowlist. This creates an SSRF boundary if the API is exposed to untrusted callers.
- File upload reads the complete uploaded file into memory and has no explicit size limit. Invalid-file HTTP exceptions raised inside the broad handler are converted into generic server errors.
- Destructive delete endpoints are reachable without an authorization check.
- There is no rate limit, per-user quota, crawl budget, or maximum extracted-link count.

Do not deploy this API publicly without authentication, strict URL/redirect/DNS validation, upload limits, network egress controls, rate limits, and authorization on destructive operations.

## 6. LLM extraction and evidence quality

### Link classification

LinkClassifier sends link text and URL to an OpenAI model to decide whether the link is scholarship-related. There is no durable classification rationale, source snapshot, cache, or human-review state. External page text is untrusted input and is not strongly isolated from prompt instructions.

### Scholarship extraction

ScholarshipAIProcessor sends extracted page text to GPT-4 and requests JSON fields for title, amount, deadline, field, degree level, eligibility, location, and application URL. The result is parsed with json.loads and no strict Pydantic/JSON-schema validation. The confidence score is generated by the same model and is not calibrated against a labelled evaluation set.

Important defects:
- Scraped page content is embedded in the model prompt without an explicit untrusted-content boundary or injection-resistant extraction protocol.
- Amount normalization recognizes dollar amounts but does not preserve a currency code, exchange-rate date, award period, or tuition-versus-stipend decomposition.
- Deadline extraction supports only a limited set of date patterns and has no timezone or cut-off semantics.
- The worker maps application_url using data.get("url", source_url), while the AI processor returns application_url rather than url. The extracted application link is therefore ignored and the source page URL is stored as the application URL.
- The AI processor returns normalized amount metadata, but the worker stores only display_amount in the amount field. Database columns for normalized minimum/maximum, amount type, and renewable status are not populated.
- The database stores an LLM confidence score and summary, but no evidence spans or source snapshots that justify individual fields.
- The parser primarily recognizes USD-style amounts, so international funding packages can be misread or lose currency semantics.

LLM extraction should propose typed claims, not certify that an opportunity is real, funded, current, or eligible.

## 7. Persistence and API contract defects

- Scholarship records have no canonical URL uniqueness constraint or source-alias model. Duplicate opportunities from different pages/providers can be stored.
- ScrapingTask URLs are indexed but not unique; exact-string checks in the API are vulnerable to normalization differences and concurrent duplicate submissions.
- ScrapingProgress is modeled as a one-to-one relationship, but task_id is not unique in the migration. Retry logic inserts another progress row instead of resetting or versioning the existing row.
- TaskProgressResponse omits fields such as success_count, fail_count, created_at, last_run, and next_run that are expected by the TypeScript frontend. Extra fields passed by the endpoint are not part of the declared response contract.
- The detailed task success_rate calculation divides completed tasks by total attempts rather than successful attempts by total attempts.
- min_amount and max_amount are accepted by the scholarship filter API but are not applied to the SQL query.
- amount_ranges and deadline_distribution in the statistics response are initialized but not populated.
- The worker does not persist complete raw observations, source revision/hash, extraction version, or a field-level evidence record.

## 8. Frontend fidelity and build quality

- frontend/lib/api.ts hard-codes a public HTTP API endpoint. This creates environment coupling and sends requests without TLS.
- Dashboard passes console.log as FilterPanel.onFilter, while FilterPanel does not invoke its callback or bind its controls to filter state. The visible filters do not affect the dataset.
- The API client sends min/max amount filters that the backend ignores.
- The /scholarships route is implemented as a URL-upload form, not a scholarship listing page, despite its navigation label.
- TaskProgress.tsx references Card without importing it. The Next.js configuration and build script disable ESLint and TypeScript build failures, masking this class of defect.
- StatusCards display a success rate derived from the incorrect backend formula.
- The frontend has no authentication flow or user-specific workspace separation.

## 9. Adoption decision

Retain the broad architecture concepts: URL ingestion, source-specific crawling, asynchronous worker separation, SQL persistence, task progress, API-backed UI, and LLM-assisted extraction.

Do not adopt the implementation as a production system. A mature replacement needs:
1. authenticated API access and tenant-aware authorization;
2. strict URL/redirect/DNS egress controls and bounded upload/crawl budgets;
3. explicit task leases, bounded retries, transactional progress, and a notification/outbox state machine;
4. one SQLAlchemy session per worker task and no sync DB/LLM calls on the async event loop;
5. Playwright as a pinned dependency with browser provisioning and isolated execution;
6. canonical opportunity identity, source snapshots, field-level evidence, and source aliases;
7. validated extraction schemas, untrusted-content boundaries, currency/deadline normalization, and calibrated evaluation;
8. one shared backend/frontend schema with working filters and deployment configuration;
9. tests, CI, migration tests, and reproducible setup documentation.

## 10. Coverage and verification

Inspected the recursive tree, README, requirements, main.py, API endpoints, settings, database setup, ORM models, Alembic migration, worker, parser, AI service, URL utilities, Next.js package/configuration, API client, pages, and core dashboard/upload/export components.

Not performed: application startup, Playwright installation, database migration execution, LLM calls, live URL fetching, frontend build, API tests, or database binary inspection. No live scholarship, funding package, applicant eligibility, or runtime behavior is verified.

Evidence:
- [Repository](https://github.com/atomdbc/scholarship_scraper)
- [FastAPI startup](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/main.py)
- [API endpoints](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/api/endpoints.py)
- [Worker](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/scraper/worker.py)
- [Parser](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/scraper/parser.py)
- [AI extraction](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/services/ai.py)
- [ORM models and database schema](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/app/models/schemas.py)
- [Frontend API client](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/frontend/lib/api.ts)
- [Frontend dashboard](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/frontend/pages/dashboard.tsx)
- [Frontend build configuration](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/frontend/next.config.js)
- [Requirements](https://github.com/atomdbc/scholarship_scraper/blob/b53d5decb4bc2ae4f603ed340adb7f606eaf80ad/requirements.txt)
