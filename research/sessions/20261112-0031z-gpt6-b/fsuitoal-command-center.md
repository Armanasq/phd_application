# Deep static repository audit — fsuitoal-code/phd-application-command-center

**Reviewed:** 2026-11-12  
**Upstream:** https://github.com/fsuitoal-code/phd-application-command-center  
**Pinned main commit:** [`ea240bc0189038881306ccd34a5b9cbf525aaebd`](https://github.com/fsuitoal-code/phd-application-command-center/commit/ea240bc0189038881306ccd34a5b9cbf525aaebd)  
**Git tree SHA:** `87cf714b7f0df7f90582955f785529e9597c3668`  
**Scope:** DEEP_STATIC_REVIEW_COMPLETE for architecture, API, persistence, research-agent boundaries, selected tests and operational entry points; LIVE_AGENT/RUNTIME_NOT_TESTED.  
**Decision:** ADAPT_SELECTED_LOCAL_FIRST_PATTERNS; REJECT_SOURCE_VALIDATION_AND_MULTITENANT_ASSUMPTIONS_AS_IS.

## 1. Purpose, lineage and inspected scope

A personal, single-user, local-first application command center for university programs, deadlines, faculty notes, application steps, applicant-specific files and cited AI research. The author describes it as an unsupported personal project, not a funded vacancy discovery service or a production SaaS. The main commit dates to 2026-11-02, with 177 recursive tree entries (154 blobs) and 24 test files by filename inventory. GitHub returned no issues, pull requests or workflow-run history.

Inspected README, `docs/principles.md`, Python package declaration, program/faculty/deadline/requirement/document models, DB and file paths, application startup, migration and backup paths, Claude research/faculty/dossier contracts, program/faculty/document/dashboard routers, and unit/integration-test source. No third-party code, authenticated agent, network scraper, migration, or runtime test was executed in this session.

## 2. Actual architecture and boundaries

- **Client:** Vite/React generated frontend and a Python FastAPI backend; the backend can serve prebuilt UI as a catch-all after API routes.
- **Persistence:** SQLite database under an OS-specific user application-data directory; SQLAlchemy models, session-per-request dependency and Alembic migrations.
- **Programs:** university, department, degree, department/program research URL, distinct central application URL, optional admissions email and model attribution.
- **Relations:** faculty, deadlines, requirements, program steps, sourced program notes, user notes, per-program document types and files. Child relationships use delete-orphan cascade.
- **Research:** optional Claude Agent SDK invoked from the current user's Claude account. Program research is intended to use in-domain WebFetch only. Faculty dossier research permits WebSearch and most external WebFetch, with search-engine/Scholar exclusion.
- **Workflow:** automatic seeding of blank/unverified requirement and application-deadline placeholders; only the user marks a step completed.
- **Private files:** program-local CV/SOP/custom files; uploaded document *content* is not read by the Claude integration in the current implementation.

This is a manually controlled personal tracker, not a verification engine capable of certifying current university admissions rules or funded openings.

## 3. Strong implementation patterns

### 3.1 Fail-closed local-data directory

[`app/paths.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/paths.py) refuses to start against a nonexistent or uninitialized data folder without explicit initialization (`create=True` or the setup flag). This prevents a mistaken path configuration from silently presenting an apparently empty user database after an update. Application data is outside the git checkout, so code updates do not overwrite records.

### 3.2 Migration safety

[`app/migrate.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/migrate.py) compares the existing migration revision with known Alembic heads, refuses an unknown newer version, runs a WAL-safe SQLite online backup before applying upgrades, and checks the resulting migration head. [`app/backup.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/backup.py) uses `sqlite3.Connection.backup()` rather than copying a live DB byte-for-byte. Tests include first initialization, no-op migration, incompatible newer schema, snapshot failure, and failed-upgrade behavior. This is valuable for durable applicant data.

### 3.3 Facts versus user decisions

[`app/models/deadline.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/models/deadline.py) and [`app/models/requirement.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/models/requirement.py) distinguish `researched` from `confirmed_by_program` and carry a human-verification marker. [`app/models/program_step.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/models/program_step.py) holds user-selected completion independently of the presence of a document, deadline or other fact. [`app/models/program.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/models/program.py) separates program information URL from the actual application portal URL.

### 3.4 Scoped document storage

[`routers/docs.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/routers/docs.py) checks document type membership in the requested program on upload and checks resolved file paths remain under the configured documents directory before serving them. Uploaded files are stored with generated file ID prefixes, while original file names remain metadata. Documents are separated by program to avoid accidental use of the wrong application-specific SOP. Files are not submitted to Claude by the app.

### 3.5 Checklist and export

[`routers/dashboard.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/routers/dashboard.py) aggregates deadline/reminder agenda, stale and missing-data attention flags, per-program checklists, comparisons and Excel-friendly UTF-8 BOM CSV export. Unknown deadline dates remain null instead of being invented. Tests cover backend routes, source attribution flags, document ownership in program scope, migrations and dashboard scenarios.

## 4. Principal source-boundary defect: public-suffix overbreadth

[`app/claude/research.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/claude/research.py) defines:

- `registrable_domain(url)` = the last **two** hostname labels;
- `_host_in_domain(url, domain)` = hostname equals domain or ends with `"." + domain`;
- `_make_permission_callback(domain)` allows WebFetch only when that predicate passes and denies all other tools.

For `https://www.ox.ac.uk`, the purported university boundary becomes `ac.uk`, so **any `*.ac.uk` university hostname passes the callback**, even if it belongs to a different university. The code comments explicitly acknowledge the public-suffix limitation. The [research tests](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/tests/test_research.py) check `stanford.edu` but do not test `ac.uk`, `edu.au`, and other multi-level public suffixes. This is a deterministic authorization-scope bug, not merely a speculative LLM risk.

The user-supplied initial URL is also not verified against an institution-domain registry. The predicate does not enforce HTTPS or public-address restrictions; the transport tools may impose their own constraints, but this app-level callback does not. In-domain assertions therefore cannot be treated as a verified official-source boundary.

**Required repair:** canonical institution-host allowlist with a maintained public-suffix list (or verified institutional domain mapping), exact host and explicitly approved subdomains, HTTPS enforcement, and tests for lookalikes, multi-label suffixes and private targets. Do not call an arbitrary caller URL official merely because it has an education-like suffix.

## 5. Citation and evidence-validation gap

The prompt asks Claude to return *exact* quotes and fetched official URLs, but this is not enforced by independent retrieval.

[`ResearchedProgram._drop_uncited_notes`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/claude/research.py) checks only nonempty `text`, `quote`, and `source_url`. It does not fetch the page to validate the quote, prove the URL was among actually visited pages, or establish correct program/cycle scope. [`routers/programs.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/routers/programs.py) persists the returned notes as researched/unverified and converts URLs to browser text-fragment links. That presentation is not evidence verification. Deadline, requirement and faculty fields are not individually anchored to source URLs in the structured output.

Similarly, [`faculty_dossier.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/claude/faculty_dossier.py) renders citations if the model-supplied fields are nonempty; it does not independently check source/quote semantics or provide source-capture provenance. Its standalone `Bottom line` summary is model judgment and may remain visible without quote-level support. Human verification flags reduce overconfidence but do not make claims true.

**Required repair:** capture each tool-fetched page and content hash on the server, validate exact URL/host identity and quotes against the fetched text, bind facts to the correct program/intake/funding class and timestamp, track unsupported fields separately, and keep user confirmation independent of model output.

## 6. Operational and security constraints

- **Not multi-user protected:** [`app/main.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/main.py) and its routers contain no authenticated account or access-control middleware. The documented `uvicorn app.main:app --port 8000` launch normally binds loopback unless overridden, consistent with a personal desktop use case. If exposed to a LAN/public interface, program details and uploaded documents can be read or modified without app-level login. Do not deploy as a public server unchanged.
- **Large file uploads:** [`routers/docs.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/routers/docs.py) uses `await file.read()` for a whole file and does not impose an explicit application upload-byte limit before writing. This can consume unbounded worker memory/disk for an exposed or careless workflow. Frontend client limits would not replace server enforcement.
- **Unbounded AI spend/duration:** [`app/config.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/backend/app/config.py) and [`docs/principles.md`](https://github.com/fsuitoal-code/phd-application-command-center/blob/ea240bc0189038881306ccd34a5b9cbf525aaebd/docs/principles.md) deliberately omit provider-turn/time/spend caps. The stated rationale is a single terminal JSON result, but a research pass can use substantial tokens or run unexpectedly long. Production use needs bounded attempts, cost observability and incremental checkpoints.
- **Sensitive paths in health response:** `GET /api/health` returns actual data-folder and database paths; useful for local debugging but unnecessary in an externally exposed deployment.
- **Upload deletion:** `delete_file`/bulk type deletion unlink paths saved in local DB without repeating the containment check used for read. A locally modified/corrupt database path can trigger removal outside the docs directory. Harden before accepting untrusted DB imports.
- **Research-graph limits:** no first-class country-specific visa, nationality, salary/tuition component, evidence freshness, mandatory employer offer, or applicant-specific funding coverage model. A manual “submitted” checkbox is not external submission proof.
- **Testing boundary:** source contains 24 test files, including authorization callback unit tests and migration fixtures, but no CI execution records were returned. Tests use temporary app-data directories and monkeypatched AI calls; none establishes current external URL or source-quote correctness.

## 7. Relevance to `phd_application`

Adopt/adapt:
1. Strictly separate persisted applicant artifacts from code and remote research operations.
2. Fail closed on missing/misresolved local data; do not silently create an empty replacement workspace.
3. Backup before forward-only schema migrations; refuse newer unknown schema revisions.
4. Separate program homepage, application portal, research result, verified institutional requirement and applicant-side action.
5. Keep a user-set application-step state separate from document presence and model speculation.
6. Support individual program-specific SOP/CV artifact versions and an agenda of dated requirements/reminders.

Do **not** adopt unchanged:
1. Last-two-label university domain scope or user-supplied URL trust.
2. Model-supplied citation strings as source verification.
3. No authentication for reachable server deployments.
4. Unlimited AI calls and unbounded uploads as operational defaults.
5. Free-text funding assumptions rather than typed salary, stipend, tuition, fee and applicant eligibility claims.

### Interconnections

- PhD Atlas is stronger for scoped agent authorization and official-source crawler host/DNS checks.
- This command center provides a clearer lightweight, relational SQLite/Alembic and local document lifecycle design.
- The central project should combine fail-closed local-data migration practices with independently fetched, source-grounded claims and explicit approval/submission evidence gates.

## 8. Verification result and limitations

**Disposition:** DEEP_STATIC_REVIEW_COMPLETE for the enumerated major paths, not exhaustive line-by-line verification of all 154 blobs.  
**Runtime execution:** NOT_PERFORMED.  
**External page/citation verification:** NOT_PERFORMED.  
**Credential/API use:** NONE.  
**Observed upstream CI:** NO_RUNS_RETURNED.  
**Vacancy availability/funding:** NOT_VERIFIED.

The repository is an instructive personal admissions workspace with strong local-data safeguards and a concrete research-domain authorization error. Its AI citations and claimed official-only scope should not be used as verified facts without additional controls.
