# JaykishanJ/PhD_Finder — deep static crawler audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/JaykishanJ/PhD_Finder | **Pinned commit:** [`809cb3cc4edef615fe12eea1cb53f28a73b10d8b`](https://github.com/JaykishanJ/PhD_Finder/commit/809cb3cc4edef615fe12eea1cb53f28a73b10d8b) | **Review state:** DEEP_REVIEW_DOCUMENTED (static) | **Decision:** selective architecture reference only; not a verified current vacancy feed.

## 1. Scope and implementation

A July 2026 Python desktop application for searching PhD vacancies in multi-omics, bioinformatics, genomics, computational biology and adjacent machine-learning topics. It comprises one 741-line crawler (`phd_vacancy_finder_pro.py`), a 154-line CustomTkinter GUI (`gui_app.py`), `seeds.json`, batch launchers, and a placeholder PyPI release workflow. The README describes direct page crawling, keyword scoring, SQLite deduplication and CSV/HTML reporting.

The recursive tree has 14 entries. No license file, unit tests, issues, PRs, or completed Actions runs were returned. The latest source commit is 2026-07-01.

## 2. Actual acquisition and dataflow

The crawler loads a set of university, job-board, research-institute and social/aggregator seed URLs, selected by geographic substring filters. It requests raw HTML with `requests.get`, strips scripts/styles with BeautifulSoup, follows RSS links and text/path-matched page links with bounded depth/page counts, and identifies candidate pages using keyword inclusion and exclusion. It extracts a title, inferred institution and country, supervisor name, deadline text, posted date, and contact email from page text using regular expressions and heuristic classifiers.

Accepted observations are written to a local SQLite `vacancies` table with a unique `canonical_url`, content hash, `first_seen`, `last_seen`, deadline/status fields and a weighted keyword score. A separate `crawl_errors` table records failures. Outputs are CSV groupings (all, new today, closing soon, strong matches) and a Pandas-escaped HTML report.

Positive mechanisms: persistent content hashes and first/last seen timestamps, source-specific observations, bounded crawl depth, explicit fetch errors, response timeout, separation of extraction and scoring, and HTML escaping in the generated Pandas tables. These are useful starting points but not current-fact verification.

## 3. Reproducible control-flow defect

**The normal GUI does not crawl when its default report option is enabled.** `gui_app.py:start_crawling()` launches `python phd_vacancy_finder_pro.py --daily` and appends `--report` whenever the GUI's `Generate HTML Report` checkbox is true, which it is by default.

In `phd_vacancy_finder_pro.py:main()`, the conditional `if args.report:` loads the existing SQLite table, writes the report and `return`s **before** the `if args.daily` crawler branch. Therefore, the default GUI “Start Crawling” action produces an existing-data report without fetching new sources. This is source-level deterministic control flow, not a live run claim.

The README usage implies that an enabled report option accompanies the crawl. The implementation violates that expectation. Move reporting after crawling or make `--report` report-only only when `--daily` is absent.

## 4. Security and source-integrity weaknesses

- `fetch_url()` follows HTTP redirects automatically, with no policy for initial/final scheme, approved hostname, DNS result, private/reserved IP address or content size. Seeds are curated, but discovered links come from untrusted HTML.
- `discover_links()` accepts links when either the parsed domain matches or the original domain string occurs **anywhere** inside the final URL. A link to a host that merely embeds the seed domain in its name/path can pass. RSS links have no equivalent hostname check at discovery.
- The `get_sitemap_urls()` helper constructs robots and sitemap paths but no robots.txt authorization check is applied in the active crawl function. A robots path is not a robots-policy implementation.
- No content-type allowlist or HTML-size limit is enforced before parsing.
- The crawler uses an arbitrary browser-like user agent and a fixed sleep. It has no persistent per-origin robots/rate policy, circuit breaker, ETag conditional requests or partial-run completeness gate.

The current code is unsafe for unrestricted server-side web crawling until SSRF and request-budget controls are implemented.

## 5. Factual and temporal classification errors

