# yongruiyu/CS_APP_Agent — source-level repository investigation

**Date:** 2026-11-11  
**Pinned upstream commit:** [`5b644384787993d27443434f0319819654bb491c`](https://github.com/yongruiyu/CS_APP_Agent/commit/5b644384787993d27443434f0319819654bb491c)  
**Review state:** PRELIMINARY_FOCUSED. Substantive static inspection, not full-file exhaustive review or independent runtime validation.  
**Applicability:** evidence_scoped_program_research_agent  
**Primary risk:** per_section_sources_not_quote_verified_and_unbounded_legacy_cache  
**Reuse decision:** original methods only; no unreviewed code adoption

## 1. Purpose and scope

A command-line one-program-per-turn admissions research agent, deliberately favoring depth and source attribution over processing many institutions at once. It illustrates a practical workflow to recover incomplete program facts across official subpages while preserving which page provided which section. This is relevant for distinct tuition, language score, deadline and funding requirements.

## 2. Architecture and actual components

An interactive REPL in `agent.py` defines tools for official program discovery, structured website collection and finding application examples. `tools/search.py` ranks candidate URLs by plausible school host and admissions path; `tools/collect.py` uses Tavily or direct HTML extraction and an LLM for typed program fields. `checker.py` audits missing critical sections. `tools/cache.py` retains results for seven days; `agent.py` saves interim Markdown and can issue one bounded completeness follow-up. The JSON models carry `field_sources` for source-per-section linking.

## 3. Task-to-data flow and dependencies

Execution interconnection: given `(school, program)` -> search official page -> collect source text -> extract date, English test/waiver, local and international tuition, RA/TA/fellowship funding, length, courses -> if critical fields are sparse, search a more targeted URL on the same hostname and merge only missing facts -> fetch examples -> run completeness checker -> store a per-program Markdown document. Cache keys include school and program to prevent mixing MS and PhD information from a shared university landing page.

## 4. Methods and source-level evidence

Useful conventions: one tool call per round trip so evidence is inspectable, one retry limit to bound cost, explicit Not available rather than invented values, and source-per-section citations rather than a bibliography at the top. Tests assert different program identities have different cache keys and merge source links properly. The approach is stronger than a general chatbot response but still lacks factual span matching.

## 5. Implementation and operational reconstruction

Confirmed limits: `tools/search.py` treats educational TLD or a school-name substring in hostname as 'official' rather than validating the exact institution's authorized registrable domains. `tools/collect.py` `_merge` accepts LLM-extracted values and fills missing fields without source-quote checking; conflicts are first-source-wins and not escalated. `tools/cache.py` returns unwrapped legacy cache entries without TTL expiration, even though current entries expire after seven days. Per-section citation assignment can still point to a page that does not actually prove the displayed value.

## 6. Failure modes and validation gaps

Scientific application adaptation: retrieve exact program and cycle first; require an evidence span per field, not only a section URL; record alternate claims, contradictions, qualification/fee category and source publication time; detect institution-controlled host and redirects robustly; invalidate caches on source content hash/version, and require closer recheck near the deadline. Applications must not proceed if international tuition or funding are merely mentioned, rather than guaranteed by the relevant award.

## 7. Transfer to PhD Atlas and admissions workflow

Adopt cost-bounded focused retrieval, typed fields, source-per-section provenance, a completeness checker and incremental persisted research. Add local fact checking against original text, confidence derived from evidence quality not LLM self-report, and a verifier that can reject information copied from an unrelated MS track or past intake year.

## 8. Provenance and outstanding verification

Inspected agent orchestration, schema, web search/extraction, cache, checker and regression tests at pinned commit. No Tavily/LLM call, source recrawl, official-domain validation beyond code inspection, or upstream unit test execution performed.

## Pinned source files inspected

- [`agent.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/agent.py)
- [`tools/collect.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/tools/collect.py)
- [`tools/search.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/tools/search.py)
- [`tools/web.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/tools/web.py)
- [`tools/cache.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/tools/cache.py)
- [`models.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/models.py)
- [`checker.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/checker.py)
- [`tests/test_regressions.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/5b644384787993d27443434f0319819654bb491c/tests/test_regressions.py)

## Validation protocol not yet completed

1. Inspect remaining implementation paths, licenses, issues, history and source links, then record coverage independently.
2. Run tests with pinned toolchain in a sandbox; capture commands, fixtures, exit codes and outputs.
3. Verify each admissions, fee, funding and applicant eligibility claim against authoritative live sources for the correct cycle.
4. Record conflicting claims, reviewer authorization and revisions; never infer an application was sent or an offer obtained.
