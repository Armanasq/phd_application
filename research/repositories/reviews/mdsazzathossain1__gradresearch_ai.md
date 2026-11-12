# mdsazzathossain1/GradResearch_AI — deep static agent, CV and privacy audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/mdsazzathossain1/GradResearch_AI | **Pinned revision:** [`953d52dd223c635f38d3b864acf66d4a6111da9a`](https://github.com/mdsazzathossain1/GradResearch_AI/commit/953d52dd223c635f38d3b864acf66d4a6111da9a) | **State:** DEEP_REVIEW_DOCUMENTED (source static; no model/browser execution) | **Verdict:** adapt private research-fit workflow only; reject present unauthenticated shared-state service for actual CVs.

## 1. Objective and scope

A 2025 FastAPI/LangChain/Gemini agent that researches professors and PhD position pages, extracts an applicant's local PDF CV into FAISS using Google Generative AI embeddings, analyses research alignment and drafts prospective-professor emails. It also attempts Firecrawl extraction with a Requests/BeautifulSoup fallback and keeps conversation sessions. The 17-entry tree includes Python source, frontend template, a committed `.env` path, compiled Python bytecode, model configuration and prompt files. Its README calls the workflow an email **generator**, not a verified email delivery or application submission service.

## 2. Research and personal-data flow

`main.py` instantiates one global LangChain agent with `ChatGoogleGenerativeAI`, registers `/start_session`, `/sessions`, `/load_session/{thread_id}`, `/chat`, `/comprehensive_research`, `/update_session` and `/clear_history`, and stores all conversations in `chat_history.json`. At session start it attempts to load a fixed `cv.pdf` with `initialize_vectorstore_with_cv`; `tools.py` embeds extracted CV content using an external Google embedding API and retains a vector store. Professor data is collected through search links, Scholar/institution pages and generic web scraping, then combined with user background for email generation.

This produces two distinct unverified inputs: externally retrieved academic claims and private applicant CV content. Neither is a verified institution hiring authorization, and the model's final email is **not** evidence of being sent or accepted.

## 3. Authentication and session isolation risks

The inspected FastAPI routes have **no authentication or request ownership checks**. `/sessions` exposes stored session identifiers/titles and `/load_session/{thread_id}` returns a named conversation by arbitrary ID. `/update_session` updates identified session metadata and `/clear_history` deletes the global history file. These are direct source-level confidentiality/integrity risks if deployed beyond a strictly isolated, single-user loopback.

One `chat_history.json` is shared across the process; access control, per-user segregation, retention/deletion and authenticated audit events are not implemented. A generated UUID is an identifier, not a sufficient standalone security boundary. Use a private owner-scoped datastore and authenticated session authorization before handling any real applicant details.

## 4. CV and external provider privacy

The CV is a fixed-path local document, which makes multi-user use ambiguous and creates risk of loading the wrong applicant's file if shared. The embedding engine is Google-hosted, so CV text leaves the local runtime; the README does not implement a separately verified consent/privacy gate for that transfer. The global tool vector index and verbose agent logging can retain or expose CV-derived content across sessions.

A `.env` path is tracked in the repository. Its presence is an exposure-control failure even if its actual contents are not assessed here; this review did **not** read, use or reproduce any credential values. Rotate and remove any secrets if the file ever contained active credentials, and enforce environment/secret scanning in CI.

## 5. Source reliability and unsupported research claims

`tools.py` uses external search snippets, institution pages, Scholar/arXiv/PubMed heuristics and raw HTML extraction. It has retries and per-request timeout in some paths, a positive operational pattern, but no institution-identity resolution, official open-vacancy verification or field-level source span with independent corroboration. Search results may contain false homonyms or historical supervisor affiliations.

The system prompt mandates a lengthy step-by-step research and email workflow and prescribes U.S.-specific prospective-supervisor conventions. These are heuristics, not validated universal admissions communication protocols. A detailed AI-written email may be persuasive without establishing actual research fit, funded PI capacity, consent to outreach, or scholarship eligibility. The model's confidence should not be treated as admission probability.

## 6. Runtime, failure and tool boundaries

The service calls synchronous LangChain agent execution from asynchronous FastAPI route code and keeps shared mutable session state. This can block concurrency and cause cross-request interference in a deployed multi-user service. Catch-all exceptions often return raw `str(e)` to clients, potentially exposing implementation details. `tools.py` is roughly 1,600 lines and contains multiple extraction fallbacks; no test modules, security CI, authorization contract or benchmark dataset was observed in the tree.

The pinned dependencies are declared in `requirements.txt`. No pinned runtime container, browser fixtures, output-evidence checker or verified outreach API is present. This audit did not run the service, obtain a Gemini/Firecrawl account, parse an actual CV, or access a real professor.

## 7. Transfer into a safe PhD research architecture

Reusable: multi-step scientific research dossiers, separable CV retrieval, source-specific professor profiles, explicit applicant fit comparison, and *draft-only* outreach. Required redesign:
1. Authenticated private user sessions and owner-scoped chat/CV data.
2. Explicit consent and a local-only option before uploading CV embeddings/model prompts to an external service.
3. Verified professor identity (institution, ORCID/papers), current publications and source-claim spans.
4. Separate a historical lab research page from an officially active funded doctoral position.
5. Require user approval and verifiable outbound-mail sent receipts before recording any communication action.
6. Never expose private applicant data in public Git, logs, session browsing or unprotected web endpoints.
7. Add unit tests for CV isolation, source drift, extraction unknowns, hallucinated publications, retries and concurrency.

## 8. Pinned evidence and validation limits

- [README and intended email workflow](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/README.md)
- [FastAPI routes and session handling](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/main.py)
- [Scrapers, FAISS, CV ingestion and research tools](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/tools.py)
- [Gemini and embedding providers](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/model.py)
- [Agent instruction template](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/system_prompt.py)
- [Declared dependencies](https://github.com/mdsazzathossain1/GradResearch_AI/blob/953d52dd223c635f38d3b864acf66d4a6111da9a/requirements.txt)

**DEEP_REVIEW_DOCUMENTED — static implementation.** No secret values, CV PDFs or third-party applicant records were accessed. No live provider call, penetration test, published paper verification, actual email transmission or admission result validation occurred.
