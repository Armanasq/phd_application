# PhdInfoHub — supplemental implementation investigation

- Upstream review baseline referenced by existing canonical note: `832b374b539ad1a3fd775c3b628444b88ba1374e`
- Current source structure separately inspected during this session; exact current upstream HEAD was not pinned in this supplemental pass.
- Status: substantial additional static source inspection; no runtime execution.

## Data model and semantics

The admissions subsystem is modeled as a set of related entities rather than one row per institution:
- `University`: stable code, aliases, official-domain allowlist, geography and roster provenance.
- `UpdateRun`: a batch execution, requested years, model/provider, budgets, counters, lifecycle timestamps and execution token.
- `UniversityYearCoverage`: per-institution/per-year status, checked/success timestamps, query/page/model counters and budget-exhaustion marker.
- `AdmissionWindow`: a single cycle-specific window, scoped by institution, department, campus, admission year, method, round, stage and period slot; dates/times, timezone, source URL/title, evidence excerpts, source hashes and verification status.
- `AdmissionWindowRevision`: append-only historical snapshot and reason for a change.
- `UpdateUnit`: per-institution unit within a run, including attempts, errors, source URLs, counts and execution token.
- `AdmissionReviewItem`: unresolved candidate/fingerprint and reasons requiring human review.
- `AdmissionSource`: source URL/content hash/extraction version and cached extraction.

This is a useful separation of three states often collapsed by basic trackers: source coverage, extracted candidate, and verified admission window. A missing result is not necessarily a closed intake.

## Date semantics

The `AdmissionWindow.status_at` method uses an explicit Asia/Shanghai timezone and distinguishes:
- verified versus conflict;
- closed before today;
- deadline today with or without a published cutoff time;
- upcoming;
- starts today;
- closing within seven days;
- open;
- unknown when the date interval is incomplete.

The database constraints prevent start dates after end dates and prevent a time value when its associated date is absent. The identity key includes university, year, department, campus, method, round, stage and period slot. This avoids conflating multiple rounds or distinct departmental windows.

## Evidence extraction and validation

The source collector defines a strict JSON schema for each date window. It instructs the model to:
- use only fetched page bodies, not search snippets or model memory;
- distinguish admission year from publication year;
- preserve department/campus/method/round/stage;
- extract one contiguous local date passage;
- require start/end evidence to be literal substrings of the selected window;
- keep start/end roles within the same explicit date range;
- avoid inferring missing years or midnight/23:59 cutoffs;
- exclude non-target applicant cohorts and unrelated degree/postdoc announcements.

The evidence helper normalizes whitespace for substring comparison and parses full dates, month/day dates, ranges and time tokens. Literal quote checks improve traceability, but they do not prove the model assigned the quote to the correct semantic scope; scope and applicant-class classification still need human/independent verification.

## Concurrency, cache and revision model

The schema carries both run-level and unit-level execution tokens. The existing canonical review reports transactional locks and stale-worker rejection in refresh logic. The data model supports idempotent updates, explicit coverage state, and append-only revisions. This is a sound architecture for long-running multi-school collection.

The key lesson for Atlas is to make every refresh a bounded, observable unit with a unique lease/token and to reject writes from stale attempts. A failed or budget-exhausted unit must retain its prior verified facts and update its coverage status rather than silently replacing it with an empty result.

## Transferable architecture

Adopt the separation:
`SourceSnapshot -> ExtractionCandidate -> Claim/Window -> VerificationDecision -> Revision`.

Every claim should carry:
- cycle and applicant scope;
- exact source URL and content hash;
- source fetch time and publication time separately;
- contiguous evidence spans;
- field-specific verifier result;
- prior value and correction lineage;
- collection run and worker identity.

Funding, tuition, salary, fee coverage and nationality eligibility require parallel claim types. The Chinese domestic intake implementation cannot simply be relabeled as a universal international PhD model.

## Additional implementation caveats

- The model schema is specialized to Chinese admission modes and stage vocabulary; translation/generalization requires new domain tests.
- `University.clean` checks hostname-like syntax and rejects broad suffixes, but domain enrollment still requires independent institutional verification.
- Search and model extraction budgets are recorded, but model-derived classifications remain fallible.
- The source collector can process many pages; the operational ceiling, fairness across universities and rate-limit behavior require execution evidence.
- No tests, live collection, or database concurrency test were executed in this session.

## Files examined in this supplement

`apps/admissions/models.py`, `apps/admissions/services/evidence.py`, `apps/admissions/services/collection.py`, and the previously recorded refresh/official HTML/test paths in the canonical review.

## Remaining validation

Pin the exact current HEAD and inspect complete refresh transaction/lease paths, source import URL validation, task scheduling, migrations and all relevant fixtures. Run the Django test suite against isolated Postgres/Redis services and test stale-worker writes, correction chronology, scope collisions, partial fetches, quota exhaustion, and timezone edge cases.
