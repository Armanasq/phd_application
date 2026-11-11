# Deep static reviews — admissions automation, local tracking and outreach

Session: gpt6-20261112-01  
Review date: 2026-11-12  
All findings are static source observations at the pinned upstream commits. No third-party service, database, email account or browser automation was executed.

## 1. centrixsol/phd-applicant

- Upstream: https://github.com/centrixsol/phd-applicant
- Snapshot: `c1b33eb17d8c57efed957c3cd33fe2ebb2355927` (main)
- Repository metadata: 853 KB; no license or issue history observed.
- Inspected: README, Prisma schema/seeds, Next API routes, middleware, automation engine, Varbi crawler, Docker/Python service and requirements.
- Review state: `DEEP_REVIEW_DOCUMENTED` — static architecture and high-risk execution paths inspected; runtime not executed.

### Intended product and architecture

A full-stack PhD application CRM with Next.js/TypeScript UI, Prisma/MongoDB persistence, applicant profile and document storage, AI-assisted program research, opportunity seeding, and a Python Playwright automation service. The advertised workflow covers program discovery, applicant profile completion, document uploads and portal form automation.

### Data and execution flow

1. Prisma seeds create program records from hard-coded university/program entries.
2. The Next.js UI stores applicant/profile/application records in MongoDB.
3. AI routes assemble a candidate profile and generate program-specific application material.
4. The apply API sends applicant data, document paths, portal credentials and application URL to a Python FastAPI automation service.
5. Playwright navigates to the portal, attempts login/registration, fills fields and uploads documents.
6. The Next API updates application state based on the automation response.

### Critical correctness and integrity defects

- The Prisma `Program` model defaults `fullyFunded` to `true`; the seeded records do not provide field-level source citations, verification timestamps, award terms or international-fee evidence. Missing funding data can therefore become a positive funding claim.
- The field `stipendUSD` is populated with values from programs whose source currency is GBP, EUR or CHF. This creates unit corruption unless conversion is explicit and timestamped.
- Several seed deadlines are month/day strings without a year or timezone. They cannot be safely interpreted as an application cycle or compared chronologically.
- The data model mixes program, admission route and funding opportunity. A program record is not proof of an open funded vacancy or guaranteed funding.
- The apply route uses a hard-coded/default applicant identity rather than deriving the owner from the authenticated session and enforcing ownership on the application record. This is not a safe multi-user boundary.
- The Python automation service listens on `0.0.0.0` and has no service-to-service authentication in the inspected route. CORS restrictions do not authenticate direct HTTP clients.
- The automation request accepts an application URL and local document paths without a robust portal-domain allowlist or canonical file-root enforcement. This creates SSRF and local-file exposure risk if the service is reachable by an untrusted caller.
- The automation engine uses generic field-name heuristics and portal aliases rather than verified per-portal form adapters. It can map semantically different fields (for example, residence country versus citizenship) incorrectly.
- The Varbi and generic paths report a submitted state after form filling/manual-review prompts; they do not prove that the final application was actually submitted.
- If the automation service is unavailable, the Next API fallback can still set a demo/submitted state. This is a false positive and corrupts application history.
- The Prisma `Application` model stores portal credentials as plaintext fields. Sensitive credentials should be encrypted with key management or, preferably, not retained.
- Uploaded documents are placed under `public/docs`; the application expects publicly addressable URLs. This is inappropriate for transcripts, CVs, recommendation letters and identity documents.
- The document upload route lacks robust server-side file type/size validation. The file naming path incorporates caller-controlled values; enforce a generated safe filename and storage-root containment.
- The AI route uses a default applicant identity. Profile ownership and data minimization must be enforced before sending personal data to an external model.

### Positive patterns

- The product separates program discovery, applicant profile, document management and portal automation into identifiable components.
- A dedicated automation service is a useful boundary if it is authenticated, network-restricted and constrained to allowlisted portals and explicitly selected files.
- The UI/CRM concept captures the need to track requirements and application state rather than only store a list of links.

### Adoption decision

Do not reuse the current auto-apply path or schema as-is. Retain only the broad domain decomposition. A production design needs evidence-bound program/funding records, per-user authorization, encrypted secrets, private object storage, allowlisted portal adapters, explicit user confirmation, and a submission receipt before the state can become `SUBMITTED`.

