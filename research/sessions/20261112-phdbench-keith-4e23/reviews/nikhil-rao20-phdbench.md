# Nikhil-Rao20/phdbench — deep static implementation review

**Upstream:** https://github.com/Nikhil-Rao20/phdbench
**Pinned revision:** [4ff6ca4948a6dc820366b4a5342f6adbdd6269df](https://github.com/Nikhil-Rao20/phdbench/commit/4ff6ca4948a6dc820366b4a5342f6adbdd6269df)
**Review date:** 2026-11-12
**Review state:** DEEP_STATIC_SOURCE_REVIEW, not runtime or rules-emulator tested.
**License:** MIT in upstream tree.
**Disposition:** Valuable applicant-workspace architecture and tests; do not use its current shared-group authorization rules in a production multi-tenant application.

## Scope, architecture and implementation

Complete recursive tree examined (104 tracked files, including images and dependency lockfile). Read README, Firestore security rules, rule/client parity checks, access logic and tests, group mutation and subscriptions, application persistence and status transitions, lifecycle derivations, deadline normalization, selected UI and deployment code; inspected the latest commit history and open issues/PR lists. Third-party Firebase accounts, data, deployed rules, login and end-to-end browser behaviour were not accessed. Tests were not executed.

React 18 + Vite 6 + Firebase Auth + Firestore + persistent offline cache + PWA; GitHub Pages deployment. Applicant-specific applications, documents, scores, referee status and activity are stored under private user paths. A separate shared group contains common leads and a per-UID state map. Login uses Google; an administrator approves requests. Workflows include leads-to-applications promotion, staged applications, recommendation/document readiness, date-timezone conversion, local export/restore, archive, calendars, email drafting and segmented analytics.

Positive source-level design choices: explicitly separate shared lead facts from applicant-owned applications, avoid marking lead conversion as submission, preserve old application state in migrations instead of fabricating outcomes, default unknown legacy date zones conservatively, reserve private applicant paths, use HTTPS URL scheme validation in the UI, and export shared boards in the backup format. The README claims 114 tests, layout parity and screenshot suites; source test files and automation scripts exist, but their execution results were not reproduced.

## P0 — Firestore group metadata listing exceeds membership boundary

In [firestore.rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules), within the group document match, single-document get is limited to inGroup(gid) or isAdmin(), but the separate collection-list permission is simply **allow list: if approved()**.

This allows *any approved account* to query group documents without the membership filter. Those documents hold memberEmails, members' display names/addresses, invited users and group names. [groupsDb.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js) uses a membership-constrained query for its normal UI, but an API client can issue a different query; the server rule must enforce the restriction. Firestore's [official rules documentation](https://firebase.google.com/docs/firestore/security/rules-conditions) states rules are not client-side filters; [granular get/list behavior](https://firebase.google.com/docs/firestore/security/rules-structure) applies separately.

**Repair:** require list-result membership in server-enforced document conditions, ensure member-filtered queries satisfy rules, and deny unfiltered collection queries. Test with the Firebase Rules emulator for approved non-members and revoked accounts. **Evidence type:** direct static rule semantics, **not** evidence of a live data leak or exploitation.

## P0/P1 — Group members can change another member's personal decision map

A shared lead's state map is keyed by user UID. [groupsDb.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js) intentionally edits only the caller's dot-path through setMyLeadState. However [firestore.rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules) permits **allow update: if inGroup(gid) && sane()** on every shared lead, with no diff constraint on the states object. Any approved group member can therefore supply a direct Firestore update to another UID's state key, changing an archive flag, fit score, priority, or converted decision. The README claims a member cannot disturb anyone else's opinion; that is true of the normal UI's update payload, **not** of the security boundary.

**Repair:** separate per-member state into a subcollection keyed by UID, with server-side owner matching, or enforce a safe nested-map diff allowing only the caller's UID while independently validating the editable shared factual fields. Run adversarial Rules emulator tests, including cross-member update and arbitrary top-level additions. This is a source-level authorization design flaw; no live exploit performed.

## P1 — 'submitted' statistics include applications that missed their deadline

[model.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/model.js) defines SUBMITTED_STAGES by taking **all** stages whose group is not 'preparing'. Both MISSED_DEADLINE and WITHDRAWN are grouped as 'decided', so they are included even if no application was ever submitted. [derive.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/derive.js) uses SUBMITTED_STAGES for submittedApplications and its response-rate denominator. Thus a 'missed deadline' entry can inflate submissions, directly contradicting the README's 'only genuinely submitted applications count'.

[db.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/db.js) sets submittedAt when a user selects SUBMITTED, but the selector is not keyed to receipt evidence or submittedAt. **Repair:** classify a submission only with explicit submittedAt plus an optional verified portal receipt and allow withdrawn pre-submission applications to remain non-submitted; do not infer a submission from the current terminal stage.

## P1 — Published per-account limits are not enforced by server rules

[access.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/access.js) declares 500 leads, 500 applications and 10 groups per user. The Firestore rules enforce a 25-member list cap and per-document size but **not** a cardinality cap on applications/leads/groups. Direct SDK users can bypass client counters. This is a quota/cost-integrity mismatch rather than proof of abuse. Require server-enforced reservation counters, entitlement-aware backend writes, or explicit clarification that caps are client-only.

## P1/P2 — Mutable workflow evidence and collaboration races

- The application stage is mutable and logActivity writes a separate document **after** the stage change; log failures are swallowed, so the timeline is not guaranteed to contain all state transitions. The source does not require an immutable portal acknowledgement for SUBMITTED, INTERVIEW or OFFER.
- Conversion first creates a private application then marks the shared lead converted. The developer explicitly notes the operations are not an atomic batch. A second-write failure can leave the application present and lead shown as active, requiring reconciliation or idempotent retry.
- Deleting a group intentionally deletes its child lead documents before the parent, a necessary Firestore orphan-prevention measure. A concurrent member creating a new lead during deletion can race with the snapshot and leave an orphan; a 'deleting' lock or controlled server-side purge would close the gap.
- Client-side group roleIn may trust members[uid].role while server groupAdmin uses createdBy. The self-claim rule restricts the modified members map key but does not constrain role values or all other top-level fields. Verify UI authorization parity and require safe shape validation rather than relying on client role labels.

## Tests and empirical boundary

The repository contains Vitest tests for access, safety, dates, derivations, migration and toast behaviour; it also has Playwright screenshot/layout/modal harnesses, parity script and GitHub Pages workflow. The UI screenshot harness substitutes in-memory Firebase and a fixture identity; it cannot validate production Firestore rules or OAuth. No rules-emulator security test or upstream runtime/test execution was established here. Source history includes explicit fixes for revoked access, onboarding re-render loops, lost shared-board backups and CSP auth initialization, showing active iteration but not independently audited production assurance.

**Transfer:** adopt candidate-owned application domain separation, timezone objects, staged lifecycle with preparatory states, migration caution, derived readiness, local backups and adversarial test methodology. Reject unrestricted group listing, editable per-user state maps, status-as-receipt accounting and client-only caps for a multi-session PhD research platform.

**Primary evidence:** [rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules), [access tests](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/access.test.js), [rule parity script](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/scripts/check-access-parity.mjs), [groups DB](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js), [lifecycle model](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/model.js), [derivations](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/derive.js), [application DB](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/db.js), [project README](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/README.md).
