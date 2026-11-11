# benhichem/scholarships_scraper — deep static source review

**Review date:** 2026-11-12  
**Pinned commit:** [e3220c1bf032f151c210ebfb44b0f0bdb5a92c58](https://github.com/benhichem/scholarships_scraper/commit/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58)  
**Classification:** DEEP_REVIEW_DOCUMENTED (source-level only, not executable validation).  
**Disposition:** reject current crawl/queue algorithm; adapt typed source adapters after redesign.  
**Scope:** README, complete 17-file source/data tree, package metadata, BigFuture and College Scholarships extractors, Scholarships.com extractor, CSV utilities, types, history, issue/PR listing; CareerOneStop implementation only partially accessible via connector.

## 1. Intended capability

A Bun/TypeScript crawler for four US scholarship portals: BigFuture/College Board, CareerOneStop, College Scholarships, and Scholarships.com. The application uses source-specific scripts, Cheerio HTML parsing, a common scholarship shape and PapaParse CSV persistence. Four repository-stored directory CSVs total approximately 7.6 MB, but these prebuilt URL inventories do not establish valid current awards, complete source coverage, or live crawler success. The project is not a PhD-specific search engine.

## 2. Execution architecture and record model

The `package.json` scripts directly invoke `src/big_future.ts`, `src/careeronstop.ts`, `src/collegescholarships_org.ts`, and `src/scholarships.com.ts`. The collectors read a comma-joined URL list from the first row of an existing directory CSV; fetch one scholarship page at a time; parse free-text award, eligibility and deadline fields; then export scholarship objects and the remaining URL queue to CSV.

The shared `ScholarshipScrapeResult` type defines amount ranges, award frequency, opening/closing dates, geography, age/degree/major requirements, sponsor, and optional essay/merit/need attributes. It does not attach source-specific content hashes, acquisition timestamp, claim evidence spans, cycle, applicant nationality, tuition coverage, stipend duration, or independent verification state. A loosely typed extraction result is not evidence that a scholarship is currently open.

## 3. Deterministic queue-correctness defects

- **Index skipping:** all inspected `Main` loops use `for (var i = 0; i < dirs.length; i++)` and call `dirs.splice(urlIndex,1)` after completing the current URL. The next URL shifts into the current index; incrementing `i` skips it. A list of four URLs can process the first and third while leaving the second and fourth as remaining. This is deterministic source-level behavior, not speculation.
- **Ineffective retry cap:** `TRIES` and `MAX_RETRIES` both increase after failure. The invariant `MAX_RETRIES - TRIES = 3` is preserved, so `TRIES === MAX_RETRIES` can never become true through that path. The loop advances to the next URL rather than retrying the failed one, despite the README's “up to 3 attempts per URL” claim.
- **Crash-unsafe progress:** the queue and accumulated results are written at the **end** of the run, rather than after each completed item. An interrupted process loses in-memory completions and repeats them after restart. Calling the persistence “real-time” and “automatically resumable” is not supported by these paths.
- **Append without stable key:** `exportToCSV` reads the previous CSV and concatenates new rows, then rewrites the whole file. There is no unique scholarship ID or idempotent upsert, so retries can duplicate awards and source records. Writes are non-atomic.
- **Unreachable initialization:** `readCSV(DIR_URLS_PATH)` is invoked before the `if (dirs.length > 0)` branch. With a missing directory file, `readFileSync` raises before the code can discover URLs. The documented empty-start discovery path requires a file with the correct row shape to exist first.
- **Silent parsing failures:** the College Scholarships per-page parser catches errors and returns `undefined`, yet the caller still removes that URL from the queue. A page with missing `dl` pairs reaches `results.reduce` without an initial accumulator and can throw.
- **Data mapping error:** the College Scholarships result maps `ageMax` from `"Min. Age"` rather than the maximum-age field.

## 4. Source acquisition and trust

BigFuture extracts `script#__NEXT_DATA__` page properties and a CSS-selected directory. College Scholarships uses fixed page structures, `dl` pairs and fragile positional selectors. Scholarships.com uses nested positional selectors such as `nth-child` to extract award fields; a redesign can silently change field meaning without an error.

The College Scholarships pagination path uses `eval(FinalPageUrl?.split("=")[1])` on data derived from fetched HTML. This is unnecessary execution of untrusted source data and must be replaced by strict integer parsing and a bounded page limit. HTTP fetch paths lack explicit consistent timeouts, abort budgets, retry classification and health telemetry.

Some link extraction uses string concatenation and substring checks rather than parsed origin validation. Current implementations should not be used for arbitrary, unaudited URLs.

## 5. Provenance, currency and eligibility

Award amount and date fields are raw strings. There is no verified applicant class, nationality/country restriction, doctoral-only filter, funding duration, minimum/maximum academic-year interpretation or official funder confirmation. Precommitted directories are discovery leads; their size does not demonstrate a valid number of awards.

The project should distinguish a scholarship directory, award listing, application page and authoritative funder notice. Retain `source_url`, `fetched_at`, `content_hash`, normalized cycle, raw field text, verified claims and a reviewer decision. Unknown must not mean open, fully funded or eligible.

## 6. Security, reliability and licensing

The README claims an MIT license and points to a LICENSE file, but none exists in the 17-file default-branch tree. Treat reuse rights as unconfirmed pending explicit permission or a published license. No test suite, CI workflow, database schema, migration policy, rate-limit handling or error-budget service contract was found.

The upstream source files contain no apparent direct applicant document processing, which limits personal-data exposure. However, scraping third-party sites requires adherence to site access terms, robots policy and suitable pacing.

## 7. Static evidence versus runtime claims

Observed source logic proves queue skipping, inconsistent retry arithmetic, append semantics and `eval` exposure. It does **not** establish which portals currently accept requests, how many awards are active, whether selectors still work, or whether the Bun TypeScript version compiles. No upstream dependencies, scraper or test suite was executed; `src/careeronstop.ts` could not be fetched through the connector, so its internals remain **NOT_INSPECTED**.

## 8. PhD Atlas design transfer

Preserve source adapter boundaries and a typed extraction schema, but implement the queue as a durable work table: `source_id`, canonical URL, fingerprint, state, attempts, next retry, last error and last successful snapshot. Atomically persist each transition. Never mutate an indexed array while iterating. Use a bounded backoff policy, safe integer parsing, origin allowlisting, test fixtures, source-completeness state and a separate verification pipeline. Keep historical scraped awards distinct from current official funded PhD vacancies.

**Implementation reference:** do not adopt without significant redesign.

### Pinned code evidence

- [README](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/README.md)
- [Package scripts](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/package.json)
- [BigFuture source](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/src/big_future.ts)
- [College Scholarships source](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/src/collegescholarships_org.ts)
- [Scholarships.com source](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/src/scholarships.com.ts)
- [CSV utilities](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/src/utls.ts)
- [Type schema](https://github.com/benhichem/scholarships_scraper/blob/e3220c1bf032f151c210ebfb44b0f0bdb5a92c58/src/index.types.ts)
