# 0612Leo/phd-application-tracker — focused source review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [31c372cb2ae4df16cc4b1b1ae1c55bd167e93887](https://github.com/0612Leo/phd-application-tracker/commit/31c372cb2ae4df16cc4b1b1ae1c55bd167e93887); latest commit observed 2026-06-16.
- **Category:** minimal daily application/research journal.
- **Review state:** PRELIMINARY_FOCUSED. Static review of the browser application and its data flow; no runtime tests executed.
- **License:** no explicit license metadata or license file confirmed in this pass.

## 1. Problem and intended user

A small, single-page tracker records daily research reading, English practice, supervisor outreach, application stage, focus, mood, wins and next actions. It is a daily execution journal, not an opportunity-discovery system or application CRM.

## 2. Architecture and data flow

The application is plain browser HTML/CSS/JavaScript. All records are stored under one localStorage key. The UI loads a JSON object, applies the selected date to the form, derives weekly totals, renders history cards, and supports JSON export/import. There is no backend, account model, synchronization, evidence store or external service dependency.

Primary implementation: [app.js](https://github.com/0612Leo/phd-application-tracker/blob/31c372cb2ae4df16cc4b1b1ae1c55bd167e93887/app.js).

## 3. Useful implementation ideas

- Low operational complexity and offline-capable daily capture.
- A compact daily record combines research activity, outreach and next action.
- JSON export makes the state portable without a server.
- Weekly aggregation is simple and understandable; the user can inspect the underlying records.

## 4. Correctness and security findings

The import path checks only that parsed JSON is a top-level object. It merges arbitrary keys and values into localStorage without validating the date key, field types, numeric ranges or record schema. The history renderer interpolates record fields such as date and reflection text into `innerHTML` without HTML escaping. Consequently, importing an untrusted or malicious export can create persistent markup/script injection in the local application origin. This is an import-triggered stored-XSS risk, not evidence of a remotely exploitable server endpoint.

The date key is derived from UTC ISO time while date selection and week calculations use local Date parsing. Around local midnight and timezone boundaries, the displayed day and the stored key can diverge. The system has no migration/versioning strategy beyond the storage-key suffix and no automatic backup.

## 5. Data and evidence quality

The app records user-entered activity, not independently verified admissions facts. It does not model source URLs, effective cycles, funding terms, eligibility or claim-level evidence. The weekly summary is operational self-report and should not be treated as evidence of application progress unless linked to actual submitted artifacts.

## 6. Testing and operational maturity

No automated test suite or schema-validation layer was identified in the inspected files. Import/export, date-boundary behavior, malformed values, quota errors and malicious HTML payloads were not executed in a browser during this review.

## 7. Adoption judgment

**ADAPT THE DAILY-JOURNAL CONCEPT, NOT THE DATA MODEL.** A small daily execution log can complement PhD Atlas, but its records should link to canonical application, opportunity and evidence IDs. Use structured validation, safe DOM text rendering, versioned exports and an explicit backup/restore path before importing the implementation.

## 8. Unresolved work

Inspect the full repository and issue history; test timezone boundaries and browser storage limits; verify all form constraints; add schema migrations and safe import validation; assess accessibility and mobile layout. This is not a complete software audit.