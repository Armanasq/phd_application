# aluminium5/ScholarshipScraper — supplemental deep static findings

**Coordination note:** a separate canonical preliminary review already exists at `research/repositories/reviews/aluminium5__scholarshipscraper.md`, registered by an earlier session. This report is retained as a session-owned supplement only; it does not replace or upgrade that record.

**Review date:** 2026-11-12  
**Pinned upstream revision:** [36a8f80a95e336a13114c8c23d8df698e0d96c10](https://github.com/aluminium5/ScholarshipScraper/commit/36a8f80a95e336a13114c8c23d8df698e0d96c10)  
**Review state:** DEEP_REVIEW_DOCUMENTED — static source and fixture review; runtime tests not executed.  
**Category:** Australia/India scholarship structured scraping and applicant tracker.  
**Verdict:** adapt only after hardening.  
**Primary risk:** partial-source crawl deactivates valid unseen records.

## 1. Purpose and scope

A small scholarship discovery and application-tracking application for Indian students. The implementation combines a React frontend, FastAPI backend, SQLAlchemy persistence, JWT authentication, a student portfolio, application statuses, and scheduled refresh through Vercel. It is not a general international PhD vacancy engine: its source set and level taxonomy are India-oriented and include school, undergraduate, postgraduate and doctoral awards.

The pinned repository has 79 tracked files. The README claims 157 tests. Test modules and saved HTML fixtures exist, but this session did not execute them. No license file, CI workflow or independent runtime result was established.

## 2. Architecture and data model

The backend stores `Scholarship`, `Application`, `Portfolio`, `User` and `RefreshRun` records. Scholarship identity is unique only on `(source, external_id)`. Scraped fields include title, provider, free-text award amount, eligibility, level, tags, open/deadline dates, apply/info URLs, active flag and `last_seen_at`.

The application model stores one current status, optional applied date and notes. It does not provide an append-only application event history, proof of submission, offer evidence or a cycle-aware application timeline.

The portfolio is a whole-document JSON payload divided into personal, academic, family, bank, documents and CV sections. Pydantic schemas restrict fields and deliberately store only the last four bank-account digits and document-presence metadata, not full identity numbers.

## 3. Source adapters and extraction

- **National Scholarship Portal (NSP):** parses the central-sector scholarship listing HTML. Fixture tests assert 31 schemes, dates, ministry attribution, tags and the shared application form URL. It does not cover all state or university schemes.
- **Buddy4Study:** parses the site sitemap and each scholarship detail page's `__NEXT_DATA__` payload. The sitemap documents approximately 1,350 pages, but the scraper visits only the 25 most recently modified pages by default. It uses the embedded year-specific edition data and brand-page deep link.
- **Vidyasaarathi:** extracts an embedded JavaScript array. The portal has no public per-scheme deep link, so the record links to the common application portal and tells the student which scheme to select after login.

The shared `ScrapedScholarship` schema is intentionally small and useful for adapter consistency. However, `award_amount` is free text; the schema does not distinguish tuition waiver, stipend, salary, duration, renewal, separate award components, currency, international fee coverage or nationality restrictions. It also has no source snapshot, content hash, exact evidence span or cycle field.

## 4. Ingestion and data-integrity analysis

The most serious defect is in the source reconciliation contract.

`Buddy4StudyScraper.fetch()` intentionally crawls only `urls[:MAX_PAGES]` (default 25), sorted by sitemap `lastmod`. It is therefore an incremental/partial sample, not a complete source snapshot. Nevertheless, `run_ingest()` calls `_deactivate_unseen()` whenever `result.fetched > 0`. The reconciliation then deactivates every active row for that source whose database ID was not returned by the current 25-page sample.

The failure path makes this worse: if one or more detail pages fail but other pages yield records, Buddy4Study logs the failures and returns the partial result. It raises only when failures occurred and no records were returned. The ingest service therefore treats a partial crawl as successful and retires valid rows from pages that were not crawled or could not be fetched.

There is a second route to the same destructive outcome. `result.fetched` is set to the number of scraper records before `_upsert()` validates them. If a source returns records but every record is skipped for a missing or invalid apply URL, `seen_ids` remains empty while `result.fetched > 0`; `_deactivate_unseen()` then deactivates all active records for that source.

Existing tests cover a complete successful source refresh, a scraper exception, and an empty successful result. They do not cover partial pagination, partial page failure with some successful records, or a non-empty result in which all rows are rejected.

**Required repair:** return a typed source result with explicit `complete_snapshot`, pages attempted/succeeded, parser status and errors. Reconcile unseen rows only after a complete, authoritative snapshot. For bounded/incremental crawls, update `last_seen_at` for observed records and apply a conservative stale-age policy instead of deleting unseen rows.

## 5. Authentication, privacy and security

- `JWT_SECRET` defaults to the literal `dev-only-insecure-secret`. There is no startup validation that refuses production when the secret is absent or unchanged.
- Passwords are silently truncated to the first 72 UTF-8 bytes for bcrypt. The schema permits up to 128 characters, so distinct long passwords sharing the same first 72 bytes authenticate identically. Reject overlong byte sequences or use a password-hashing scheme without this truncation behavior.
- Login/signup routes have no visible rate limiting, progressive delay or lockout.
- The frontend stores the bearer token in `localStorage`, making token theft possible under an XSS compromise.
- Portfolio fields include date of birth, gender, phone, address, state/district, caste/category, religion, disability status, family names/occupations/income, IFSC and bank last four digits. These are sensitive personal and financial attributes. The application has no application-level encryption or documented retention/deletion workflow in the inspected code.
- Portfolio updates replace the entire JSON document and have no optimistic version check; concurrent edits can overwrite one another.

The cron refresh endpoint correctly refuses to run without `CRON_SECRET` and uses constant-time comparison. The API health endpoint, however, always returns `{"ok": true}`; startup logs and suppresses database initialization failures, so health can be green while the database is unavailable.

## 6. Runtime, deployment and test evidence

The project supports SQLite locally and a PostgreSQL/Neon URL in production. `Base.metadata.create_all()` is described as keeping the project migration-free, but SQLAlchemy `create_all` does not alter existing tables when columns or constraints change. A real migration process is required for deployed schema evolution.

The date parser uses `datetime.fromtimestamp()` and `date.today()` without an explicit `Asia/Kolkata` timezone. On hosts configured for UTC, epoch-derived dates and local deadline comparisons can differ from the portal's Indian calendar around midnight.

The README claims 157 tests and the repository includes parser fixtures and tests for ingestion and API behavior. No CI workflow was found. Tests were not executed in this review. The current test suite does not cover the partial-crawl deactivation defect described above.

## 7. Findings, limitations and adoption risks

**P0**
- Partial Buddy4Study crawls can deactivate valid opportunities.
- Unchanged or unconfigured JWT secret can be used in production.
- Long passwords are silently truncated.
- Sensitive applicant data is stored in a broadly structured portfolio without an evidenced retention/encryption model.

**P1**
- A parser/layout failure can be represented as an empty successful scrape. Vidyasaarathi logs that it could not find the expected array and returns `[]`; `run_ingest` treats this as a successful empty source result.
- `VidyasaarathiScraper.verified` is true while the registry comment describes the source as unverified/unreachable. The `verified` flag is not enforced by ingestion.
- No explicit source timezone, deadline cutoff time, cycle, source content hash or claim-level evidence is stored.
- Application status is a mutable field rather than an auditable lifecycle.
- `_is_portal_homepage()` checks only whether a URL has a path; it does not validate an allowed host or scheme.

**P2**
- No explicit license or CI pipeline was established.
- Source coverage is narrow and does not provide a general international PhD opportunity inventory.

## 8. Transfer decision for PhD Atlas

Adopt the adapter separation, source-specific fixtures, deterministic source/external-ID keys, structured application status, user portfolio separation and per-run telemetry as design references.

Do not adopt the current reconciliation algorithm, boolean funding representation, or trust model. Atlas should model source snapshots and completeness, preserve source-specific aliases, and store each funding/eligibility/deadline fact as a claim with exact source evidence, cycle, applicant scope and verification state. Keep private applicant documents and sensitive attributes in a separate protected data domain.

**Overall decision:** useful architecture and source-adapter lessons, but not safe to adopt or deploy unchanged.

## Pinned implementation evidence

- [README](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/README.md)
- [Buddy4Study scraper](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/scrapers/buddy4study.py)
- [Vidyasaarathi scraper](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/scrapers/vidyasaarathi.py)
- [NSP scraper](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/scrapers/nsp.py)
- [Ingest service](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/services/ingest.py)
- [Models](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/models.py)
- [Auth utilities](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/auth.py)
- [Auth routes](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/routers/auth.py)
- [Portfolio schema](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/schemas.py)
- [Portfolio routes](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/routers/portfolio.py)
- [Application tests](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/tests/test_ingest.py)
- [Scraper fixture tests](https://github.com/aluminium5/ScholarshipScraper/blob/36a8f80a95e336a13114c8c23d8df698e0d96c10/backend/tests/test_scrapers.py)

**Validation boundary:** source and fixture files were inspected. No pytest run, live scrape, Vercel deployment, Neon migration, browser test or security test was executed.
