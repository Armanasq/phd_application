# psyho/ai-job-scraper — deep implementation audit

**Review date:** 2026-11-12  
**Upstream repository:** https://github.com/psyho/ai-job-scraper  
**Upstream revision:** [8a2944ee1b3c3d50524c6d86b4b3b2155f47ef66](https://github.com/psyho/ai-job-scraper/commit/8a2944ee1b3c3d50524c6d86b4b3b2155f47ef66)  
**Repository ID:** 808089790  
**Review state:** DEEP_REVIEW_DOCUMENTED — core Ruby runtime, parser generation, adapter catalogue, persistence, and notification code inspected statically. No third-party execution.

## 1. Purpose, context and scope
The project monitors academic employment pages, currently a pinned list of 40 German university employment/professorship URLs. Its keyword regex is limited to history/Historiker/Heritage terms; it is neither a comprehensive PhD vacancy database nor a verified funded robotics/AI position finder. It may find scientific staff posts but does not classify doctoral contract eligibility, gross pay, visa status, or deadline.

## 2. Architecture and complete source shape
The 64-file pinned tree includes metadata.json, sites.txt, forty generated Ruby parsers, source under lib/, scripts under bin/, Gemfile/lock and a Ruby 3.3.1 Dockerfile. A rake task starts Runner. The site adapter chooses a Faraday HTML download or Watir headless-Chrome downloader. Downloads are parsed through a per-site Ruby method. New parsed JobPosting records are compared against a JSON file and selected using the fixed regex. Matching jobs are grouped by site and emailed via SMTP using Pony.

Relevant source: [Runner](https://github.com/psyho/ai-job-scraper/blob/8a2944ee1b3c3d50524c6d86b4b3b2155f47ef66/lib/runner.rb), [site dispatch](https://github.com/psyho/ai-job-scraper/blob/8a2944ee1b3c3d50524c6d86b4b3b2155f47ef66/lib/site.rb), [metadata](https://github.com/psyho/ai-job-scraper/blob/8a2944ee1b3c3d50524c6d86b4b3b2155f47ef66/metadata.json).

## 3. Data and decision flow
A site entry holds URL, parser index and whether static HTML suffices. Site.fetch_all_listings runs in parallel threads. Parser.for_site reads a parser source file and invokes instance_eval to define parse_job_postings. The parser converts each returned hash into a record containing title, description, URL, source URL and download time. JobPosting#key concatenates title, description, URL and site URL; the persisted JSON set is used to suppress repeats, and KEYWORDS matches the title/description. Email is delivered only when newly observed matching jobs exist.

The generator script bin/make_parsers feeds downloaded HTML to GPT-4o, requests Ruby parser code, executes that generated code against the HTML, and iterates model revisions. This offline code-generation path is different from normal recurring scraping, but both consume generated parser files.

## 4. Evidence-supported failures and trust boundaries
- **LLM-to-code execution:** bin/make_parsers evaluates generated Ruby using instance_eval. Parsing untrusted source HTML into executable code crosses an unsafe trust boundary. This is not a defensible auto-deploy design without code review, isolation and policy checks.
- **Lost notifications on failure:** Runner saves all newly fetched job records to JSON **before** calling NewJobsEmail.deliver. If SMTP fails, the next run may consider these records already seen and never retry the missed alerts.
- **Fragile identity:** A small change in description/title changes the key and can re-alert the same opportunity; identical URLs with slightly different text are not normalized. Records also lack a lifecycle or closed/expired state.
- **Parser masking:** Parser#try_parse catches StandardError, logs it and returns [], so a broken selector becomes a zero-result site without a clear persisted source-health failure.
- **HTTP and page failure controls:** SimpleDownloader applies three retries but sets no explicit HTTP timeout in its Faraday request and does not check the HTTP status before parsing; a transient error page can be classified as zero vacancies.
- **Unsafe outbound HTML rendering:** The email ERB template interpolates scraped job title, URL and description directly into HTML without explicit escaping. Source content is not trusted.
- **No verified eligibility fields:** JobPosting stores no funding, salary, location normalization, application closing date or international applicant eligibility.

These findings are static code inspection, not evidence of an exposed deployment or an actual exploit.

## 5. Software and testing quality
The project has runtime dependencies for Faraday, Nokogiri, Watir, Honeycomb, OpenAI, Pony and Parallel. Docker installs Chrome and executes a rake task. bin/test_parsers checks only whether a generated parser returns a non-empty list from a sample HTML file. It does not assert record accuracy, correct URLs, deduplication, delivery idempotency, temporal validity or source compliance. No CI workflow or rigorous regression suite was found in the inspected tree. No source website, browser, SMTP endpoint, OpenAI API or Docker container was run.

## 6. Provenance and ethics
The repo stores site URLs and collection timestamp but not the raw HTML snapshot checksum, CSS/parser version per record, evidence excerpt or original recruitment notice revision. Scraping source institutions requires current terms/robots/rate-limit review. Emailing on regex matches is discovery only; it cannot substantiate live PhD recruitment or funded employment.

## 7. Cross-repository comparison and transferable patterns
Relative to dhcoders/JobsACUK-WebScraper, this has a richer adapter catalogue, configurable parallelism, per-site static/dynamic selectors and SMTP monitoring, but a more severe generated-executable-code surface. Relative to Mohamed-2030-M/scholarship-scraper, it has less defensible semantic evidence verification. Retain the architecture of per-site collectors, common typed record output and observability, but replace parser generation with reviewed, sandboxed templates and fixture-based tests. Use canonical posting URLs, snapshot hashes, explicit source health, expiration rechecks, per-site fetch budgets, and an outbox that retries until delivery acknowledgment.

## 8. Verdict and verification
**DEEP_REVIEW_DOCUMENTED, BLOCK production reuse as-is.** Source files, dependency manifests, scraper metadata, representative generated parser, email template and local test harness were inspected. Remaining: inspect every one of the forty generated parsers individually; confirm source permissions and contemporary selector validity; run tests with deterministic fixtures; measure false positives and duplicate alerts; perform secure execution and SMTP failure testing. No live vacancy or funding claim verified.
