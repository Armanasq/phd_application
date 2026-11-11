# Cross-repository synthesis — session 2cabbe82

Date: 2026-11-12  
Scope: ten assigned repository investigations; session-specific evidence only. This is a methodological synthesis, not an independently validated systematic review.

## 1. Functional architecture taxonomy

| Capability | Observed implementation patterns | Main weakness exposed |
|---|---|---|
| Vacancy capture | Browser DOM, HTTP fetch, share intents, CSV, source adapters | Fetch failure and source identity often poorly modeled |
| Opportunity discovery | Search APIs, source lists, official-domain heuristics, social platforms | Search result and official source are conflated |
| Extraction | LLM JSON/schema/tool calls, regex parsing, HTML parsing | Model confidence is mistaken for truth |
| Normalization | Typed records, country/date/funding normalization, per-source IDs | Ambiguous dates and funding collapsed into binary values |
| Evidence verification | Quotes, content hashes, URL checks, secondary model checks | Quote existence is not proof of officialness or applicability |
| Deduplication | Source-prefixed IDs, title/provider hashes, canonical IDs | Cross-source duplicates survive; same-name awards can be merged |
| Workflow state | pending/approved, application statuses, review queues | Crawlers or model outputs can prematurely approve facts |
| Persistence | Firestore, SQLite/Django, Turso, local JSON | Privacy, transactions, history and multi-user boundaries vary |
| Monitoring | Scheduled jobs, coverage rows, notifications, progress counters | Failure and budget exhaustion may be hidden as empty success |

## 2. Reusable architecture

The strongest combined design is a claim-centered, event-auditable pipeline:

`SourceRegistry -> FetchAttempt -> SourceSnapshot -> ExtractionCandidate -> Claim -> VerificationDecision -> CanonicalOpportunity -> ApplicantEligibility -> ApplicationAction`

### SourceRegistry
Stable source identity, owner institution, exact permitted hosts, source class, retrieval policy, rate limits, cycle and applicant scope.

### SourceSnapshot
Exact URL after redirects, fetched timestamp, publication date, content hash, HTTP status, parser version, raw artifact pointer and content type. Failed fetches remain failed attempts; they do not advance the successful-content hash.

### ExtractionCandidate
Typed model output with schema version, provider/model, prompt version, token/cost telemetry, nullable fields and explicit missing-field list. Treat all source text as untrusted input.

### Claim
One claim per field: deadline, cutoff time, funding amount, tuition coverage, duration, eligible nationality, separate application, language score, degree prerequisite, etc. Store exact evidence span and scope (institution, department, program, cycle, applicant class).

### VerificationDecision
Independent reviewer, timestamp, decision (confirmed/corrected/conflict/unresolved), source revision, reasoning and superseded claim. Model confidence must not be a verification status.

### CanonicalOpportunity
A vacancy/program/award can be supported by multiple upstream sources. Keep upstream IDs and URLs as aliases; merge only when identity confidence is sufficient. Model bundled scholarships as parent/child awards, not one giant row.

### ApplicantEligibility
Join private applicant facts to public verified requirements. Unknown qualification, nationality, fee, funding or language state blocks a positive eligibility conclusion. Do not store private evidence in the public source corpus.

### ApplicationAction
Track draft, reviewed, approved, submitted, interview, offer and rejection as separate states. External email/submission actions require explicit user authorization and immutable action evidence.

## 3. Cross-cutting engineering principles

1. **Tri-state semantics:** `eligible / ineligible / unknown`, `funded / unfunded / unknown`, and `confirmed / conflict / unresolved`. Never map missing information to positive eligibility.
2. **Temporal correctness:** keep publication time, retrieval time, cycle year, source timezone, date-only vs cutoff time, and last verification separately.
3. **Idempotency:** stable source observation IDs and content hashes; replaying the same fetch must not duplicate or mutate user application state.
4. **Concurrency:** run/unit leases, execution tokens, stale-worker rejection, bounded retries, and transactional commits.
5. **Evidence provenance:** every material displayed fact needs a URL and field-specific support, not a generic citation at record level.
6. **Untrusted input:** prompt injection isolation, safe HTML rendering, SSRF-resistant URL fetchers, redirect revalidation, private IP blocking and strict outbound allowlists.
7. **Privacy separation:** private CV, SOP, email, referees, immigration and degree evidence are isolated from public repository research.
8. **Human authority:** LLMs propose, parse and summarize; humans or independently verified official sources establish factual truth and approve external actions.
9. **Operational observability:** track attempted/successful fetches, extraction failures, budget exhaustion, review backlog, freshness and source drift.
10. **Reproducibility:** pin source commit, parser/prompt/schema version, dependencies, test fixture, command and execution environment.

## 4. Repeated failure patterns and evidence

- **Auto-approval:** FundMyStudy's direct insert path promotes pending items and exposes no-op moderation helpers. A crawler must never be able to approve its own output.
- **False international eligibility:** scholarship scraper verification logic treats missing restriction as a positive international result. Missing text is Unknown, not Eligible.
- **Weak domain checks:** VidyaSetu substring host checks and CS_APP_Agent educational-TLD/substring heuristics can misclassify non-official hosts.
- **False confidence:** PhDHub and tracker agents expose confidence values without calibrated validation; PhD Tracker uses model confidence to auto-save.
- **Lossy dates:** local date-only deadlines, inferred year, ambiguous day/month and timezone mismatch can change actual cutoff.
- **Poor cross-source identity:** source-prefixed deduplication does not merge mirrored vacancies.
- **Privacy/security:** plaintext API keys, unauthenticated Streamlit deployments, wildcard CORS, unescaped `innerHTML`, untrusted email content and unrestricted URL fetching.
- **Stale cycles:** annual scholarships require cycle-specific records; prior confirmed deadlines cannot confirm the next cycle.

## 5. Admissions methodology learned from non-software sources

The curated reading list and personal SOP corpus contribute a different evidence type:
- Strong applications connect prior research contributions to a specific future agenda.
- Program-specific fit should be grounded in faculty/lab work, not rankings alone.
- Advisor evaluation includes supervision style, group culture, publication expectations, funding continuity and autonomy.
- SOP examples are structural references, not reusable prose or proof of admission.
- Applicant artifacts must be distinguished from verified admission/funding outcomes.

The SOP corpus is private-sensitive and lacks a license; do not republish its contents. Its best use is a private version-comparison and claim-grounding workflow.

## 6. Prioritized PhD Atlas adoption backlog

### P0 — correctness and trust
- Claim-level provenance and evidence spans.
- Explicit Unknown/conflict states.
- Official host verification and safe fetch policy.
- Cycle-specific deadlines with timezone/cutoff semantics.
- Independent funding and international eligibility gates.
- No auto-approval from ingestion/model confidence.

### P1 — data and workflow integrity
- Canonical opportunity + source alias model.
- Parent/child scholarship awards.
- Source snapshots and versioned extraction.
- Run/unit leases and stale-worker protection.
- Append-only verification and application-action history.
- Private artifact vault with access controls.

### P2 — usability and automation
- Browser-rendered capture and CSV import/export.
- Deadline notifications and backlog views.
- Supervisor/PI research and structured outreach review.
- Email classification with prompt-injection boundary.
- Interview preparation linked to verified papers and applicant research.

## 7. Evidence and limits

The findings above are supported by the session's per-repository artifacts under `research/sessions/2cabbe82/reviews/`. They are source-level static findings. The session could not clone repositories or execute tests because its container could not resolve `github.com`. No third-party code is certified secure, production-ready or runtime-validated by this work.
