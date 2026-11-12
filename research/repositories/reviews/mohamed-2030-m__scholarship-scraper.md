# Mohamed-2030-M/scholarship-scraper — deep evidence-first scholarship extraction audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/Mohamed-2030-M/scholarship-scraper | **Pinned commit:** [`124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b`](https://github.com/Mohamed-2030-M/scholarship-scraper/commit/124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b) | **State:** DEEP_REVIEW_DOCUMENTED (static) | **Verdict:** adapt evidence-anchored extraction and incremental persistence; do not interpret literal substring checks as independent official validation.

## 1. Actual project and source scope

A Python 3.10+ source-specific pipeline for Turkish scholarship announcement pages on Guncel Eğitim. It fetches WordPress REST API posts, shortens long pages, asks a local Ollama or remote OpenAI-compatible LLM to extract the final application deadline and whether international students may apply, checks that the quoted supporting text exists in the original page, caches answers and maintains a CSV. Its README correctly warns that an OK extraction is not a guarantee an offer is currently open. The 18-file tree contains `main.py`, selectors/heading probes, a legacy Playwright scraper, a small test and documentation images. Latest source update observed: 2026-10-12.

The pipeline is primarily about scholarship **postings and eligibility statements**, not live doctoral labor contracts or executed admissions submissions.

## 2. Data flow and source contract

`fetch_page()` queries the publisher's `/wp-json/wp/v2/posts` endpoint using WordPress category/pagination, modified timestamps and fields for ID/link/title/content. `select_relevant()` prioritizes deadline and nationality lines within a bounded LLM context. Provider adapters route through Ollama/Gemini/Groq with fallback, retries and permanent-provider failure semantics. A structured JSON answer contains `deadline`, `deadline_evidence`, `foreigners_allowed`, and nationality `evidence`.

`evaluate()` normalizes Turkish text to compare the model's quotes against the full page. It rejects missing or nonmatching quotes, marks unknown values incomplete, and distinguishes `OK`, `Incomplete`, `Check`, and `Failed`. This is a positive source-grounding gate that many broader scholarship scrapers lack.

## 3. Evidence strength: literal text versus semantic verification

An `OK` status establishes **syntactic support** for extraction, not that the statement is true, pertains to the intended award, applies to the current intake, or is issued by the award owner. `squash()` discards punctuation and whitespace; a substring can still match within irrelevant policy text or a quoted older announcement. `NATIONALITY_WORDS` only requires a lexical reference to nationality; it cannot reliably distinguish who is eligible from an exception, negation or unrelated contextual sentence.

The `deadline` and `deadline_evidence` substrings are checked separately; the code does not require a single exact original source span or verify whether the extracted date was an **opening** rather than a **closing** date. A third-party educational information blog is not the official issuer of a named funding award. Independent current institution/source confirmation is mandatory before `OPEN_VERIFIED` or `INTERNATIONAL_ELIGIBILITY_VERIFIED`.

## 4. Date, locale and deadline errors

`parse_deadline()` recognizes Turkish month-name dates and `DD.MM.YYYY` or `DD/MM/YYYY` patterns, then selects the date appearing last in the extracted string. Multiple dates can encode interviews, document submissions and award start dates, so positional “last date” is not a semantic closing-date guarantee. Timezone and exact cutoff times are not tracked, and records with ambiguous/missing dates remain null in parsed date.

`refresh_dates()` computes `Days Left` and an `Expired` flag from local `date.today()`; that reflects the **stored** parsed date, not a live sponsor portal check. The publisher might replace the call, reopen it, or advertise a different future cycle. Do not conflate the CSV's `Expired` field with official provider closure.

## 5. Incremental scan, idempotency and failure handling

The source ID is a stable WordPress post ID. `needs_analysis()` checks modified timestamps and previous failures, and `upsert()` preserves added manual CSV columns while updating extracted fields. Output is written to a temporary file and atomically replaced, with a fallback filename if Excel locks the current master. Those are useful idempotency and durability patterns.

An incremental run stops after one page containing no new or changed posts, assuming modified-descending WordPress order and complete pagination. A changed ordering, incorrectly cached modified date, or stale provider response could silently leave later-page changes unseen; the run needs a formal source-snapshot completeness marker and periodic full comparison.

The model cache key includes post ID, WordPress modified time, and first model name, but **not prompt version or extraction schema version**. The README instructs `--no-cache` after editing a prompt; this is operationally fragile. Include prompt/schema hashes and source content hash in cache identities.

## 6. Privacy, licensing and operational constraints

The code uses explicit HTTP request timeouts, bounded retries and source-specific rather than unrestricted URL access. That is better than arbitrary-browser job scrapers. Still verify origin terms, provider quotas and full URL redirects before putting it on a public scheduling service. Remote LLM providers receive publisher-sourced post text; applicant CVs do not appear in the inspected flow.

No automated multi-source award-owner verification, signed official funding evidence, cross-source dedup, applicant nationality verification, source timestamp normalization, or anti-hallucination semantic benchmark is demonstrated. One test file covers heading filtering only; it is not a comprehensive source correctness suite.

## 7. Transferable architecture and required checks

Transfer: source registry, exact quote evidence, Turkish normalization, typed missing values, provider failover, freshness-aware reruns, stable post IDs, atomic output, manual annotation preservation. Extend with:
1. Named source type and publisher-versus-award-owner authority.
2. Field-specific exact passage offsets/hashes and recruitment cycle IDs.
3. Semantic entailment/negation validation for nationality and deadline meaning.
4. Dates with locale, timezone and cutoff-precision flags.
5. Source completeness/delta strategy and expiring prior verification.
6. Prompt/schema version keys, test fixtures, human-reviewed discrepancy cases, formal funding coverage.
7. Explicit distinction between extractable **claim** and current **institution-verified program**.

## 8. Evidence and execution boundary

- [README](https://github.com/Mohamed-2030-M/scholarship-scraper/blob/124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b/README.md)
- [WordPress acquisition, extraction, evidence, cache and persistence](https://github.com/Mohamed-2030-M/scholarship-scraper/blob/124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b/main.py)
- [Heading test](https://github.com/Mohamed-2030-M/scholarship-scraper/blob/124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b/test_heading_filter.py)
- [Legacy browser adapter](https://github.com/Mohamed-2030-M/scholarship-scraper/blob/124ef1cbb7fb9fad6e3723b41dbaeea15b2f477b/legacy/playwright_scraper.py)

**DEEP_REVIEW_DOCUMENTED — static complete main pipeline.** No provider API calls, site-restrictions tests, actual Turkish scholarship eligibility rechecks, source-owner correspondence, LLM runtime, or empirical extraction benchmark were executed. Code-level quote validation is **not independent factual verification**.
