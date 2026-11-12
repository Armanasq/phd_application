# DanialRamezani/PhD-Hunt — deep static audit of multi-source vacancy discovery

**Reviewed:** 2026-11-12  
**Repository:** https://github.com/DanialRamezani/PhD-Hunt  
**GitHub repository ID:** 1055611637  
**Pinned revision:** [b58b728dd36b4281a6a7564d6aa211264cbd1c9b](https://github.com/DanialRamezani/PhD-Hunt/commit/b58b728dd36b4281a6a7564d6aa211264cbd1c9b)  
**Review state:** DEEP_REVIEW_DOCUMENTED — complete four-file source inventory, all `Hunt.py` methods, dependency manifest, README and notebook code cells inspected statically; model calls and live Google searches NOT_TESTED.  
**Verdict:** ADAPT retrieval/query-expansion ideas; do not use scored matches as verified funded PhD vacancies.

## 1. Intended use and evidence limits

PhD-Hunt is a short Python API plus Colab notebook which builds a Google Custom Search query with Gemini, fetches search-engine results and offers embedding or second-stage LLM relevance checks. It is a discovery assistant for prospective positions in any discipline/location represented by the input prompt. It has no authoritative employer ingestion, canonical application database, official deadline verifier, formal funding classifier, or applicant-specific eligibility model. No resulting search hit is a documented live vacancy solely by appearing in search results.

## 2. Full architecture and dependencies

The pinned tree contains `Hunt.py` (7,378 bytes), `README.md`, `requirements.txt` and `Search Example.ipynb`. The public `Searcher` interface accepts a Gemini API key, Google Programmable Search API key and Search Engine ID, as well as model and embedding-model parameters. `LLM_query` sends the user prompt and a default 14-day recency instruction to `GoogleGenerativeAI`. `search_google` calls Google Custom Search JSON API, incrementing `start` by ten. `search_no_filter` returns raw hits, `filtered_search` uses one model yes/no response per hit, and `analyze_relevance` computes cosine similarity using locally loaded HuggingFace embeddings. The notebook demonstrates the same calls with placeholder credentials.

Source: [Hunt.py](https://github.com/DanialRamezani/PhD-Hunt/blob/b58b728dd36b4281a6a7564d6aa211264cbd1c9b/Hunt.py), [requirements](https://github.com/DanialRamezani/PhD-Hunt/blob/b58b728dd36b4281a6a7564d6aa211264cbd1c9b/requirements.txt), [notebook](https://github.com/DanialRamezani/PhD-Hunt/blob/b58b728dd36b4281a6a7564d6aa211264cbd1c9b/Search%20Example.ipynb), [README](https://github.com/DanialRamezani/PhD-Hunt/blob/b58b728dd36b4281a6a7564d6aa211264cbd1c9b/README.md).

## 3. Execution sequence and interconnections

The dataflow is user intent -> LLM-generated Google search string -> Custom Search API hits (title, snippet, URL) -> either printed dense-vector ranking or LLM yes/no classification -> minimal formatted title/link/snippet records. It does not visit retrieved job pages and check their body, dates or job identifier. Embedding similarity only assesses semantic proximity of the query to snippet/title; it cannot assess funded status, current employment, PhD level, university sponsorship, overseas fee coverage, or citizenship restrictions.

The notebook contains 14 Markdown/code cells and demonstrates imports, explicit API-key placeholders, an operations-research/industrial-engineering example, Google search, vector similarity and model filtering. Two cells contain stored outputs. These are demonstration artifacts, not independently re-fetched postings or evaluation results.

## 4. Source-verified correctness and reliability gaps

1. **Recency is an LLM instruction, not an enforced filter.** `LLM_query` asks for results no older than `period=14` days using its stored UTC date, but `search_google` does not pass a Google date restriction or publication-time predicate; neither search result metadata nor fetched employer publication dates are verified. Consequently, apparent recency is unproven.
2. **Requested result count is not enforced.** `search_google` iterates `range(1, max_results+1, 10)` without supplying `num` or trimming the final collection. A `max_results=1` request may retrieve up to the API default page length, and `max_results=11` may return up to 20. A caller's item budget is therefore advisory rather than exact.
3. **HTTP control is incomplete.** `requests.get` has no request timeout, retry/backoff, persistent session or explicit 429 quota handling. `raise_for_status` aborts an entire run rather than creating an auditable source-health status.
4. **LLM filtering is not factual verification.** `is_relevant_result` passes the untrusted search title, URL and snippet into the model, accepting exactly YES as a match. It neither reads the official page nor checks what YES entails. Model self-assessment, snippets and search ranking are weak evidence.
5. **Silent result loss.** `filter_results` catches all exceptions per result and `continue`s without logging a failure record; operational failures appear as missing opportunities. This is especially problematic for recall-sensitive vacancy research.
6. **Embedding score is not machine-readable.** `analyze_relevance` prints ranked hits but does not return the scored records (the return statement is commented out). This limits downstream reproducibility, thresholding, calibration and quantitative benchmarking.
7. **No source identity or state.** The formatted output has only title/link/snippet. It does not persist canonical posting ID, first/last seen, document hash, official versus aggregator status, professor or employer, funding terms, eligibility evidence, deadline time zone, or closure recheck.
8. **Dependency contract is unstable.** The manifest lists six unpinned packages; `Hunt.py` also imports legacy LangChain namespaces, including `LLMChain`, `RetrievalQA`, older document loaders and embeddings not used by the active functions. Their compatibility with a fresh installation is not established. It also lacks an explicit direct `langchain` dependency despite importing that namespace. This is a reproducibility risk, not a claim of a proven import failure.
9. **No test/measurement framework.** No automated tests, pinned snapshots, precision/recall study, fixed random seeds, source annotation set or integration CI was present in this four-file tree. The notebook's stored outputs cannot prove current Google/LLM behavior.

## 5. Security, cost and provenance

The pattern uses two external cloud APIs and downloads a local HuggingFace embedding model; API billing, availability and data retention depend on their current contracts. User prompts and search snippets are sent to the model provider, and Google receives searches. Secrets are entered in notebook variables, with no vault/env-file design; the checked-in notebook shows placeholders, not demonstrated exposed production keys. Untrusted search snippets are inserted into LLM prompts, so prompt-injection and adversarial-source resistance remain untested. GitHub metadata did not advertise a repository license at audit time; confirm reuse rights before porting code.

## 6. Reproducibility and testing boundary

Only static inspection occurred; no `pip install`, notebook execution, embedding download, Google Custom Search, Gemini call, source recrawl or external website probing. Do not infer working compatibility, runtime throughput, actual result quality, API cost, up-to-date job postings or funded international eligibility from the code. The default model named by the README is a historical configuration and must be verified against today's provider API before deploying.

## 7. Transfer to PhD Atlas and comparisons

This is the **recall-oriented retrieval layer**. It complements, but does not replace, the source-specific parsers and source-claim validation of `dxeledx/PhdInfoHub` and `yongruiyu/CS_APP_Agent`. Compared with `psyho/ai-job-scraper`, it searches beyond a configured list of sites but cannot perform durable multi-site change tracking. Compared with evidence-anchored source scrapers, it is far weaker on deadline and eligibility verification.

A defensible adaptation is: diverse query expansion -> bounded search with explicit date filtering -> normalize/canonicalize URLs -> fetch official employer programme/call sources -> extract quoted funding, eligibility, source authority, PhD level, deadline and cycle claims -> enforce evidence entailment and contradiction gates -> deduplicate by stable opening identity -> recheck closure and source revision -> only then rank by scientific fit. Preserve every rejected result and collection failure for recall analysis.

## 8. Final disposition

**DEEP_REVIEW_DOCUMENTED — ADAPT_CONCEPTS_ONLY.** Entire code inventory, source functions, dependencies and notebook cells inspected at the pinned revision. Not done: live vacancy verification, runtime tests, imported-package test, security exploitation, terms-of-use review for scraping, precision/recall benchmark or applicant-specific funding assessment. No positions advertised by the example were added to the official opportunity ledger.
