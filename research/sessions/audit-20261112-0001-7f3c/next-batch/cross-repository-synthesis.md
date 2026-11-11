# Cross-repository synthesis — batch 2

**Scope:** atomdbc/scholarship_scraper, dhcoders/JobsACUK-WebScraper, evamaxfield/phd, and D4vidHuang/PhD_scanner.

## 1. Comparative findings

| Repository | Resource class | Reusable value | Main limitation | Disposition |
|---|---|---|---|---|
| atomdbc/scholarship_scraper | Full-stack scholarship ingestion and LLM extraction platform | API/worker separation, SQL persistence, dynamic rendering, task progress, dashboard concept | SSRF/auth gaps, missing Playwright dependency, worker state defects, broken data mappings, uncalibrated LLM claims | Deep static review |
| dhcoders/JobsACUK-WebScraper | One-file Jobs.ac.uk polling script | Minimal source-specific extraction example | Incorrect refresh units, wrong deadline association, no timeout/retry/persistence/dedup | Deep static review |
| evamaxfield/phd | Personal doctoral archive | Interview-preparation question bank and post-admission milestone planning | Single-person, personal documents, no cohort or outcome evidence | Preliminary firsthand resource |
| D4vidHuang/PhD_scanner | Empty repository | None | No branches or content | Exclude |

## 2. LLM extraction is not evidence verification

Atomdbc demonstrates a common architecture pattern: crawl pages, classify links with an LLM, ask a second LLM to extract scholarship fields, and store the output in a database. The architecture is reusable, but the output is not authoritative. The model-generated confidence score is uncalibrated, there are no evidence spans, and the source snapshot is not preserved. The pipeline can silently mis-map application URLs, discard normalized amount fields, and treat unverified extraction as a scholarship record.

The PhD Atlas should instead store source observations and field-level claims first. LLMs may propose structured candidates, but the system must verify the original page and preserve currency, award type, amount period, eligibility, deadline, and source provenance independently.

## 3. Source-specific parsing beats generic scraping

The JobsACUK script illustrates how a small scraper can still fail on basic data association. It collects deadline elements globally and assigns the final page deadline to every job. It also uses a refresh interval in the wrong unit. A mature adapter must parse each job card as one atomic record, bind its own deadline and URL, validate source responses, and test selectors against fixtures.

## 4. Workflow state must reflect real operations

Atomdbc's task and progress models are a useful conceptual decomposition, but state transitions are incomplete. A task marked completed is not selected for future scheduling; failed tasks can retry every minute; and a link inserted before AI processing can become permanently skipped if processing fails. A production pipeline needs explicit queued/running/succeeded/retryable-failed/dead-letter states, idempotency, a bounded retry policy, and delivery/extraction receipts.

## 5. Applicant archives are not population evidence

The evamaxfield repository is a personal doctoral archive. Interview notes and planning files can inform checklists, but they are not verified interview transcripts or representative admissions evidence. Personal CVs and statements remain private source material and are not copied into the research corpus. The archive is most useful for distinguishing application preparation from post-admission milestones such as coursework and general examinations.

## 6. Cross-batch engineering conclusions

The two scraper projects expose different failure modes:
- A large stack can still have broken URL safety, dependencies, state transitions, and data contracts.
- A small script can still misassociate deadlines and use incorrect scheduling units.
- A user-facing dashboard can create a false impression of completeness when filters and API contracts are inert.
- LLM confidence is not calibration, and an extracted field is not a verified fact.
- Personal applicant documents require consent and privacy controls, even when publicly accessible.

The combined target architecture remains:

SourceRegistry
  -> FetchAttempt
  -> ImmutableSourceSnapshot
  -> RawListing
  -> TypedExtractionCandidate
  -> FieldLevelClaim
  -> IndependentVerification
  -> CanonicalOpportunity
  -> ApplicantEligibility
  -> Action/NotificationReceipt

Each transition should be observable, versioned, idempotent, and auditable.
