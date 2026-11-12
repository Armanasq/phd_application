# mdsamhussain1996/vidyasetu-scholarship-portal — deep static pipeline audit

**Reviewed:** 2026-11-12. **Pinned upstream:** [fc11048d6488c86d9da373795d857f2019f88204](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/commit/fc11048d6488c86d9da373795d857f2019f88204).  
**State:** DEEP_REVIEW_DOCUMENTED — substantive source/schema/test/workflow/config inspection; no live grants, API calls or tests executed.  
**Verdict:** adapt the temporal schema and review queue; reject its automatic verification semantics.

## 1. Scope and source authority

An India-focused portal aggregating government, university, laboratory, corporate and international scholarship/fellowship leads, from high school to postdoctoral level. Its README claims a verified catalogue, but catalogue counts and actual current program eligibility were not independently confirmed. Its inclusion of a named funder is not evidence of an open international PhD position.

## 2. Dataflow, schema and lifecycle

The daily GitHub Actions job invokes a Python discovery engine, verifies JSON dataset shape, commits updates to main and opens review PRs for newly found opportunities. The engine reads watched official pages, hashes content, optionally asks Claude for structured extraction, deduplicates by provider slug/fuzzy title, stages new records into pending.json, updates existing records in opportunities.json, rolls annual cycles, archives expired one-off opportunities, checks links periodically and publishes metadata. The JSON schema preserves dateConfidence confirmed/expected/unknown, firstSeen, lastVerified, verifiedBy, source URL and evidence. This is a useful domain separation.

## 3. Source-identity validation flaw

The is_official_link function lowercases the entire URL string and checks whether it **contains** a trusted-domain substring. It therefore does not prove that the parsed hostname belongs to a trusted provider. Its fallback compares provider hostname and destination hostname via substring in either direction; lookalike domains or nested names can pass. It also checks blacklisted aggregator names via substring, which can reject otherwise benign pages that quote a disallowed domain in the path/query. Parsed IDNA hostname boundaries, public-suffix rules, redirect validation and actual evidence of provider control are missing.

## 4. Hash-before-extraction loss

run_discovery sets hashes[url] = new_hash immediately on detecting a changed page, before checking whether ANTHROPIC_API_KEY exists or whether the per-run 10-call budget is exhausted, and before extraction success. It saves source_hashes.json at the end of scanning. A fetched changed page with no key, exhausted quota, invalid JSON or model failure is marked seen and will not be retried on the next unchanged crawl. Thus the source's change detector can permanently omit a valid opportunity without an explicit retryable failure state.

## 5. Model evidence and unsafe publication updates

New candidates get confidence 0.9 solely if a nonempty evidence field exists, without checking whether that quote occurs in the fetched document, is in the correct recruiting cycle or proves the specific amount/eligibility. For a fuzzy-duplicate existing item, any candidate with an evidence string replaces evidence/source URL and sets lastVerified to today and confidence 0.9, even if earlier code classified the candidate's official link as suspicious or status needs-review. Its deadline becomes dateConfidence confirmed if a date exists, regardless of reviewer approval. New items are held in pending.json, but existing published items bypass the human-review PR gate. This is not independent verification.

## 6. Additional data-integrity limitations

The daily workflow commits opportunities, metadata, hashes and archive to main separately from the pending-items PR; concurrent edits can conflict. save_json writes directly rather than atomic rename. The source's fallback YAML parser only covers selected fields and ignores configured query frequency; a defined query list is not by itself an implemented web-search collection API. In the inspected run_discovery source, watched pages are processed but parsed search queries are not executed through a general search provider. The server-local date can misinterpret a source's deadline timezone. Non-negative amountValINR is required even when a provider hasn't stated an amount, increasing placeholder pressure.

## 7. Test evidence and runtime boundaries

Tests cover recurring-cycle rollover, leap-year date handling, fuzzy dedup, basic scam keywords, some trusted and blacklisted links, and JSON schema bounds. They **do not** establish malicious lookalike hostname rejection, hash retry on failed extraction, evidence-to-page quote validation, malicious model-generated duplicate update handling, or multi-writer consistency. No tests, job, Claude call, actual HTTP-200 check or program outcome was executed during this investigation. README claims about currently available funding are not independently verified.

Pinned evidence: [discovery source](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/scripts/discover.py), [schema](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/data/schema.json), [validator](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/scripts/validate.py), [tests](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/tests/test_portal.py), [Actions](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/.github/workflows/daily-update.yml), [source registry](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/fc11048d6488c86d9da373795d857f2019f88204/config/sources.yaml).

## 8. Transfer to PhD Atlas

Preserve the difference between current confirmed dates, expected future rounds and unknown deadlines. Store each source observation and extracted claim with page hash, quote span, official hostname, cycle, success state and independent reviewer decision. Only advance a watched page's processed hash after successful extraction/validation checkpoint; retain retryable failures. Require provider-domain and redirect checks and block any automatic published-date/verification updates when evidence is missing, contradictory or suspicious. Give different identities to recurring grants and one-off jobs, and do not treat machine-generated confidence as admission or funding probability.
