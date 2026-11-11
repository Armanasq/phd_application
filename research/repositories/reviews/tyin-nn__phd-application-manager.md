# Tyin-nn/phd-application-manager — eight-section static source investigation

**Snapshot:** 23b1a01294c077e3469053782f061950ecb01a57; **checked:** 2026-11-12; **validation:** SOURCE_INSPECTION_ONLY; **runtime:** NOT_EXECUTED; **review state:** DEEP_REVIEW_DOCUMENTED.

## 1. Purpose and actual audience

Chinese-language single-page, no-build PhD application manager combining saved programs, submission statuses, recommendation letter assignments, document editing, program materials and local map. application_materials includes CV, motivation letter, research proposal, cold email and recommender checklist templates. The checklist is explicitly focused on Northern European position-based doctorates plus selected Australia, China and UAE astronomy programs.

## 2. Repository and deployment model

43 tracked entries including index.html, css/style.css, js/state.js, js/backup.js, page components, js/seed.js and a vendored jsVectorMap. MIT license is stated in README; an external professor roster or central vacancy API is not demonstrated. Source was reviewed at pinned revision; browser run and dependency audit were not performed.

## 3. State ownership and migration

js/state.js stores programs, materials per program ID, recommenders and documents under phd_app_state in localStorage. AppState.init handles versioned prior saved data and calls migrate to append new seed programs and document templates while retaining prior edits. Migration uses institution name as a merge key for programs, title for documents, rather than stable external opportunity identifiers; same-institution multiple PhD openings could be merged incorrectly. There are explicit statuses for inquiry, preparing, submitted, interview, offer, rejection and withdrawal.

## 4. Document and recommender workflow

Application-specific materials track completion, inapplicability, notes and progress. Documents carry versions; recommendation assignments link recommender IDs to program IDs. Backups are client-side JSON exports/imports. js/backup.js asks confirmation before overwriting all current state; the importData validator only checks app marker and programs array, then writes to localStorage. An untrusted import could introduce malformed nested values; data loss and integrity need stronger schema validation, size limits and rollback.

## 5. Official evidence verification boundaries

The checklist contains program-specific 2026/27 deadlines and language requirements including ANU, NYUAD and Westlake, but these are third-party author notes, not official pages independently rechecked in this audit. The README says user-private supervisor and personal drafts were excluded from the public repo; the sample seed list still requires source validation. A local status marked Offer is user input, not proof of an award.

## 6. Privacy, operations and security

LocalStorage holds personally sensitive applicant details, letter drafts and contacts in ordinary browser origin storage. No server transfer is claimed, but data may be exposed by same-origin script compromise, browser sync/backups or shared devices. Offline jsVectorMap is useful for portability. Version mismatch migration avoids forced reset, but missing encryption and strong import schema checks prevent treating it as a secure applicant vault.

## 7. Transfer to canonical research system

Adopt program-specific checklists, separate candidate status from verifiable official status, recommender assignment, explicit unknown/not-applicable flags and non-destructive data migrations. Replace institution-name dedupe with URL/official requisition ID, record original source timestamps and deadline timezone, and store applicant materials in private encrypted storage with role-based permissions and backup controls. This project complements rather than replaces evidence-grounded source ingestion.

## 8. Verdict and pinned evidence

DEEP_REVIEW_DOCUMENTED (static source review). Useful as a localized workflow template; don't reuse unverified 2027 application dates or assume browser storage is a protected evidence vault. [README](https://github.com/Tyin-nn/phd-application-manager/blob/23b1a01294c077e3469053782f061950ecb01a57/README.md), [state and migration](https://github.com/Tyin-nn/phd-application-manager/blob/23b1a01294c077e3469053782f061950ecb01a57/js/state.js), [backup import](https://github.com/Tyin-nn/phd-application-manager/blob/23b1a01294c077e3469053782f061950ecb01a57/js/backup.js), [application checklist](https://github.com/Tyin-nn/phd-application-manager/blob/23b1a01294c077e3469053782f061950ecb01a57/application_materials/06_ApplicationChecklist.md).
