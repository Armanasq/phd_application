# Academic vacancy crawlers and scholarship scraper prototypes

Session: gpt6-20261112-01  
Review date: 2026-11-12  
Static source review only; no crawler was executed.

## 1. Khayrulbuet13/AcademicJobScraper

- Upstream: https://github.com/Khayrulbuet13/AcademicJobScraper
- Snapshot: `13981e7dd13cab8a56a566b677833959b99f440f` (main)
- License: MIT. Inspected README, package source, CLI and full tree.
- Scope: one source, AcademicJobsOnline. The user supplies a search-results URL manually; the package extracts job links, fetches detail pages, extracts title/institute/description/canonical URL and keyword-filters the descriptions.
- The scraper uses fixed URL-path matching and brittle HTML structure/style selectors. It does not normalize job records beyond four fields.
- `requests.get` has no explicit timeout, retry/backoff, user-agent policy or source-specific error classification. A one-second delay is used between detail pages.
- Absolute links are accepted if they contain `/ajo/jobs/`; no strict same-origin validation is applied before fetching them.
- Keyword matching is raw substring inclusion; no field-specific weighting, negation handling, phrase normalization or relevance evaluation.
- Each run overwrites links CSV, full JSON and filtered CSV. There is no historical snapshot, stable opportunity ID, status, deadline, funding, eligibility, supervisor or source freshness record.
- The CLI is a thin wrapper around the scraper; no tests or CI were found.

Disposition: `PRELIMINARY_FOCUSED`; a simple single-source extraction example, not a complete opportunity-monitoring system.

