# monees007/phd_application_tracker — session investigation

- Repository: https://github.com/monees007/phd_application_tracker
- Inspected revision: `e4a8d1c5050a2cbaa49c376e6811e4b02bcf145d`
- Release observed: `v1.0.0`, published 2026-09-22
- Review status: source-level static investigation; runtime execution not performed
- License: MIT, declared in README
- Issues / pull requests: none returned by the inspected API query
- Scope: repository tree, README, Firestore rules, Flutter models/services, import pipeline, Chrome extension, Cloud Function, tests and change notes

## Purpose and architecture

A Flutter/Android and Chrome extension application tracker. It is optimized for rapid capture of doctoral and research job adverts, not for discovering and verifying opportunities itself.

Capture paths:
1. Android share intent accepts a URL or text.
2. Chrome context-menu action reads selected text or the rendered page DOM.
3. CSV import supports spreadsheet migration.

The mobile path uses `PageFetcher` for ordinary HTTP HTML and `GeminiService` for structured extraction. The Chrome path uses `chrome.scripting.executeScript` to read the rendered DOM, then calls Gemini through extension code. Both write position records into Firestore under `users/{uid}/positions/{id}`.

The core `Position` model includes institution, programme, date-only deadline, inferred-year flag, nullable funded flag, application fee/currency, URL, status, notes, tags, country, applied/result timestamps, archive/reminder flags and a bounded status history. Status buckets are To apply, Pending and Decided.

## Data and operational flow

- `PageFetcher` GETs HTML with a browser-like user agent, enforces HTTP 200 and text/html content, decodes UTF-8, reduces markup to text, and caps model input at 24,000 characters. A page is considered shell-like when it is short or contains fewer than two application-related markers.
- `GeminiService` requests JSON output with temperature zero and a response schema. It asks the model to use null for unstated fields, mark inferred deadline years, distinguish application fees from salary/tuition, and report missing fields.
- `ImportQueueService` persists pending import state in SharedPreferences, retains up to 20 recent imports, records extraction results, and marks still-running jobs failed on next launch. It can save failed shares as notes and supports undoing auto-save.
- `FirestoreService` provides per-user streaming CRUD, status transitions with history, and 400-record batched seed writes.
- `PositionsController` applies local filtering/sorting, computes urgency and upcoming/missed deadlines, and debounces full reminder rescheduling.
- `NotificationService` rebuilds on-device alarms for unsubmitted, non-archived positions, sorting candidates and retaining only the nearest configured alarm budget.
- `DeadlineWidgetProvider` renders a native Android widget from a local snapshot; it recalculates day counts but cannot discover new opportunities without the app refreshing the snapshot.
- Optional Cloud Function is a second reminder channel requiring Blaze billing and FCM device tokens.

## Verified implementation strengths

1. Cross-surface capture reduces manual transcription and preserves original advert text.
2. Rendered-DOM extraction solves an important limitation of plain HTTP retrieval for JavaScript-heavy job boards.
3. Nullable extraction fields and `deadlineYearAssumed` avoid silently representing every field/date as known.
4. Failed imports are retained instead of dropped.
5. Owner-only Firestore rules scope all position records to the authenticated UID; unmatched paths default deny.
6. CSV import/export and deterministic seed IDs reduce lock-in.
7. Status history and timestamps preserve basic application lifecycle evidence.
8. On-device reminders work offline and avoid a mandatory recurring server cost.

## Defects, risks and limits

- **Extraction confidence is not evidence verification.** `_isConfident` auto-saves when the model's confidence is not low and institution is non-empty. This is a UX threshold, not a verified claim state.
- **Funding semantics are too coarse.** `funded: bool?` cannot distinguish tuition waiver, stipend, salary, duration, fees, international coverage or eligibility. The extractor prompt treats explicit salaried/stipend language as funded, but does not validate contract terms.
- **Mobile and Chrome differ.** The extension can inspect rendered DOM; the mobile HTTP fetcher cannot. Their extraction and failure/save behavior must not be assumed identical.
- **HTML reduction is approximate.** Regex-based stripping may lose table structure, headings, scope relationships and deadline context. Character caps may truncate material requirements.
- **URL fetching lacks an evidenced SSRF/redirect policy in the inspected `PageFetcher`.** User-supplied links should be constrained with HTTPS policy, DNS/IP validation, redirect revalidation, private-network blocking, content-size limits and timeouts.
- **Model key storage is plaintext** in app preferences and extension storage. The README explicitly warns about this.
- **Import durability is limited.** Work runs in the app isolate; force-closing the process can interrupt an import. The queue is persisted but not a background worker with guaranteed execution.
- **Cloud reminder date mismatch.** The optional function schedules at 09:00 Europe/Stockholm but calculates `today` using UTC day boundaries. Near timezone boundaries, matching can select the wrong calendar date. It also needs the documented FCM token subcollection and Blaze billing.
- **Full-advert notes have scale implications.** Firestore document size is capped by rules at 40,000 characters, and the model code caps page text at 24,000. The controller streams all position records, so storage/network cost grows with archived adverts.
- **Date model is date-only and uses local calendar arithmetic.** It does not retain source timezone or explicit local deadline time; this is insufficient for globally distributed deadlines with exact submission cutoffs.
- **Security rules validate only selected fields.** They do not enforce a rich field schema for all optional fields, and clients are trusted to set status/history values.
- No upstream test execution, emulator test, Firebase security-rules test, or live Gemini test was performed in this session.

## PhD Atlas transfer

Adopt:
- browser-rendered capture as a separate adapter from HTTP fetching;
- preservation of raw advert text and original URL;
- explicit inferred-date flags;
- import failure retention and retry;
- CSV portability;
- per-applicant isolation;
- bounded reminder scheduling.

Do not adopt:
- model-confidence-based promotion to verified status;
- boolean-only funding;
- a date-only model without timezone and time semantics;
- plaintext API-key storage;
- unrestricted URL fetching;
- a client-controlled approval state.

Recommended Atlas pipeline: `captured -> source_fetched -> extracted -> field_evidence_attached -> official_source_checked -> cycle_scoped -> funding_verified -> eligibility_checked -> human_approved -> actionable`. Keep public opportunity evidence separate from private applicant state.

## Provenance and coverage

Files inspected: README, `firestore.rules`, `pubspec.yaml`, `firebase.json`, `firestore.indexes.json`, `lib/models/position.dart`, `lib/services/gemini_service.dart`, `lib/services/import_queue_service.dart`, `lib/services/page_fetcher.dart`, `lib/services/firestore_service.dart`, `lib/services/auth_service.dart`, `lib/services/csv_service.dart`, `lib/services/notification_service.dart`, `lib/state/positions_controller.dart`, `chrome_extension/background.js`, extension manifest/config/auth/firestore/Gemini files, `functions/index.js`, `test/position_test.dart`, `lib/CHANGES.md`, and README.

Not inspected or not verified: every UI screen and Kotlin widget source, all dependency transitive source, live Firestore deployment, rules emulator, model output accuracy, current API/model availability, actual APK/CRX binary behavior, and live push notifications. This is a focused source-level audit, not runtime validation.
