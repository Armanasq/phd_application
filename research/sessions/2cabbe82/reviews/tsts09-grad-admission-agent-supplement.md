# TSTS09/Grad-Admission-Agent — supplemental implementation investigation

- Existing canonical review pin: `74de7b33e227e94c3af097d03f0a73a6bd16090f`
- Status: additional static inspection of active FastAPI entry point, agent, security utilities and test expectations; no runtime execution.

## Active application wiring

The inspected `app/main.py` creates a FastAPI app with permissive CORS (`allow_origins=["*"]`, credentials enabled), initializes Gemini and optional Firebase during lifespan, and instantiates a global `EnhancedChatAgent`. The active `/api/v1/chat/query` route accepts a Pydantic `ChatRequest`, calls `process_message`, and returns faculty/program matches, confidence scalar and source list. The route signature has no request dependency for `get_current_user` and no auth decorator.

The dashboard's inline JavaScript sends the chat request without an Authorization header. It appends user/model content to `innerHTML`, which also creates a DOM injection/XSS risk if returned text is not escaped. The endpoint catches broad exceptions and returns exception text in HTTP 500 detail, potentially exposing internal error details.

## Agent execution model

The realtime agent uses Gemini for intent analysis, executes selected sources (university pages, SerpAPI, Reddit and optional Twitter), and asks Gemini to synthesize the result. Async collection is attempted, but the source classes are heterogeneous and the implementation's actual concurrency, request timeout and cancellation behavior must be tested. Faculty and program outputs are not necessarily verified vacancy records.

The security helper file contains JWT token verification, password hashing, a rate-limiting middleware, API-key helpers and decorators. These utilities do not secure a route unless wired into that route or applied globally. The rate limiter stores per-IP timestamps in process memory, trusts the first X-Forwarded-For value, and is not distributed across workers. Production API-key verification returns false by default; development accepts `demo_` prefixes. The existence of helpers is not proof of route protection.

## Contradiction between implementation and tests

The repository's API tests expect unauthenticated access to return 401 and import auth/faculty endpoints. The active main file inspected does not mount those routes or enforce authentication on the chat route. Therefore the test suite and active server entry point appear inconsistent. This is a source-level contradiction, not a reported test failure; the tests were not run.

## Critical operational risks

- Wildcard CORS with credentials is an unsafe configuration for a production API.
- Inline dashboard uses `innerHTML` for user input and response rendering without demonstrated escaping.
- Chat endpoint is unauthenticated in the active entry point.
- Model synthesis combines source types with different evidentiary strength; social discussions must not establish official hiring or funding.
- A scalar confidence score is not calibrated evidence quality.
- Query-derived university searches may miss non-`.edu` domains, including common European institutional domains.
- Error details are returned to clients.
- No verified applicant-specific fee, funding or nationality eligibility gates are evident in this path.

## Transfer

Use source collectors only as typed ingestion adapters. Every source observation must be classified as official policy, official vacancy, faculty profile, publication, firsthand account or discussion. Use the LLM for candidate extraction and question generation, not final verification. Require the final claim to be rechecked against the official source, with cycle, department, date, excerpt and fetch timestamp.

Before reuse, establish an integration test that imports the actual app entry point and checks all mounted routes, authentication, CORS, input/output escaping, malformed model output, provider failure, timeouts and source attribution.

## Files examined

`app/main.py`, `app/agents/realtime_intelligence_agent.py`, `app/core/security.py`, and test expectations in `tests/test_api/test_chat.py` and `tests/test_api/test_faculty.py`, alongside the pinned files in the canonical review.

## Outstanding verification

No runtime, integration, security or network tests were executed. Inspect the complete source adapters and deployment configuration; verify actual mounted routes and current HEAD; run test suite only in a separate isolated environment with dummy credentials.
