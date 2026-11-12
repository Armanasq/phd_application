# imranbinyounos/PhdApply — deep local-first macOS admissions tracker audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/imranbinyounos/PhdApply | **Pinned revision:** [`091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e`](https://github.com/imranbinyounos/PhdApply/commit/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e) | **State:** DEEP_REVIEW_DOCUMENTED (Swift source static) | **Decision:** adapt local state schema, interaction journal and notices; require privacy-safe storage and verified submission events.

## 1. Actual purpose and source structure

A native SwiftUI/macOS PhD application planning app, branded GradKit Pro, with SwiftData application records, university/professor/scholarship tables, customizable columns, CSV import/export, mailto templates and local deadline notifications. The inspected tree includes project and Xcode config, eleven Swift source/test files and binaries/assets. Last observed upstream update: 2025-07-27. It is a local single-user tracker, not a live university vacancy crawler, verified funding source or actual submission client.

## 2. Primary domain model

`Models.swift` declares `ApplicationRecord` with UUID, professor name/email, university, department, research interests, deadline, priority, notes, links, interaction log and timestamps. `ApplicationStatus` states include `Researching`, `Drafting Email`, `Contacted`, `Awaiting Response`, `Interview Scheduled`, `Submitted`, `Accepted`, and `Rejected`. `InteractionLog` distinguishes sent email, received email, meetings and free notes, a useful foundation for an event ledger.

The statuses are **user-mutated enum values**. Code does not require message-id, portal receipt, institution decision letter, or proof of funded admission before setting “Submitted” or “Accepted.” Use self-reported or draft state explicitly in a research-grade successor.

## 3. Persistence layers and migrations

The SwiftData `@Model` application stores nested link and interaction objects with cascading delete rules. Separately, `GradKitStore.swift` persists dynamic tables (universities, professors, scholarships) by JSON-encoding one `GradKitDB` into `UserDefaults.standard` under `phdapply:v3-custom-columns`. On initialization, it adds mandatory status columns to older table definitions and rewrites state.

This is local-first and avoids mandatory external LLM transmission, but `UserDefaults` is not encrypted private-document storage. The table model has no stable row UUID, source/provenance identifier, signed application evidence, multi-device merge, backup/restore lifecycle or external institution database. Reordering/deleting rows changes positional identity.

## 4. CSV import/export correctness and privacy

`Services.swift:CSVService` writes CSV for professor/application records, including email addresses, interests, notes, links, status and priority, with quoted-field escaping and ISO dates. Its importer is a hand-written per-line CSV parser with heuristic header skipping and defaults unknown status strings to `Researching`. It does not preserve immutable UUIDs, interaction logs, creation/update timestamps or every custom field, so import→export→import is **not** a lossless identity/event-history round trip.

The `GradKitCSVService` export concatenates three independently formatted section tables with `# Section` headers. It does not expose a versioned workbook schema or corresponding section importer in the inspected code. Personal applicant/contact data in CSV exports are unencrypted and require local access/retention controls.

## 5. Mail composition and delivery semantics

`EmailService.composeEmail()` percent-encodes subject/body into a `mailto:` URL and opens it using `NSWorkspace.shared.open`. This opens a user mail client, not a verified outbound send or recipient delivery. A status of “Contacted” or an `Email Sent` interaction written manually must be tagged `USER_REPORTED` until confirmed by a sent-message record.

No bulk faculty outreach, university portal application automation, verified professor hiring status, or GDPR/consent workflow is present.

## 6. Deadline reminders and time boundary

`NotificationService.scheduleDeadlineNotification()` uses `Calendar.current` to subtract days from a manually entered `deadline` and registers a local `UNCalendarNotificationTrigger`. `daysUntilDeadline` operates on start-of-day local calendar dates. Neither stores an institution's exact closing timezone/cutoff, a recruitment cycle, or a verified source timestamp. A local notification may be correct for a user-entered date while the official portal closes earlier in another zone.

There is no automated authoritative website recheck; scholarship amount/eligibility and professor availability remain unknown unless separately researched.

## 7. Validation and transfer decision

The Xcode project includes test targets, but the observed `PhdApplyTests.swift` is only a generated minimal test scaffold and does not validate application state, CSV round trips, migrations, receipt-gated transitions or reminders. No Xcode compile, device test or iCloud synchronization test was performed.

Transferable: typed states, separate university/professor/award categories, contact interactions, local-first workflow, reminder scheduling, editable tables and CSV export. Require an immutable event/receipt ledger, authenticated/private document references, precise deadline timezones, source-claim provenance, stable row IDs, robust RFC-compatible CSV import and explicit backup/restore testing.

## 8. Pinned implementation evidence

- [SwiftData application states/models](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/Models.swift)
- [Dynamic table store and migration](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/GradKitStore.swift)
- [CSV, mailto and local notifications](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/Services.swift)
- [Application tests](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApplyTests/PhdApplyTests.swift)
- [GradKit views](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/GradKitProViews.swift)

**DEEP_REVIEW_DOCUMENTED — static macOS source audit.** No real personal data, email sending, application submission, current admissions/country regulations, Swift/Xcode runtime or official funding source was independently verified.
