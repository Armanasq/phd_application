# ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER — deep static audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER | **Pinned commit:** [`18b4c4a163bbd908ff434d47a7cf570686962e83`](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/commit/18b4c4a163bbd908ff434d47a7cf570686962e83) | **Branch:** `main` | **Status:** DEEP_REVIEW_DOCUMENTED (static; no runtime test) | **Verdict:** reject as live admissions or funding feed; limited local dashboard reference only.

## 1. Actual purpose and scope

A September 2026 prototype for tracking corporate and academic applications, CS and management PhD positions, university rankings, tasks and interviews. The repository consists of a static browser dashboard, a FastAPI stub, JSON files under `data/`, CSS/JS modules, and an empty deployment workflow. Its two-line README describes broad ambitions but does not claim that official university recruitment sources are verified.

The repository has 48 recursive tree entries, including committed `__pycache__/*.pyc` binaries. Latest commit is 2026-09-25. No issues or pull requests were returned. All eight recent Actions push runs retrieved for the empty deploy workflow were reported as failures. No automated tests were found. No LICENSE file or reliable reuse grant was established.

## 2. End-to-end dataflow and live wiring

**Data plane:** `index.html` loads only `js/data.js`, `js/api.js`, `js/app.js`, and `js/settings.js`. The richer `js/jobs.js`, `js/phd-cs.js`, `js/phd-management.js`, `js/applications.js`, `js/tasks.js`, `js/companies.js`, and `js/analytics.js` are present but not loaded as scripts by the inspected HTML entry point.

`js/app.js:setPage()` calls their global functions, so selecting many navigation destinations in the current static page produces missing-function errors rather than functioning modules. The later fallback branches for the same page names are unreachable because earlier `else if` conditions match first. The HTML source also contains literal backtick/CRLF-escape text between two script tags; that should be corrected even though the stronger blocker is missing script imports.

**Backend:** `backend/app/main.py` defines `/`, `/api/health`, `/api/jobs`, `/api/phd/cs`, and `/api/phd/management`. The three list endpoints always return `items: []` and `total: 0`. There is no source collector, database query, user account, authorization boundary, CRUD endpoint, or funding verification in this entry point. The Python dependencies include `sqlalchemy`, `httpx`, and BeautifulSoup, but imported dependencies alone do not implement a crawler.

**Frontend API:** `js/api.js` hardcodes `http://127.0.0.1:8001/api`; the inspected page does not automatically fetch/merge real PhD vacancy results. The backend config allows wildcard CORS origins with credentials, which is an overly broad cross-origin policy. The available API returns placeholders only.

**Persistence:** richer frontend modules use browser `localStorage` keys such as `career_tracker_applications`, `career_tracker_phd_cs`, and `career_tracker_tasks`. This is not synchronized with the FastAPI backend or a shared database. There is no backup, migration, revision, provenance, or multi-user synchronization model.

## 3. Concrete data-model defects

`js/data.js` defines PhD positions as six-element arrays (`[university,country,position,area,status,deadline]`), while `js/phd-cs.js` and `js/phd-management.js` treat those entries as objects (`item.university`, `item.status`, `item.deadline`). If those unimported modules were linked without normalizing the seed dataset, the example rows would render empty fields, the funded count would be zero, and the filters would malfunction.

The dashboard uses a configured QS coverage **target** of 300 rather than 300 fetched or validated university rows. The data modules include mock institutional names, funded labels and dated PhD positions without source URLs or official evidence. They are example fixtures, **not verified 2026 vacancies**, funded offers, or current ranking observations.

`APP_DATA.applications` is initialized to a scalar `3` for dashboard display, whereas `js/applications.js` maintains a separate array in localStorage. Consequently, the headline application count is not derived from persisted applications. Job data uses `mode` in demo fixtures while `js/jobs.js` filters `classification`. Status and location semantics are inconsistent between modules.

## 4. Security and privacy

- Browser modules interpolate user-generated organization, role, notes, position, and task values into `innerHTML` without consistent escaping. Once those modules are loaded, a malicious local record could create stored DOM injection. This is a source-level risk, not a demonstrated exploit.
- Application notes and potentially sensitive tracking data are stored unencrypted in localStorage and lack user isolation, access policy or retention control.
- The FastAPI stub has no authentication, and wildcard CORS with credentials should not be copied as a security pattern.
- User input can mark a position as `FUNDED` without evidence; the funding field is self-declared rather than verified.

## 5. Operations and history

The blank `.github/workflows/deploy.yml` is not an implemented deployment or CI pipeline. Recent GitHub Actions run metadata indicates repeated failures, but a concrete root cause was not independently established from job logs. The repository has no reproducible tests or automated evidence checks. Its `data/phd_cs/opportunities.json` and `data/phd_management/opportunities.json` are empty files at the pinned revision.

The frontend and backend do not form an end-to-end application lifecycle. No real crawler, current vacancy verification, deployment qualification, or functioning cross-device synchronization has been demonstrated.

## 6. Transfer and source-policy decision

Retain only the conceptual separation of application pipeline, research area, country, deadlines, interviews, tasks and analytics. Do **not** reuse the example vacancy list or `FUNDED` labels as factual sources.

If rebuilding, require:
1. One typed opportunity/application schema for seed, API and frontend.
2. Verified official URLs, fetched timestamps, funding components, cycle/date semantics and unknown values.
3. API-backed persistence with versioned writes, owner authorization and audit events.
4. Explicit module imports/route tests and integration tests from HTML entry point through API.
5. Safe DOM rendering and conservative CORS.
6. Tests that distinguish demo fixtures, opportunities, applications and funded offers.

## 7. Inspected evidence

- [HTML entry and script wiring](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/index.html)
- [Frontend router and demo UI](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/app.js)
- [Seed data and example PhD positions](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/data.js)
- [CS and management positions](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/phd-cs.js)
- [Local application persistence](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/applications.js)
- [FastAPI placeholder endpoints](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/backend/app/main.py)
- [Frontend API client](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/api.js)

## 8. Review state

**DEEP_REVIEW_DOCUMENTED (static)**. Repository tree, source architecture, key models, routing, dataflow, backend stubs, deployment metadata and development history inspected. No local server, browser, database, live scraping or tests executed; external vacancy/funding truth remains **NOT_VERIFIED**. Do not infer real-world admission availability from the demo dataset.
