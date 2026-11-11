# chuyaowang/nl-phd-tracker — deep static repository review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [e31c72bb3ea4548f222f8564be352dd269d602ae](https://github.com/chuyaowang/nl-phd-tracker/commit/e31c72bb3ea4548f222f8564be352dd269d602ae)  
**Review state:** DEEP_REVIEW_DOCUMENTED — static source inspection; no runtime tests.  
**Category:** Netherlands AcademicTransfer local vacancy monitor.  
**Verdict:** adapt concepts only; license and token-handling constraints apply.  
**Primary risk:** empty or invalid API response can overwrite the local job catalogue.

## 1. Purpose and scope

A local-first PhD/job tracker for vacancies saved by the user on AcademicTransfer. It combines a browser extension that captures the user's authenticated AcademicTransfer token, a local FastAPI sync endpoint, a Python fetch/normalization script and a Streamlit interface for filtering, editing and tracking jobs.

The repository has 21 tracked files. Latest commit: 8 May 2026. It has no test suite or CI workflow. The LICENSE is PolyForm Noncommercial 1.0.0; commercial reuse is not permitted by that license without separate permission.

## 2. Acquisition and authentication flow

The Chrome extension runs only on AcademicTransfer domains. A content script scans localStorage/sessionStorage for JWT-like strings; a background `webRequest` listener observes Authorization headers on AcademicTransfer API requests. The token is kept in `chrome.storage.session`, then passed from the extension popup to the local FastAPI service.

The Python client calls AcademicTransfer's saved-jobs API with the bearer token and follows the API's `next` pagination URL until no further page remains. This avoids scraping HTML and is a cleaner acquisition path than generic page parsing.

The repository relies on an observed authenticated web API and browser session token rather than a documented public OAuth integration. Before production reuse, confirm API terms and authorization boundaries. The extension's broad JWT regex may capture unrelated JWT values stored on the same origin; it should be narrowed to the expected API credential and request context.

## 3. Local architecture and persistence

The Streamlit UI reads a local CSV, supports keyword filtering and manual fields such as type, fit, application status and notes. The sync script keys rows by AcademicTransfer job ID and merges user-maintained fields from existing rows into refreshed records. It creates a `.bak` copy before writing.

The local server is explicitly bound to `127.0.0.1`, which limits network exposure. It exposes sync/status routes without application authentication and configures CORS with wildcard origins. This creates a local-origin request surface: an arbitrary website may be able to issue requests to the loopback service, subject to browser local-network protections. Restrict allowed origins to the extension and add a one-time pairing/CSRF token.

## 4. Merge and destructive-sync semantics

The merge preserves manual fields for records whose job IDs remain in the new API response. It intentionally removes jobs no longer saved on AcademicTransfer. That is a reasonable single-user workflow, but the sync writes a new CSV even when the API returns zero records. If the token is stale, the API behavior changes, or the response is unexpectedly empty, a previously populated CSV can be replaced with an empty file. The `.bak` file is a useful recovery mechanism but only retains the most recent backup.

The file is written directly rather than to a temporary file followed by an atomic replace. Concurrent syncs or process interruption can produce a partial write. There is no explicit lock around the CSV.

**Required repair:** if an existing catalogue is non-empty and a refresh returns zero records, stop and require explicit confirmation or retain the prior file. Validate required job IDs and pagination metadata, record sync provenance, write atomically, and protect against concurrent sync operations.

## 5. Date and normalization semantics

The parser normalizes job ID, title, employer, location, start date, end date, salary, weekly hours, job type, research group, description and contact. Keyword matching is deterministic and configurable. HTML is converted to text/Markdown for local review.

A domain-specific workaround subtracts one day from date strings whose parsed time is midnight, based on an observed AcademicTransfer exclusive-end-date convention. This fixed a documented off-by-one issue, but it is an unverified assumption for all future API records. It needs regression fixtures and an explicit API date contract. Some optional numeric fields can also be absent; parsers should handle mixed null/number cases without aborting the full sync.

## 6. Security and privacy

The design is local-first and does not demonstrate sending job records to an external AI provider. The bearer token is held in extension session storage and local environment configuration rather than committed to the repository. However:
- the extension scans all storage values for JWT-shaped strings rather than a specific known key;
- the local sync endpoint has no authentication and wildcard CORS;
- the local CSV contains the user's saved vacancies and manual application notes;
- no encryption-at-rest, backup retention or deletion policy is documented.

Keep the token ephemeral, narrow the capture scope, protect the local endpoint, and keep the CSV and backups out of public Git.

## 7. Operational and validation gaps

The implementation uses pagination and request timeouts, but the inspected fetch path does not demonstrate bounded retries/backoff, pagination-loop detection or structured partial-failure handling. There are no automated tests for API schema drift, date semantics, empty responses, manual-field preservation, concurrent syncs or extension token capture.

The UI stores application status as a mutable field; it does not provide a full event history, reminder system, funding verification or applicant eligibility model. The source is specific to AcademicTransfer and the Netherlands.

## 8. Transfer decision for PhD Atlas

The useful design patterns are local-first storage, a source-specific API adapter, stable external job IDs, preservation of manual applicant annotations, paginated retrieval and a pre-sync backup.

Do not copy the implementation into a commercial Atlas product without resolving the PolyForm Noncommercial license. Do not use browser token scraping as the default integration pattern; prefer an official API/OAuth authorization flow. Add:
- a verified API contract and consent flow;
- strict local origin and pairing-token controls;
- empty-result and partial-result guards;
- atomic writes and sync locking;
- source snapshot/hash and fetch timestamps;
- explicit date timezone and cutoff semantics;
- a state-transition history separate from upstream saved/favorite state.

**Overall decision:** useful local tracker reference, but source-specific, noncommercially licensed and not a general opportunity verification system.

## Pinned implementation evidence

- [README](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/README.md)
- [Fetch and merge](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/src/fetch_saved_jobs.py)
- [Streamlit application](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/src/app.py)
- [Local FastAPI service](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/src/local_server.py)
- [Extension background script](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/extension/background.js)
- [Extension content script](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/extension/content.js)
- [Extension manifest](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/extension/manifest.json)
- [License](https://github.com/chuyaowang/nl-phd-tracker/blob/e31c72bb3ea4548f222f8564be352dd269d602ae/LICENSE)

**Validation boundary:** repository source and documentation were inspected. No live AcademicTransfer API request, extension install, sync, browser test or data-loss regression test was executed.
