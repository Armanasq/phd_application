# KnowMe777/scholarship-scraper — source-level preliminary review

**Reviewed:** 2026-11-12. **Pinned upstream:** [0c0514685b95b5ef09c69c48e4c95036d6e72a0d](https://github.com/KnowMe777/scholarship-scraper/commit/0c0514685b95b5ef09c69c48e4c95036d6e72a0d).  
**State:** PRELIMINARY_FOCUSED; all six Python/dependency files inspected, no runtime tests.  
**Disposition:** incomplete Phase 1 smoke-test, not a working live scholarship scraper.

## Observed architecture

The code models a scholarship dataclass, a PostgreSQL insert/lookup layer using psycopg2, a few normalization utilities, and Pandas Excel export. The CLI `main.py` is explicit about being a "Phase 1 Smoke Test": it inserts a **hardcoded fake example** with a link at `example.com`, fetches rows and exports them. No HTTP requests, source adapters, browser crawling or scholarship updates are called. The dependency list includes Requests, BeautifulSoup, Playwright and APScheduler but none are exercised by the shipped CLI. There is no schema migration SQL or database creation definition.

## Data correctness and failure modes

- `ON CONFLICT (link) DO UPDATE SET last_seen_at=NOW()` requires a preexisting database unique constraint on link; none is declared in the repo. Without it, the SQL fails.
- The insert catches database errors, rolls back, logs a generic message and returns without surfacing failure to the CLI, which may still print a successful-looking fetch/export.
- Existing records' title, dates, funding or eligibility are **never updated**, only `last_seen_at`.
- `normailze_degree` uses substring matching and checks bachelor/master before doctoral. Wording such as "Postgraduate and PhD" can incorrectly normalize to Master. Missing degree returns "Any"; not evidence of unrestricted eligibility.
- `normalize_funding` accepts any text containing "full" as "Fully Funded", including negative/conditional sentences; no tuition/maintenance component proof.
- `parse_deadline` silently returns null for unsupported date formats, omitting timezone, cycle, time and validation confidence.
- A CSV/Excel export rewrites the same date-named file with no atomic replacement or manual-note preservation.

## Research transfer and limitations

A typed record, a database uniqueness/upsert principle and separation between normalization/persistence/export are positive foundations. Replace the smoke-test with explicit source adapters, source snapshots, a schema migration, a complete field-update contract, uncertainty states, official evidence spans and tests. The only example link is demonstrably dummy: **no scholarship validity or current funding can be inferred**.

**Evidence:** [CLI](https://github.com/KnowMe777/scholarship-scraper/blob/0c0514685b95b5ef09c69c48e4c95036d6e72a0d/main.py), [DB](https://github.com/KnowMe777/scholarship-scraper/blob/0c0514685b95b5ef09c69c48e4c95036d6e72a0d/core/db.py), [normalizer](https://github.com/KnowMe777/scholarship-scraper/blob/0c0514685b95b5ef09c69c48e4c95036d6e72a0d/core/normalizer.py), [model](https://github.com/KnowMe777/scholarship-scraper/blob/0c0514685b95b5ef09c69c48e4c95036d6e72a0d/core/models.py).

**Validation boundary:** source analysis only, no PostgreSQL, API fetch, exports or tests executed.
