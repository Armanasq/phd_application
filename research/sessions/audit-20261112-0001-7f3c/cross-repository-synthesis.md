# Cross-repository synthesis — audit 20261112-0001-7f3c

**Scope:** archna1212/PHD-OPENINGS, Ariaeimehr/PHD-Position-Finder, and arbitan/ScholarshipWebsite. This is a source-backed synthesis of the current batch, not a completed global systematic review.

## 1. Comparative disposition

| Repository | Actual artifact | Evidence status | Disposition |
|---|---|---|---|
| archna1212/PHD-OPENINGS | Copy of the PhD-Seeker Python scraper | 9/9 non-README file blobs identical to Aghababaei/PhD-Seeker | Exclude as an independent implementation; retain MIRROR_OF lineage |
| Ariaeimehr/PHD-Position-Finder | Python multi-source scraper plus React/Express demonstration UI | Source implementation inspected; funding and vacancy claims are not independently verified; no runtime tests | Deep static review; do not adopt current truth/verification semantics |
| arbitan/ScholarshipWebsite | Legacy static faculty article page | Scope established from HTML and permission notice; PDF body not inspected | Exclude as a scholarship/admissions keyword collision |

## 2. Source lineage is not independent evidence

PHD-OPENINGS is not a distinct implementation. Its nine non-README files are byte-identical to the corresponding Aghababaei/PhD-Seeker files, and it contains no unique code path. Its separate repository identity must not be counted as independent corroboration, engineering novelty, or an additional successful applicant experience.

The copied implementation inherits the upstream scraper's unsafe eval of scraped date text, disabled TLS verification caused by a configuration-key mismatch, brittle selectors, weak date semantics, and lack of source-level funding verification. The existing canonical PhD-Seeker review should remain the primary technical analysis; this session adds the repository-lineage evidence.

## 3. A multi-source crawler is not automatically an evidence system

Ariaeimehr's Python worker has useful engineering building blocks: source adapters, bounded retries, request timeouts, jitter, optional proxy support, SQLite seen-state, and separate notification transports. However, its central classification decisions are unsound:
- missing funding evidence defaults to fully funded;
- the AcademicPositions adapter hardcodes salaried funding without checking terms;
- EURAXESS R1 is treated as funding evidence;
- US exclusion ignores the full listing text and relies on fragile location strings;
- topic matching uses substring checks that produce false positives;
- provider-specific result limits are not paginated.

The UI further overstates implementation maturity. The Express endpoint serves a static ten-record fixture rather than the Python worker's database or output. The simulator is timer-driven, the code inspector uses stale embedded snippets, and the config generator embeds credential-shaped defaults. The displayed "100% Fully Funded" and "14 US vacancies filtered" figures are not measured runtime results.

## 4. State and evidence must precede alerts

The Python worker marks a position as seen before notification dispatch and ignores notifier return values. A failed Telegram/email send can therefore permanently suppress an alert. A transactional outbox with pending/sent/failed states, bounded retries, and idempotent delivery is required.

Funding, location, eligibility, deadline, and supervisor availability should be independent field-level claims. A missing value must remain Unknown. A search-provider filter, generic institutional career URL, or LLM-generated summary is not evidence that the vacancy exists or is fully funded.

## 5. UI and backend contracts must be real

The current Python dataclass, TypeScript interface, Express fixture, and static simulator represent different data contracts. A production implementation should define one versioned schema and map every source observation into it. The UI should read from the persisted canonical opportunity store, show source URLs and verification states, and label fixtures explicitly as examples.

The deployment model should separate the worker, API, and frontend or clearly document a worker-only deployment. Docker currently packages only the Python worker; it does not deploy the React/Express interface.

## 6. False-positive control

ScholarshipWebsite uses "scholarship" to mean academic publication, not doctoral funding. It is an unrelated faculty article site with no admissions or opportunity workflow. Keeping the exclusion rationale prevents the same search collision from being repeatedly re-investigated.

## 7. Reusable PhD Atlas architecture

The combined evidence supports the following pipeline:

SourceRegistry
  -> FetchAttempt
  -> ImmutableSourceSnapshot
  -> RawListing
  -> TypedExtractionCandidate
  -> FieldLevelClaim
  -> IndependentVerification
  -> CanonicalOpportunity
  -> ApplicantEligibility
  -> TransactionalNotificationOutbox
  -> ApplicationActionEvidence

Non-negotiable properties:
- canonical source identity and alias graph;
- source revision, fetch time, publication date, and content hash;
- field-specific evidence spans and explicit verification states;
- funding decomposition into salary/stipend/tuition/fees/duration/eligibility;
- tri-state geography and applicant eligibility;
- phrase/token topic matching with ambiguity handling;
- idempotent persistence and delivery;
- escaped notification rendering and validated links;
- secret-free frontend bundles;
- one versioned worker/API/UI data contract;
- parser fixtures, integration tests, and concurrency controls.

## 8. Limits

All findings are static source-level observations. The three projects were not cloned or executed. No live vacancy, funding package, notification delivery, security exploit, or production behavior was independently verified. The Arbitan article PDF was not downloaded or reproduced because it is outside the admissions scope and its permission notice restricts redistribution.
