# RahulShastri003/application-tracker — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [5cda0d97907f7940f94dff312a5196da7f54f981](https://github.com/RahulShastri003/application-tracker/commit/5cda0d97907f7940f94dff312a5196da7f54f981).  
**State:** DEEP_REVIEW_DOCUMENTED — server, discovery, data persistence, local UI and workflow static audit; no runtime execution.  
**Verdict:** useful local-first application management reference; adapt with state concurrency and privacy safeguards.

## 1. Purpose and scope

A dependency-light local web application for tracking academic PhD, postdoctoral, grant, fellowship and industry-job applications. It has checklists, preparation notes, document uploads, reminders, customizable applicant profiles and a discovery/watch interface. The backend is a plain Node.js HTTP server bound to `127.0.0.1`; the browser uses separate JS modules, without a multi-user hosted account backend. Its 21-file tree includes tests/check workflows and some vendored PDF JS resources.

## 2. Data model and architecture

`server.mjs` persists `profiles.json`, per-profile `applications.json`, AI provider settings and uploaded files under a configurable local data folder. API routes handle profile creation/switch/rename/delete, current state PUT/GET, document uploads, AI requests and opportunity refresh. Local profiles are organization namespaces for one machine, **not authenticated users**. The public state response includes entry records, document metadata, discovery state and local storage paths.

The UI stores discovery settings in `localStorage` and provides source, country, topic and type filters. Users can preserve their own state separate from scraped listing attributes. This separation is a positive feature for applicant workflow design.

## 3. Source acquisition and ranking

The server implements five fixed first-party collector adapters: Quantiki, EURAXESS, jobs.ac.uk, AcademicJobsOnline and AcademicTransfer. `handleOpportunityRefresh` matches requested IDs against that known list, calls collectors with `Promise.allSettled`, and reports errors/unsupported sources independently. This is safer and more transparent than silently treating unimplemented source connectors as successful crawls.

Collector HTML parsing is based on source-specific regex/markup heuristics rather than official API contracts. The source catalogue also includes manually maintained/nonlive sources, which must not be presented as freshly fetched evidence. `opportunity-watch.js` applies deterministic keyword-weighted matching; those scores are sorting priorities, not trained admission probabilities. The code does not store field-level proof of full funding, citizenship eligibility or official application cycle.

## 4. Local state correctness

`handleSaveState` replaces the **entire per-profile JSON document** on each PUT, writing directly to `applications.json`. It has no optimistic revision/ETag check, atomic temporary-file replacement, conflict resolution or append-only event history. Two browser tabs or interrupted writes can lose annotations. Deleting a profile removes it from the registry but the code comment says its underlying files are kept. That needs an explicit user-facing retention and deletion policy.

The local discovery client similarly writes a complete `localStorage` object; two tabs may overwrite the last saved state. A live source refresh is not a transaction with applicant workflow annotations.

## 5. Authentication, privacy and AI

Binding the server to loopback is a useful local isolation boundary, but API endpoints have **no per-user authentication**. Other local processes can use them; browser-origin protection, anti-CSRF pairing and an explicit localhost threat model are not shown in the route dispatcher. The upload route parses base64 `data:` content, writes it to the configured uploads directory, and exposes `GET /uploads/*` without per-document authorization. Applicant transcripts, statements, referee documents and identification files require a private, authenticated storage boundary if hosted or shared.

The AI settings are saved as JSON under the local data folder, including provider API keys. The public settings endpoint omits the key and returns only a presence boolean, which is a good UI practice, but the storage itself is not encrypted in the inspected code. The configuration accepts a user-specified provider `baseUrl`; this should be restricted/validated if local APIs are ever exposed beyond the trusted user.

## 6. Operational design and time semantics

The backend uses finite HTTP timeouts (25 s for source fetches, 45 s for AI requests) and a body-size cap; page collection errors are returned separately. The calendar/front-end date logic uses local-day approximations that are not equivalent to source-defined closing timezone/time. URL-based source IDs and inferred opportunity type are useful discovery keys, not official award proof.

The repository has an explicit license, contributor notes, a check workflow and static Pages deployment workflow. These artifacts establish a tested development intent, but this review did not run tests or verify a deployed build.

## 7. Evidence and validation limits

Inspected `server.mjs`, `opportunity-watch.js`, architecture docs, workflows, package/source tree and route implementations. No live fetch, local app, upload, AI API call, browser test, permission test or concurrent-write experiment was run. Network-origin/cross-site exploitability was not independently established.

Pinned evidence: [server](https://github.com/RahulShastri003/application-tracker/blob/5cda0d97907f7940f94dff312a5196da7f54f981/server.mjs), [discovery view](https://github.com/RahulShastri003/application-tracker/blob/5cda0d97907f7940f94dff312a5196da7f54f981/opportunity-watch.js), [architecture](https://github.com/RahulShastri003/application-tracker/blob/5cda0d97907f7940f94dff312a5196da7f54f981/docs/ARCHITECTURE.md), [check workflow](https://github.com/RahulShastri003/application-tracker/blob/5cda0d97907f7940f94dff312a5196da7f54f981/.github/workflows/check.yml).

## 8. PhD Atlas transfer decision

Adopt local-first storage, profile isolation, visible source/adapter errors, customizable discovery filters, per-source provenance and timeouts. Add per-document authorization, encrypted credentials, event-sourced applicant status with versioning, atomic writes, source-snapshot hashes, official deadline timezone and confirmed funding/eligibility evidence before hosted deployment. Do not use heuristic match scores as chances of admission.
