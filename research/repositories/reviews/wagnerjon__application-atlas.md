# WagnerJon/application-atlas — eight-section static source investigation

**Snapshot:** 1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8; **checked:** 2026-11-12; **validation:** SOURCE_INSPECTION_ONLY; **runtime:** NOT_EXECUTED; **review state:** DEEP_REVIEW_DOCUMENTED.

## 1. Research question and scope

Examine whether a local-first application ledger preserves evolving applicant states, documents, backups and event history without claiming that a job or PhD opportunity is verified. The README presents a native SwiftUI application for macOS 14+ managing job and PhD submissions.

## 2. Snapshot and software organization

43 tracked entries including Sources/App.swift, Models.swift, Pipeline.swift, MapLocations.swift, Backup.swift, SettingsMenu.swift, Tests/StorageTests.swift, BackupTests.swift and CategoryTests.swift, plus build and release workflows. README states MIT licensing, ad-hoc signed releases and no notarization; no independent binary provenance or runtime test performed. Sources were read at the pinned commit.

## 3. State model and calculations

Application in Sources/Models.swift uses stable UUID, role, organization, URL, notes, optional deadline, sent date, categorized job/PhD kind, status enum and dated statusHistory. The computed history returns an undated legacy event when a database predates history support, rather than fabricating earlier dates. Waiting days and deadline days use a supplied Calendar and start-of-day boundaries. Pipeline.swift builds Sankey nodes/edges from each application's recorded transition path, grouping by category and step index.

## 4. Persistence, restore and test evidence

README places applications.json and Attachments under the user's Application Support directory. ApplicationStore writes atomically and sets canWrite=false upon failed load, preventing blind overwrite. Backup.swift version-tags backups, validates duplicate IDs, event alignment, referenced attachment names and path separators, caps payloads, checks geographic coordinates, stages a full replacement and uses an atomic swap while retaining recovery data. CSV export quotes cells and prefixes spreadsheet-formula leading characters to mitigate CSV formula execution. Tests/StorageTests.swift includes cases for historical migrations, copied-submitted attachment immutability, status journey order, offer reminder behavior and backing-store recovery. These are code-level test cases, not executed test results.

## 5. Source trust and personal-data boundary

The application stores applicant-entered states; it does not validate offer existence, official job closing dates, or supervisor funding. No account or server sync is claimed. MapKit geocoding may send city/country place names; README explicitly distinguishes this from sending applicant roles/notes/attachments and says maps are illustrative, not real travel routes. A local disk, backups, and shared machine can still expose sensitive records; encryption-at-rest and secure deletion were not independently verified.

## 6. Reusable techniques

Use immutable submitted-document copies, event-sourced status history without fabricated historical timestamps, typed state enums, transactional backups with filename checks, canWrite safety gate on load failure, casefold-stable categories and CSV injection guards. Pair with source-pinned vacancy claims, time-zone-aware official deadlines and private evidence vault; keep candidate assertions separate from official admissions events.

## 7. Limitations and cross-repo comparison

Strong local ledger and recovery concept compared with simpler browser-localStorage trackers, but macOS-only, single-user, local map and no official position ingestion or verified submission API. It cannot satisfy the eight-country vacancy intelligence requirement alone. Do not assume user-reported offers equal institution-confirmed offers.

## 8. Verdict and source record

DEEP_REVIEW_DOCUMENTED (source-only). High-value engineering design reference; not an official opportunity source. [README](https://github.com/WagnerJon/application-atlas/blob/1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8/README.md), [models](https://github.com/WagnerJon/application-atlas/blob/1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8/Sources/Models.swift), [backup validation and CSV](https://github.com/WagnerJon/application-atlas/blob/1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8/Sources/Backup.swift), [storage tests](https://github.com/WagnerJon/application-atlas/blob/1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8/Tests/StorageTests.swift), [Sankey pipeline](https://github.com/WagnerJon/application-atlas/blob/1bdb0f2b88b0e3fc5118c620e7bb90a27ab2b1e8/Sources/Pipeline.swift).
