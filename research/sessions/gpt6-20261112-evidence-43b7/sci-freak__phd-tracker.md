# sci-freak/phd-tracker — pinned source investigation

- Revision: `13afd78b8302674caabd21036f90020aa788aa62`
- Inspected on: 2026-11-12
- State: **DEEP_STATIC_READY_FOR_CANONICAL_RECONCILIATION**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: PENDING (do not count this session report as a canonical audited candidate)

## 1. Purpose

Cross-platform React/Vite and Expo application workflow for statuses, institutions, documents, recommendations and deadlines.

## 2. Architecture

Monorepo shared JS schemas with mobile/web clients and Firebase Firestore/Storage; source code and authored rules inspected.

## 3. Data flow

firestore.rules and storage.rules scope user documents to matching request.auth.uid; actual deployed rules were not confirmed.

## 4. Critical correctness

DataService.uploadDocumentForUser catches Firebase Storage failure and embeds entire base64 document dataUrl into a Firestore record; this silently alters storage/privacy/size semantics and is an anti-pattern for sensitive applicant files.

## 5. Identity and state

Guest-to-account merge and JSON/CSV imports carry user-supplied data. Conflict confirmation exists, but nested document data require robust schema/size validation and rollback.

## 6. Security and privacy

syncCloudDocuments deletes existing remote storage objects while writing replacements; no cross-resource transaction was established.

## 7. Validation boundaries

Shared tests check normalization, date and application status behavior; Firebase integration, security rules and device sync were NOT executed.

## 8. Transfer verdict

Adopt per-user access controls and shared normalization, but require explicit upload failure state, private encrypted file handling, idempotent sync, retention controls and verified deployment.

## Pinned upstream source paths

- [README.md](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/README.md)
- [src/services/DataService.js](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/src/services/DataService.js)
- [firestore.rules](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/firestore.rules)
- [storage.rules](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/storage.rules)
- [src/hooks/useGuestMerge.js](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/src/hooks/useGuestMerge.js)
- [packages/shared/test/run-shared-tests.mjs](https://github.com/sci-freak/phd-tracker/blob/13afd78b8302674caabd21036f90020aa788aa62/packages/shared/test/run-shared-tests.mjs)
