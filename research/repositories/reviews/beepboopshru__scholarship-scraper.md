# beepboopshru/scholarship-scraper — preliminary review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [978efe791425ff407bcc8597fd536e1448b93eb1](https://github.com/beepboopshru/scholarship-scraper/commit/978efe791425ff407bcc8597fd536e1448b93eb1)  
**Review state:** PRELIMINARY_FOCUSED. Focused source-file inspection.  
**Category:** vacancy and scholarship scrapers.  
**Verdict:** reject as a production implementation; limited educational reference.  
**Primary risk:** fragile source selectors and silent failures produce incomplete data without freshness or error state.

## Purpose and implementation

A small initial-commit project with separate scraper modules for DAAD, Chegg and Fastweb, a main orchestrator that combines results into JSON, and a separate document/CV formatter. The repository has nine tracked files, no README, no license, no tests and no CI workflow. Latest commit: 19 August 2026.

## Findings

- Scrapers use fixed CSS selectors and page structures; there is no evidence of saved HTML fixtures or selector regression tests.
- HTTP requests do not set an explicit timeout or retry/backoff policy in the inspected scraper modules.
- Exceptions are caught and converted to empty result lists, making a broken source indistinguishable from a genuinely empty source.
- The orchestrator writes to `output/scholarships.json`, but the repository does not contain an output directory and the script does not create it before opening the file.
- The separate formatter calls the legacy `openai.ChatCompletion.create` interface while `requirements.txt` allows OpenAI SDK versions 1.0.0 and later; that version range is not compatible with the legacy interface without migration.
- No evidence provenance, content hash, stable cross-source identity, cycle, funding decomposition or applicant eligibility model is present.

## PhD Atlas decision

Do not adopt the scraper implementation. It can be used as a minimal example of source-specific adapters, but any production collector needs explicit HTTP timeouts, bounded retries, robots/rate-limit handling, saved fixtures, parser-health signals, structured records, source timestamps, idempotent identity and an error state that cannot masquerade as zero results.

**Coverage boundary:** the README-less tree, main orchestrator, three scraper modules, formatter and requirements were inspected; no live requests or code execution were performed.
