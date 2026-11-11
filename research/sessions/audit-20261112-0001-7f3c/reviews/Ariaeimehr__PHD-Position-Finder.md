# Ariaeimehr/PHD-Position-Finder — implementation-level static review

- Repository ID: 1341632205
- Default branch: main
- Inspected commit: d79a989edbbd70635c7480b659a34116f856a930
- Created: 2026-08-21; last observed push: 2026-08-21
- Tree: 33 entries
- Review state: DEEP_REVIEW_DOCUMENTED (static source review; runtime/tests not executed)
- Confidence: High for source-level architecture and logic; vacancy truth and runtime behavior remain unverified

## 1. Problem and intended product

The repository aims to search for non-US PhD positions in three target areas—federated learning, human activity recognition, and transformer/deep learning—and send daily Telegram/email digests. It also includes a React dashboard intended to display vacancies, configure credentials, inspect code, simulate scraping, and guide deployment.

The product combines two different systems:
1. a Python scraping/notification worker; and
2. a React/Vite/Express demonstration dashboard.

The repository does not implement a coherent live integration between them.

## 2. Architecture and data flow

### Python worker

- Source adapters: EURAXESS, FindAPhD, and AcademicPositions.
- HTTP layer: cloudscraper-backed session, urllib3 Retry with three retries, jitter delay, a 25-second request timeout, status validation, and optional proxy.
- Topic and country/funding filters: PositionFilter.
- Data model: PhDPosition dataclass.
- Persistence: SQLite seen_positions table keyed by a SHA-256 hash of URL plus title.
- Notifications: Telegram Bot API and SMTP email.
- Local scheduling: schedule library in main(), with a 24-hour loop.
- GitHub Actions: scheduled one-shot invocation at 07:00 UTC, with the SQLite file restored/saved through Actions Cache.
- Docker: Python 3.11 worker image and persistent /app/data volume.

The orchestrator selects only the first three keywords from each of the three topic lists, then runs the three scrapers sequentially. The source adapters inspect only the first 15 EURAXESS cards, 12 FindAPhD cards, and 10 AcademicPositions cards per keyword. No pagination or source-completeness tracking is implemented.

### Web application

- React 19 + TypeScript + Vite frontend.
- Express server exposes GET /api/phd-positions.
- UI components provide a vacancy explorer, code inspector, .env generator, scraper simulator, and setup guide.
- The Express endpoint returns a hard-coded ten-position fixture. It does not invoke the Python pipeline, read the SQLite database, or call the source adapters.
- App.tsx contains a second copy of the same static vacancy dataset and uses it as fallback.

The Python dataclass and TypeScript PhDPosition interface are also different contracts: the Python model has no id, city, or deadline fields, while the TypeScript interface expects an id and may display city/deadline. The static Express fixture supplies those fields, which masks the absence of a real worker-to-API integration.

## 3. Critical correctness defects

### Funding is not verified

PositionFilter.is_fully_funded() returns True by default whenever no explicit negative phrase is found. Missing funding evidence is therefore interpreted as positive funding.

- EURAXESS calls the function with the literal field "EURAXESS R1"; that string is not a funding award. The default branch still returns True, after which the scraper hardcodes "Fully Funded (MSCA / EU Standard)".
- FindAPhD uses a Funding=F1 query parameter, but then hardcodes full tuition plus maintenance stipend without extracting or verifying the actual award terms, fee category, duration, or nationality restrictions.
- AcademicPositions does not call the funding filter at all and hardcodes "Fully Funded (Salaried University Position)" for every parsed result.

The resulting funding labels are not supported by field-level evidence and cannot be used for admissions decisions.

### US exclusion is not reliable

is_in_usa() computes normalized_text from the full listing but never uses it. It checks only the country and institution strings. If those fields are missing, generic, or incorrectly parsed, US listings can pass even when the title/description identifies a US location. EURAXESS defaults to "Europe / International"; FindAPhD defaults to "United Kingdom / EU / Global"; AcademicPositions defaults to "Europe (Non-US)". These fallback strings are not evidence of country.

The exclusion keyword list also includes US state names such as Georgia. A position in the country of Georgia can therefore be falsely excluded when that country name appears as the parsed location.

### Topic matching creates substring false positives

match_topic() uses raw substring membership rather than token/phrase boundaries. The HAR keyword "har" can match the word "share"; the transformer keyword "vit" can match the substring in "activity". A generic description can therefore be assigned to an unrelated research cluster. Matching needs normalized tokens, phrase aliases, and ambiguity handling.

### Weak source identity and date semantics

- position_hash is derived only from normalized URL plus title. Equivalent vacancies on different provider URLs remain separate; a title change creates a new identity.
- discovered_date is evaluated when the module is imported, not when each PhDPosition instance is created. In a long-running process, later discoveries retain the process-start date.
- SQLite stores only the seen hash and a small subset of metadata. It does not retain the complete source observation, raw content, source platform, funding claim, evidence, or notification delivery state.
- There is no source snapshot/hash, extraction version, deadline provenance, or stale-record lifecycle.

