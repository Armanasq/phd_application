# Cross-repository synthesis — mainline batch, 2026-11-12

## 1. Distinct evidence classes discovered

The latest batch contains several different kinds of repositories that should not be collapsed into one opportunity table:

| Evidence class | Repositories | What the data can establish |
|---|---|---|
| Scholarship ingestion software | aluminium5, atomdbc, benhichem, beepboopshru, colonket | Source acquisition and extraction patterns; not current eligibility without verification |
| Faculty discovery directory | bodzioney/phd-applications | Researcher identity and research-area leads; not current hiring or funding |
| Local vacancy monitor | chuyaowang/nl-phd-tracker | User-saved job records and applicant annotations; not an authoritative vacancy source |
| Applicant preparation guides | binhu02, chinasaokolo | Preparation methodology and support-program discovery; not current institutional rules |
| Historical vacancy/resource lists | arunrathi9, borekda | Historical discovery leads and example schemas; not current openings |
| Applicant research proposal | CodeBoyPhilo | Example of research framing; not proof of admission or successful submission |

This taxonomy should be reflected in the PhD Atlas data model. A supervisor directory, current vacancy, funding award, applicant-support program and SOP/proposal artifact have different freshness, evidence and privacy requirements.

## 2. Ingestion completeness is a first-class property

The ScholarshipScraper audit exposes a dangerous pattern: a bounded 25-page incremental crawl is treated as a complete source snapshot. Any observed record set can then deactivate every database row not seen in the partial sample. Partial page failures and rejected rows can produce the same destructive outcome.

Atlas ingestion should return an explicit result:
- `complete_snapshot`: authoritative complete inventory;
- `partial_snapshot`: some pages fetched, source coverage incomplete;
- `empty_verified`: complete source checked and no current opportunities found;
- `failed`: fetch/parser/source contract failed.

Only `complete_snapshot` may reconcile unseen records. Incremental crawls should update `last_seen_at` and use a conservative expiry policy. Empty results must never be conflated with parser failure.

## 3. Extraction is not verification

The Telegram monitor and multiple scholarship scrapers use an LLM to classify or extract content. They do not consistently preserve exact claim evidence, official-source identity, current-cycle applicability or an independent verification decision.

A robust record needs separate states:
`discovered -> fetched -> extracted -> evidence_attached -> source_verified -> cycle_verified -> applicant_scope_verified -> human_approved`.

Model confidence should control review priority, not factual truth. A public Telegram post or scholarship aggregator is a lead; the official funder or university page must establish the claim.

## 4. Faculty availability must be time-bounded

The PL Theory directory demonstrates a useful tri-state `taking_students` field. Of 367 faculty entries, only 24 are marked true, 4 false and 339 unknown. However, there is no claim-level source, quote, checked timestamp or validity period for that field.

Atlas should distinguish:
- faculty identity;
- research fit;
- expressed willingness to supervise;
- currently recruiting;
- funded opening;
- funding available to the applicant's citizenship/class.

These must be separate claims, each with evidence and freshness. A faculty homepage or Google Scholar profile is not evidence of a funded vacancy.

## 5. Local-first tracking and data preservation

The AcademicTransfer tracker shows the value of local-first storage, stable external job IDs, pagination and preserving manual annotations across refreshes. Its empty-result sync can still overwrite the local catalogue. A safe sync must validate response completeness, protect non-empty data from unexpected empty responses, write atomically, and retain multiple recoverable backups.

The tracker is also noncommercially licensed; implementation patterns may inform design, but code reuse requires separate permission.

## 6. Applicant materials and support programs

The research-proposal repository and curated guides should live in a private applicant-preparation workspace, not the public opportunity registry. Their content may contain personal academic information and third-party copyrighted text. The applicant-support catalogue should be a separate entity from funded PhD opportunities and should be revalidated every cycle.

## 7. Security and operational controls

The scholarship-scraping prototype demonstrates why public URL ingestion requires:
- SSRF-resistant URL validation and redirect revalidation;
- network-isolated browser workers;
- authentication and authorization on task and destructive endpoints;
- bounded crawl/model budgets;
- prompt-injection isolation for source pages;
- durable worker leases and per-task database sessions.

The Telegram monitor needs per-message cursors, durable processing states, explicit send acknowledgements, deterministic retention and an audit queue for human approval. Mark a message processed only after extraction and delivery/review state have been persisted.

## 8. PhD Atlas implementation priorities

1. Add source-snapshot completeness and explicit parser-health states.
2. Model claim-level evidence, source scope, cycle and validity.
3. Keep Unknown distinct from ineligible, unfunded or not recruiting.
4. Separate public opportunity data from private applicant artifacts.
5. Implement canonical opportunity identity with source aliases and parent/child awards.
6. Use safe URL/browser execution and strict API authorization.
7. Protect local syncs against empty responses, concurrent writes and process interruption.
8. Add regression fixtures for partial crawls, source layout changes, date/timezone behavior, duplicate records and model failures.

**Evidence boundary:** this synthesis is based on pinned repository source/documentation reviews. No third-party code was executed and no live scholarship, faculty hiring or admissions claim was verified.
