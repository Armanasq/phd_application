# aluminium5/ScholarshipScraper — source-pinned preliminary investigation

- Upstream: https://github.com/aluminium5/ScholarshipScraper
- Repository ID: 1422499968
- Snapshot: `36a8f80a95e336a13114c8c23d8df698e0d96c10` (2026-10-17)
- Inspection date: 2026-11-12
- State: **PRELIMINARY_FOCUSED**, source-level/static only; upstream tests **NOT_EXECUTED**.
- Country/applicant scope: Indian student scholarships, school through doctoral (not evidence of global funded PhD positions).
- Tree: 95 entries; README, Python backend/scrapers/tests, React/TypeScript frontend, seeded awards, diagrams and report artifacts. No LICENSE file observed in the complete tracked tree. Legal reuse rights are not established.

## 1. Purpose, product, scope
The README identifies ScholarTrack as a scholarship search and personal application-tracking tool for Indian students. It aggregates the National Scholarship Portal (NSP), Buddy4Study and Vidyasaarathi; saves a structured user portfolio; displays scholarships by due date; and tracks saved/applied/under-review/awarded/rejected stages. This is a general scholarship tool with a `phd` level category, not a vetted international doctoral employment vacancy source. Funding amount, tuition coverage and international eligibility are not independently verified.

## 2. Architecture and contracts
- Frontend: React 18, TypeScript and Vite. Calls a same-origin FastAPI `/api` backend through relative paths. Authentication uses JWT.
- Backend: FastAPI, Pydantic v2, SQLAlchemy with PostgreSQL/Neon for deployment and SQLite for local execution.
- Source adapters: `backend/scrapers/nsp.py`, `buddy4study.py`, and `vidyasaarathi.py`; `registry.py` explicitly documents verified/unverified fixtures.
- Ingest: `backend/services/ingest.py` creates a refresh-run record, individually catches source errors, upserts records on `(source, external_id)`, deactivates stale records, expires past deadlines and falls back to seed data when the table is empty.
- Application tracking: database uniqueness on `(user_id, scholarship_id)`; source-level code scopes reads and writes to the active user. Portfolio stores structured personal, family, educational, bank-last-four, document checklist and CV fields.
- Cron is authenticated with a bearer secret; missing configuration returns HTTP 503. Admin refresh is restricted to configured emails.

## 3. Source parsing and extraction
NSP parses server-rendered scholarship rows, their provider, dates, titles and links; NSP does not expose scheme-specific public application links, so the scraper uses the portal application form with a scheme-specific note. Buddy4Study uses a sitemap and per-scholarship Next.js JSON, with a 25-page default crawl limit; it does not provide exhaustive collection. Vidyasaarathi parses a JavaScript-embedded array and handles encoding and a misleading empty-state string that also occurs in source scripts. The `ScrapedScholarship` dataclass carries source, external ID, title, apply URL, dates, level, tags, provider and eligibility text. Date parsing assumes day-first numeric dates and can infer level from heuristic phrase matching. Neither inferred level nor raw eligibility prose establishes individual applicant eligibility.

## 4. Tests and development evidence
Source tree contains `backend/tests/test_scrapers.py`, `test_ingest.py`, `test_api.py`, committed parser fixtures, `pytest.ini`, and frontend TypeScript configuration. The README claims 157 tests; this is a **project claim**, not a result of this investigation. Static inspection confirmed test cases for duplicate upsert, transient-fetch isolation, stale/expired rows, deep-link filtering, auth-related flows and seeded fallback. Upstream tests, HTTP fetches, frontend build, live sources, release pipeline and database deployment were **not executed**.

The pinned October 17 commit updates dependencies; other observed commits include a Python-version pin, report publication and seed deep-link fixes. GitHub issue/PR inspection returned one closed PR and no ordinary issues in the retrieved snapshot. Historical project activity is not a freshness guarantee for every award.

## 5. Concrete source-level correctness problem
`run_ingest` deactivates unseen source records when `result.fetched > 0`. Yet `_upsert` rejects records without a sufficiently specific `apply_url`. If a scraper returns a nonempty list and **all** items are rejected, `seen_ids` remains empty but `_deactivate_unseen` is still invoked; its update has no `NOT IN` restriction and can deactivate *every* previously active row for that source. This contradicts the advertised failure-preservation contract. The conclusion is derived from the control flow, **not** a runtime reproduction.

A second source-trust limit: `_is_portal_homepage` checks for any path after the host, not verified HTTPS scheme, approved host or the correctness of a destination. `ScholarshipOut.apply_url` is a plain string. A plausible-looking path does not prove a legitimate scholarship-specific destination or safe link.

## 6. Evidence, coverage and privacy limits
- Source membership and `external_id` deduplication cannot collapse duplicate awards syndicated across portals.
- A capped crawl cannot establish completeness; empty source fetches preserve stale rows indefinitely until a new valid source refresh or deadline expiry. This protects against accidental deletion but does not independently confirm that a vacancy/award remains open.
- The fallback file contains dated scholarships and may become stale; it is not official evidence of availability. The README explicitly warns that availability/eligibility must be checked on the source portal.
- JWT is retained in browser `localStorage`; any same-origin script compromise could expose it. The backend includes sensitive personal/family/academic portfolio data; it excludes full bank account numbers and rejects unknown document fields, but an independent privacy, retention and access-control review was not performed.
- No verified software license file was present, so patterns can be learned from without assuming permission to copy code.

## 7. Transfer to PhD admissions intelligence
**Adopt concepts, not unverified scholarship facts or source code.** Useful patterns: source-isolated ingest, stable source IDs, source-specific parsers and captured fixtures, explicit exception accounting, bounded crawls, date ordering, user-scoped tracking, restricted cron and non-destructive refresh. Necessary hardening: deactivate only after a verified *complete* source snapshot; separate fetch/parse coverage from valid-record counts; preserve source revision and evidence; require source-domain and URL validation; carry explicit funding/tuition/eligibility `UNKNOWN` statuses; reconcile cross-source award identity; capture schema/versioned migrations and private-data access/retention policy.

## 8. Cross-repository comparison and verdict
Relative to the previously studied scraper-only projects and scholarship portals, ScholarTrack adds source-isolated persistence, user-specific workflow and test fixtures. It does not supply the cycle-specific, internationally valid funded doctoral proof required for the eight-country PhD strategy. The ingest deactivation defect is a specific anti-pattern for the canonical Atlas pipeline; an immutable fetch snapshot plus verification/coverage gate should precede state mutation.

**Verdict:** include for preliminary technical comparison, not deployment or evidence reuse. No empirical execution, independent source recheck, current 2026/27 PhD scholarship validation or privacy certification.

### Pinned source evidence
- [Project README](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/README.md)
- [Ingest and deactivation control flow](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/services/ingest.py)
- [Shared scraper and date/level helpers](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/scrapers/base.py)
- [Source registry](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/scrapers/registry.py)
- [Per-user application state](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/routers/applications.py)
- [Cron authentication](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/routers/cron.py)
- [Ingest regression tests](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/tests/test_ingest.py)
- [Response and portfolio schemas](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/schemas.py)
