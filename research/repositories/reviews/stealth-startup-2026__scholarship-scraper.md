# stealth-startup-2026/scholarship-scraper — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`dee3edaa40ed8c06821d337721259e146d79caf7`](https://github.com/stealth-startup-2026/scholarship-scraper/commit/dee3edaa40ed8c06821d337721259e146d79caf7)  
**Review state:** DEEP_REVIEW_DOCUMENTED. Risk-focused static implementation inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** australia_scholarship_structured_scraping  
**Primary risk:** absence_of_citizenship_rule_treated_as_international_eligible  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A purpose-built Australian university scholarship data extraction project emphasizing University of Sydney and UNSW. It directly addresses a key PhD Atlas challenge: one university scholarship listing may describe multiple distinct awards with different eligibility and separate application requirements, so blindly treating the page as a single fully funded PhD award is wrong.

## 2. Architecture and actual components

Source adapters collect USyd's underlying AEM scholarship JSON and details pages and UNSW HTML; `scholarship_common.py` centralizes a CSV contract compatible with downstream import. `requirements_extractor.py` isolates optional DeepSeek-compatible LLM extraction with strict structured outputs and cached request hashes. `build_sub_rows` creates child scholarship award records with parent URL, code and eligibility. A separate audit script cross-checks extracted international-student tags against model verdicts. `tests/test_stamps.py` checks per-page source synchronization timestamps.

## 3. Task-to-data flow and dependencies

Dataflow: source listing feed -> detail fetch -> source-specific extraction -> detect bundled multi-award pages -> classifier and optional LLM splitter -> parent/child award records -> structured application mode (`automatic` vs `manual`), requirement bullets, amount and eligibility -> CSV import. The parent-child relation is an important improvement over flattening 'scholarship funding' into a program's generic property. Original raw payload allows offline disagreement analysis and repairs without re-crawling.

## 4. Methods and source-level evidence

Correct separation: `source_last_synced_at` is the time a page was fetched; `last_verified_at` is intentionally left empty by scrapers for a later independent refresh process. The two timestamps should never be conflated. More importantly, `unsw/verify_international.py` states that the classifier should mark `is_international=True` when no citizenship or residence restriction is mentioned. That changes Unknown into Eligible without evidence. For many scholarships, the application category or embedded conditions can still exclude international applicants.

## 5. Implementation and operational reconstruction

A separate tri-state bug appears in `usyd/verify_usyd_international.py`: `baseline_verdict()` can return `None` when no usable student-type tag exists; `write_baseline` serializes the compact boolean export as `False` for both None and False. The parallel reasons CSV does preserve Unknown, but any consumer of the compact file alone will treat unknown applicants as ineligible. A correct canonical type must remain `eligible | ineligible | unknown`, and any derived binary view must explicitly exclude unknown cases rather than silently recode.

## 6. Failure modes and validation gaps

Additional caution: an official scholarship page can mix a general research training allowance, international fee waiver, top-up stipend, application-stage fee and separate research award. The project has extraction hooks but does not prove a full specific PhD package. A model QA decision is a second model opinion, not independent institutional attestation. No current international eligibility, funding amounts or advertised dataset sizes were independently re-fetched here.

## 7. Transfer to PhD Atlas and admissions workflow

Adopt Australian-specific decomposition: `program`, `award_scheme`, `award_component`, `tuition_scope`, `applicant_class`, `application_mode`, `eligibility_rule`, `source_version`, and `review_status`. Before rating Fully Funded for an international applicant, require coverage of overseas tuition, living stipend, duration and conditional scholarship award. Add explicit Unknown as non-actionable funding gap. Use source citation spans per subaward and manually inspect conflicting classifications.

## 8. Provenance and outstanding verification

Inspected USyd/UNSW scrapers, canonical CSV, LLM extraction/classification, international audits and timestamp tests at pinned commit. The original upstream webpages, PDF attachments, full award inventory and live international grant rules have not been independently validated or execution-tested.

## Pinned source files inspected

- [`scholarship_common.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/scholarship_common.py)
- [`requirements_extractor.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/requirements_extractor.py)
- [`usyd/usyd_scraper.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/usyd/usyd_scraper.py)
- [`unsw/unsw_scraper.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/unsw/unsw_scraper.py)
- [`tests/test_stamps.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/tests/test_stamps.py)
- [`usyd/verify_usyd_international.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/usyd/verify_usyd_international.py)
- [`unsw/verify_international.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/unsw/verify_international.py)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.

## Additional pinned implementation reinspection — 2026-11-12

**Confirmed code paths at `dee3edaa40ed8c06821d337721259e146d79caf7`:** `usyd/usyd_scraper.py` (572 lines) and `unsw/unsw_scraper.py` (464 lines) implement source-specific listing/detail extraction, amount and highlight/date parsing, citizenship and funding-type classification, and multi-award parent/child bundle splitting. A useful provenance distinction is retained: `source_last_synced_at` comes from the actual page fetch, while `last_verified_at` is left blank for later independent verification. The 127-line `tests/test_stamps.py` has fixtures for CSV shape, distinct page timestamps, failed fetch not yielding fresh records, and child awards inheriting the parent's fetch stamp without an independent verification timestamp; **tests were inspected, not run**.

The key semantic failure in `unsw/verify_international.py` (273 lines) is its LLM prompt: it allows `is_international=true` when the text *does not mention* a citizenship or residency restriction. Unknown eligibility therefore becomes positive eligibility without affirmative issuer language. Conversely missing source text or model failures are written as `is_international=false`, which is not proof of ineligibility either. Use a ternary `ELIGIBLE | INELIGIBLE | UNKNOWN` tied to a literal issuer excerpt, exact award/term and nationality scope; separately verify stipend period, tuition coverage and intake deadline. No live award or model call performed.

**Transfer:** source-scoped adapters; parent/child awards; fetch-versus-verified timestamps; negative HTTP fixtures. Reject binary eligibility inferred from absent conditions. GitHub metadata at inspection: no license recognized; latest upstream push 2026-11-05; one open upstream PR (#1, Helm workflow integration) that was **not** merged into the pinned default branch. [USyd](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/usyd/usyd_scraper.py), [UNSW](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/unsw/unsw_scraper.py), [international classifier](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/unsw/verify_international.py), [stamp tests](https://github.com/stealth-startup-2026/scholarship-scraper/blob/dee3edaa40ed8c06821d337721259e146d79caf7/tests/test_stamps.py).
