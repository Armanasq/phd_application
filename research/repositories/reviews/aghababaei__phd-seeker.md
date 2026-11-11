# Deep review — Aghababaei/PhD-Seeker

## 1. Repository identification
- **Canonical:** https://github.com/Aghababaei/PhD-Seeker
- **Owner:** Amin Aghababaei / collaborators; name as stated in packaging.
- **Purpose:** Python CLI to discover advertised doctoral listings from ScholarshipDB and FindAPhD; categorization vacancy scraper and export.
- **Relevant to:** global search, especially positions listed in target countries; not field-specific.
- **License:** GPL-3.0 as reported by repository API and `setup.py`; check copyleft obligations before reuse.
- **Source snapshot:** `93ad22ea8bc0a04bbf566613650b36a58ff2c063`; inspected on 2026-11-11. Last commit 2025-03-12. No GitHub releases observed through API; source branch is not archived.
- **Review type:** code-level static methodological examination plus issues/PR metadata. **NOT EXECUTED**. No employment or funding claims independently checked on its target sites.

## 2. Problem and applicant assumptions
The software attempts to reduce manual searching across two job boards by querying keywords and filtering location, with an exportable CSV/XLSX. A user must already know research keywords, data sites must be parseable via public HTML, and the opportunity remains a search *lead*. The repository is not a formal international applicant eligibility or funding verifier.

## 3. Actual implementation and data flow
Evidence:
- [Core async parser, version-pinned](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/phdseeker/main.py) — `__get_page__` builds source URL, fetches HTML with httpx, selects title/country/date/link, aligns records using `zip`, and builds a DataFrame.
- [Source adapter configuration](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/phdseeker/repo.yaml) — one ScholarshipDB selector set and two FindAPhD URLs split by EU status.
- [CLI](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/phdseeker/phdseeker_cli.py) — docopt arguments for keyword, country, pages, output; passes them to `PhDSeeker`.
- [Package setup](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/setup.py) — setuptools CLI, pandas, httpx, openpyxl and related dependencies.
- Data path: query → HTML parse → four parallel scraped lists → string-based date conversion → DataFrame sort/drop exact duplicates → CSV/XLSX. No structured proof of fees, stipend, funded term, PI recruiting or closing date. The site's posted-date text is not a deadline.
- User-facing [README](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/README.md) claims fully funded results, but code does not substantiate the **funding amount/international tuition/eligibility**. Treat as search relevance rather than verified funding.

## 4. Critical assessment — verified source defects
**Security — high / direct source fact:** core `main.py` calls `httpx.AsyncClient(verify=(repo == "findaphd"))` in `__get_page__`, while `repo.yaml` uses `scholarshipdb`, `findaphd-noneu`, and `findaphd-eu`. None equals `findaphd`, so **certificate verification is disabled for all configured sources**. This was missed in first-pass assessment.

**Security — high / direct source fact:** date sorting computes `self.df["timedelta"].apply(lambda x: eval(x) if x else x)` on text transformed from remote webpages. This is an unsafe evaluation primitive reachable from third-party HTML parsing (exact exploitability not tested). Replace with an allowlisted interval parser; never run the upstream parser on untrusted input.

**Reliability:** `zip(titles,countries,dates,links)` silently truncates misaligned selector lists; page parser swallows arbitrary exceptions into `False`, loses error cause; no guaranteed rate control or canonical source snapshots; `drop_duplicates` only exact rows, not duplicate jobs under alternate ads.

**Maintenance:** [Issue #22](https://github.com/Aghababaei/PhD-Seeker/issues/22) asks whether CAPTCHA breaks current functionality (open). [Issue #16](https://github.com/Aghababaei/PhD-Seeker/issues/16) requests deadline support (open). [PR #20](https://github.com/Aghababaei/PhD-Seeker/pull/20) proposes tests but remains open; source inspection did not find a merged, proven test gate. [Issue #19](https://github.com/Aghababaei/PhD-Seeker/issues/19) reports an h11/httpcore compatibility issue (closed; closed status does not prove all versions supported).

**Bias and legal:** relies on two commercial search directories, misses unindexed department vacancies, and does not establish scraping permission / legal compliance. No published benchmark of current precision/recall was verified.

## 5. Application relevance and transferability
A configurable multi-board scraper is a useful **discovery stage**, but neither posted-date recency, a “fully funded” phrase, nor export count proves an active international-funded vacancy. For Swiss/Norwegian employee positions, inspect employer portal, actual requirements, nationality/security clearance and gross contract salary. For UK, explicitly check international tuition awards rather than search tags.

## 6. Comparators and derivatives
- [ScholarshipScout](https://github.com/danielhafezi/ScholarshipScout) shares ScholarshipDB/FindAPhD patterns but contains a placeholder `extract_info`; no advantage in verified financing.
- [PhD-Hunter](https://github.com/you27-mohamed/PhD-Hunter) explicitly credits PhD-Seeker and combines it with a LinkedIn scraper, so they are **not independent evidence** for scraper reliability. PhD-Hunter also contains credential-like strings and has distinct access risks.
- [academic-job-digest](https://github.com/BaseLayerAI/academic-job-digest) offers source-specific adapters, persistence and dedup but is US biomedical and needs TLS/schema hardening. It is better systems-design reference, not a plug-in replacement.

## 7. Judgment
**Verdict: REJECT executable implementation as-is; ADAPT narrowly the conceptual adapter interface and CLI.** Quality is insufficient for unattended ingestion, especially for current funding decisions. Source-file review confidently identifies TLS misconfiguration and unsafe `eval`; real-world failure rates, exploitability and scraped-site availability remain untested. Rebuild with TLS on, strict HTML parser, sandboxed retrieval, safe date parsing, deterministic dedup and official-source verification gate. No upstream code or credential copied.

## 8. Evidence and outstanding review
Sources above are permalinks at the cited snapshot plus issue/PR status observed on 2026-11-11. What remains: site Terms/robots review, legal assessment, current live fetching, controlled malicious-date fixture, target selector drift test and exact dependency vulnerability testing. Do not promote this review to runtime/security certification.
