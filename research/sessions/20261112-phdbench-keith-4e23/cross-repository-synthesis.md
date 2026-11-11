# Cross-repository synthesis — shared research leads versus private applications

**Session:** 20261112-phdbench-keith-4e23
**Source audits:** [PhDBench](reviews/nikhil-rao20-phdbench.md) · [Industrial-AI PhD positions](reviews/keithbh-phd-positions.md)
**Validation type:** Static, pinned source inspection only. No Firestore emulator, live recruiter, third-party browser, integration or performance execution.

## Different products, different evidence

| Concern | Nikhil-Rao20/phdbench | KeithBH/phd-positions | Safe integration contract |
| --- | --- | --- | --- |
| Source and freshness | User-entered and group-shared lead facts | Author-curated 192-row embedded table, last commit Oct 2026 | Immutable observation with source URL, checked-at, cycle and claims |
| Applicant activity | Private application stages and document/recommender readiness | No user-account workflow; a manual status field | Private status machine with immutable submission receipt |
| Sharing boundary | Private Firestore users plus shared group leads | Public, unauthenticated static web page | Authenticated per-member access, field-level ownership |
| Status meaning | Stage derived in client, even missed deadline counts as submitted | 'Pending review' can remain despite elapsed ISO date | Separate observed, time-evaluated and verified statuses |
| Funding/eligibility | Free-text lead funding notes | Free-text role notes and mixed PhD/EngD/CSC types | Explicit conditional verified funding and applicant eligibility |
| Evidence | User-generated activity log; no portal receipt enforced | No source snapshot hash, independent validation or field spans | Provenance graph and action receipts |

## Major implementation lessons

1. **Server rules must own collaboration privacy.** PhDBench's normal UI filters group membership, but Firestore's group-list permission allows any approved user to enumerate group documents. A member's direct API writes can also change others' nested per-user lead states. UI-only rules are insufficient. Build and run negative authorization tests for cross-group reads, member impersonation, revoked users, ownership changes and self-approval.
2. **Do not infer 'submitted' from a terminal label.** PhDBench's computed SUBMITTED_STAGES includes MISSED_DEADLINE and WITHDRAWN, even for never-submitted records; its activity events can fail after the stage write. A publication-quality outcomes dataset requires recorded send/portal receipts and consistent stage-transition provenance, not inferred application counts.
3. **Freshness is a property of individual claims.** The static tracker shows 192 entries while its header claims 144; 14 ISO deadlines before 2026-11-12 are still pending-review. A global page update timestamp or human-entered 'active' label cannot replace employer confirmation. Unknown/rolling dates remain unknown.
4. **Type and identity must be normalized.** A source record may describe an EngD, postdoc, engineer, PhD vacancy or restricted funding instrument. Do not collapse them into one PhD opportunity count; never use title+city or a local table ID as the sole canonical vacancy identity.
5. **Separate source evidence from applicant-private data.** Shared public research can reference an opportunity; personal documents, funding constraints, referee details, actions and receipts are protected records. Group-state edits and exports need server-side authorization, revision tracking and conflict handling.

## Suggested acceptance tests for the PhD application platform

- A member of group A cannot list or read group B's metadata, including email addresses or membership maps.
- A group A member cannot write another UID's status, priority, archive flag or converted-to-application ID; removing a member revokes all reads.
- An applicant with only a 'missed deadline' or pre-submission 'withdrawn' stage is not counted as submitted.
- Updating a stage and writing an audit event is atomic or reconciled; 'submitted' requires a user-verified portal receipt where the workflow claims proof.
- An imported vacancy dated before the current day with pending-review source status is not promoted to verified open.
- The candidate ingestion schema preserves unknown deadlines, rolling status, timezones and distinct vacancy types.
- Hardcoded UI counters are replaced by tests asserting totals computed from typed records. Blank or unsafe URLs are not navigable.
- Generated citations contain original employer URL, exact observation date, content hash, field-level evidence, and verification status.

## Integration disposition

- **PhDBench:** Deep static source reference, strong modular applicant-workspace patterns but cross-member data integrity and group metadata confidentiality gaps. Runtime risk NOT_TESTED. No deployed data accessed.
- **KeithBH/phd-positions:** Complete single-file static source and embedded-data audit, historically useful manual leads, but cannot be admitted as a verified or current PhD funding database.
- Both were UNTRIAGED in the canonical 404-identity candidate set when claimed by this session. These reports should not be counted as canonical reviewed rows until an authorized inventory-owner transaction records and validates them.
- All research artifacts belong under this unique session directory. No shared CSV, global status, issue, branch or other session's file is updated here.

## Source pointers

- [PhDBench pinned security rules](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/firestore.rules)
- [PhDBench private and shared application state](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/groupsDb.js)
- [PhDBench derived submission counts](https://github.com/Nikhil-Rao20/phdbench/blob/4ff6ca4948a6dc820366b4a5342f6adbdd6269df/src/lib/derive.js)
- [Industrial AI standalone source](https://github.com/KeithBH/phd-positions/blob/2dfe11ac0d7403e3f143ab7aab7c45f05574edff/index.html)
