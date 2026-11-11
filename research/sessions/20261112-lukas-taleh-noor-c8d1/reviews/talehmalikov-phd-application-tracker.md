# TalehMalikov/phd-application-tracker — static source investigation

**Original:** https://github.com/TalehMalikov/phd-application-tracker  
**Pinned revision:** [77baf5b2e17c88732875794a48d6b2b4f0388f13](https://github.com/TalehMalikov/phd-application-tracker/commit/77baf5b2e17c88732875794a48d6b2b4f0388f13)  
**As inspected:** 2026-11-12. **Last push:** 2026-08-27. No license file, tests, CI or open upstream PR/issue found in the inspected sources.  
**Review:** DEEP_REVIEW_DOCUMENTED — all 9 tracked source filenames inventoried; README, complete app.js, HTML pages inspected; CSS inventoried but not manually audited. Static only; no live browser or IndexedDB execution.

## 1. Purpose and architecture

This is a client-only PhD preparation tracker: home shortlist, CV, statement of purpose, professor emailing, recommendations and school/application-status tracker. No backend, JavaScript package manager or build pipeline. `index.html` and `tracker.html` use shared `app.js`; each checklist is embedded as a static data array in its respective HTML page.

- `localStorage`: shared checklist state under `phd_checklist`, schools under `phd_schools`.
- `IndexedDB`: `phdtrack_files` / `files` object store, indexed by page; retains uploaded CV, SOP, outreach and recommender-preparation files as browser blobs. A per-file upper bound of 15 MiB is checked before write.
- Status vocabulary: Researching, Emailed advisor, Writing SOP, Submitted, Interview scheduled, Decision received. No provenance or status-change history.
- File names are escaped before inclusion in dynamic HTML by `escapeHtml`, a correct safety measure at that specific display site.

Evidence: [app.js](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js), [README.md](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/README.md), [tracker.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html).

## 2. Source-confirmed issues

**P0/P1 — persistent client-side HTML injection from tracked university name.**

`renderSchoolList()` stores user-edited school names in localStorage. The `tracker.html` function `renderTrackerStats()` retrieves the earliest dated row and interpolates `upcoming.school` directly into an `innerHTML` template without `escapeHtml` or `textContent`. A school string containing HTML is parsed as markup whenever the stats panel rerenders; script-capable HTML payloads can execute in the site's origin. The intended school-name text field is locally controlled, so this is not evidence of a remote unauthenticated attack, but pasted/shared strings or compromised browser-origin state create a persistent DOM injection path. The app also stores sensitive applicant drafts in the same origin's IndexedDB; an origin-level injection could potentially read/exfiltrate such data, subject to browser permissions. Use DOM node creation with `textContent` for the school name and fixed date format, never string concatenation into HTML.

Evidence: [tracker.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html), [app.js](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js).

**P1 — reported next deadline may already be expired.** `renderTrackerStats()` filters only for non-empty deadline, creates Date instances, and chooses earliest. It does not require a future deadline. In a tracker containing past applications, the "Next deadline" card can show an expired date instead of the next actionable deadline. Parse calendar dates explicitly and filter by current local date and verified status.

Evidence: [tracker.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html).

**P1 — deadline date can shift across timezones.** Dates are entered through HTML `input type=date` (calendar string `YYYY-MM-DD`), then converted with `new Date(s.deadline)`; JavaScript interprets date-only ISO strings at UTC midnight. `toLocaleDateString()` in a timezone behind UTC can display the preceding day. Retain local civil dates until display, converting only with explicit timezone semantics.

Evidence: [app.js](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js), [tracker.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html).

**P1 — no durable applicant backup or import/export workflow.** The read/write path is browser origin storage only. No CSV/JSON export, version history, synchronization, cryptographic backup, document integrity hash, migration or recovery from browser clearing/eviction is present in the tracked code. A device change or origin migration can lose statuses and files. IndexedDB blob storage is not equivalent to durable document custody.

Evidence: [app.js](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js), [README.md](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/README.md).

**P1 — statuses are editable assertions, not verifiable outcomes.** A single status per school is overwritten on change. No transcript of advisor correspondence, application submission ID, actual portal URL, deadline source/cycle, funding terms, acceptance letter or supporting evidence is retained. "Submitted" and "Decision received" counts are not independently verified facts. Statuses cannot distinguish application track/department when one university has multiple openings.

Evidence: [app.js](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js), [index.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/index.html), [tracker.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html).

**P2 — scope of "nothing sent over the network" is imprecise.** The JavaScript source does not implement network upload for user documents, but HTML pages load Google Fonts CSS from an external domain. Therefore a general no-network-traffic claim is too broad; user document blobs appear local in inspected code. This distinction matters for privacy documentation.

Evidence: [cv.html](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/cv.html), [README.md](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/README.md).

## 3. Usable design patterns

This is a good minimal baseline for a personal applicant workbench: serverless browser storage, low-friction checklists, isolated draft collections, explicit user-controlled status labels and no obligatory external account. To adopt safely, separate raw source facts, user notes, and sensitive files into independently permissioned data domains. Use escaped DOM updates; export/restore; source-linked verified deadlines; school/program/opportunity ID rather than school name alone; and append-only evidence-backed status events.

Cross-source connection: compare the local-only state with [NaughtFound/Go2Phd](https://github.com/NaughtFound/Go2Phd)'s read-only Google Sheets adapter. Both are applicant-side capture surfaces, **not live evidence of admissions or funding**. A future Atlas system can offer local-first capture and optional Sheets import without routing OAuth refresh tokens as arbitrary request headers.

## 4. Suggested regression tests and limitations

Tests to add: malicious school names rendered safely in stats, pasted bracket/quotes and Unicode, same university with multiple departments/cycles, all deadlines expired, timezone behind UTC, file deletion and re-download, backup/restore completeness, storage quota and storage eviction, and status change auditability. No browser tests were run; the DOM-injection path is a direct source-level trace, not a performed exploit.
