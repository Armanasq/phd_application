# Focused full-tree static review — RaveeshM/Scholarship-Web-Scraper

**Upstream revision:** `5ee5bf7be12e2c64f964840de0c84d8d708579a7`; **checked:** 2026-11-12. **Review state:** PRELIMINARY_FOCUSED; the complete three-file tree was inspected, including the example scholarship CSV, README and scraper. **Runtime:** NOT_TESTED. **License:** no license file identified; no code-reuse grant verified.

## Purpose, actual implementation and source evidence

This historical single-source US scholarship data scraper exports a general-purpose scholarship catalogue, not confirmed fully funded doctoral vacancies. The [README](https://github.com/RaveeshM/Scholarship-Web-Scraper/blob/5ee5bf7be12e2c64f964840de0c84d8d708579a7/README.md) describes ~23,041 scraped general scholarships; this is an author-reported number, not a reproducible current coverage count. The [scraper](https://github.com/RaveeshM/Scholarship-Web-Scraper/blob/5ee5bf7be12e2c64f964840de0c84d8d708579a7/scraper.py) iterates exactly 769 pages of an HTTP (unencrypted) `collegescholarships.org/financial-aid` endpoint and extracts names, due-date fragments, amounts, descriptions, geography, study-level years and links from raw HTML using fixed substring delimiters. The resulting CSV contains no source-snapshot hash, observation timestamp, programme official ID, verified funding contract, eligibility adjudication or year for many day-month deadlines.

The [example CSV](https://github.com/RaveeshM/Scholarship-Web-Scraper/blob/5ee5bf7be12e2c64f964840de0c84d8d708579a7/example-scholarships.csv) includes undergraduate awards, local eligibility constraints, general postgraduate awards and some doctoral-study entries. Their presence does not mean a generic US scholarship is available to a given international PhD applicant, that a programme offers guaranteed full funding or that a historical row remains open.

## Algorithmic defects and evidence limits

1. `snip(src, sub1, sub2)` increments a missing delimiter's `find() == -1` result and proceeds to slice through another missing delimiter. When page HTML changes or a field is missing, it can return garbage or silently misalign fields. The README itself notes missing amounts may become `v` and named HTML entities remain unescaped.
2. The network URL uses **HTTP**, not HTTPS; the scraper has no request timeout, retries, rate-limit handling, robots/permission checks, error ledger, stable item ID or per-page schema validation. A network failure aborts a whole run.
3. It overwrites `scholarships.csv` on every execution without durable provenance, change history or atomic replacement. No source-level dedup or validation of amount, date-year, location, citizenship/residency or doctorate-stage admissibility.
4. `for page_num in range(1, 770)` assumes a fixed 769-page catalogue and hard-coded HTML classes/tags. There is no cursor termination or completeness record; source drift can lead to missing pages, malformed data and false evidence of source coverage.
5. Dataset rows mix awards, student loans and study levels; no official awarding-institution links or current eligibility checks were independently followed. Date-only month/day values cannot establish a **2026** or **2027** application deadline.

## Interconnections and verdict

Compared with [Mhrnqaruni funded-PhD monitor](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor), it lacks mandatory official funding and eligibility gates, audit history and independent review. Compared with [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator), it has no structured schema or hybrid retrieval. **REJECT AS LIVE EVIDENCE OR DIRECT IMPORT.** Keep only the conceptual idea of source-specific extraction and illustrative source-failure fixtures. Before reconsidering: validate HTTPS and permitted source access, parse real structured source data, preserve year+timezone, identify doctoral/fee-coverage eligibility, recheck each issuer's current official notice, and add bounded test fixtures. The 2021 scrape was not rerun, and no current scholarship amount/deadline is verified.
