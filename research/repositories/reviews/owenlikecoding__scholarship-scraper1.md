# owenlikecoding/scholarship-scraper1 — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [70181bc6d3716c60036b9a21006d9578dbafbed8](https://github.com/owenlikecoding/scholarship-scraper1/commit/70181bc6d3716c60036b9a21006d9578dbafbed8).  
**State:** DEEP_REVIEW_DOCUMENTED — full core crawler, TUI, dependency and source tree inspected; HTTP/runtime tests NOT_RUN.  
**Verdict:** strongest lightweight crawler foundations in this batch; adapt after URL safety, extraction semantics and persistence hardening.

## 1. Purpose

A seed-driven privacy-first, local scholarship collector. Python `asyncio`/`httpx`/BeautifulSoup crawler writes a CSV of recognized scholarship pages, without applicant accounts, sign-ins or email collection. An optional Textual UI exposes progress, max pages, max depth, concurrency, per-domain delay, cache and robots controls. It is a generalized scholarship collector, not a dedicated international PhD official-source validator.

## 2. Architecture and model

`scholarship_scraper.py` defines `ScholarshipRecord` with title, canonical-ish page URL, source domain, discovered-from URL, amount min/max/raw text, deadline parsed/raw text, rolling flag, eligibility excerpt, description and `fetched_at`. `crawl_and_extract` seeds an async queue, starts bounded worker coroutines, fetches HTML, extracts text, heuristically classifies a scholarship page, traverses related same-origin links by depth, deduplicates by stripped URL and writes CSV.

The TUI reads config from form controls and streams page events via an in-process async queue, while allowing cancellation and seed selection. The crawler implements a per-domain lock and time gap, a robots.txt parser/cache, HTTP timeouts and TTL-based disk HTML cache. These design choices improve bounded work over common one-off scripts.

## 3. URL and network trust boundary

`normalize_url` uses `urlparse` then adds a scheme to a parsed **path** when the user provides a bare domain. For `example.edu`, the netloc remains empty and URL serialization does not produce a valid `https://example.edu` address. This needs an explicit URL parser/normalization test.

The seeds are otherwise accepted without a scheme/hostname allowlist or DNS/IP/private-range validation, and the `httpx.AsyncClient` uses `follow_redirects=True`. Same-host checks are applied to links **before** fetching them, not to the ultimate redirect target. A malicious or compromised source can therefore redirect requests toward loopback, cloud-metadata endpoints or another private network address if this collector runs in a sensitive environment. Enforce redirect revalidation and network sandboxing for hosted use.

## 4. Robots, crawling and rate limits

The crawler offers a robots.txt check on each uncached page. If robots fetch returns non-200 or raises, the code calls `RobotFileParser.parse([])`, which does not constitute evidence of permission. The outer `fetch_html` catch even sets `ok=True` for unexpected robots-check exceptions. Make the source's fail-open/fail-closed policy explicit rather than claiming universal robots compliance.

The page budget is tracked as the size of a `visited` set and the depth/worker count are bounded; within the async worker path the visited mutation occurs before awaiting a network call. This is useful for avoiding uncontrolled crawl expansion. The implementation does not enforce a response byte cap or a global wall-clock/extraction budget; non-HTML pages are rejected **after** an HTTP response body is fetched. Per-domain throttling is in-memory, so two different processes are not mutually throttled.

## 5. Extraction and date correctness

The page classifier is heuristic keyword matching, not a verified scholarship definition. Amounts and deadlines are inferred from text spans. The date parser uses `PREFER_DATES_FROM=future` and assigns UTC to generic text, even if the source defines its own timezone, cutoff or year. Ambiguous date expressions may be interpreted as future closing dates without explicit source-cycle evidence. `rolling_deadline` is detected via keywords that can appear in surrounding unrelated descriptions.

The output does not separate exact official award evidence from page metadata or advertising content. There is no scholar/institution authority list, applicant-nationality class, scholarship cycle, living stipend and fee breakdown, or source-confidence field.

## 6. Persistence, idempotency and interruption

Records are deduplicated only by a canonical-ish URL within the current run. Every execution opens its CSV output file with mode `w` and overwrites the prior catalogue. User annotations or previous version history in the same CSV are not preserved. Writing is not a temporary-plus-atomic-replace operation; cancellation just before output could drop the current crawl's progress, although the HTTP cache may reduce repeated network work on a retry. Cached HTML files also use direct writes and store no immutable checked snapshot history.

For a growing research corpus, preserve a durable append-only `SourceObservation` collection and separate current record materialization from raw source history.

## 7. Tests and source verification boundary

Inspected the full 19,700-character source crawler, Textual UI, dependencies, README and nine-file tracked tree. No automated tests or CI workflow were found. No live crawl or robots request was executed; no HTTP redirection or date accuracy benchmark was run. The source shows mechanism but cannot prove that any target university currently offers a funded PhD or that sites permit scraping.

Pinned evidence: [crawler](https://github.com/owenlikecoding/scholarship-scraper1/blob/70181bc6d3716c60036b9a21006d9578dbafbed8/scholarship_scraper.py), [TUI](https://github.com/owenlikecoding/scholarship-scraper1/blob/70181bc6d3716c60036b9a21006d9578dbafbed8/scholarship_tui.py), [README](https://github.com/owenlikecoding/scholarship-scraper1/blob/70181bc6d3716c60036b9a21006d9578dbafbed8/README.md), [requirements](https://github.com/owenlikecoding/scholarship-scraper1/blob/70181bc6d3716c60036b9a21006d9578dbafbed8/requirements.txt).

## 8. PhD Atlas transfer decision

Adopt the bounded async queue, source-aware rate limiter, robots policy mechanism, raw HTML cache, `discovered_from` lineage, explicit fetch timestamps and UI cancellation pattern. Add URL/redirect/DNS allowlists and HTTP response-size caps, deterministic fixture tests, source-defined timezone/cycle semantics, schema-based extraction with claim-level evidence, immutable snapshots, atomic writes and per-source completeness status. Do not infer that `record_from_page` classification equals a verified scholarship.
