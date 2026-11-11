# xzxLeslie/phd-2027-admissions — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`e786284496997d8eb3ca87cb8f7ce4f7121fc6ef`](https://github.com/xzxLeslie/phd-2027-admissions/commit/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef)  
**Review state:** PRELIMINARY_FOCUSED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** international_program_faculty_directory  
**Primary risk:** static_funding_and_recruiting_claims_not_field_verified  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A Chinese-language 2027 admissions directory aimed at CS, visual computing, graphics and robotics across multiple world regions. It demonstrates useful presentation of program routes and faculty research areas for discovery, but is a manually maintained static reference, not a system for verifying current fully funded offers, closing dates or whether a supervisor has active funded vacancies.

## 2. Architecture and actual components

The site uses generated `window.ADMISSIONS_DATA` and `window.FACULTY_DATA` loaded into `app.js`, with builders `build_data.py` and `build_faculty.py`. A client-side filter supports geography, PhD-versus-coursework degree, funding class, deadlines, graphics, robotics and professor keyword associations. `sources/SOURCES.md` is a broad link ledger to universities, scholarship portals, rankings and selected faculty homepages rather than a field-by-field evidence register.

## 3. Task-to-data flow and dependencies

Dataflow: hand-curated university/campus/program entries -> builders produce static front-end data -> program list and faculty group selectors linked via `schoolKeys` substring matching -> sorting and filters -> CSV export. The `recruiting` field in faculty items is set manually. This means a research interest or manually annotated recruitment statement can be shown alongside a program record without a shared provenance revision and is not automatically synchronized with official vacancies.

## 4. Methods and source-level evidence

Positive concepts are degree-type separation, distinguishing mainland/overseas campus admission pathways, field aliases and useful robotics-specific faculty filtering. But `fundingLevel='full'` often denotes the common institutional funding pattern or a competitive funding route, not a signed funding guarantee; `confidence='high'` is manually assigned in Python. Broad campus/program source strings in the site are not sufficient to prove an exact amount, date or international eligibility, even when the original URL is on a university domain.

## 5. Implementation and operational reconstruction

Use for discovery: choose institution -> identify correct campus/program -> locate central graduate admission and lab webpage -> verify program deadline and applicable cycle -> check international tuition/fellowship -> fetch current PI research publications -> document actual lab hiring status and evidence -> calculate research alignment. Preserve national sub-campus distinctions and render alternative Masters/PhD funding routes distinctly. Never carry over confidence labels as verification.

## 6. Failure modes and validation gaps

The repository has few tracked files and no source-level automated test suite in the inspected tree; no fresh source crawl is visible in `app.js`. Substring school matching may join similarly named institutions or different campuses; recruitment assertions can age quickly. A PhD Atlas import must record `original_source`, `retrieved_at`, `valid_cycle`, specific `funding_scope` and recheck obligations rather than treating a static generated row as Verified.

## 7. Transfer to PhD Atlas and admissions workflow

Adopt the region/degree/faculty browsing vocabulary and human-readable filters as a supplementary index. Compute a scientific-fit score from *current publications and methods*, not only checkbox tags. Distinguish verified live vacancy, annual program route, fellowship competition and general lab-interest lead. Program availability and individual PI capacity are separate facts.

## 8. Provenance and outstanding verification

Read the source-linked index, the 426-line UI controller, substantial portions of the two large generated-data builders and the deployment instructions at the pinned commit. The full 2,674-line data authoring table and 1,505-line faculty declarations have not received a claim-by-claim independent portal recheck. No live site tests or international funding verification performed.

## Pinned source files inspected

- [`README.md`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/README.md)
- [`sources/SOURCES.md`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/sources/SOURCES.md)
- [`app.js`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/app.js)
- [`build_data.py`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/build_data.py)
- [`build_faculty.py`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/build_faculty.py)
- [`OPEN.md`](https://github.com/xzxLeslie/phd-2027-admissions/blob/e786284496997d8eb3ca87cb8f7ce4f7121fc6ef/OPEN.md)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.
