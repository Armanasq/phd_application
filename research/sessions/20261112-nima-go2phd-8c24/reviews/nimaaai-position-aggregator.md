# NimaaaAI/Position-Aggregator — deep static source audit

**Checked:** 2026-11-12  
**Upstream:** https://github.com/NimaaaAI/Position-Aggregator  
**Pinned commit:** [0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef](https://github.com/NimaaaAI/Position-Aggregator/commit/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef)  
**Review depth:** DEEP_STATIC_SOURCE_REVIEW; upstream runtime, database, crawler, embeddings and model APIs **NOT_EXECUTED**.  
**Verdict:** Strong architectural research reference, but reject production adoption without source-completeness, data-freshness, deduplication and privacy fixes.  
**Scope:** complete 19-file tree; `README.md`, `schema.sql`, `sites.yml`, `scrape.py`, `extract.py`, `embed.py`, `search.py`, `ask.py`, `chat.py`, `update.py`, dependencies, environment template and web templates; commit history, issues and PRs. No live source pages, downloaded HTML cache or database snapshots were independently inspected.

## 1. Scope, dataflow and verified implementation

A local-first academic-vacancy collection and search system built with Python 3.11, PostgreSQL/pgvector, SentenceTransformers and FastAPI. Five configured job boards: Academic Positions, AcademicTransfer, jobs.ac.uk, Nature Careers and EURAXESS. `sites.yml` declares sitemap or listing discovery, per-source job-ID regex, collection delay, optional extraction fields and selectors.

The implemented pipeline is: `scrape.py` discovers advertisement URLs and stores raw HTML under `data/raw/<source>/<id>.html`; `extract.py` extracts schema.org `JobPosting` or definition-list fields and upserts normalized positions; multilingual title regexes label PhD/postdoc/etc.; ISO-country mapping normalizes country aliases; corpus-derived stopwords populate a PostgreSQL table; `embed.py` generates 768-dimensional normalized multilingual-e5 vectors for positions and overlapping description chunks; `search.py` combines position-vector, chunk-vector and lexical full-text ranking via reciprocal rank fusion, then optional BGE cross-encoder reranking; `ask.py` builds an answer from ranked advertisements via a configurable external OpenAI-compatible API; `chat.py` provides the authenticated user interface and usage accounting.

Useful implemented choices: a `(source,source_id)` compound primary key; date-bearing source rows; type/country filters **before** ranking; multilingual job-title taxonomy; source-specific capture; local retrieval/reranking; explicit citation indexing; PostgreSQL HNSW/GiN indexes; password hashing with per-user salt and scrypt; HttpOnly SameSite cookies, session revocation and admin-approved registration.

**Source links:** [configuration](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/sites.yml), [schema](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/schema.sql), [search](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/search.py), [API](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/chat.py).

## 2. P0: database configuration diverges across pipeline stages

`update.py` and `search.py` read `DATABASE_URL` from the environment; `extract.py` and `embed.py` hard-code `postgresql://positions:positions@localhost:5432/positions`. A user following the documented configurable environment with a different database can have the update controller count one database while extraction and embedding write another, or fail when the hard-coded database does not exist. `chat.py` uses `search.DSN` and therefore inherits the configured path.

**Required fix:** one validated DB config import used by every process, environment/config smoke test with a non-default DSN, connection role/grant tests and a single tracked schema-migration mechanism.

Evidence: [update.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/update.py), [extract.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/extract.py), [embed.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/embed.py), [search.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/search.py).

## 3. P0: cross-source deduplication conflates distinct opportunities

`search.py:collapse` deduplicates by **lowercased title + city only**. The commentary says it must distinguish same-source adverts, but the actual key lacks `source`, `source_id`, employer and recruitment identifier. Thus two independently advertised posts named, for example, "PhD Student" in the same city can collapse, including two posts **on the same board**. The merged row keeps only one vacancy's primary record, with the second demoted to an `also_on` link, potentially hiding a different deadline, group, employer or application.

**Required fix:** candidate-pair generation with official position ID and canonical employer/institution identity; confidence-scored cross-source alias links and an explicit cannot-merge rule for distinct source IDs absent identity evidence. Preserve every opportunity and funding/deadline claim. Add same-title/same-city/different-vacancy and cross-board duplicate fixtures.

Evidence: [search.py, collapse](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/search.py).

## 4. P0/P1: sitemap failures can be recorded as complete closures

`scrape.py` marks a URL census `complete=True` before visiting sitemap index and child sitemaps, then reads `get(...).text` without checking HTTP 200, valid XML or a minimum/reference-set threshold for that sitemap branch. A 403, 500 or changed index structure may produce an empty set while still passing the completeness gate. The code then overwrites `<source>_urls.txt` and appends all previously seen URLs to `<source>_closed.txt` as disappeared. This is a **false source-disappearance signal**, not proof that positions closed. The EURAXESS listing branch does mark non-200 pages as incomplete, which is a useful contrasting guard; it nevertheless stops at the first page with no fresh matching links, so a parser/layout change can look like normal completion.

The `extract.py --archive` command is **separate**; it archives on parsed closing date and was **not** found to automatically consume the disappearance file. Do not claim that the default updater automatically deletes all postings on the false signal.

**Required fix:** explicit `COMPLETE / PARTIAL / FAILED` enumeration per source run, verified status/schema and page coverage, conservative disappearance quarantine, source-census generation ID, and no closure transitions on partial or untrusted observations.

Evidence: [scrape.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/scrape.py), [update.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/update.py).

## 5. P1: stale HTML and chunk embeddings after changes

`scrape.py` skips every URL with an existing HTML filename; its normal update discovers new URLs rather than re-fetching old advertisements. Extensions to deadlines, funding and positions are consequently missed until an explicit refresh is implemented. `extract.py` correctly clears the **position-level** vector if `embed_text` changed on re-extraction, but `embed.py:embed_chunks` considers an ad complete when **any** chunk already exists and skips all old chunks unless `--force` rebuilds the chunk table. A changed description may therefore have a refreshed position embedding while its chunk-ranking index remains stale.

**Required fix:** scheduled conditional re-fetch with source content hash/ETag, atomic generation keyed to content version, and per-ad targeted chunk replacement with validation; do not rebuild/delete every chunk globally for a single changed ad.

Evidence: [scrape.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/scrape.py), [extract.py UPSERT](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/extract.py), [embed.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/embed.py).

## 6. P1: source rights, deadlines and provenance

- The `sites.yml` author notes that EURAXESS `robots.txt` disallows the jobs and query paths, then explicitly chooses to download them regardless. This is documented *upstream code intent*, not independent verification of current website policy. **Do not reuse this crawler for a compliant production ingestion process** without current authorization; prefer sanctioned APIs, RSS, feeds, employer pages and permitted access.
- `read()` takes the URL only from an HTML canonical link; when absent it stores an empty URL instead of preserving the fetched URL. There is no immutable source content hash, exact evidence span, verification decision, or application-cycle provenance.
- A missing closing date satisfies `open_only` filters, so "no published deadline" is presented within the same result set as verified future deadlines. It is not evidence of an open vacancy.
- Parsed `validThrough` dates use `datetime.fromisoformat` without an explicit timezone or source-local cutoff contract. Conversions and midnight boundaries need source-zone handling.
- Explicit `extract.py --archive` retains metadata but nulls the description and vectors and removes chunks; absent a separate immutable snapshot, the original evidence body cannot be reconstructed from the DB after archiving.

Evidence: [sites.yml](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/sites.yml), [extract.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/extract.py), [search.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/search.py).

## 7. User/account, cost and AI trust boundaries

The FastAPI UI is authenticated, contrary to stale introductory comments in `chat.py`; password verification uses constant-time compare, random salts and scrypt, and registration requires an admin activation. Positive controls are visible, but login lacks rate limiting; the session cookie is not `Secure` (upstream default binds localhost/HTTP). `api_chat` checks the user's daily quota and logs **after** the LLM call; concurrent requests can pass the preflight quota before either is charged, so the limit is not an atomic cost cap. `Question.show`, `context` and `model` are not server-side bounded/allowlisted for resource/cost purposes. The source advert text and user question are concatenated into a model user message; no separate programmatic prompt-injection or output-fact validation barrier is established. Display HTML escapes most inserted fields, but links require URL-scheme allowlisting and data-origin validation in addition to HTML escaping.

**Required fix:** atomic quota reservation, restricted model choices, bounded request sizes, login throttling, secure-cookie policy for remote deployment, untrusted-source markup/URL validation, strict claim-level grounding and non-LLM deadline confirmation.

Evidence: [chat.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/chat.py), [ask.py](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/ask.py), [chat template](https://github.com/NimaaaAI/Position-Aggregator/blob/0919cb7ad541b53f85ddb669d62b3c5a0a94f2ef/templates/chat.html).

## 8. Maintenance, empirical confidence and transfer recommendation

Latest inspected upstream commit: **2026-09-30**. The repository has 19 files, no license file, no listed test modules, no open issues/PRs and no detected GitHub Actions workflow path. A README badge claims **21,659 advertisements and 32,815 chunks**, but there is no public database snapshot, crawl log or reproducible benchmark in this repository to independently validate its current count, PhD share, precision, recall or ranking latency. Do **not** elevate these values to independently verified statistics. The claimed absence of a `LICENSE` limits code reuse; abstract techniques and interfaces can be independently implemented.

**Adopt as architecture references:** source-configured adapters, distinct position/chunk/lexical retrieval, reciprocal rank fusion, a second-pass reranker, eligibility type/country filters before ranking, corpus-derived stopwords and explicit unknown values.

**Reject until repaired:** uncontrolled closure inference, title+city canonical identity, stale re-fetch/chunk indexes, unlicensed source copying, the current access policy for restricted boards, inconsistent DSN, weak evidence lineage and unconditional "open" semantics. An admissions intelligence system must treat an observed advert as a source observation, not a verified current, funded, international-eligible PhD opening. Pair each field with source/time/scope, and separately verify official employers before applicant action.

## 9. Validation boundary

No dependencies were installed, PostgreSQL instance created, unauthenticated or authenticated external source crawls performed, external model called, benchmark executed, screenshots generated, or upstream tests run. Findings are based on complete tree enumeration and static inspection of the cited source. No vulnerability exploit is claimed.
