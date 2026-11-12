# AlanWang610/academic-cv-scraper — deep static academic-CV pipeline audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/AlanWang610/academic-cv-scraper | **Pinned revision:** [`4862fc7cf220efa7bb802f8f452e05c66d3dd7de`](https://github.com/AlanWang610/academic-cv-scraper/commit/4862fc7cf220efa7bb802f8f452e05c66d3dd7de) | **State:** DEEP_REVIEW_DOCUMENTED (source static only) | **Decision:** reject automated collection/reuse of third-party CVs by default; adapt only consent-based extraction architecture.

## 1. Purpose and scope

A 2025 Python research data pipeline for locating public academic CVs of finance/economics researchers, extracting undergraduate, master's and doctoral institutions and employment history, and resolving article authors/first-name initials through DOI/search. The 12-file MIT repository includes `scrape.py`, `parse.py`, `build_author_list.py`, `find_first_names_and_doi.py`, small CSV/JSONL examples, and dependency definitions. It is *academic biography extraction*, not a funded vacancy tracker, doctoral admissions eligibility engine or supervisor availability verifier.

The repository includes output files of identifiable scholars; this audit inspected implementation logic and file inventory, **not** individual scholar records.

## 2. Source acquisition flow

`scrape.py` takes a CSV of academic names and uses a `browser_use.Agent` with a `ChatOpenAI` model to search for a PDF/DOCX/HTML CV. Its natural-language prompt prioritizes finance/economics relevance and university-hosted pages. It parses the agent's final result through an implementation-specific `str(result.history[-1])` textual delimiter, finds an HTTPS URL, requests the URL with Requests, checks response Content-Type and saves raw content as `downloaded_CVs/{name}.{ext}`. It runs one agent per input row, sleeping two seconds between rows.

This chain creates multiple unverified identity transitions: scholar name → search result → CV candidate → inferred discipline → file download. Checking a URL suffix and page title is not proof that the CV belongs to the intended person.

## 3. Structured extraction and prompt-data boundary

`parse.py` reads PDF text with `pdfplumber`, sends extracted CV text to OpenAI Chat Completions and requests a JSON education/affiliation structure. It tries to recover malformed JSON by prepending an opening brace rather than using a strict schema or verified parse repair. Source spans, page numbers, original document hashes, title/degree confidence, identity match evidence and explicit temporal validity are not preserved per field.

The code reads a spaCy `en_core_web_md` pipeline on import but the shown extraction path does not use its entity output; a missing model can abort execution even when the OpenAI extractor is sufficient. `page.extract_text()` may return None for image-only pages; concatenating None would fail. No systematic evaluation against human-labeled CVs was found.

Untrusted CV content is model input. The system lacks an explicit prompt-injection boundary and a prohibition on inferring missing years/institutions beyond source evidence. Its “use null if uncertain” prompt is positive but is not an independent validator.

## 4. Retrieval correctness and operational risks

- `scrape.py` relies on a fragile text serialization of the browser-agent execution history and magic delimiter strings; a new agent version or response format can produce silent missing URLs.
- Raw downloads lack explicit timeouts, content-size limits, safe final redirect/DNS/IP validation, canonical institution identity checks or per-domain terms compliance.
- The filename uses an untrusted name value directly, without a documented safe path-component sanitizer or collisions/version management.
- Requests to third-party URLs and CVs can reveal or ingest personal academic histories not licensed for redistribution.
- The pipeline identifies employment and doctoral completion dates from historical CVs, which may be stale; no source retrieval date/version is attached to each extracted claim.

These are source-level risks, not a demonstrated exploit.

## 5. DOI/author-resolution subpipeline

`build_author_list.py` collects distinct researcher names from article JSONL author lists and references. `find_first_names_and_doi.py` uses DOI publication URLs or a research citation query to resolve first-name initials, with optional browser-agent search and per-output JSONL checkpoints. The source attempts to minimize repeated DOI calls and preserve progress.

However, assigning a full name from initials without an authoritative paper/ORCID identity can conflate homonyms or authors sharing surname and first initial. Name inference should be `AMBIGUOUS` until confirmed with publication metadata, institution/ORCID and publication-year context.

## 6. Privacy, ethics and scientific validity

A CV's public availability is not blanket consent for copying a person's complete document, uploading it to an external LLM or publishing compiled academic biographies. The pipeline lacks an explicit opt-out, retention/deletion contract, lawful purpose check or dataset provenance license inventory. For an applicant's own uploaded CV, consent and local handling can be appropriate; third-party collection requires stronger constraints. No personal CVs from this repository were copied into the PhD application project.

Education institutions and appointments could inform supervisor expertise research, but they do not establish available doctoral slots, hiring budgets, grant funding, or a prospective PI's willingness to supervise. Avoid using extracted CVs to estimate admission probability.

## 7. Transfer and redesign

Reusable only with authorization: document fetch interface, separate parser/structured extraction, DOI-backed author metadata and checkpointed batch processing. Rebuild as:
1. Consent-gated private document ingestion or institution-licensed faculty profile retrieval.
2. URL/host validation, TLS and size limits, robots/terms compliance and rate controls.
3. Strict typed schema with page-span citations and `UNKNOWN` for missing data.
4. Privacy-preserving storage, encryption, retention/deletion and source versioning.
5. Independent scholar identity resolution (ORCID/DOI/institution) and explicit ambiguity.
6. Empirical parser fixtures against permitted CVs, homonyms and multi-column layouts.

## 8. Pinned evidence and limits

- [README](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/README.md)
- [Browser-agent search and download](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/scrape.py)
- [PDF/LLM extraction](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/parse.py)
- [Publication author list builder](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/build_author_list.py)
- [DOI author resolver](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/find_first_names_and_doi.py)
- [Dependency manifest](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/requirements.txt)

**DEEP_REVIEW_DOCUMENTED — static relevant implementation.** No third-party CV download, browser-agent execution, paper search, model inference, private data access, installation or benchmark performed; external academic facts remain **NOT_VERIFIED**.
