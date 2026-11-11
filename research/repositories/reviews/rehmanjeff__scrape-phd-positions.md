# Rehmanjeff/scrape-phd-positions — source-pinned preliminary review

**Upstream revision:** `b086e5cf78ec75d8fdfee8795488fa319747568e`; **inspected:** 2026-11-12; **review:** PRELIMINARY_FOCUSED; **runtime validation:** NOT_PERFORMED; **source action:** READ_ONLY.

## Actual scraper pipeline

The tree has 30 entries, including Scrapy spider, database adapter, settings, cached HTML and JSON, tracked __pycache__/Python 3.9 bytecode and IDE files. There is no root README in the committed tree. PhdSpider.start_requests contains a hard-coded scholarshipdb.net IoT PhD query at page 3. parse extracts a '.position-details' block and follows h4 links plus next-page links, recursively returning dict fields: application link, title, university, country and summary. Selectors depend on old static page structures, with no evidence provenance, typed deadline or funded-status verification. A legacy scraped HTML dump is not a current vacancy.

## Critical static security/code quality issue

phdPositions/spiders/dbModule.py contains a plaintext PostgreSQL connection password and a fixed local service user; values are **not copied into this review**. It initializes the connection as a top-level side effect, prints DSN/server properties and uses connection in finally although initial connection assignment can fail, risking secondary UnboundLocalError. The spider imports dbModule as an unqualified local module and otherwise does not demonstrate a robust database write path. The spider also accesses detail.css('div::text')[1] without a length check, a possible IndexError. It uses one globally selected heading/apply link for each position-details loop, not per-card, risking wrong associations.

## Transfer verdict

PRELIMINARY_FOCUSED for anti-pattern study only. Do not run or deploy the source; ensure any still-valid committed credential is revoked by its owner, move secrets to environment/secret store, and use source-owned IDs, official-host verification, safe pagination limits and parser fixtures. No secrets, raw cached vacancy records or private data have been imported.

Pinned [spider](https://github.com/Rehmanjeff/scrape-phd-positions/blob/b086e5cf78ec75d8fdfee8795488fa319747568e/phdPositions/spiders/phdPosition_spider.py), [database adapter (contains a plaintext credential; don't open casually)](https://github.com/Rehmanjeff/scrape-phd-positions/blob/b086e5cf78ec75d8fdfee8795488fa319747568e/phdPositions/spiders/dbModule.py).
