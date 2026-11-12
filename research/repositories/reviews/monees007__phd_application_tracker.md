# monees007/phd_application_tracker — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d`](https://github.com/monees007/phd_application_tracker/commit/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d)  
**Review state:** DEEP_REVIEW_DOCUMENTED. Risk-focused static implementation inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** mobile_application_capture  
**Primary risk:** model_confidence_bypasses_source_truth_and_automatic_import  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

The project addresses friction in capturing a doctoral opportunity from a mobile browser or a rendered page into an application tracker. Its meaningful contribution is not a funding search algorithm: it is reliable capture despite page-rendering differences, interrupted mobile processes, unavailable model APIs and imperfect extraction. Unlike a fully autonomous applicant, the code primarily saves vacancy leads and reminds the applicant to act.

## 2. Architecture and actual components

The architecture has a Flutter client, a Chromium Manifest V3 `activeTab` capture extension, Gemini extraction through a direct HTTP service, Firebase Auth/Firestore, local SharedPreferences, and optional Firebase Cloud Functions deadline reminders. `ImportQueueService` is a persistent transport boundary, not a background OS worker: its own comments acknowledge that Android may kill the app before completion. `PendingImport` stores URL, raw shared text, run state, extracted JSON, error/hint and resulting position ID; state is retained when an API request fails.

## 3. Task-to-data flow and dependencies

Trace: user shares URL or selected text -> append `PendingImport(running)` -> prefer shared text of sufficient length, otherwise fetch URL -> detect JavaScript-empty page -> call Gemini schema-constrained extraction -> persist extracted nullable facts -> save a new `Position` in Firestore if authenticated, or keep queue for review -> notify user -> support retry/undo. Failure to extract can still save a `needs-details` note containing up to 20,000 characters of source text. Chrome extension obtains the rendered DOM via a user-triggered context-menu click, handling pages Flutter's plain GET cannot parse.

## 4. Methods and source-level evidence

`ExtractedPosition` explicitly distinguishes missing funding, application fee, deadline and deadline-year assumption. The prompt instructs the model to return null when not stated; however `_isConfident` considers any non-low confidence plus a university name sufficient for automatic insertion. That is not a test of official-source authenticity, fully funded terms, eligible citizenship, degree prerequisites, or correct deadline time. `funded: true` is at best an extracted claim and has neither a citation span nor an international tuition audit. Persistent notes are helpful provenance but not verified evidence.

## 5. Implementation and operational reconstruction

Transfer the resilience pattern: every capture creates a durable ingest event before any network call; store original URL and content hash; on failure preserve a retriable review item rather than losing the lead; distinguish page-content acquisition, field extraction, source validation and acceptance. The Chrome `activeTab` pattern is useful where terms and privacy permit user-mediated rendered-page capture. For PhD Atlas, explicitly require source and applicant-specific verification before a record enters the actionable-funded queue.

## 6. Failure modes and validation gaps

Risks: app-killed mid-run leaves a recovered failed item rather than seamless resumption; unauthenticated `_store` returns null, so a locally completed extraction is not a submitted cloud record; model-controlled confidence bypasses checking; client-app key management and logged source text require privacy review. Firestore rules restrict documents under authenticated user UID but not substantive truth. Optional cloud reminder requires FCM device-token setup and paid scheduler; source does not demonstrate it running. The test file checks status and date behavior, not live LLM or funding accuracy.

## 7. Transfer to PhD Atlas and admissions workflow

Adopt a `capture -> extraction -> independent validation -> candidate review -> accepted opportunity` state machine, preserving `needs-details` until source proof exists. Add `source_snapshot`, `field_evidence`, `model_version`, `deadline_year_explicit`, `funding_scope`, `eligibility_scope`, `retry_count` and `human_review_receipt`. Store private CV and documents outside the public research repository; do not auto-publish model-detected funding or claim applicant action without official confirmation.

## 8. Provenance and outstanding verification

Inspected source files linked below at the specified commit, including Flutter queue/Gemini logic, Chrome extension capture, security rules, optional reminder and date tests. Additional Flutter UI/controllers and all network services remain for later file-level inspection. No Flutter tests, Firebase emulator, browser extension or live Gemini extraction were executed; performance and factual extraction quality are UNKNOWN.

## Pinned source files inspected

- [`lib/services/import_queue_service.dart`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/lib/services/import_queue_service.dart)
- [`lib/services/gemini_service.dart`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/lib/services/gemini_service.dart)
- [`lib/models/position.dart`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/lib/models/position.dart)
- [`chrome_extension/background.js`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/chrome_extension/background.js)
- [`chrome_extension/manifest.json`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/chrome_extension/manifest.json)
- [`firestore.rules`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/firestore.rules)
- [`functions/index.js`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/functions/index.js)
- [`test/position_test.dart`](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/test/position_test.dart)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.

## Additional pinned implementation reinspection — 2026-11-12

**Confirmed code paths at `e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d` (default branch `master`):** `lib/services/import_queue_service.dart` (543 lines) maintains recoverable `PendingImport` records in local SharedPreferences, supports retry, interruption recovery and undo, and checks `FirebaseAuth.instance.currentUser?.uid` when constructing the Firestore service. `_isConfident(ExtractedPosition e)` only requires `e.confidence != 'low'` and a nonempty university name; neither a quoted official vacancy, current-cycle deadline, funding terms nor applicant eligibility is required before `_autoSave`. Text explicitly pasted through `runWithText` disables silent auto-save, a useful boundary that is *not* extended to all shared pages. The fallback note preserves unverified source text for review.

`lib/services/gemini_service.dart` (376 lines) defines optional fields, a `deadlineYearExplicit` flag, a model-provided `confidence`, and requests schema-structured extraction via the Gemini API; schema validation is not source-owner authentication. `chrome_extension/background.js` captures a browser-rendered page or selected text via user action, converts it into the same save-or-note workflow, and records whether deadline year was assumed. `lib/services/firestore_service.dart` uses user-scoped Firebase documents; deployed Firestore rules were **not** examined. `test/position_test.dart` tests local date/status-bucket urgency but not LLM extraction truthfulness, official-source validation, cross-user database authorization or automatic-save safety. No live tests run.

**Transfer:** adopt resumable queue, user-triggered DOM capture, nullable typed claims, deadline-year uncertainty, notes with manual retry, undo and per-user storage. Require an explicit `UNVERIFIED_SOURCE` state and human confirmation of official original source/date/fees/funding before promoting any scholarship or funded position to an actionable verified offer. GitHub metadata at inspection: no open upstream PR or issue; no license recognized by GitHub; last upstream push 2026-09-22. [queue](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/lib/services/import_queue_service.dart), [extractor](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/lib/services/gemini_service.dart), [extension](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/chrome_extension/background.js), [tests](https://github.com/monees007/phd_application_tracker/blob/e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d/test/position_test.dart).