- `deadline_status()` returns `unknown` when date parsing fails or no deadline is found. `crawl_seed()` then maps unknown to `status="OPEN"`. Thus a webpage without a parseable deadline is presented as open, a false-positive state transition.
- `parse_deadline_to_date()` attempts day/month/year formats before month/day/year. Ambiguous dates such as `05/06/2026` silently acquire one interpretation instead of an unknown/needs-confirmation state.
- Substring scoring treats `ai` as an ordinary token anywhere in full page text; it can match unrelated words, inflate relevancy and label generic job pages as AI opportunities.
- The negative keyword check rejects whole pages containing “postdoc”, “seminar”, “news”, etc.; mixed career or university directory pages can be rejected even when they contain a valid PhD posting.
- `extract_country()` searches the entire page text plus URL for domain/term fragments; unrelated institutional links can cause geographic misclassification.
- `score_text()` gives bonus points for keywords such as funded, stipend, grant, scholarship and source-domain fragments; this is *ranking*, not evidence of stipend coverage, international tuition, eligibility or a current paid job.
- SQLite upsert uses canonical URL uniqueness only. A job mirrored on two sources remains a duplicate; one listing URL reused for annual cycles collapses distinct opportunities.
- Old rows are not reconciled against verified source closure; `--list-open` selects every row not marked expired, including unknown deadlines and stale, previously observed pages.
- `--region` filters seeds by broad domain fragments. When no seed matches, `filter_seeds_by_region()` falls back to **all** seeds, which can silently violate a geographic choice. This filter operates on hostnames, not the actual vacancy locations.

## 6. Operations, tests and release

The CLI exposes `--daily`, `--report`, `--list-open`, `--quick`, `--region`, `--max-depth`, `--max-pages`, `--sleep`, and `--timeout`. The `--quick` mode retains the first 20 alphabetically sorted seeds rather than a stratified region/source sample. Database upserts commit each record, preserving basic durability but imposing high overhead for larger batches. There is no transaction to atomically mark a full crawl's completeness.

The repository's `.github/workflows/python-publish.yml` is the generic PyPI publishing template. No packaging metadata (`setup.py` or `pyproject.toml`) is present in the tree, so the configured `python -m build` lacks normal package build inputs; no successful run was found.

## 7. Transfer to the admissions evidence framework

Adopt only: source registry, reproducible keyword scorer (explicitly non-authoritative), SQLite observation identity, content hashes, first/last seen timestamps and HTML-escaped reports.

Required changes before production adoption:
1. Enforce HTTPS/host allowlisting, per-redirect DNS/IP validation, robots rules, body limits and per-host scheduling.
2. Treat result URLs as source observations with an independently verified canonical opportunity entity.
3. Persist raw or bounded evidence, source content hash, statement-specific source spans and evaluation timestamp.
4. Separate `OPEN_VERIFIED`, `UNKNOWN`, `EXPIRED_VERIFIED` and `STALE_SOURCE` states.
5. Record date precision, locale, timezone and recruitment cycle, preserving ambiguous dates as unknown.
6. Maintain crawl run/coverage records and avoid falsely deactivating rows after partial failures.
7. Repair GUI/CLI option handling and add tests for `--daily --report`, redirects, duplicate pages, false-positive funding and date parsing.
8. Verify all position and funding claims from employer institution or award-owner pages, never merely from a high keyword score.

## 8. Pinned evidence and disposition

- [Crawler, classification, DB, CLI](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/phd_vacancy_finder_pro.py)
- [GUI invocation and default report flag](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/gui_app.py)
- [Seed domains and source categories](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/seeds.json)
- [Publish workflow](https://github.com/JaykishanJ/PhD_Finder/blob/809cb3cc4edef615fe12eea1cb53f28a73b10d8b/.github/workflows/python-publish.yml)

**DEEP_REVIEW_DOCUMENTED (static)**, not a source of verified current jobs. Source history, relevant complete crawler code, frontend launch path, DB schema, CLI, config, workflow and security/factual semantics inspected. No live network crawl, test suite, package build, deployment or runtime security validation was performed.
