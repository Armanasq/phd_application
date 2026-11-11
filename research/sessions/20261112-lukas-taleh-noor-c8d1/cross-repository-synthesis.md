# PhD research operations — primary vacancy feeds, local applicant custody, and policy evidence

**Session:** `20261112-lukas-taleh-noor-c8d1`. All claims are derived from pinned repository sources in the three sibling reviews. Findings are source-level, **not** production validation.

## 1. Three distinct system roles

| Layer | Example | Strength | Failure mode to avoid |
| --- | --- | --- | --- |
| Primary university job ingestion | [Lukas-Vasionis/PhD_Positions](reviews/lukas-vasionis-phd-positions.md) | Institution-targeted adapters and local SQLite snapshots | Empty crawls overwrite records, inconsistent processed/label keys, no source continuity |
| Local applicant operations | [TalehMalikov/phd-application-tracker](reviews/talehmalikov-phd-application-tracker.md) | Zero-login offline-first drafts, checklists, candidate statuses | Client-side injection in stats, no durable backup, no evidence-linked decisions |
| Applicant strategy anecdote | [NoorMohammadTalukder/usa-masters-phd-scholarship-guide](reviews/noormohammadtalukder-usa-masters-phd-scholarship-guide.md) | Concrete shortlisting/outreach writing heuristics | Unsupported numerical response generalization, visa/admission/funding “rules” inferred from one account |

Complementary earlier deep reviews: [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator) supplies multilingual/lexical semantic retrieval; [NaughtFound/Go2Phd](https://github.com/NaughtFound/Go2Phd) supplies a read-only Sheets adapter, but both had source-confirmed correctness defects in the prior session. These systems model different data authorities and should not be collapsed into a single undifferentiated “verified” dataset.

## 2. Suggested typed evidence model

- `SourceObservation`: origin URL, institution/country identifiers, retrieval timestamp, HTTP status, snapshot hash, extraction version, complete/partial/refused state, source credibility, outbound URLs, age.
- `OpportunityClaim`: source observation ID, field name, literal claim, source excerpt/span, validity cycle, confidence, last verification, `UNKNOWN | SUPPORTED | CONFLICTED | RETIRED` state. Keep funding, fee coverage, language score, eligibility, start date and deadline as independent claims; a missing field is **UNKNOWN**.
- `OpportunityIdentity`: university, department, vacancy ID, program, supervisor, cycle and primary URL. Source-native IDs take precedence over fuzzy title/city matching; grouping must keep conflicting notices visible.
- `ApplicantWorkflow`: opportunity ID, local status, review checklist, work product references, outreach thread, evidence of submitted application, private attachment custody, update history and responsible session/author.
- `ReviewAssignment`: candidate URI, owner/session, pinned upstream commit, files examined, verification type, status, link to review evidence, review notes and next verification action.

**A job ad shown on a third-party board is not proof that an official vacancy is currently open.** Likewise, user-marked “Applied” does not prove successful portal submission; anecdotal acceptance does not prove a program's funding policy.

## 3. Non-negotiable transition guards

1. Fetch: retain the previous successful complete snapshot if any HTTP error, blank sitemap, JS-only listing, parser exception, missing pagination, or robots/terms refusal occurs; record an explicit failure event. Never infer closures from incomplete listings.
2. Parse: validate mandatory university/job keys and type-specific deadlines; do not insert synthetic blank listings or erase prior evidence on zero parse.
3. Reconcile: update only when source revisions are verified; append an observation and field-level provenance; automatically flag conflicting deadlines, extensions and reopening.
4. Canonicalize: keep per-source IDs, original URLs and source-specific language; dedupe only when institutional identity, cycle and position match; do not conflate identical titles in one city.
5. Applicant state: use append-only review/application events and separate encrypted or user-owned files, not a single mutable status string with no receipts.
6. Privacy: escape all user-controlled DOM content; no external model receives personal applicant artifacts by default. Require direct, source-specific consent where external processing is actually intended.
7. Coverage: treat full source reading, static code review, executed tests and live policy verification as **different axes**, not interchangeable depth labels.

## 4. Incremental implementation sequence

- **Integrity first:** shared table schema for source/processed/labels; transactionally preserve observations and labels; add empty-list and deadline-extension tests.
- **Correctness next:** source adapter heartbeats, completeness thresholds, verification state transitions and per-field evidence snapshots.
- **UX next:** private draft custody with export/restore; calendar-safe date handling, future-only deadline reminder, sanitized application statistics.
- **Retrieval later:** use source-weighted hybrid search only over validated opportunity claims; citations resolve to exact primary source and snapshot date; model-generated summaries cannot authorize applicant-state or funding changes.

## 5. Integration and coordination notes

The isolated branch contributes only new files under `research/sessions/20261112-lukas-taleh-noor-c8d1/`. It does not modify other sessions' research or active canonical CSVs. **Canonical ledger integration remains a follow-up requiring a fresh atomic reconciliation against current main** because numerous agents are concurrently updating the 404-candidate inventory. The three names should be reconciled by exact case-sensitive repository slug, deduplicating if another session has published a review in the meantime. None of the upstream authors or universities was contacted.
