# PankidT/phd_tracker — deep source audit of a public Google Sheets PhD dashboard

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/PankidT/phd_tracker | **Pinned source:** [`16986762c20b100554de2c799301374586ad2c87`](https://github.com/PankidT/phd_tracker/commit/16986762c20b100554de2c799301374586ad2c87) | **Review state:** DEEP_REVIEW_DOCUMENTED (static) | **Decision:** use as read-only visualization reference; do not adopt deadline/funding/status semantics as verified.

## 1. Actual product and provenance

A Svelte 5 + TypeScript + Vite client for visualizing an applicant's published-to-web Google spreadsheet of positions, university names, countries, deadlines, application progress and notes. The 122-entry source tree includes views for dashboard, Kanban, maps, tables, timeline, chart components, a Google Sheet import parser and deployment workflow. Latest observed revision is 2026-05-19. The README is the generic Svelte/Vite starter README, not documentation of the real spreadsheet schema, privacy policy or employer-source provenance.

No separate backend or API authentication module appears in the inspected application path; the frontend consumes a publicly published Sheet as a read-only data source.

## 2. Data acquisition and identity

`src/lib/config.ts` holds a public Google Sheets document ID and separately a published-sheet key for `/pubhtml/sheet?gid=...`. The `fetchPositions()` function downloads HTML without browser cache, parses rows with DOMParser and identifies rows by `th[id^='0R']`. It determines column indices from a limited header-name mapping and skips section headings; it also unwraps Google hyperlink redirects to their original URL.

This is more robust than fixed-position parsers for schema changes; however, a published Google Sheet is user-controlled data, not proof of opportunity legitimacy. Parsing depends on the Google HTML export's DOM structure and generated row identifiers. Google can change that representation without an API contract.

## 3. Deadline semantics and a reproducible error class

`parseDeadline()` removes an optional weekday prefix and calls JavaScript `new Date(cleaned)`; failed/empty parses return `null`. `fetchPositions()` sets `isRolling = !parsedDate`. Thus **any malformed, unknown, ambiguous or missing deadline becomes “rolling”**, even if the actual opportunity is closed or the source is incomplete. It may also treat a professor name in the deadline cell as evidence of a rolling call.

This is a classification bug with operational impact: the Kanban/timeline view can show an unknown date as a continuing opening. A valid domain model needs separate `ROLLING_OFFICIAL`, `UNKNOWN`, `DATE_WITH_TIMEZONE` and `HISTORICAL_OR_CLOSED` states backed by the source text.

## 4. Stable record identity and reconciliation

`makeId()` computes a JavaScript hash of `university|link|deadline`; changing a deadline or correcting an institution name changes the ID of the same application. Conversely, collisions and reused form links can identify different recruitment cycles incorrectly. The parser's dedup set is within one refresh; it cannot reconcile a position across versions or distinguish reopened calls.

`sheetRow` is stored for deep-linking to the source Sheet, but inserting/sorting rows changes this position. Use a user-assigned immutable application ID, canonical employer opportunity ID and explicit cycle/version instead.

## 5. Privacy and credential boundaries

The source spreadsheet is intentionally **published to the web**, not merely shared within one authenticated account. Any personal application notes, supervisor correspondence, decision status or contact data placed in the source can therefore be indexed/shared outside the app. The UI includes a direct link back to the source Sheet. The current code does not provide owner-scoped authorization or confidential record storage; this is appropriate only for deliberately public, non-sensitive data.

No passwords or private OAuth tokens appear in the inspected source, but the public sheet identifiers must not be assumed to provide access control. Protect private applicant state outside a public GitHub Pages or Google pubhtml channel.

## 6. Store, UI and operational behavior

`store.svelte.ts` tracks positions, load/error status, last refresh, status counts and upcoming deadlines from the downloaded snapshot. `refresh()` replaces state only after successful import and records an error on network failure. The app has read-only data views and a refresh button; the set of progress states derives from the sheet and is not a verified portal receipt or offer.

The GitHub Actions deploy workflow publishes static assets; `package.json` supports Vite build and Svelte/TS checks. No independent automated tests for Google HTML schema drift, historical/unknown deadlines, ID stability, date timezone, deleted/reopened positions or source truth were found. Runtime browser and public Google Sheet access were not executed.

## 7. Transfer and research framework

Reusable patterns: header-name mapping, rich-text URL extraction, linked sheet row references, fallback error handling, different dashboard views over one typed model, and explicit source refresh provenance. Critical repairs:
1. Separate personal application states from employer-verified opportunity status.
2. Keep unknown dates unknown and verify rolling recruitment via official employer pages.
3. Use immutable application/opportunity IDs and explicit recruitment cycles.
4. Do not expose applicant notes in publicly published Sheets.
5. Capture source hash, fetch time and provenance for every row and support comparison across refreshes.
6. Add contract tests with Google pubhtml HTML fixtures, malformed dates, reordered headers, partial data and duplicate cycles.

## 8. Source references and evidence limits

- [Public Sheet config](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/config.ts)
- [DOM extraction and deadline classification](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/loadPositions.ts)
- [State and refresh](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/store.svelte.ts)
- [Typed position model](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/data/types.ts)
- [User-triggered sheet sync](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/components/SyncCard.svelte)
- [Kanban status display](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/src/lib/views/KanbanView.svelte)
- [Build config](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/package.json)
- [Deploy workflow](https://github.com/PankidT/phd_tracker/blob/16986762c20b100554de2c799301374586ad2c87/.github/workflows/deploy.yml)

**DEEP_REVIEW_DOCUMENTED — static code inspection.** Key ingestion/storage/view paths and repository tree examined. No Google Sheet content, live user records, browser execution, tests, authorization proof, source verification or actual application submission was accessed.
