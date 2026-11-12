# Repository review: EydlinIlya/BlueSky-PhD-jobs (PhD Sky)

## Review disposition
- Depth: deep static implementation and generated-output review; not runtime-tested.
- Pinned upstream commit: 352551f3ffa4b880e09635f66ea2b06d888e8ef3 (2026-11-11).
- Scope: 19,681 tracked files; 19,583 under docs/, predominantly generated static output; 32 source modules, 29 test files, 9 migrations, 6 workflows. The generated corpus was inspected by representative pages and generator logic, not by reading every generated page.
- GitHub metadata: Apache-2.0, 15 merged pull requests, zero open issues at inspection. A sequence of daily generated SEO commits demonstrates active automated publishing; it does not establish data accuracy.
- Runtime: no execution; GitHub API source inspection only.

## Purpose
Discover academic jobs from public Bluesky posts, classify them, deduplicate reposts, enrich job metadata, publish a searchable feed and SEO pages, and notify subscribers. The project includes PhD and postdoctoral opportunities and is not restricted to doctoral admission.

## Architecture and data flow
1. **Acquisition**: src/sources/bluesky.py authenticates with AT Protocol, searches a configurable list of PhD/postdoc phrases, expands facet URLs, extracts quoted-post and embedded-preview context, skips the service's own account, and tracks seen URIs.
2. **Persistent staging**: src/pipeline/stages/fetch.py writes rows into Supabase phd_positions_staging keyed by (run_date, uri). It also merges a known aggregator's root+reply posts.
3. **Classification**: src/pipeline/stages/filter.py runs a structured LLM classifier, storing verification flag, discipline, country, position type, job title, organization, application URL, deadline, and enrichment timestamp. Provider adapters include Mistral, Gemini, Groq, and NVIDIA NIM with a fallback abstraction.
4. **Deduplication**: src/dedup.py first normalizes application URLs, checks quote/reply relationships, then compares TF-IDF n-gram cosine similarities. Exact or high-similarity matches can be resolved deterministically; uncertain pairs can be checked by an LLM. Canonical post URI is retained with duplicate_of links.
5. **Publish**: src/pipeline/stages/publish.py upserts all staging rows, including rejected and duplicate posts, into the canonical Supabase table and clears staging/checkpoints after a successful save. The public queries select verified canonical rows.
6. **Presentation**: scripts/generate_seo_pages.py creates docs/positions pagination, per-position pages, country/discipline hubs, snapshots, sitemap index and JobPosting JSON-LD for sufficiently enriched active listings. docs/app.js powers search, saved filters, follows and account UI.
7. **Delivery**: scripts/send_subscription_digests.py groups saved searches per owner, sends a weekly Resend digest, and advances each subscription watermark only after the provider accepts delivery. Unsubscribe uses token-based one-click and human-confirmation routes.
8. **Automation**: GitHub Actions schedules four ingestion runs per day; the static site is regenerated once daily. Other workflows cover digests, SEO metadata backfill and related publishing.

## Data and provenance
- Canonical position key: AT URI; post text, original Bluesky URL, poster handle, creation/indexing timestamps.
- Classification fields: is_verified_job, disciplines, country, position_type.
- Enrichment fields: job_title, hiring_organization, application_url, application_deadline, location_text, seo_enriched_at.
- Dedup: duplicate_of; staging additionally stores raw_text, metadata_text, quoted_uri, reply_parent_uri.
- Subscriptions: user_id, filters, cadence, delivery flags, watermark and unsubscribe token.
- The term is_verified_job denotes LLM/classifier acceptance, not verification against an official hiring organization's application page. Do not map it to the research project's OFFICIAL_VERIFIED status.

## Source-verified engineering findings

### Positive patterns
- Durable per-row filter completion and run checkpoints allow retry after interruption.
- Exact application-link normalization preserves meaningful vacancy query parameters and strips tracking noise; regression tests cover this.
- Batch and existing-post dedup are separated, and newer posts can supersede older canonical records.
- A 2026-09-16 merged hotfix preserves staging on a failed upsert and checks the save count before cleanup. PR #7 reports 188 passing tests at merge time; this is historical PR evidence, not a test result from this session.
- Public Supabase rows are protected by row-level security policies for read-only access, while user subscriptions have owner-scoped policies.
- HTML/script embedding uses JSON escaping and has tests for stored XSS payloads.
- JobPosting structured data is gated on presence and validity of essential fields; incomplete or archived pages are noindex.
- Digest tests cover unsubscribe, duplicate matching, watermark behavior and overflow disclosure.

### 1. LLM parse failures can become permanent false negatives
src/llm/classifier.py catches malformed model JSON and produces a negative classification. src/pipeline/stages/filter.py marks that row filter_completed=True, and the publisher persists it. Unlike LLMUnavailableError, which interrupts and resumes, parse failure is not retried. A genuine position can be silently rejected.

