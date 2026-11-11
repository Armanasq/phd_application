# Deep static audit — Nikhil-Rao20/phdbench

**Inspected:** 2026-11-12. **Pinned upstream commit:** [`4ff6ca4948a6dc820366b4a5342f6adbdd6269df`](https://github.com/Nikhil-Rao20/phdbench/commit/4ff6ca4948a6dc820366b4a5342f6adbdd6269df). **State:** DEEP_REVIEW_DOCUMENTED, static source and security-rules review, NOT a live or emulator-tested exploit. **Verdict:** selectively adopt applicant workflow architecture; **reject existing group authorization and submitted-count semantics** as production evidence.

## 1. Repository, scope, maintenance and inspected material

PhDBench is a collaborative PhD application tracking app built with React/Vite, Firebase Authentication, Firestore and an offline-capable PWA. The inspected upstream tree contains 104 files. Applicant-specific applications, documents, progress states and recommendation readiness are distinct from group-shared vacancy leads and per-user states. Source review covered Firestore authorization rules, group persistence and mutation logic, stage taxonomy, derived analytics and selected access/tests, plus the upstream README and CI presence. The original session audit additionally enumerated source/Playwright tests and release history. No Firebase user accounts, production data, browser or Rules emulator were accessed.

Upstream sources: [rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules), [model](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/model.js), [group client](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js). Original supplemental: [full session audit](../../sessions/20261112-phdbench-keith-4e23/reviews/nikhil-rao20-phdbench.md).

## 2. Domain model, dataflow and privacy separation

Google-authenticated users manage private per-applicant application records; group records store shared vacancy leads and nested `states.{uid}` personal preference maps. Users can add and rank leads, convert a lead to their own application, track lifecycle stages, recommendations, deadlines and documents, and export/import backups. Dates have explicit timezone normalization, including conservative treatment of unknown legacy timezone fields. The UI is applicant-workspace software, not a crawler or independently verified funded-vacancy provider.

A correct integration must split **public opportunity observations** from **privately authorized application state**, then separately identify verification provenance, institution/programme/source identity, candidate eligibility and portal receipt. Group membership is a permission boundary, not a front-end display option.

## 3. P0: shared-group list authorization is too broad

In [firestore.rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules), line 179 limits individual group `get` to `inGroup(gid) || isAdmin()`, whereas line 184 independently allows collection `list` when `approved()`. A merely approved account need not belong to the group whose document it queries. The normal client sends a membership-filtered query, but Firestore rules protect all SDK requests, not only the UI's selected query.

Group documents can contain group names, members and invitations. Thus the source exposes a possible cross-group metadata-discovery authorization gap. This is a deterministic rules discrepancy, **not** evidence that an unauthorized account was tested or that a real person's data was accessed. Require membership-scoped listing with emulator tests for approved non-members, revoked users, mixed-membership queries and administrative exceptions. Follow Google's rules-not-filters semantics: [Firestore security rules conditions](https://firebase.google.com/docs/firestore/security/rules-conditions).

## 4. P0/P1: per-user state updates rely on client restraint

A shared lead's `states` map is keyed by Firebase user UID. The normal client [setMyLeadState](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js) writes `states.${uid}.${key}`, which correctly scopes the *intended* update. However the general shared-lead [rule](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules) permits `allow update: if inGroup(gid) && sane()` without a nested-diff check proving only the caller's UID changed.

An authorized group member using a custom SDK request could therefore attempt changing another member's personal priority/archive/conversion fields. Client-side behavior is not a security guarantee. Prefer `groups/{gid}/leads/{leadId}/memberStates/{uid}` with a server UID ownership rule, or explicit map-key diff validation. Add negative tests for cross-member updates and self-granted roles.

## 5. P1: reported application submissions are not evidence-backed

The exact [stage model](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/model.js) at line 147 computes `SUBMITTED_STAGES = STAGE_ORDER.filter(s => STAGES[s].group !== 'preparing')`. Both `MISSED_DEADLINE` and `WITHDRAWN` are terminal non-preparing groups, even if no application was ever submitted. [derive.js](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/derive.js) lines 67–81 counts all those stages as submitted and uses the result in response-rate denominators.

This can inflate application/submission outcomes and confound both research statistics and applicant planning. A stage is **not proof**; require an independently recorded `submittedAt`, external portal acknowledgement/evidence reference and coherent event history. Withdrawn-before-submission and missed-deadline must remain non-submitted unless a prior receipt exists.

## 6. Consistency, quotas, tests and deployment boundaries

The client uses a multistep lead-to-application conversion where the personal application can be written before the shared conversion marker. A second-write failure requires idempotent reconciliation; these operations are not documented as one Firestore transaction. Stage updates and activity log writes are separate, so timeline failure can leave records with no corresponding immutable event. Published 500-application/500-lead/10-group usage limits are declared by client logic, not by server-enforced Firestore cardinality limits. Those are quota/accounting boundaries rather than proven abuse.

The repository contains unit tests for dates/access/derived status, UI screenshot fixtures and CI workflow, but the audited source did not establish negative Firebase Security Rules emulator tests exercising the listed rules. No upstream tests were executed by this investigation. Do not interpret existing green CI as verification of multi-tenant authorization.

## 7. Cross-project synthesis and transferable design

Useful patterns: separate shared opportunity facts and private candidate decisions, explicit historical timezone behavior, staged applicant lifecycle, document/recommender readiness, export/backups and typed screen-derived analytics. Distinguish collaboration membership from applicant ownership and avoid promoting tentative opportunities to verified open jobs.

Compare the [Java 2015 portal review](deepak0004__phd-admission.md), which illustrates unsafe flat-file and unauthenticated admin separation, and the [source-verified research-command-center audit](fsuitoal-code__phd-application-command-center.md), which illustrates fail-closed local data and research-domain-scoping defects. A unified design needs server-side policy enforcement, immutable evidence, per-claim provenance, concurrency-safe conversion, and exact official vacancy identity. Multiple source listings are not independent verification of the same job.

## 8. Verification status, priority and nonclaims

**Disposition:** DEEP_STATIC_SOURCE_REVIEW, **NOT_RUNTIME_VERIFIED**, **NOT_SECURITY_EMULATOR_TESTED**. P0/P1 identified rule/logic mismatches are grounded in exact pinned source. No exploit was executed, deployed account probed, private data extracted or current PhD opening independently validated. A finding of broad rule semantics does not prove any particular production configuration has deployed those exact rules.

The reviewed source is valuable for candidate-workspace architecture, but not authoritative admissions/funding data. Before reuse, add Firestore Rules emulator adversarial tests, private state ownership, approved-group listing constraints, atomic audit events and receipt-backed application metrics.
