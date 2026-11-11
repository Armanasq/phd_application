# Cross-repository synthesis — admissions research and execution systems

Session: gpt6-20261112-01  
Date: 2026-11-12  
Scope: 18 relevant/adjacent repository identities or fork variants inspected in this session, plus one static marketing-site exclusion and one keyword-collision false positive. All source findings are pinned in the individual review files.

## Scope note

The AcademicTransfer tracker (`chuyaowang/nl-phd-tracker`) and the scholarship scraper skeleton (`beepboopshru/scholarship-scraper`) have since been reviewed and committed by another session on `main`. Their mainline reports are treated as existing evidence; they are not counted as independent reviews produced by this session.

## 1. The common system is a lifecycle, not a single tracker

The repositories collectively expose a multi-stage applicant lifecycle:

1. **Discover** institutions, supervisors, vacancies and scholarships.
2. **Extract** source content into candidate records.
3. **Normalize** institutions, people, locations, degree levels, cycles and award components.
4. **Verify** each claim against the original source.
5. **Assess fit and eligibility** for the candidate, country and application cycle.
6. **Prepare** CV, research narrative, SOP, recommendation packet and supporting documents.
7. **Contact** supervisors and record correspondence.
8. **Apply** through the official portal with explicit authorization.
9. **Prove submission** using a receipt/confirmation.
10. **Track decisions, funding terms, immigration and onboarding** after an offer.

No inspected repository implements this entire chain reliably. Scrapers usually stop at link extraction; trackers usually begin after a user has already found a position; outreach systems focus on supervisor communication; applicant guides cover post-admission steps but are not current policy databases.

## 2. Distinguish the core entities

The repositories repeatedly conflate entities that must remain separate:

| Entity | Meaning | Evidence required |
|---|---|---|
| Institution | University/research organization | official institutional identity |
| Supervisor | Researcher and research fit | authoritative profile/publications; identity confidence |
| Vacancy | Specific funded employment/research call | vacancy-specific official notice |
| Program | Doctoral admission route | program and cycle requirements |
| Scholarship/award | Funding mechanism attached to a candidate/program | official award terms, eligible nationalities, amount and duration |
| Funding component | Tuition, stipend, travel, insurance, relocation, fees | component-level evidence and currency |
| Applicant eligibility | Candidate-specific gate | degree, grades, language, nationality/residence and other requirements |
| Application | Candidate's instance for a particular vacancy/program/cycle | owner, stage, documents and actions |
| Submission event | Actual external submission | portal receipt/confirmation and timestamp |
| Offer | Formal admission/employment offer | official offer letter and funding terms |

A professor's research fit is not proof of an open position. A program page is not a vacancy. A scholarship title is not a complete funding package. An application status is not a submission receipt.

## 3. Strong reusable implementation patterns

### Source ingestion

- Aditi's source-specific listing/detail split and Khayrulbuet's simple extraction pipeline demonstrate why each source needs its own adapter and selectors.
- Jaykishan's bounded breadth-first crawl, SQLite storage and first/last-seen fields are useful starting points for change detection.
- Chuyao's stable external job ID and preservation of user-owned notes/status across sync is a strong pattern: remote refresh must not overwrite human annotations.
- Source adapters should emit raw observations and extraction candidates, not verified opportunity records.

### Applicant workspaces

- GradKit's configurable columns and local-first workflow provide flexible personal case management, but stable row IDs are essential.
- DrPod separates programs, requirements, documents and associations; its data model is useful if ownership, RLS and private storage are made explicit.
- ATUL's module breadth shows the expected user-facing surface (applications, tasks, calendar, interviews, analytics), but hard-coded demo data and disconnected backend modules must not be mistaken for a functioning data layer.
- The Chinese workbench provides a useful artifact sequence: research identity, school/advisor notes, CV, research summary, outreach, SOP, recommender packet, submission checklist, interviews and offer comparison.

### Supervisor outreach

- AcademiaReach provides the clearest end-to-end supervisor workflow: discovery, enrichment, paper recommendations, draft generation, review, explicit send, and reply tracking.
- Its database deduplication and modular SMTP/IMAP boundaries are worth studying.
- Sending needs a server-enforced approval state, explicit attachment allowlist, per-user authorization, rate limits, idempotent outbox and delivery receipt.

### Post-admission operations

- The Farsi-language Groningen guide shows that application management does not end at acceptance. Registration, document submission, university immigration services, residence authorization, embassy, travel, housing and onboarding are separate tasks with different owners and evidence.
- Its fork lineage demonstrates why source dependence must be tracked: multiple forks of one guide are not multiple independent applicant experiences.

## 4. Recurrent anti-patterns and failure modes

### Evidence and funding

- Defaulting missing funding evidence to `Fully Funded` (Centrix and the static scholarship directory) creates false-positive funding claims.
- Treating a broad program page as a current vacancy or a historical scholarship as an open call is invalid.
- A stipend field without currency normalization is not comparable; `stipendUSD` populated with GBP/EUR/CHF values is a data-integrity defect.
- Unknown deadline, nationality or tuition coverage must remain `UNKNOWN`, not `OPEN`, `ELIGIBLE` or `FULLY_FUNDED`.

### State integrity