Recommendation: distinguish CLASSIFICATION_FAILED from NOT_A_JOB, persist the failure reason and retry budget, and require positive evidence for a negative classification when the input is otherwise a plausible vacancy.

### 2. The --no-llm path violates the meaning of verified
In src/pipeline/stages/filter.py, classifier=None sets is_verified_job=True for every pending row. bluesky_search.py also treats a missing provider as no classifier. Thus absence of credentials or an explicit bypass can promote unclassified social posts to the public verified set.

Recommendation: use UNCLASSIFIED, CLASSIFIED_JOB, REJECTED, and OFFICIAL_VERIFIED as separate states. Bypass should not produce verified rows.

### 3. Supabase publish cleanup is not atomic
The publish stage upserts canonical rows, then separately deletes staging and run records. A crash between these operations can replay rows; the URI upsert makes this mostly idempotent, but duplicate relationship updates and checkpoint consistency are not transactional across the whole operation. A full staging delete also assumes no other worker is concurrently inserting.

Recommendation: publish in a transaction or use run-scoped state transitions with concurrency locks, not a global delete.

### 4. Unbounded historical dedup computation
src/dedup.py retrieves all existing canonical posts and performs TF-IDF comparisons. Batch pairwise cosine similarity grows quadratically in batch size; existing-post comparison scans the historical corpus. The 19k generated-page repository is not itself the input size, but the architecture has no retrieval index or bounded candidate generation.

Recommendation: use deterministic URL/URI keys first, then indexed candidate retrieval by organization, title, domain, and time window before semantic/LLM comparison.

### 5. Social source is not official evidence
The system extracts social posts, quotes and previews but does not universally fetch and verify the university's official job listing. Its verification flag therefore means relevance classification, not that the position, deadline, funding or eligibility is officially confirmed.

Recommendation: retain the social post as a lead; create a separate official-source verification task with source URL, capture date, exact quotation and change history.

### 6. Email delivery is at-least-once, not exactly-once
After a successful send, subscription watermarks are updated in separate database calls. A crash between provider acceptance and watermark commit can resend a digest. This is preferable to losing an alert, but must be described accurately.

Recommendation: store a delivery outbox with idempotency keys and per-recipient state, then reconcile accepted sends.

### 7. Legacy static test is stale
tests/test_subscription_editor_static.py asserts that docs/index.html contains the literal phrase "gathered from Bluesky with help from artificial intelligence". The pinned docs/index.html does not contain it; the current meta description instead says positions are collected from public Bluesky posts. The exact assertion therefore cannot pass at the pinned snapshot. PR #15 also documented one pre-existing homepage-copy assertion failure at that time. This is a static contradiction, not an executed test result.

### 8. Search and freshness limitations
The AT Protocol search calls are query-based and limited per query; the source does not exhaustively crawl all academic vacancies. Posts are filtered by created_at and seen URI, so backfilled, edited, late-indexed, or search-missed posts can be lost without a recovery run. A 90-day age fallback keeps positions visible when no supported deadline exists, but does not prove that applications remain open.

## Development history
- Early architecture introduced persistent four-stage pipeline and scheduled runs.
- September 2026 PRs added SEO metadata, publish-failure recovery, frontend fixes, archive views, and subscription digests.
- PR #13 migrated digest delivery to opted-in subscribers, including owner-wide unsubscribe.
- PR #15 kept digest links on the site's own domain; its description reports 218 tests passing and one known failing homepage-copy assertion at that revision.
- November daily commits mostly regenerate static SEO content; they are not evidence of new algorithmic features.

## Reusable methodology
Use this project as an opportunity-intake subsystem, not as an authoritative admissions source:
social lead -> canonical opportunity identity -> relevance classification -> official vacancy retrieval -> evidence extraction -> eligibility and funding validation -> deadline status -> dedup -> applicant fit -> alert.
Preserve source provenance, extraction timestamp, model/prompt version, and independent verification status.

## Coverage and limitations
Inspected source, migrations, GitHub workflows, PR descriptions/diffs, representative generated pages, and tests across classification, dedup, SEO, security and digests. Did not execute the 29 test files, verify production credentials, inspect the entire 19,583-file generated docs corpus, or verify live vacancies. No claims of current acceptance or job availability are made.

## Evidence
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/tree/352551f3ffa4b880e09635f66ea2b06d888e8ef3
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/pipeline/stages/filter.py
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/dedup.py
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/src/storage/supabase.py
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/352551f3ffa4b880e09635f66ea2b06d888e8ef3/scripts/send_subscription_digests.py
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/pull/7
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/pull/13
- https://github.com/EydlinIlya/BlueSky-PhD-jobs/pull/15