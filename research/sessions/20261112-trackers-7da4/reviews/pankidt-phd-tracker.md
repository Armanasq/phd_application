# PankidT/phd_tracker — published Google Sheets SPA review

**Upstream:** https://github.com/PankidT/phd_tracker
**Pinned revision:** [16986762c20b100554de2c799301374586ad2c87](https://github.com/PankidT/phd_tracker/commit/16986762c20b100554de2c799301374586ad2c87)
**Review date:** 2026-11-12
**Classification:** DEEP_STATIC_SOURCE_REVIEW, no live spreadsheet, browser or real application data processed.
**Scope:** Full recursive tree of 122 entries; source parser, store, filters, URL state, link/navigation, modal, dashboard, deploy workflow, package, application shell and current developer guide inspected. No automated test suite in tracked tree.
**License:** No LICENSE file found in pinned tree; do not assume permissive reuse.

## 1. Implemented architecture

Svelte 5 + TypeScript + Vite SPA with dashboard, table, kanban, timeline, map, geographic aggregates and record detail panels. Browser fetchPositions() retrieves a **Google Sheets published-to-web HTML** document, parses its row/header cells, normalizes a small set of columns, and produces a local in-memory Position[] array. Svelte runes derive counts, upcoming dates, monthly distribution, filters and status board. A link from each row can return to the original sheet. It has no authenticated applicant workspace, server-side job verification, source-capture pipeline, database, credentialed Google Sheets edit flow or submission receipt implementation. Manual spreadsheet edits are read on the next refresh; this client **does not write back to Sheets**.

The source's CLAUDE.md still describes a CSV export and PapaParse-based import. The current [loadPositions.ts](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/loadPositions.ts) instead fetches a **published HTML sheet via pubhtmlSheetUrl()** and parses DOM rows. The developer guide is stale relative to actual implementation, so architecture extraction must prioritize code over prose. README.md is the generic Svelte/Vite template and does not describe application behavior.

Positive practices: typed Position contract, status-load-error UI, network fetch failure reporting, source row numbers, explicit user refresh, consistent shared derived metrics, valid route/filter serialization, non-mutating record views, accessible detail modals, and GitHub Pages build/deploy workflow.

## 2. P0/P1 — unknown or malformed deadlines silently become 'rolling'

[loadPositions.ts](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/loadPositions.ts) parses dates using new Date(cleaned). A missing, unknown, unrecognized or malformed date produces null. It then unconditionally sets isRolling = !parsedDate and Position.kind to 'rolling' for that row. Both [PositionDetailDialog.svelte](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/components/PositionDetailDialog.svelte) and [TableView.svelte](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/views/TableView.svelte) display 'Rolling' for kind=rolling.

**Consequence:** unknown, invalid, sheet-header drift or locale-specific dates can be misrepresented as an employer's confirmed open-ended application window. Without an authoritative source, rolling is a claim that needs distinct evidence; parsing failure is not evidence of rolling recruitment. Fix with at least {known_date, verified_rolling, unknown, invalid}, preserve original string and structured timezone, and require explicit rolling cues. Avoid implicit browser locale parsing for admissions deadlines.

## 3. P1 — brittle DOM-to-sheet coupling can produce misleading zero results

The parser depends on Google published HTML containing row headers like th[id^='0R'], a particular sheet-row indexing convention, and header labels mapped to deadline, link, university, country, progress, note. Missing header rows, reordered server markup or an unexpected published table may cause it to skip rows and **return an empty or partial array without throwing**. store.refresh() then sets status='ready' and lastUpdated to the current time, so a source-schema failure may look like a successful zero-position refresh. No minimum row expectation, explicit required-column validation, per-row error telemetry or source-shape test fixtures were found.

**Repair:** validate required columns and row extraction, fail closed to prior known snapshot on structural mismatch, retain source revision/checksum, show degraded freshness and an error instead of an apparently healthy empty board. Test realistic Google pubhtml snapshots with changed row IDs, headers, merged sections and moved columns.

## 4. P1 — identity and vacancy truth are fragile

makeId(deadline, linkCell.text, university) produces a 32-bit JavaScript integer hash. If a university corrects or extends its deadline, or edits a link label, the same opportunity receives a **different ID**, losing continuity of the client selection and any future user annotations associated with that key. Conversely hash collisions are possible, and seen deduplicates records within one fetch by this hash rather than an employer-assigned vacancy reference.

The UI's activeCount counts applicant workflow labels 'In progress', 'Follow-up already' and 'Respond pending'. It does not count independently confirmed **vacant, funded, open doctoral positions**. A status like 'Reject' is a human workflow state from the sheet, not a hiring-site answer. The app does not independently fetch employer URLs, capture official deadlines or validate funding/visa eligibility.

**Repair:** stable canonical source IDs, versioned observations, separate applicant_progress from verified_vacancy_status, independent employer URL evidence, and history of deadline changes.

## 5. P1/P2 — URL and timezone boundaries

unwrapGoogleRedirect() extracts the q query parameter from google.com/url without validating the extracted scheme. cellHref() may therefore accept a rich-text destination without an HTTP(S)-only check, while a raw URL field is constrained by URL_RE. [PositionLink.svelte](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/components/PositionLink.svelte) and [PositionDetailDialog.svelte](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/components/PositionDetailDialog.svelte) bind this destination into outgoing hrefs. Browser/framework-level handling was **not tested**; enforce explicit destination allowlisting to avoid relying solely on template escaping.

The parser's new Date(string) uses implementation-dependent/locale-sensitive interpretations of some date strings and stores a JavaScript Date without the source university's advertised cutoff timezone. Urgency and monthly charts run in the viewer's browser timezone, which can be wrong by a day for international applications. Distinguish deadline date from exact instant and preserve the institution-local closing time and timezone.

## 6. Privacy, operational boundaries and tests

The sheet's published-to-web endpoint is intentionally a **public read surface**; the app hardcodes its published key and sheet ID in [config.ts](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/config.ts). Any personal notes, applicant status or contacts present in that sheet must be treated as published, not private. Do not ingest or display the source author's live sheet rows in a multi-user PhD research platform without redaction and consent. No private upstream sheet contents were retrieved for this audit.

The tracked GitHub Actions [deploy.yml](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/.github/workflows/deploy.yml) builds and deploys on main; it does **not** run a data refresh, unit tests, a source-contract test or even the separate available Svelte/TS check script. No test files appeared in the inspected tree. We cannot infer the build or the live sheet actually succeeds.

## 7. Transfer and acceptance criteria

**Transfer:** simple source-view workflow, typed state selectors, linked table/kanban/timeline/map views, URL-persisted filters, explicit fetch status, and manual refresh. These components could support a research dashboard once data authenticity and applicant privacy are addressed.

**Do not transfer:** published applicant source data as a private account store; conflation of unparseable deadlines with verified rolling, DOM structure assumptions without a schema contract, volatile IDs, browser-local timezone as canonical deadline instant, or sheet progress badges as verified vacancy/admission outcome.

**Test cases:** empty/malformed sheet should show source error; unknown dates must remain unknown; verified rolling distinguish from parse failure; same opportunity edited deadline retains canonical ID; foreign timezones map to correct cutoff instant; unsafe rich-text URLs rejected; duplicate and header-reordered fixtures; clear separation between data fetch timestamp and actual source updated_at; type checking and parser unit tests in CI.

**Limitations:** static evidence only; Google sheet publishing permissions, actual rows, CORS, browser rendering, external applications, GitHub Actions job success and private data were not tested.
