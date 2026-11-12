# centrixsol/phd-applicant — deep static implementation and security review

**Review date:** 2026-11-12  
**Upstream:** https://github.com/centrixsol/phd-applicant  
**Pinned commit:** [`c1b33eb17d8c57efed957c3cd33fe2ebb2355927`](https://github.com/centrixsol/phd-applicant/commit/c1b33eb17d8c57efed957c3cd33fe2ebb2355927)  
**State:** DEEP_REVIEW_DOCUMENTED (source-level only; no live execution).  
**Decision:** reject the current deployment/auto-submission implementation; retain only carefully redesigned workflow ideas.  
**Principal risk:** a demo or form-fill action can be recorded as a real, timestamped **submitted** application without a submission receipt.

## 1. Scope, history and evidence

The repository advertises a Next.js 16 application tracker, Prisma/MongoDB models, credentials-based NextAuth authentication, Claude-powered writing, seeded programs, a Playwright/FastAPI automation service, and Swedish Varbi crawling. The inspected pinned tree contains 110 entries, including API routes, a Python browser engine, seed scripts and two CI workflows. Last observed upstream commit: 2026-05-15. README describes a publicly reachable demonstration, but this review did not access or validate the deployed site or any real admissions portal.

README advertises one-click autonomous submission across Slate, ApplyYourself, CollegeNET, Varbi and generic university systems, with 350+ programs. The implementation must be evaluated independently of those claims. The inspected tree exposes no unit/integration test files; the CI workflow performs npm dependency installation, Prisma generation, TypeScript checking and build, not an application/receipt audit. README says MIT, but no independently inspected LICENSE file was present.

## 2. Concrete dataflow and architecture

`UserProfile` includes personal, academic, employment, publication, language score and contact fields; related `Document`, `Statement`, `Application`, `Program`, `University` and `VarbiPosition` entities persist via Prisma MongoDB. A NextAuth credentials provider checks bcrypt password hashes and issues a JWT session. However, critical API routes do not use or verify that session.

`POST /api/apply` accepts an application ID, looks up a user profile using a **global environment-selected email**, finds the application by ID, checks minimal profile fields, and forwards all profile fields, document paths, statements and portal credentials to a separate FastAPI `POST /apply` service. The browser engine visits an application URL, heuristically matches labels, fills fields and uploads selected local files. It does not implement a required receipt-capture and final human-approval step.

`POST /api/crawl` proxies to the browser service, which scans a static list of Swedish Varbi hosts and persists results keyed by `(universityCode, jobId)`. Source discovery, applicant readiness, submission action and official evidence are not separate authorization/evidence layers.

## 3. Critical false-submission states (P0)

The Next.js apply handler catches a missing/unreachable automation service and explicitly substitutes a *demo* response with `status: "submitted"`. It then persists the same status and assigns `submittedAt = new Date()`. This can transform a failed automation connection into a false application submission.

Independently, the Playwright `apply_varbi()` handler logs that fields were filled and manual review/submission is still required, but returns `{"status": "submitted"}` immediately after filling. The generic form handler also returns `submitted` while its message says to review and submit. ApplyYourself, Slate and CollegeNET handlers delegate to this same generic handler. No portal-generated receipt ID, confirmation URL, server-signed event or immutable submission artifact is validated before changing state.

The public API also permits clients to set `status: "submitted"` directly via `PUT /api/applications`, assigning `submittedAt` from the server clock without external proof.

**Required repair:** distinguish `DEMO_SIMULATED`, `FIELDS_PREFILLED`, `READY_FOR_HUMAN_REVIEW`, `SUBMISSION_ATTEMPTED`, `SUBMITTED_RECEIPT_VERIFIED` and `UNKNOWN`. Only receipt-backed, user-authorized events can create an actual submitted state. Do not infer success from a generic form button, remote service response or local timestamp.

## 4. Authentication, privacy and browser security (P0)

- The implemented NextAuth credentials provider is not sufficient: `/api/profile`, `/api/documents`, `/api/applications`, `/api/apply` and `/api/ai` operate on one globally configured email without verifying the caller's session or binding resource IDs to the authenticated subject. An exposed deployment of these handlers could permit unauthorized reads, updates, AI charges and application triggers.
- The documents handler writes uploaded CVs/transcripts/recommendation files under `public/docs/{user.id}/...`, which is a static public-serving directory in typical Next.js deployments. This is not a protected private document store. No size, MIME/content validation, virus scanning or read authorization is demonstrated.
- The `Application` model stores `portalPassword` as a regular database string. The browser service accepts login credentials without service-to-service authentication and exposes `/apply` and `/crawl` in a process configured to bind to `0.0.0.0`.
- `automation/main.py` accepts an arbitrary user-provided application URL and launches Playwright with server network privileges; the inspected execution path does not enforce public HTTPS, an employer allowlist, DNS/IP restrictions or redirect checks. This is a source-level SSRF/unsafe automation risk, not a tested exploit.
- `/api/profile` accepts spread request fields; broad update semantics risk modifying server-owned fields rather than an explicit allowlist. Writing assistants may include sensitive applicant narratives in external LLM requests without a separate source/consent audit.

Do not reproduce or use hardcoded identifiers or any credential data from this repository. Do not run its automation against real application portals without authorization.

## 5. Opportunity, funding and deadline veracity

`Program.fullyFunded` defaults to **true** in the database model, and the listing API filters for `fullyFunded: true`. Thus funded classification is a default property of records, not independent evidence. The AI program summary expands this to “Funding: Fully employed” with a generic competitive stipend fallback. A target program's advertised funding cannot be established this way.

The Varbi scraper sets `stipendUSD: 33000` as a hardcoded value even when scraping a detail page fails; it also defaults an absent deadline to `Rolling`. The fallback returns a program record with missing details. These values are assumptions, not source-verifiable salary or live vacancy facts. Ranking values are hardcoded per university in the adapter and are not sourced by date or subject category.

The repository does not track exact source statement spans, current cycle, international tuition classification, admission versus employment contract, candidate nationality constraints, or funding award state. README's 350+ program count was not independently reconciled against current official employer vacancies.

## 6. Testability, operations and failure handling

The Python automation script matches form names and placeholder substrings, silently ignores many form-field errors, and handles only one next/continue step in the Varbi path. It cannot establish compatibility with every institution's complex portal or dynamic field validation. No CAPTCHA/2FA/fee authorization, reference contact, final consent or receipt validation is implemented in the inspected flow.

The FastAPI service routes return result logs, but its status route always returns `unknown`, so no durable end-to-end status reconciliation exists. The crawler stores most recent seen postings but does not demonstrate complete source snapshot/version control, per-source timeout/backoff policy, authoritative close state, or safe failure semantics.

The CI build is not an upstream security or admissions-path integration test. This review did not execute browsers, package dependencies, MongoDB, LLM calls, or any real application action.

## 7. Transfer and inter-repository conclusions

Transferable concepts: user-authenticated personal profile, program-specific statements, reusable typed document references, source-specific vacancy adapters, stable external IDs, and an application event ledger.

Required redesign before any adoption:
1. Enforce session-bound authorization on every personal/profile/document/application route and service-to-service authentication on the browser worker.
2. Encrypt portal credentials or avoid retaining them; store personal files in private object storage and issue short-lived authorized downloads.
3. Restrict browser execution by verified official hostname/URL allowlists, DNS/IP/redirect policy and resource budgets.
4. Separate sourced opportunity claims (salary, funded status, cycle, deadline) from default UI data; Unknown remains Unknown.
5. Add a verified explicit user approval stage and immutable portal receipts for external submission, with per-action audit logs.
6. Test failure-mode transitions: automation offline, form only prefilling, partial upload, retries, duplicate submissions, and source/crawl incompleteness.
7. Distinguish proposal drafting from factual program verification and authentic applicant statement approval.

The source is an important counterexample to the assumption that “automated” is equivalent to “submitted”; it reinforces the evidence/authorization separation already required by the PhD application workspace.

## 8. Pinned implementation references and validation limits

- [README](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/README.md)
- [Next.js apply handler](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/app/api/apply/route.ts)
- [Application CRUD](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/app/api/applications/route.ts)
- [Profile API](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/app/api/profile/route.ts)
- [Document storage API](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/app/api/documents/route.ts)
- [Auth provider](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/lib/auth.ts)
- [Prisma data models](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/prisma/schema.prisma)
- [Browser automation engine](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/automation/engine.py)
- [FastAPI service](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/automation/main.py)
- [Varbi scraper](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/automation/varbi_crawler.py)
- [CI workflow](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/.github/workflows/ci.yml)

**DEEP_REVIEW_DOCUMENTED — static only.** The source defects are evident from inspected code at the pinned revision. No dynamic exploit, authenticated session, real portal submission, correctness test, license legal opinion or funding verification was performed.
