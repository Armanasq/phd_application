# TalehMalikov/phd-application-tracker — source-pinned deep static review

**Pinned upstream:** [77baf5b2e17c88732875794a48d6b2b4f0388f13](https://github.com/TalehMalikov/phd-application-tracker/commit/77baf5b2e17c88732875794a48d6b2b4f0388f13), main, checked 2026-11-12. **Runtime:** NOT_TESTED. **License:** no license found. Full evidence: [session source audit](../../sessions/20261112-lukas-taleh-noor-c8d1/reviews/talehmalikov-phd-application-tracker.md).

## 1. Research objective and scope

Assess a fully browser-side checklist and application tracker against the need for durable applicant records, private CV/SOP files, status auditability and accurate deadlines. This is not a vacancy finder or institutional eligibility database.

## 2. Source snapshot and organization

Nine tracked HTML/JS/CSS/README files. Inspected app.js and all six site pages, tracked CSS without a separate rendering audit. Entire workflow runs with static HTML/JS; no build, server database, GitHub Actions, open issues or PRs. [Source](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/app.js).

## 3. State model and storage

Checklist selections and school rows use localStorage, while uploaded CV, SOP, recommendation and emailing materials use IndexedDB blobs indexed by page. Status options cover Researching, Emailed advisor, Writing SOP, Submitted, Interview scheduled and Decision received. The 15 MiB per-file limit is enforced in client code; no evidence-backed submitted receipt or historical status log exists.

## 4. Confirmed source-level vulnerability

[P0/P1] `tracker.html` renders `upcoming.school` directly inside an `innerHTML` template without escaping. The same name is user-editable and stored in localStorage. A malicious HTML value can be parsed on the next stats render. This is a locally supplied/retained-input DOM injection boundary, not evidence of an unauthenticated remote exploit. The application's own file list correctly escapes file names, making the missing stats escaping an inconsistent trust boundary. [Tracker source](https://github.com/TalehMalikov/phd-application-tracker/blob/77baf5b2e17c88732875794a48d6b2b4f0388f13/tracker.html).

## 5. Deadline and durable-custody defects

The “next deadline” calculation sorts all stored dates, including expired ones, and chooses the earliest rather than nearest future deadline. Date-only strings are parsed as UTC instants then rendered in local time, potentially shifting a date in negative UTC offsets. No backup, export/restore, encrypted custody, schema migration or cross-device sync is implemented; browser clearing/eviction can lose applicant documents.

## 6. Interconnections to other applicant trackers

Compared with [WagnerJon/application-atlas](wagnerjon__application-atlas.md) and [NaughtFound/Go2Phd](https://github.com/NaughtFound/Go2Phd), this offers minimal offline-first access but no backup and no trusted status evidence. Google Sheets integrations require user-specific authorization; a browser-only approach avoids backend token custody but introduces browser-origin security and data-loss risks. No sampled application status may be called “verified submission” without receipt.

## 7. Decision and adoption priority

**ADAPT_LOCAL_FIRST_INTERFACE_AFTER_SECURITY_FIXES; P1.** Use checklist structures, page-scoped draft collections and local storage only as optional capture. Replace dynamic HTML interpolation with DOM text nodes, use source-linked deadlines, add data export/restore and append-only application events. Do not adopt its implicit data-durability or policy evidence assumptions.

## 8. Evidence gaps and regression tests

No real browser execution, XSS exploit, timezone replay, file storage migration, origin privacy probe or offline deployment performed. Required tests include HTML payload in school name, civil-date preservation across timezones, all-expired deadlines, file quota/eviction, safe import and export, duplicate program/cycle and restoration of evidence-linked statuses.
