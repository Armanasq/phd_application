# Cross-repository synthesis — applicant workspace versus vacancy intelligence

**Session:** 20261112-nima-go2phd-8c24  
**Source audits:** [NimaaaAI Position-Aggregator](reviews/nimaaai-position-aggregator.md); [NaughtFound Go2Phd](reviews/naughtfound-go2phd.md)  
**Scope:** two newly selected canonical UNTRIAGED repository identities. Both are independent projects; no shared upstream blobs or fork relationship was established.

## What the implementations actually do

| Project | Evidence boundary | What is usable | What is not established |
|---|---|---|---|
| NimaaaAI/Position-Aggregator | Five public job boards, raw HTML, Postgres, hybrid semantic search, model-generated descriptions | Source-adapter configuration, multimodal retrieval by position/chunk/lexical text, RRF, reranking, country/type filters | A verified live PhD opening, funded status, international tuition coverage, scraper permissions, population completeness, precision/recall, safe deployment |
| NaughtFound/Go2Phd | User-controlled Google Sheet with OAuth read-only access, statistics API | Local applicant-stage organization, simple grouped metrics, Google Sheets as a private workspace backend | Live opportunity discovery, official vacancy evidence, confirmed submission, authenticated applicant eligibility, working documented sheet schema |

Do **not** combine scraped advertisements and user-entered application statuses into a single row with a single unqualified `verified` flag. They have different owners, access boundaries, temporal semantics and evidence requirements.

## Cross-repository engineering defects and their generalization

1. **Contract mismatch:** Go2Phd's nine-column documented input and eight-position parser silently corrupt deadline/rolling/link data. Position-Aggregator's controller and workers disagree on the database DSN. Both need schema/config contracts validated at process boundaries rather than inferred from prose.
2. **Identity mismatch:** Go2Phd assigns row-index IDs that change when a sheet is reordered; Position-Aggregator merges same-title/same-city roles even if their source IDs differ. Durable identity must come from canonical vacancy issuer and application-cycle IDs; cross-source aliases are relations, not destructive merges.
3. **Temporal data loss:** Position-Aggregator can mark an incomplete sitemap census as a full one, skips re-fetch of already-downloaded ads, and can retain stale chunk embeddings after source edits. A vacancy record is *not* a live-opening truth statement; every deadline, funding and hiring assertion needs a dated immutable observation, valid-from/checked-at and current-cycle verification.
4. **Private-state vs public intelligence:** Go2Phd passes per-user OAuth refresh tokens through request headers. Position-Aggregator persists login activity and question text and forwards selected source excerpts to an external LLM endpoint. A private applicant workspace must have its own auth/secrets, retention controls and explicit operation receipts; source discovery and LLM summarization must not imply permission to submit or send email.
5. **Workflow state is not proof:** A Google Sheet `Applied` label and a crawler `closed_at IS NULL` predicate express local state, not source-verified submission or live vacancy. Use `UNKNOWN / SOURCE_OBSERVED / PRIMARY_VERIFIED / CONFLICT / EXPIRED / SUBMITTED_WITH_RECEIPT` as semantically distinct states.
6. **Access and publication rights:** Position-Aggregator explicitly documents scraping pages that its author believes robots rules disallow; the current permission state was not independently verified. Its repository has no visible license. Reuse methods independently, but do not copy code or deploy inaccessible source collectors without rights review.

## Recommended integration architecture

`Official source/allowed feed` -> `bounded acquisition + HTTP/parser status` -> `immutable source snapshot, hash and URL` -> `field-level extracted claims with source span, cycle, locale/timezone` -> `deterministic normalization + non-destructive identity resolution` -> `human or official-source validation` -> `current opportunity index` -> `separate private candidate application workspace` -> `receipt-backed action history`.

Machine retrieval should use Position-Aggregator's demonstrated *structural* idea (position embeddings + chunk vectors + multilingual lexical search fused by RRF), but not assume its result ranking constitutes provenance or funding verification. The prior [PhdInfoHub session supplement](../../2cabbe82/reviews/dxeledx-phdinfohub-supplement.md) offers complementary source evidence and concurrency patterns; its model outputs likewise require deterministic checks and human review.

## Implementation acceptance tests suggested for the main application

- Known nine-column Google Sheet fixture preserves country, deadline, rolling flag and full links; invalid/missing headers fail explicitly.
- Non-default `DATABASE_URL` is honored by scraping, extraction, embedding, search, API and update controller.
- Two PhD openings with the same title/city but distinct issuer IDs are never destructively collapsed; true duplicates retain all source aliases.
- A 403/500 or structurally empty sitemap does not replace a successful census and does not create `closed` evidence.
- Source edit invalidates precisely its stale position/chunk embeddings; an updated deadline is re-fetched with a new snapshot revision.
- Unknown/naive closing date is never promoted to verified open, and a visa/tuition/funding assertion without applicant scope remains unknown.
- Per-user LLM usage allowance is atomically reserved, request size/model IDs are bounded, and application submission status requires an immutable receipt.

## Disposition and validation

- **NimaaaAI/Position-Aggregator:** DEEP_STATIC_SOURCE_REVIEW, `reference`, major correctness/access risks, no upstream runtime test.
- **NaughtFound/Go2Phd:** DEEP_STATIC_SOURCE_REVIEW, `reference`, blocking parser/OAuth documentation mismatches, no upstream runtime test.
- Neither can be treated as a verified opportunity source. Neither contributes independently verified funding, deadline or acceptance-outcome data.
- These session notes are additive; shared candidate CSV, canonical review CSV, exclusion table, research index, status reports and global issue states are left unchanged to avoid conflicts with concurrent agents.
- Canonical integration is **pending a coordinated queue-owner transaction**; after these two reviews are registered, recalculate all coverage counts from primary CSV rows and run repository validation/generator scripts. Do not increase canonical deep-review counts based solely on these session files.
