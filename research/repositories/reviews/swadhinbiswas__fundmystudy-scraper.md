# swadhinbiswas/fundmystudy-scraper — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`7b9337280032d748c10fd136cf74ba8e1da7cd68`](https://github.com/swadhinbiswas/fundmystudy-scraper/commit/7b9337280032d748c10fd136cf74ba8e1da7cd68)  
**Review state:** PRELIMINARY_FOCUSED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** multi_source_opportunity_ingestion  
**Primary risk:** pending_autoapproved_no_real_moderation_funding_inferred  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A TypeScript scholarship and doctoral job intake service with schedules, normalized records, adapter plugins, idempotent database identity and controlled batch submissions. Its most useful result is negative: the project README promises moderation, while the active code path directly writes and auto-approves items, illustrating how documentation can become disconnected from operational safeguards.

## 2. Architecture and actual components

`src/index.ts` schedules `runSource` over enabled adapters; `src/runner.ts` fetches raw listings, validates source-specific shape, normalizes country/degree/funding/date, fetches existing same-source rows for deduplication, and submits batches. `src/api.ts` now wraps direct Turso operations. `src/db.ts` builds `opp-${source}-${externalId}` and persists `raw_payload`. Its individual adapters include EURAXESS, jobs.ac.uk and a curated dictionary of schemes. Unit tests cover normalizer and deduper behavior.

## 3. Task-to-data flow and dependencies

Dataflow is source discovery -> normalize -> identity match -> direct Turso UPSERT; the published state is not an independent review outcome. In `src/db.ts`, `o.status === 'pending' ? 'approved' : o.status ?? 'approved'` promotes pending records. `src/api.ts` explicitly says the bot inserts approved by default and `approve()` and `reject()` are no-ops. The README's moderation promise cannot be used as evidence of implemented moderation. In dry-run, returned accepted count equals request count, which can mislead if interpreted as actual database writes.

## 4. Methods and source-level evidence

Two independent semantic failures: `src/deduper.ts` keys external ID, URL and normalized title/provider with a *source prefix*, so cross-board duplicate jobs are not resolved. Tests explicitly assert different sources should not deduplicate. `src/sources/euraxess.ts` assigns `rawFundingKind = 'full'` whenever `fundingProgramme` is not recognized as 'not funded', including an empty string or named funding scheme; `src/sources/jobs-ac-uk.ts` uses words in search-result title or URL-derived pseudo-provider for 'funded' guesses. Neither proves an individual award covers international tuition and stipend.

## 5. Implementation and operational reconstruction

Date handling also converts date-only/ambiguous source formats to UTC instants without the university's source timezone. `src/normalizer.ts` silently interprets DD/MM or MM/DD depending on inferred order. For a global applicant, the final UTC hour, whether campus-local midnight or 17:00, cannot be invented. Source-specific scraping, fallback/robots compliance and server reliability need independent execution.

## 6. Failure modes and validation gaps

Do not adopt direct writes as authoritative. Require a *real* server-enforced pending/approved/rejected transition with audit actor ID and evidence basis; prevent all crawler jobs from setting `approved`. Compute cross-source canonical vacancy IDs with ambiguity thresholds and preserve each upstream alias; leave funding as Unknown unless covered by official terms. Capture source snippets for each extracted field, source job ID and last-seen date; separately verify eligibility.

## 7. Transfer to PhD Atlas and admissions workflow

Positive transferable engineering: typed adapter interface, normalization maps, raw payload retention, batch submission and explicit per-source metrics. Use them only as ingestion conveniences. Keep user-editable application state in a separate table that scraping cannot overwrite. Source parser assertions must verify that job type and employer name are not inferred from URL slug when actual DOM fields exist.

## 8. Provenance and outstanding verification

Inspected runner, direct DB API, external adapters and unit tests at pinned revision. Finding of autoapproval and absence of cross-source dedup derives from actual code, not README text. Upstream tests, live HTTP, database migrations and 2026 funding/fee claims remain unexecuted/unverified.

## Pinned source files inspected

- [`src/index.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/index.ts)
- [`src/runner.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/runner.ts)
- [`src/api.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/api.ts)
- [`src/db.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/db.ts)
- [`src/deduper.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/deduper.ts)
- [`src/normalizer.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/normalizer.ts)
- [`src/sources/euraxess.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/sources/euraxess.ts)
- [`src/sources/jobs-ac-uk.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/sources/jobs-ac-uk.ts)
- [`src/sources/curated.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/src/sources/curated.ts)
- [`tests/deduper.test.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/tests/deduper.test.ts)
- [`tests/normalizer.test.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/7b9337280032d748c10fd136cf74ba8e1da7cd68/tests/normalizer.test.ts)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.
