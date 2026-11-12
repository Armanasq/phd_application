# siyahalp-prog/scholarship-scraper — deep static review

**Reviewed:** 2026-11-12. **Pinned upstream:** [37aac0e88e105364db3bcaa82dd72a4b58d20dcf](https://github.com/siyahalp-prog/scholarship-scraper/commit/37aac0e88e105364db3bcaa82dd72a4b58d20dcf).  
**State:** DEEP_REVIEW_DOCUMENTED; README, tree and all six Python source files inspected. Runtime NOT_RUN.  
**Verdict:** adapt source boundaries, reject as verified international PhD feed.

## 1. Scope

A Python CLI collecting award leads from DAAD, Stipendium Hungaricum and Scholars4Dev, exporting JSON and CSV. Its results cover broad degree levels. No current funded PhD-only status, applicant-class verification or official award confirmation follows from being in this output.

## 2. Architecture

The orchestrator dynamically loads three adapters and invokes each sequentially; Pydantic Scholarship objects contain title, country, nullable date-only deadline, raw amount, raw eligibility and URL. DAAD and Stipendium use Playwright and BeautifulSoup; Scholars4Dev uses Requests. Adapter exceptions are logged while other sources continue. Country filtering checks a substring of title or location rather than applicant eligibility.

## 3. Completeness and source classification

DAAD link discovery includes generic programme anchors, not only award calls. Stipendium follows broad “scholarship”, “programme” and “apply” hrefs. If none are found, it **creates one scholarship row from the homepage heading** and page text; a landing page is not a verified call. Scholars4Dev reads headings and next-page links until its limit but does not record page coverage, authoritative source class or completeness. Relative Scholars4Dev article URLs are passed to Requests without a guaranteed urljoin, potentially failing while still leaving an incomplete record.

## 4. URL and error handling

The browser adapters use urljoin on scraped links without verifying the destination host, redirect IP or accepted scheme, so an absolute link can move the browser outside its intended source. The browser detail steps catch broad exceptions and may append records with null fields. The CLI exits with status zero on an empty result, even after every source fails; a scheduler could misinterpret collection failure as an authoritative empty set. Only the Requests adapter has explicit HTTP status validation and timeout; network quotas and rate budgets are not coherent across adapters.

## 5. Date, amount, eligibility and evidence

Pydantic's dateutil parser uses fuzzy date matching and returns null on failure without retaining raw date text or source timezone. Amount extraction takes the first text regex match, not the verified stipend/tuition components. Country inference from article prose need not describe eligible nationalities. No stable award identity, cycle, status, tuition fee class, doctoral route, checked timestamp or field-level quote is stored.

## 6. Persistence, tests and operations

The exporter overwrites scholarships.json and scholarships.csv directly without atomic replacement or deduplication, allowing loss of previous observations. The ten-file tree does not contain a test suite or CI. README instructions are not evidence that sites currently respond or support scraping. No runtime/library install or live-source verification occurred.

## 7. Evidence and limitations

Pinned source: [orchestrator](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/scraper.py), [model](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/models.py), [DAAD](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/scrapers/daad.py), [Stipendium](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/scrapers/stipendium.py), [Scholars4Dev](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/scrapers/scholars4dev.py), [exporter](https://github.com/siyahalp-prog/scholarship-scraper/blob/37aac0e88e105364db3bcaa82dd72a4b58d20dcf/exporter.py). No site scraped or scholarship validity confirmed.

## 8. Transfer to PhD Atlas

Keep typed source adapters and isolated error reporting. Add official/aggregator source classes, allowlisted host + redirect validation, coverage metrics, immutable raw snapshots, identity/cycle-aware upserts, atomic outputs, and separate verified funding/eligibility claims with quoted evidence. A partial or failed collection must never invalidate prior verified records.