Evidence: [Prisma schema](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/prisma/schema.prisma) · [seed data](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/prisma/seed.ts) · [apply API](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/src/app/api/apply/route.ts) · [automation engine](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/automation/engine.py) · [automation service](https://github.com/centrixsol/phd-applicant/blob/c1b33eb17d8c57efed957c3cd33fe2ebb2355927/automation/main.py)

## Mainline overlap — chuyaowang/nl-phd-tracker

The repository has since received a separate review on `main` under `research/repositories/reviews/chuyaowang__nl-phd-tracker.md`. This session's earlier exploratory inspection is withdrawn from the PR to avoid duplicate ownership. The merged mainline report is authoritative for canonical review coverage.

## 2. Joky02/AcademiaReach

- Upstream: https://github.com/Joky02/AcademiaReach
- Snapshot: `ac8765fb0e559b1a5245e7b262765bf8173492dc` (main)
- License: MIT; 15 stars; no issues observed.
- Inspected: README, FastAPI routes, Pydantic models, search/enrichment/compose agents, draft-review scorer, SMTP/IMAP services, database logic, tests, Docker Compose and worker boundary.
- Review state: `DEEP_REVIEW_DOCUMENTED` — static source/test review; tests not executed and no real email sent.

### Product and workflow

AcademiaReach is a supervisor-discovery and outreach CRM. It combines CSRankings-based candidate discovery, LLM-assisted profile enrichment, research-paper recommendations, personalized email drafting, a deterministic draft-review queue, explicit send endpoints, SMTP delivery, IMAP reply polling and a professor/application dashboard.

Workflow:

1. Search candidate supervisors by research keywords and region.
2. Enrich identity, homepage, Scholar profile, research summary and recent papers.
3. Generate a personalized draft from the applicant profile and supervisor context.
4. Rank drafts using a heuristic review score and let the user edit/review them.
5. Send through SMTP using an explicit API action.
6. Poll IMAP and associate replies with supervisor records.

### Strengths

- It decomposes discovery, enrichment, composition, review, sending and reply tracking into separate services.
- Database deduplication merges duplicate professor records while preserving linked drafts and replies.
- SMTP/IMAP clients are separated from the agent layer and have unit tests.
- Docker Compose applies meaningful container hardening: read-only filesystems, tmpfs, dropped capabilities, `no-new-privileges`, internal service exposure and socket-based worker boundaries.
- The Codex worker is configured as a separate read-only service, limiting the agent execution surface.
- The README describes a review-first process and keeps SMTP/IMAP configuration in a local ignored config file rather than the public repository.

### Risks and limitations

- The FastAPI routes do not implement application-level user authentication or per-user authorization. The deployment relies on private networking and optional Cloudflare Access. Exposing the web app publicly without an Access policy would expose professor records and email-sending operations.
- `send_email` checks whether a draft is already sent, but the service layer does not require `DraftStatus.APPROVED`; the tests explicitly exercise sending a pending draft. The UI's explicit send action is therefore the effective gate, not a server-enforced approval transition.
- `send_email` attaches PDFs found in the configured papers directory, rather than a per-draft allowlisted attachment set. This can attach unrelated or sensitive papers to every message. Require explicit attachment selection and show a final attachment manifest.
- There is no atomic `pending/approved -> sending` compare-and-set or transactional outbox. Concurrent send requests can race, and an SMTP success followed by database failure can lead to duplicate delivery on retry.
- `reply_likelihood_score` is a deterministic heuristic, not a calibrated probability. It uses tags, paper/venue features and keyword signals; it must be labelled as a priority heuristic, not a predicted response probability.
- Candidate search results are enriched by an agent, but the database does not retain field-level provenance and verification timestamps for every email, research interest or recruiting claim. `source=auto` is not adequate evidence lineage.
- The candidate ranking relies partly on name/university/region and static CSRankings data; it does not establish that a professor is currently recruiting or has funded capacity.
- IMAP matching by sender/subject needs ambiguity handling for forwarded replies, shared lab inboxes and repeated subject lines.
- Batch sending is sequential but lacks a clearly enforced daily send budget and per-domain pacing in the reviewed send path.

### Adoption decision

Adopt the staged workflow, data separation, deduplication and explicit human review. Add server-side authorization, verified-email state, source evidence per claim, attachment allowlists, approval enforcement, idempotent outbox delivery, rate limits and a receipt/audit record. Do not interpret the heuristic score as admission or reply odds.

Evidence: [search agent](https://github.com/Joky02/AcademiaReach/blob/ac8765fb0e559b1a5245e7b262765bf8173492dc/backend/agents/search_agent.py) · [draft review](https://github.com/Joky02/AcademiaReach/blob/ac8765fb0e559b1a5245e7b262765bf8173492dc/backend/services/draft_review.py) · [send service](https://github.com/Joky02/AcademiaReach/blob/ac8765fb0e559b1a5245e7b262765bf8173492dc/backend/services/send_service.py) · [routes](https://github.com/Joky02/AcademiaReach/blob/ac8765fb0e559b1a5245e7b262765bf8173492dc/backend/api/routes.py) · [Docker Compose](https://github.com/Joky02/AcademiaReach/blob/ac8765fb0e559b1a5245e7b262765bf8173492dc/docker-compose.yml)

## 3. Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP

- Upstream: https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP
- Snapshot: `08b002c7db7816da198891d034c24894af1007a6` (main)
- No license or issue history observed.
- Inspected: Flask application, scraper/source lists, database setup/import, search and resume-matching routes, requirements and relevant templates.
- Safety boundary: the repository contains committed résumé PDFs and SQLite databases. Their contents were deliberately not opened or reproduced.
- Review state: `DEEP_REVIEW_DOCUMENTED` for source code; sensitive binary/database artifacts excluded.

### Architecture and dataflow

A Flask portal scrapes institute pages for JRF/SRF/RA/internship-like opportunities, stores results in SQLite, exposes search/filter pages, and accepts résumé uploads for keyword-overlap matching. The data source set is predominantly Indian institutes and is not aligned with the current target-country portfolio.

### Correctness and security findings

- Source fetching disables TLS certificate verification (`verify=False`).
- The crawler mainly identifies links using broad keyword matching; it does not robustly parse individual calls into verified title, funding, eligibility, deadline, supervisor and cycle fields.
- The résumé matcher uses basic token/keyword overlap, not semantic NLP or a calibrated fit model. Common terms can inflate the score; no validation set or precision/recall evaluation is shown.
- Uploaded résumé filenames are used in filesystem paths without robust generated-name/containment checks. There is no clear authentication, upload size/type policy, retention policy or deletion lifecycle.
- The `get_data` path deletes expired rows as a side effect of a read request. Reads should not perform destructive lifecycle mutations.
- `setup_database.py` removes/recreates the database file, which can destroy collected data if run against a live database.
- `search` uses `str.contains` with user text as a regular expression by default; malformed regex input can fail or change filtering behavior.
- Chat UI code interpolates user input and responses into `innerHTML`, creating a stored/reflected DOM-XSS risk if untrusted values reach the browser.
- The repository includes personal résumé PDFs and database files in public Git. This is a serious privacy/data-governance failure. Do not inspect or reproduce those artifacts; the owner should remove them from public history and rotate any exposed secrets if present.
- There is no test suite or documented source-verification process.

### Adoption decision

Do not reuse the current upload, database-reset, TLS or HTML-rendering patterns. The institute-source catalog can be used as a discovery lead only. Rebuild ingestion around official source adapters, claim-level evidence, safe file handling, private document storage, non-destructive migrations and a tested matching model.

Evidence: [Flask application](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP/blob/08b002c7db7816da198891d034c24894af1007a6/app.py) · [scraper](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP/blob/08b002c7db7816da198891d034c24894af1007a6/scraper.py) · [database setup](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP/blob/08b002c7db7816da198891d034c24894af1007a6/setup_database.py) · [source list](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP/blob/08b002c7db7816da198891d034c24894af1007a6/sources.py)

## Cross-repository synthesis

These systems demonstrate three distinct responsibilities: opportunity ingestion, applicant case management and supervisor outreach. They should remain separate bounded services connected through typed, evidence-backed records. Auto-application is not an acceptable default: any external submission requires user authorization and a verifiable receipt.