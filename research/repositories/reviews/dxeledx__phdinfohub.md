# dxeledx/PhdInfoHub — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`832b374b539ad1a3fd775c3b628444b88ba1374e`](https://github.com/dxeledx/PhdInfoHub/commit/832b374b539ad1a3fd775c3b628444b88ba1374e)  
**Review state:** DEEP_REVIEW_DOCUMENTED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** scope_bound_admissions_evidence_and_concurrency  
**Primary risk:** institution_scope_specific_implementation_requires_generalization  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A Chinese doctoral admissions timeline and applicant research system with unusually strong source/claim binding. Its most transferable contribution is not breadth of scholarships; it is a disciplined model of a *doctoral intake window* whose dates only apply to a specific year, department, campus, admission method, cohort, stage and authoritative publication. It addresses a common failure: an AI agent reads a real date but assigns it to the wrong program, admissions stage or academic year.

## 2. Architecture and actual components

Django models distinguish University, UpdateRun, UniversityYearCoverage, AdmissionWindow, AdmissionWindowRevision, UpdateUnit, AdmissionReviewItem and AdmissionSource. `collection.py` gathers authorized official HTML and page-scoped candidates; `official_html.py` structurally isolates article content from navigation/sidebar. `evidence.py` parses date mentions, roles, contextual ranges, department aliases, campus and degree scope. `refresh.py` validates candidate evidence, synchronizes stable identities and revisions, and uses execution leases and DB transactions. Pytest source fixtures cover scope errors and concurrency/rollback behaviors.

## 3. Task-to-data flow and dependencies

Dataflow: official university host or explicit exact-URL trusted external republication -> fetch bounded page -> extract article text with content hash -> identify admission-year and explicit start/end timestamps -> require literal contiguous source excerpts for year, stage, scope and date role -> check degree class and local department context -> validate against fetched source in this same run -> compare with previously verified window identity -> insert, maintain, reject to manual review, or record contradiction revision. The academic identity `scope_key` separates institution/year/department/campus/method/round/stage and period slot, preventing a single 'deadline' per university from flattening distinct processes.

## 4. Methods and source-level evidence

`validate_candidate` refuses a source URL not actually fetched this run or outside university official domains; it verifies quoted excerpts are physically present in the page and checks date year, start-versus-end role, complete local range, title/scope and whether a page addresses an out-of-scope applicant cohort. For the source-semantics path it rejects truncated bodies, requires one contiguous scope excerpt and one bounded date window, and ensures start/end evidence occurs inside that window. These are significantly more defensible conditions than marking any live university homepage Verified.

## 5. Implementation and operational reconstruction

Version and concurrency controls: `save_candidate` locks university and matched windows within a DB transaction; older fetched timestamps cannot replace newer snapshots, and older publication dates cannot supersede newer announcements. A changed deadline is accepted only with an explicit correction and sufficiently recent official chronology; conflicting changes create review records and history instead of silently overwriting. `UpdateRun` and `UpdateUnit` leases plus execution tokens reject writes by a stale recovered worker. Incomplete/failing collection does not cause the absence of admissions dates to be represented as institutional nonpublication.

## 6. Failure modes and validation gaps

The source-specific implementation targets Chinese domestic doctoral admissions and encodes audience and stage vocabulary accordingly. It requires careful translation/generalization for UK scholarships, Swiss employee PhDs, Canada umbrella program admissions, Norway salaried posts and Australian international stipend grants. It is not a universal verified fully-funded-offer model: it is strongest for official date/scope and source chronology; salary, nationality, international fees and hiring capacity must be added as separate evidence types. Model-extracted semantic scope can still be wrong even where quote spans are literal.

## 7. Transfer to PhD Atlas and admissions workflow

For PhD Atlas, adopt an event-sourced `Claim` with `claim_type`, `valid_cycle`, `applicant_class`, `department`, `campus`, `stage`, `start/end`, `IANA timezone`, `source_snapshot_hash`, `evidence_span`, and `review_status`. Design parallel independent facts for funding/fees/eligibility; preserve every historical revision and demand official correction before overwriting a verified deadline. Use a fairness-aware source crawler and status semantics `unchecked`, `partial`, `not_found_in_coverage`, `found`, `needs_review`, `failed` so absence after budget exhaustion is never mistaken for closed admissions.

## 8. Provenance and outstanding verification

Inspected primary evidence extraction, source collection, article isolation, refresh transactional conflict handling, models and three targeted test suites at pinned commit. Tests include same-college/campus/date mixed-scope rejection and stale-worker/write prevention. No Django tests or full crawler were executed here; neither all 284 tracked files nor every claimed university-year dataset record was independently verified. This remains a substantial **static** analysis, not an external production-certification result.

## Pinned source files inspected

- [`apps/admissions/services/evidence.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/evidence.py)
- [`apps/admissions/services/collection.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/collection.py)
- [`apps/admissions/services/refresh.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/refresh.py)
- [`apps/admissions/services/official_html.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/official_html.py)
- [`apps/admissions/models.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/models.py)
- [`apps/admissions/tests/test_evidence_and_leases.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/tests/test_evidence_and_leases.py)
- [`apps/admissions/tests/test_official_page_evidence.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/tests/test_official_page_evidence.py)
- [`apps/admissions/tests/test_collection_fairness.py`](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/tests/test_collection_fairness.py)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.


## Additional pinned source reinspection — 2026-11-12

Reinspected original commit `832b374b539ad1a3fd775c3b628444b88ba1374e` across `apps/admissions/services/evidence.py` (1,077 lines), `collection.py` (920), `refresh.py` (899), `apps/workbench/services/import_sources.py` (824), and `apps/workbench/tasks.py` (516). The executable source confirms distinct date-role, joint-doctoral-year, special-audience, campus/department and registration-method checks before saving scope-bound windows. `refresh.validate_candidate` verifies fetched-page evidence; revision writes are transactional and older snapshots are refused or diverted to review instead of overwriting newer validated data. Workbench URL import sets explicit 12 MiB general/10 MiB image/3 MiB URL bounds, 50 PDF pages and five redirects, has public-IP/DNS and pinned-address checks; the background job uses execution leases, heartbeats, owner-scoped retry/cancellation and source purging. No current university admissions date or code-runtime correctness is asserted by this static trace. Repository-specific China admissions terminology and scope must be adapted to international program contexts. Source: [evidence](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/evidence.py), [refresh](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/admissions/services/refresh.py), [import_sources](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/workbench/services/import_sources.py), [tasks](https://github.com/dxeledx/PhdInfoHub/blob/832b374b539ad1a3fd775c3b628444b88ba1374e/apps/workbench/tasks.py).