## 4. Notification and operational failure modes

- The pipeline calls mark_seen() before dispatching notifications. If Telegram or SMTP delivery fails, the record is already marked seen and will not be retried on the next run.
- The return values from send_digest() are ignored. There is no transactional outbox, delivery-attempt record, retry queue, or dead-letter state.
- Scraped values are interpolated into Telegram HTML and an HTML email without escaping. Titles, descriptions, institutions, funding strings, and URLs are external input; malformed markup or deceptive links can reach recipients.
- SMTP connection has no explicit timeout and server.quit() is only reached on the success path.
- Concurrent GitHub Actions runs can restore the same previous database cache and independently send the same alerts. The workflow has no concurrency group or distributed lease.
- The workflow calls run_daily_search() directly. RUN_ON_STARTUP and SCHEDULE_TIME are not used by that invocation; the GitHub cron itself controls one run per workflow.
- The USER_AGENTS list is defined but not used by the actual SafeScraper path.
- The helper _extract_supervisor() exists on EuraxessScraper but is not called by the extraction path.

Positive engineering patterns are the source-specific adapter classes, bounded retry/backoff, explicit request timeout, jitter, proxy support, SQLite persistence, and separate notification transports. They are useful starting points, not proof of production reliability.

## 5. Dashboard fidelity and secret-handling risks

The ten records in App.tsx and server.ts are hard-coded fixtures, not scraped vacancies. All are labelled fully funded, and their URLs point to generic institutional career/program pages rather than vacancy-specific announcements. Six of the ten fixture deadlines are earlier than 2026-11-12. The UI nevertheless labels the dataset "Live Vacancies", displays "100% Fully Funded", and claims 14 US vacancies were filtered. These metrics are static assertions, not measured crawler results.

Additional discrepancies:
- ScraperSimulator uses setTimeout-driven logs and fixed sample counts; it does not call the Python worker.
- CodeInspector renders seven hard-coded snippets from codeSnippets.ts rather than reading the repository files. The embedded phd_hunter.py snippet differs from the actual worker: it shows a different HTTP-client/source implementation and omits the current AcademicPositions adapter.
- ConfigGenerator contains credential-shaped default values and a personal-looking email address in public client-side source. Their validity is unverified; do not repeat or use them. If any are real, treat them as exposed and rotate them. The UI's "Safe Storage Guarantee" does not neutralize credentials committed in the public bundle.
- metadata.json declares a server-side Gemini capability and package.json includes @google/genai, but no Gemini client or model invocation was found in the inspected application source.
- PositionsExplorer bookmarks exist only in React component state and disappear on reload. The declared onSelectPosition prop is not used.
- The Dockerfile builds only the Python worker. It does not install Node dependencies or deploy the React/Express dashboard, despite the combined product presentation.

## 6. Dependencies, maintenance, and validation

The repository has 33 tree entries, no README, no LICENSE file, no test directory, and one scheduled scraping workflow rather than a test/CI workflow. Python requirements and npm dependencies use version ranges; no lockfile was present in the inspected tree. The package is named react-example and retains generic Google AI Studio page metadata.

The GitHub API returned no issues or pull requests. Only main exists. Static source review was completed, but npm build/lint, Python tests, live scraping, notification delivery, Docker startup, and GitHub Actions execution were not run. No security certification or live-vacancy verification is claimed.

## 7. Adoption decision and redesign

Retain the multi-source adapter, retry/jitter, SQLite persistence, and separate notification transport concepts. Do not adopt the current funding, geography, topic, deduplication, notification, or UI truth semantics.

A production-grade replacement should use:

1. Source registry and policy-aware adapters with source-specific fixture tests.
2. Raw source snapshots and typed extraction candidates.
3. Field-level claims for location, salary, stipend, tuition, duration, eligibility, deadline, and supervisor.
4. Tri-state values: verified, contradicted, unknown. Missing funding/location evidence must never become a positive result.
5. Canonical opportunity identity with source aliases and duplicate review.
6. A transactional notification outbox; mark an item delivered only after confirmed delivery.
7. Escaped HTML/Telegram rendering, URL scheme/host validation, and no credentials in client source.
8. A real API/database contract between the worker and UI, with static fixtures clearly labelled as demonstrations.
9. Version-pinned dependencies, lockfiles, unit/integration tests, workflow concurrency controls, and observability for source failures and freshness.

Primary evidence:
- [Repository](https://github.com/Ariaeimehr/PHD-Position-Finder)
- [Python worker](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/phd_hunter.py)
- [Express API and static fixture](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/server.ts)
- [React application and hard-coded positions](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/src/App.tsx)
- [Code inspector snippets](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/src/data/codeSnippets.ts)
- [Config generator](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/src/components/ConfigGenerator.tsx)
- [Daily workflow](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/.github/workflows/daily_phd_search.yml)
- [Docker deployment](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/d79a989edbbd70635c7480b659a34116f856a930/Dockerfile)
