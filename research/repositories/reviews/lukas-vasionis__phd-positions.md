# Lukas-Vasionis/PhD_Positions — source-pinned deep static review

**Pinned upstream:** [4a8e8616f72584901a3be20c62b71adced4da39a](https://github.com/Lukas-Vasionis/PhD_Positions/commit/4a8e8616f72584901a3be20c62b71adced4da39a), master, checked 2026-11-12. **Runtime:** NOT_TESTED. **License:** Apache-2.0. Full evidence: [session source audit](../../sessions/20261112-lukas-taleh-noor-c8d1/reviews/lukas-vasionis-phd-positions.md).

## 1. Research objective and scope

Evaluate whether a Python scraper aggregating first-party Norway, Swiss and experimental German/Luxembourg university job pages can reliably inform international doctoral vacancy discovery and preserve private applicant labels. Main value is first-party per-university adapter design, not independently verified funding or acceptance.

## 2. Source snapshot and implementation

41 Git-tree entries. Inspected scripts, pyproject, config, runner, shared scraping utilities, six representative university scrapers, processing processor and utility module, and both Streamlit application modules. A bundled SQLite DB exists but was not inspected; remaining university adapters were inventoried. No tracked test suite or scheduled workflow was found in the inspected tree. Main stages: [runner](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/runner.py) -> raw SQLite -> [processor](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/processor.py) -> processed tables/labels -> Streamlit.

## 3. Parsing and state model

Source-specific HTTP/Selenium adapters extract title, URL, posted/scraped date, city, contract and sometimes deadline. Processed rows and labels are intended to preserve the user's Interesting/Applied/Rejected markings across refreshes. UI is per university with optional Excel export, but lacks evidence-linked application receipts, source hashes, explicit cycle and funding verification.

## 4. Confirmed data-integrity defects

[P0] `ScrData.update_scraper_tbl` looks for `processed_raw_ethz` but `save_to_db` writes `processed_ethz`; the label restoration query repeats this mismatch. New runs can fail to recover prior vacancies and user annotations. [P0] Empty crawls are transformed into fictitious blank rows and the raw table is replaced, so transient source errors can erase usable records. [P1] Streamlit export invokes `fetch_data(conn, table, columns)` despite a two-argument signature. [P1] Lausanne `filter_CH_unil_PhD` computes filtered rows but never assigns them back. Source: [processing utils](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/utils.py), [scraping utils](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/scraping_utils.py), [viewer](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/app/viewer.py).

## 5. Operational and lifecycle risks

The runner omits UNILU/TUM despite processor references to their raw tables, and there is no DKFZ scraper wired for the processor's DKFZ dependency; fresh bootstrap can fail. Selenium HTML-return path lacks driver cleanup and uses disabled Chrome sandbox; one TUM retry loop assigns -1 on failure; Scandinavian-date conversion returns inside its first column loop; UZH pagination is capped by one page-size setting. Source: [runner](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/runner.py), [TUM](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/tum.py), [shared scraping](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/scraping_utils.py).

## 6. Interconnections and independent evidence

Compared with [NimaaaAI/Position-Aggregator](nimaaai__position-aggregator.md), university-adapter collection offers more direct source ownership but weaker canonical identity, source snapshot continuity, closure detection and multilingual hybrid search. Both must distinguish complete snapshots from transient fetch failures. Unlike applicant-facing browser trackers, the university data source should be read-only and independent of applicant annotation state.

## 7. Decision and adoption priority

**ADAPT_AFTER_DATA_INTEGRITY_FIXES; priority P0.** Transfer institution-specific adapters and local-first workflow separation, not raw-table replacement, placeholder records or unverified open/funding claims. Explicit source completeness, stable IDs, cycle, provenance and field-level evidence are prerequisites for applicant recommendations.

## 8. Evidence gaps and acceptance tests

No actual scraper, UI, SQLite migration, package install, job source, deadline or university policy execution/verification performed. Required tests: two sequential overlapping crawls retaining labels/history, empty/failed fetch preserving prior evidence, fresh bootstrap with missing adapters, Unicode date parsing, Lausanne filtering, valid export, browser driver shutdown, deadline extension and duplicate URLs. Results of these tests remain UNKNOWN.
