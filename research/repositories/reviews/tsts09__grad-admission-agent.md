# TSTS09/Grad-Admission-Agent — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`74de7b33e227e94c3af097d03f0a73a6bd16090f`](https://github.com/TSTS09/Grad-Admission-Agent/commit/74de7b33e227e94c3af097d03f0a73a6bd16090f)  
**Review state:** PRELIMINARY_FOCUSED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** multi_source_admissions_agent  
**Primary risk:** unsecured_live_chat_route_and_tests_reference_missing_api  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A proposed real-time graduate admissions intelligence backend joining scraped university pages with Reddit, social discussion, program/faculty knowledge and LLM synthesis. Its research value is as a counterexample to conflating a branded multi-source agent with verified hiring and complete endpoint coverage. Some implementation elements are present, but the tested and advertised interfaces are inconsistent.

## 2. Architecture and actual components

`app/main.py` constructs a FastAPI app and only mounts visible root/dashboard/chat/health/test-scraping routes. Its `/api/v1/chat/query` receives a `ChatRequest` and calls `EnhancedChatAgent` directly. `realtime_intelligence_agent.py` creates concurrent fetch tasks, optional Reddit/Twitter sources, SerpAPI university search and Gemini synthesis. A separate `real_ai_agent.py` includes faculty HTML parsing and a SQLite history path, while the other scraping module contains sample-data generation with simulated hiring flags; these are not proof of current recruitment.

## 3. Task-to-data flow and dependencies

The intended flow is query -> rule/LLM intent planning -> select university and community sources -> fetch/parse -> truncate to 15 sources and 800 characters each -> Gemini JSON synthesis -> send faculty/program matches and a confidence scalar. Its structural defect is that source collection and open-position verification are not independently connected: a forum reference, faculty profile and HR vacancy can all enter the same model context, with no hard requirement that an official hiring statement support 'hiring'. No applicant-specific international funding gate is implemented in the inspected route.

## 4. Methods and source-level evidence

Direct source/test mismatch: `tests/test_api/test_chat.py` demands `401` for an unauthenticated `/api/v1/chat/query` call, but the `chat_query` route shown in `app/main.py` has no `Depends(get_current_user)` or `@require_auth` dependency. The tests use `/api/v1/auth/login` and `/api/v1/faculty/*`; these routes are not mounted by the inspected `app/main.py`. The test imports database models absent from the inspected tree. Its `app/core/security.py` defines a JWT verification helper and development-only `demo_` API key acceptance, but these definitions alone do not secure the active route.

## 5. Implementation and operational reconstruction

Reconstruction for a defensible system: record every source as a typed `institutional_policy`, `official_job_post`, `faculty_profile`, `paper`, `firsthand_report` or `community_discussion`; use comments as hypotheses only; allow the LLM to propose questions and extract snippets; then independently reopen official hiring/eligibility pages, capture the exact URL, excerpt, retrieval time, applicable department/cycle and contradiction status. Require tested authentication at all external endpoints and avoid leaking private applicant context in query logs.

## 6. Failure modes and validation gaps

Do not reuse the exposed backend directly. Multi-source retrieval is not equivalent to demonstrated live hiring. `site:edu` excludes many legitimate target-country domains such as `.ac.uk`, `.lu`, `.no`, `.ch`; model-supplied scores are uncalibrated; `_create_sample_data` is mock output; test paths and server path do not align. CI/test execution not attempted, so these are static mismatches, not reported pass/fail results.

## 7. Transfer to PhD Atlas and admissions workflow

Transfer only the abstraction of pluggable source collectors and explicit source reporting, with strict source classification and targeted evidence tests. Gate any claim of `professor_is_hiring` on current official confirmation; `fully_funded` on individualized fee/salary evidence; and `applicant_eligible` on private verified credentials. Add contract tests that start the actual FastAPI app and check auth, routes, source attribution, invalid model output and unsupported funding.

## 8. Provenance and outstanding verification

Files linked below were inspected at the pinned commit. Endpoint/auth conclusion is based on the literal route registrations and test expectations, not an external penetration test. Background worker reliability, advertised dataset size, and successful live scraping remain UNVERIFIED; no tests or live credentials were run.

## Pinned source files inspected

- [`app/main.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/app/main.py)
- [`app/agents/real_ai_agent.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/app/agents/real_ai_agent.py)
- [`app/agents/realtime_intelligence_agent.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/app/agents/realtime_intelligence_agent.py)
- [`app/scrapers/real_university_scraper.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/app/scrapers/real_university_scraper.py)
- [`app/core/security.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/app/core/security.py)
- [`tests/test_api/test_faculty.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/tests/test_api/test_faculty.py)
- [`tests/test_api/test_chat.py`](https://github.com/TSTS09/Grad-Admission-Agent/blob/74de7b33e227e94c3af097d03f0a73a6bd16090f/tests/test_api/test_chat.py)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.
