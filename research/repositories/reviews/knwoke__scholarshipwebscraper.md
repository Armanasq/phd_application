# knwoke/ScholarshipWebScraper — preliminary static scraper review

**Reviewed:** 2026-11-12. **Pinned upstream:** [b675082fc23c84cba2664741fd61012d83b0330c](https://github.com/knwoke/ScholarshipWebScraper/commit/b675082fc23c84cba2664741fd61012d83b0330c).  
**State:** PRELIMINARY_FOCUSED; full two-file source tree inspected; scraper not executed.  
**Disposition:** historical demonstration of a single-source Scrapy spider, not a trustworthy scholarship feed.

The spider starts at a Scholarships.com academic-major directory, follows `ul#ullist a` links, and yields a record with **only amount and URL** from `tr` cells. It has no title, provider, deadline, academic level, funding components, nationality requirements, proof, fetch timestamp, or cycle. A broad `except:` catches missing selector values and emits a **fake placeholder record** (`missingscholarship`, `missingurl!`) as though it were an extracted scholarship, contaminating downstream datasets.

The spider concatenates its hardcoded base domain to each href before `response.follow`; absolute/non-standard links may produce malformed URLs. There is no crawler project configuration, test fixtures, scheduling, output schema, deduplication, rate policy or robust HTTP/error classification in the tracked repository.

**Atlas transfer:** restrict to an educational Scrapy structure example. Production needs canonical `urljoin`, typed parser output, explicit failure state rather than fabricated records, source-specific fixtures, bounded crawling, and current official evidence for each scholarship field.

**Evidence:** [spider](https://github.com/knwoke/ScholarshipWebScraper/blob/b675082fc23c84cba2664741fd61012d83b0330c/scholarships11.py).