- Centrix can mark applications submitted when automation only fills fields or when its service is unavailable. Only a real portal receipt can transition an application to `SUBMITTED`.
- Scrapers that mark a record seen before successful notification can permanently lose alerts.
- Email sending without an outbox/atomic claim can duplicate messages on concurrent requests or after partial failure.
- A read request that deletes expired records, or a database setup script that drops a live database, violates non-destructive state management.

### Security and privacy

- Disabling TLS verification, following unvalidated pagination URLs, accepting arbitrary crawler links, or exposing local automation endpoints creates credential and SSRF risk.
- Public Git repositories containing resumes, databases, personal correspondence or credentials create immediate privacy risk.
- Public document URLs are inappropriate for transcripts and recommendation letters.
- Unescaped scraped/user-provided text in `innerHTML`, email HTML or Telegram HTML creates injection risk.
- A local-only service still needs an origin/CSRF boundary and strict request validation.

### Scoring and matching

- Keyword overlap is not semantic fit. Very short tokens such as `ai` can create false positives.
- Heuristic fit/reply scores are not calibrated probabilities and must not be presented as acceptance or response odds.
- Name matching based on character-position similarity is not reliable identity resolution.
- Region filters must not silently return all records when no records match.

### User-interface integrity

- Sorting/filtering a display array and then using its displayed index to mutate the underlying array can edit/delete the wrong record (GradKit).
- A dashboard with hard-coded fixture data must label it as a demo and must not display live/verified counts.
- A backend folder or API health check does not prove that the visible UI uses that backend.

## 5. Recommended target architecture

### Ingestion layer

- Source registry with official domain, allowed paths, robots/terms policy, crawl frequency, pagination rules, parser version and contact.
- Per-source adapter with bounded requests, TLS verification, timeout, retries, `Retry-After`, content-size limits and same-origin/redirect validation.
- Persist raw HTML/PDF/API snapshot metadata (URL, fetched time, content hash, response status) separately from extracted fields.
- Parser emits typed candidates with field-level extraction confidence and exact source evidence spans.

### Evidence and verification layer

- Model each fact as a claim with `subject_id`, `predicate`, `value`, `source_id`, `observed_at`, `valid_for_cycle`, `evidence_span`, `verifier`, `status` and `confidence_class`.
- Use `VERIFIED_PRIMARY`, `CORROBORATED`, `FIRSTHAND_SINGLE`, `INFERENCE`, `UNVERIFIED` and `CONFLICTED` states.
- Funding must be decomposed into tuition, stipend, duration, travel, insurance, fees and eligibility. Never infer complete funding from a title or a single keyword.
- Keep source lineage and fork/copy relationships so derivative guides are not counted as independent observations.

### Matching and decision layer

- Separate research-fit scoring from vacancy availability and candidate eligibility.
- Use interpretable criteria and evidence-backed gates; do not output calibrated probabilities without outcome data and calibration.
- Keep missing values null/unknown and expose conflicts rather than choosing the favorable claim.

### Applicant workspace

- Stable IDs for programs, vacancies, supervisors, documents and applications.
- Preserve user annotations across external refreshes.
- Store private documents in non-public object storage with per-user authorization, signed URLs, retention and deletion controls.
- Use explicit state transitions with audit events; `SUBMITTED` requires a portal receipt.
- Use an outbox for email/notifications and an explicit approval step for all external actions.
- Provide CSV/JSON export, backups, migration versioning and deterministic restore tests.

### Cross-country layer

- Country policy is not a global attribute: admissions model, employment status, fee category, visa, degree equivalence and deadlines vary by country and program.
- Each country dossier should map official sources and recheck cadence; historical applicant accounts are explanatory evidence, not current policy.
- The user's target countries require dedicated coverage. Netherlands and US-specific workflows are only transferable as process patterns.

## 6. Prioritized transfer into phd_application

1. Preserve the existing evidence ledger and source-dependency crosswalk; extend them with raw snapshot hashes and claim-level evidence spans.
2. Add explicit `UNKNOWN`/`CONFLICTED` semantics for funding, fee coverage, nationality, deadline cycle and portal status.
3. Add stable source IDs and source-specific adapters with parser fixtures and freshness monitoring.
4. Model vacancies, programs, scholarships, funding components, supervisors and applications as separate entities.
5. Keep applicant-private documents outside public Git and separate from the public research inventory.
6. Use the AcademiaReach review-first outreach pattern but enforce approval and idempotent delivery server-side.
7. Use Chuyao's preservation of user annotations on sync, while hardening token handling and pagination.
8. Use the Chinese workbench's artifact sequence, but replace US-only quotas and dates with country-specific evidence.
9. Reject false-positive automation states; require external receipts for sent/submitted transitions.
10. Test failure modes explicitly: source changes, duplicate jobs, deadline ambiguity, expired funding, unauthorized access, failed notifications, concurrent sync, and interrupted document replacement.

## 7. Research limitations

- This synthesis is based on static repository inspection. No third-party project was run, no real portal submission or email was performed, and no live external database was accessed.
- Some repositories contain private or potentially identifying binary artifacts; these were deliberately not opened.
- No applicant success-rate or acceptance-probability inference is made from public repositories.
- This session's reports supplement the mainline corpus; they do not claim global repository-discovery saturation.