Evidence: [scraper](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/academicjobscraper/scraper.py) · [CLI](https://github.com/Khayrulbuet13/AcademicJobScraper/blob/13981e7dd13cab8a56a566b677833959b99f440f/academicjobscraper/academicjobscraper/cli.py)

## 2. JaykishanJ/PhD_Finder

- Upstream: https://github.com/JaykishanJ/PhD_Finder
- Snapshot: `809cb3cc4edef615fe12eea1cb53f28a73b10d8b` (main)
- Inspected: `phd_vacancy_finder_pro.py`, GUI, seed/keyword files and repository tree.
- Review state: `PRELIMINARY_FOCUSED`.

### Architecture

A multi-source crawler focused on multi-omics research opportunities. It uses seed URLs, a breadth-first crawl, requests/BeautifulSoup extraction, heuristic topic scoring, country/region inference, SQLite persistence and a desktop GUI.

### Findings

- The crawler uses a `requests` timeout and a bounded depth/page budget, and stores structured opportunity rows with first/last-seen and content-hash fields. These are useful foundations.
- `allowed_text` includes the very short token `ai`; substring matching can classify generic terms such as `training` or `paid` as AI-related. Research-topic precision is therefore unreliable.
- Domain validation accepts a URL if the base domain appears anywhere in the full URL string. A malicious link can include the trusted domain in a query/path while using a different host; validation must compare parsed hostname and registrable domain.
- A sitemap/robots helper exists but was not observed in the main crawl path. The crawler should explicitly enforce robots policy and per-source crawl constraints.
- Unknown deadlines are treated as open in the status path. Unknown must remain `UNKNOWN`, not `OPEN`.
- Country inference uses domain heuristics and a limited country map. Ireland, Luxembourg and New Zealand are not consistently represented in region selection; an empty region match falls back to all seeds, silently ignoring the selected filter.
- Deadline parsing supports a limited set of date formats and does not consistently preserve timezone/cycle semantics.
- Funding score is based on keyword presence such as funded/stipend/scholarship; this is not evidence of full tuition plus living-cost coverage or international eligibility.
- The `content_hash` is stored but the data model does not preserve a full source-history series or claim-level source snapshots.
- Topic matching and supervisor extraction are regex/substring heuristics. No calibration dataset, extraction tests or precision/recall report was found.

### Adoption decision

Retain the bounded BFS, structured SQLite records and first/last-seen concepts. Replace URL validation with parsed-origin allowlists, separate topic and funding evidence, use explicit `UNKNOWN` states, preserve snapshots and implement country coverage as a normalized ISO-code taxonomy.

Evidence: [crawler](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/phd_vacancy_finder_pro.py) · [GUI](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/gui_app.py)

## 3. ledmands/education_job_scraper

- Upstream: https://github.com/ledmands/education_job_scraper
- Snapshot: `9304bc99e92eb68dfe3c7ef8c655f48090c61ab3` (main)
- License: MIT. Inspected README, `run.py`, `scrape.py`, `extract.py`, `send.py`.
- Scope: scrape academic/education listings from Academic Jobs Online, Chronicle of Higher Education and NAAEE; extract recent postings to text files; email each source extract to a configured recipient.

### Findings

- `run.py` reads sender credentials and recipient details from local plaintext files and automatically sends all extracts after each run.
- The `if __name__ == "main"` guard is incorrect, and `main()` is also called unconditionally at module import. Importing the module can trigger scraping and email delivery. This is an unsafe side effect.
- On a first Academic Jobs Online run with no previous database row, the default cutoff string is sliced as though it were a tuple result; this can produce an invalid date string and fail before scraping.
- The Chronicle scraper checks the status code of the earlier search response rather than the actual listing response.
- Requests lack explicit timeouts, retry/backoff and structured error recovery.
- SQLite tables are described as pre-created but the README's SQL examples do not define primary keys or unique constraints. Deduplication/history guarantees are weak.
- Extract generation overwrites text files; no durable notification outbox or sent-state record exists.
- Email delivery is automatic and has no dry-run, preview, recipient allowlist, idempotency or failure recovery. It should never be run with real credentials during a repository audit.
- The project covers general education jobs, not specifically funded PhD vacancies.

Disposition: `PRELIMINARY_FOCUSED`; useful reminder that notification delivery is a separate side effect requiring explicit approval and durable idempotency.

Evidence: [run.py](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/run.py) · [scrape.py](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/scrape.py) · [send.py](https://github.com/ledmands/education_job_scraper/blob/9304bc99e92eb68dfe3c7ef8c655f48090c61ab3/send.py)

## 4. ibrar-saeed-dev/scholarship_scraper

- Upstream: https://github.com/ibrar-saeed-dev/scholarship_scraper
- Snapshot: `16d5ef8c63b8464e07aa03e80a5f7f441d79a01e` (main)
- License: MIT. Inspected Expo app structure, README, Supabase edge function and migration.
- Scope: mobile scholarship directory backed by Supabase, with an edge function intended to refresh scholarship records.

### Findings

- The edge function defines a static `TARGETS` list. Several parsers return hard-coded scholarship objects rather than extracting the program's current cycle, deadline, amount or eligibility from the fetched HTML. The network fetch mainly confirms that a page is reachable.
- Several sources that require JavaScript are explicitly skipped. This means the advertised multi-source scraper has incomplete source coverage.
- Records are marked `is_active: true` and `funding_type: Fully Funded` even when the parser has no current deadline, cycle, tuition terms or source-level funding proof.
- The target list mixes PhD, Master's, undergraduate exchange and certificate programs. Degree-level strings are inconsistent; exact-value UI filters can silently omit or misclassify records.
- Amounts and coverage are broad static descriptions, not verified award components or applicant-specific eligibility.
- The auto-expire update is only useful when a real deadline exists. Most hard-coded entries have null deadlines, so they remain active indefinitely.
- The migration contains a cron expression with placeholder project/key values; unless those placeholders are replaced in deployment configuration, the scheduled job will not run as intended.
- The repository includes Supabase temporary project metadata files. These should not be committed; they disclose infrastructure identifiers even if they are not service-role secrets.
- The migration does not establish the full table schema or RLS policy set. Security depends on external Supabase configuration not present in the repository.

### Adoption decision

Do not adopt the current static parser as a live scholarship source. Retain the app's global catalog concept only after adding per-field evidence, source snapshot/fetch date, program cycle, degree level, nationality restrictions, award-component normalization, RLS migrations and independent verification.

Evidence: [edge scraper](https://github.com/ibrar-saeed-dev/scholarship_scraper/blob/16d5ef8c63b8464e07aa03e80a5f7f441d79a01e/supabase/functions/scraper/index.ts) · [Supabase migration](https://github.com/ibrar-saeed-dev/scholarship_scraper/blob/16d5ef8c63b8464e07aa03e80a5f7f441d79a01e/supabase/migrations/20240101000000_scraper_setup.sql)

## 5. beepboopshru/scholarship-scraper

- Upstream: https://github.com/beepboopshru/scholarship-scraper
- Snapshot: `978efe791425ff407bcc8597fd536e1448b93eb1` (main)
- Inspected: scraper entry point, site modules, cleaner utility and requirements.
- Review state: `PRELIMINARY_FOCUSED`.

### Findings

- The project is a skeleton for scraping Chegg, DAAD and Fastweb scholarship pages.
- The main entry point and site modules rely on brittle CSS selectors and do not establish stable structured records.
- The selectors are placeholders/fragile; a missing element can abort extraction or return empty data.
- Requests lack timeouts, retries, rate limiting and source-level error handling.
- No source freshness, award cycle, eligibility, degree-level, deadline or funding-component verification is modeled.
- The output directory is assumed to exist; no robust persistence, deduplication or test suite is present.
- Requirements include packages that are not used in the inspected path, while the code's actual execution contract remains incomplete.

Disposition: `PRELIMINARY_FOCUSED`; incomplete prototype, not suitable for production adoption.

## 6. Atashi1990/FundBaMa

- Upstream: https://github.com/Atashi1990/FundBaMa
- Snapshot: `1a6528d6d2aca91965a0af6723935d5094ae3cb1` (main)
- Inspected: Next.js app tree, locale pages, message catalogs and package configuration.

The repository is a static multilingual marketing/information website for education/scholarship services. The reviewed pages contain static copy and promotional claims (including counts of universities/countries), but no operational scholarship database, verified opportunity ingestion, user application state, backend API, source provenance or tests were identified. It is not an implemented PhD discovery or application-management system.

Disposition: `SCREENED_EXCLUDE` from the core repository implementation corpus; retain only as a low-priority UI/content reference. Promotional counts are not evidence of actual coverage.

## 7. AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo

- Upstream: https://github.com/AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo
- Snapshot: `6dd9ad9f9a696f985b0c83877941712d3ad937f4` (main)
- The tree is an empty README and a Java Maven calculator classroom exercise; `Calculator.add` is unimplemented and returns zero.
- The `SOP` token refers to a classroom/project identifier, not Statement of Purpose.

Disposition: `SCREENED_EXCLUDE` — false positive.

## Cross-repository conclusion

Most simple scrapers stop at extracting links and keyword-filtering descriptions. A reliable pipeline must add bounded crawling, strict source-origin controls, typed records, normalized countries and cycles, evidence for every funding/eligibility claim, durable snapshots, deduplication, notification outbox semantics and human verification.