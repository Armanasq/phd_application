# nocilladoluis616-a11y/scholarships_scraper — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [e8e871b65aec605cb339fdeaeed10f7e3e209b69](https://github.com/nocilladoluis616-a11y/scholarships_scraper/commit/e8e871b65aec605cb339fdeaeed10f7e3e209b69).  
**State:** DEEP_REVIEW_DOCUMENTED — static six-file source tree; upstream execution NOT_RUN.  
**Verdict:** retain typed parsing and retry ideas, not as a verified current scholarship index.

## 1. Purpose

A small Crawl4AI browser-based scholarship extractor aimed at selected web scholarship pages. The README claims AI turns listings into Pydantic-validated records. The repository has one scraper script, one environment-debug script, two JSON resources and README/ignore files; no tests, CI, migration or official-source registry.

## 2. Architecture and execution

`scraper.py` constructs a `ScholarshipSchema` with `scholarship_name`, `organization`, `amount`, `deadline`, `eligibility`; wraps it in `ScholarshipsListSchema`; configures `LLMExtractionStrategy` using an external Groq model and JSON schema; creates a headless Crawl4AI browser; loops over a short manually selected URL list; retries failed runs up to three attempts with randomized delay; validates extraction results; then appends them to `scholarships.json`.

The function is called `run_ollama`, but its actual model configuration is `groq/openai/gpt-oss-120b`, not a local Ollama runtime. This is implementation/documentation ambiguity and potentially a paid external data-disclosure boundary.

## 3. Extraction correctness and provenance

Pydantic validates **types and required fields**, not whether the extracted text is factually supported by the source. Amount, deadline and eligibility remain strings, and the prompt supplies illustrative values. The validated output stores no `source_url`, `fetched_at`, official institution, page revision, field-level quote, source validity period, study level or citizenship class. Re-executing the same URL can append duplicates because `save_to_json` uses `existing.extend(new_data)` without stable identity/dedup.

The separate `scholarships_dataschema.json` defines richer nested financials, eligibility and pipeline metadata including `is_fully_funded` and confidence, but **the running extractor does not use that schema**. Presence of a JSON design sketch does not establish implemented verification or funding checks.

## 4. Data integrity and failure states

The scraper filters obvious empty error entries, validates through Pydantic and logs parsing errors, which is positive. However it does not distinguish complete source coverage from a partial model response or zero parsed results, lacks field-level verification and provenance, and does not record independent reviewer decisions. `save_to_json` rewrites the whole file non-atomically and has no schema validation of the existing file, revision protection or idempotent upsert.

The Pydantic exception handler catches `ValidationError` and `JSONDecodeError` but not I/O failure or all potential extraction-shape failures; a single malformed item can stop a given page and remove otherwise valid extracted entries from the output.

## 5. Browser/network safety and cost

The manually configured target URLs are sent to the browser directly, without an explicit allowlisted host, private-network resolution restriction, redirect guard, page/content-size bound, model-token budget or a source-level officialness classifier. The implementation uses `CacheMode.BYPASS`; repeated runs re-fetch and can repeat model charges. In a hosted adaptation, this is a potential SSRF and unbounded external-model consumption risk, although no exploit was executed.

## 6. Credentials and privacy

`api.py` prints whether the `GROQ_API_TOKEN` exists and logs the **first five characters** of the token. Even a prefix is credential material and must not appear in shared logs; remove all secret-derived output. The script does not otherwise show applicants' private materials in the inspected flow, but scraping user-supplied scholarship sources needs untrusted-web-content handling and terms-of-access review.

## 7. Validation and limitations

The complete `scraper.py`, `api.py`, project README and JSON schemas were inspected. No saved parser fixtures, unit tests, CI, externally reproduced browser result, source page validation, Groq bill or provider availability check was established. Source-level claims are not experimental performance or a security certification.

Pinned evidence: [scraper](https://github.com/nocilladoluis616-a11y/scholarships_scraper/blob/e8e871b65aec605cb339fdeaeed10f7e3e209b69/scraper.py), [credential debug script](https://github.com/nocilladoluis616-a11y/scholarships_scraper/blob/e8e871b65aec605cb339fdeaeed10f7e3e209b69/api.py), [unused richer schema](https://github.com/nocilladoluis616-a11y/scholarships_scraper/blob/e8e871b65aec605cb339fdeaeed10f7e3e209b69/scholarships_dataschema.json), [README](https://github.com/nocilladoluis616-a11y/scholarships_scraper/blob/e8e871b65aec605cb339fdeaeed10f7e3e209b69/README.md).

## 8. Transfer to PhD Atlas

Use a fixed source adapter registry, Pydantic schema for extraction, limited retries and explicit empty/error states. Add authoritative official-source checking; verify cycle, amount and nationality at the field level; preserve exact source quote/hash; deduplicate by source opportunity identity; atomic writes; model budget, origin allowlist and page-size limit; and do not expose token fragments in logs. Assign `EXTRACTED_UNVERIFIED` rather than `ELIGIBLE` for schema-valid model output.
