# do3-173/scholarship_scraper — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [93e406d24da01ace739ae80f1f819ab130a83962](https://github.com/do3-173/scholarship_scraper/commit/93e406d24da01ace739ae80f1f819ab130a83962).  
**Review state:** DEEP_REVIEW_DOCUMENTED, source inspection without executing upstream code.  
**Verdict:** architecture reference for multimodal evidence acquisition; reject as a current verified opportunity pipeline.

## 1. Purpose and supported documents

A scholarship ingestion tool for scholarship websites, linked PDFs and DOCX documents, configured with Bosnian/Croatian/Serbian OCR and OpenAI or Google Gemini via ScrapeGraphAI. The observed examples focus on Sarajevo, Bosnian regional/municipal and regional university awards, including school-level rather than PhD-only grants. It is a multi-format extraction demonstration, not an authoritative international PhD source registry.

## 2. Source architecture

`scholarship_scraper.py` (~1,166 lines) is the single orchestrator; `docx_processor.py` handles Word content and tables; `config.py` stores extraction prompts, languages, document limits and source defaults. The main reads `Organization: URL` entries, detects document type by suffix or HEAD response, fetches websites/documents, invokes SmartScraperGraph, follows selected linked documents, enriches source metadata and writes timestamp-named JSON and summary reports. The code records original source URL, source type, processing method, time and some auxiliary links. These are useful provenance foundations but not independent proof of each extracted eligibility/funding claim.

## 3. Sequential execution versus advertised concurrency

The README and module docstring say sources are processed simultaneously/async. Actual `scrape_all_sources` iterates `for i, source in enumerate(sources, 1)` and calls `scrape_source` synchronously before a delay. No task scheduler or `asyncio.gather` is used in that source-level orchestration. The advertised source-level parallelism is therefore not implemented in the inspected path. Third-party ScrapeGraphAI internals were not independently audited.

## 4. Fetch and resource bounds

`download_pdf` uses `requests.get(url, timeout=...)` and writes `response.content` to a temporary file. This loads the entire response into RAM before a size bound is checked; the configuration's `PDF_MAX_FILE_SIZE_MB=50` is not an enforced limit in the inspected download path. `is_pdf_url` performs HEAD with redirects and `find_pdf_links_on_page` extracts linked document URLs. Input URLs are supplied by users or link-regex matches, without a demonstrated host allowlist or DNS/private-IP/redirect containment. In a hosted execution environment this creates a potentially dangerous SSRF and resource-exhaustion surface. An explicit memory/DL budget, streaming content-length cap and safe redirect policy are required.

For scanned PDFs, the code calls `convert_from_path(pdf_path, dpi=300)`, materializing all page images before processing. There is no evident upper page/image count in this method. A large PDF can consume substantial memory and OCR cost; a page-by-page converter and bounded page budget would be safer.

## 5. Factual extraction and evidence provenance

SmartScraperGraph runs over the webpage URL or extracted document text and returns model-generated result objects, to which metadata is attached. The prompt seeks detailed eligibility, amount, institution, application materials and deadline. However there is no deterministic typed schema or field-level source quote/coordinates, no independently checked latest-cycle constraints, and no applicant-nationality-specific tuition/stipend verification. A model result may conflate different awards or source periods.

The code supports relative URL fixing and includes a secondary document-extraction track, but link association should carry document-level identity and exact evidence excerpts to avoid attributing a claim from one PDF to an unrelated program. `source_type` is not a substitute for independently verified claims.

## 6. Runtime and deployment concerns

The Dockerfile uses a non-root user, installs Tesseract/Poppler/Playwright dependencies and a Python 3.12 base image. These are positive isolation attempts but do not constitute a network sandbox or constrain resource usage. Requirements use minimum versions rather than pinned lock hashes. No automated tests or CI workflow was found in the 15-file tree. The repository includes saved demonstration JSON and TXT outputs; those are not live source validation.

Documentation claims OpenAI as default while the `ScholarshipScraper` constructor actually defaults to `ai_provider="gemini"`. CLI/config statements require reconciliation. The README contains references to `unified_scholarship_scraper.py` and `guide.py` which are absent from the tracked tree. These are documentation drift, not test-backed capabilities.

## 7. Validation and limitations

Static source and configuration prove synchronous source processing, in-memory PDF download, OCR image conversion and lack of checked claim evidence. Third-party library behavior, actual API availability/cost, document parsing success, page handling, deployment and any source's current eligibility were not tested. Binary PDFs were not downloaded.

Evidence: [main scraper](https://github.com/do3-173/scholarship_scraper/blob/93e406d24da01ace739ae80f1f819ab130a83962/scholarship_scraper.py), [DOCX processor](https://github.com/do3-173/scholarship_scraper/blob/93e406d24da01ace739ae80f1f819ab130a83962/docx_processor.py), [configuration](https://github.com/do3-173/scholarship_scraper/blob/93e406d24da01ace739ae80f1f819ab130a83962/config.py), [Dockerfile](https://github.com/do3-173/scholarship_scraper/blob/93e406d24da01ace739ae80f1f819ab130a83962/Dockerfile), [README](https://github.com/do3-173/scholarship_scraper/blob/93e406d24da01ace739ae80f1f819ab130a83962/README.md).

## 8. PhD Atlas transfer decision

Adapt format-aware acquisition (HTML, official PDFs, Word annexes), language-aware text extraction, source URLs, timestamps and per-method extraction metadata. Add private-network blocking, source allowlists, redirect validation, bounded streaming downloads, per-page rendering limits, instrumented parser failures and deterministic typed claim validation. Make each eligibility/funding/deadline field point to an exact source document and span. Distinguish discovery, extraction and official verification. Do not classify historical Sarajevo grants as current international PhD funding without fresh official corroboration.
