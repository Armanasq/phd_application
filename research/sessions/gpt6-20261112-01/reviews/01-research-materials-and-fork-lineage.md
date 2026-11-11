# Research materials, CV extraction and applicant-experience lineage

Session: gpt6-20261112-01  
Review date: 2026-11-12  
Method: pinned-source static inspection; no third-party code executed.

## 1. aditirajnish/scholarship_web_scraper

- Upstream: https://github.com/aditirajnish/scholarship_web_scraper
- Snapshot: `4786fa11d7871e37f78003babd7de5abe82d2c0f` (master)
- License: MIT. No issues or pull requests observed.
- Inspected: `README.md`, `main.py`, `verify.py`, `requirements.txt`, `LICENSE`, and full 10-entry tree.

### Purpose and dataflow

A narrowly scoped scraper for historical Schulich Leaders scholar profiles. It accepts a hard-coded year and university, fetches the yearly scholar listing, extracts profile links, fetches each profile, filters by exact university text, extracts name/program, and writes one text file per university/year.

### Implementation observations

- The source set is limited to the Schulich Leaders website; the university allowlist has 20 entries and the year allowlist ends at 2020. The default invocation targets 2020 and the University of British Columbia.
- `requests.get` is called with `verify=False` for both listing and profile pages. This disables TLS certificate verification and exposes the scraper to interception.
- Requests have no timeout, explicit status validation, retry/backoff, or per-profile failure isolation.
- Parsing assumes the `person--selected-by` element exists. A changed or incomplete page can raise an exception and terminate the run.
- University matching is exact and case-sensitive; aliases, punctuation and institutional name variants are not normalized.
- CSS selectors are hard-coded to the current page structure. There is no pagination, schema validation, source snapshot, provenance timestamp, or structured database.
- Results are written as unstructured text. Existing outputs are overwritten.
- Dependencies are pinned to 2020-era versions. No tests or CI were found.

### Transferability

The source-specific adapter pattern is useful: separate listing discovery from detail-page extraction and validate input parameters. The implementation is not a reusable PhD opportunity monitor. Its records are historical award-recipient biographies, not current funded vacancies, and must not be interpreted as evidence of current scholarship availability.

Disposition: `PRELIMINARY_FOCUSED`; useful historical scraper example, not production-grade.

Evidence: [main.py](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/main.py) · [verify.py](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/verify.py) · [requirements](https://github.com/aditirajnish/scholarship_web_scraper/blob/4786fa11d7871e37f78003babd7de5abe82d2c0f/requirements.txt)

## 2. AlanWang610/academic-cv-scraper

- Upstream: https://github.com/AlanWang610/academic-cv-scraper
- Snapshot: `4862fc7cf220efa7bb802f8f452e05c66d3dd7de` (main)
- License: MIT. Repository is archived. No issues or pull requests observed.
- Inspected: `README.md`, `scrape.py`, `parse.py`, `build_author_list.py`, `find_first_names_and_doi.py`, requirements and tracked CSV/JSONL artifacts; full tree has 12 entries.

### Purpose and architecture

The project attempts to identify academic CVs from web search, download PDF documents, extract education/appointments/publications with an LLM, and build an author list from academic-publication metadata. The workflow separates discovery, retrieval, PDF text extraction, structured parsing and author-name resolution.

### Implementation observations

- `scrape.py` uses Browser Use with `gpt-4o-mini` to locate a person's CV and applies a finance/economics relevance check. This is a domain-specific prompt, not a general academic-CV classifier.
- The LLM result is parsed by searching the string representation of `result.history[-1]` for hard-coded delimiters. This depends on an internal serialization format and can fail when Browser Use changes its result representation.
- Downloaded filenames are constructed from a person name without a robust path-safe slug or containment check. Network requests have no explicit timeout or maximum download size.
- PDF parsing concatenates `page.extract_text()` results without handling `None`; scanned or malformed pages can therefore fail.
- The parsed CV text is sent to an external LLM. CVs contain personal and potentially sensitive data; the repository has no visible consent, retention, redaction, deletion or data-minimization workflow.
- `parse.py` relies on LLM-produced JSON but does not enforce a strict schema, required fields, confidence thresholds, or robust recovery from Markdown fences and malformed output.
- The `spacy` model is loaded but does not appear to be used in the inspected parsing path. The dependency manifest does not clearly cover every imported runtime dependency, including pandas and the expected NLP model.
- Author-name resolution uses positional character similarity and last-name substring checks. This is not a reliable entity-resolution algorithm: common names, initials, transliteration and reordered names can produce false matches.
- The author resolver's matching score is not calibrated and does not use stable author identifiers as the primary key.
- The repository is archived; no test suite or CI validation was observed.

### Transferability

The decomposition into discovery, retrieval, extraction, entity resolution and structured export is useful for building supervisor/lab profiles. Reuse requires authoritative identity anchors (ORCID, institutional profile, DOI author IDs), human review, explicit provenance, strict privacy controls and schema-validated extraction. Do not scrape or redistribute personal CVs without an appropriate lawful basis.

Disposition: `PRELIMINARY_FOCUSED`; adjacent research-intelligence tool, not an admissions workflow.

Evidence: [scrape.py](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/scrape.py) · [parse.py](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/parse.py) · [author resolver](https://github.com/AlanWang610/academic-cv-scraper/blob/4862fc7cf220efa7bb802f8f452e05c66d3dd7de/find_first_names_and_doi.py)

## 3. Farsi-language PhD application and relocation guide — fork lineage

Repositories examined:

| Repository | Snapshot | Relationship |
|---|---|---|
| [AliAIOps/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad) | `6f836112c3acc66e2951714fb85b76ea3eec7319` | Fork of Fatemeh-J upstream |
| [alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad) | `87f5dc76669472ed86adc80536aa283ceb7ed009` | Fork of same upstream |
| [alistvt/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/alistvt/Putting-in-for-a-PhD-and-moving-abroad) | `e2a2ce6cd4d43cb55d1509fb7153869d8993c60b` | Fork of same upstream |
| [Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad) | compared by full tree/blob SHAs | Tree/blob-identical to Fatemeh-J upstream; already has a preliminary canonical review |

### Unique fork deltas

- AliAIOps changes seven files relative to the upstream, including job-search guidance, post-admission steps, relocation, flight booking, packing, furnishing and Groningen service information.
- alirezazolanvari has a separate set of seven modified files, one added accommodation file and four removed files. Its unique contribution is primarily accommodation/arrival and revised post-admission/relocation guidance.
- alistvt differs from the upstream only in README content at the inspected snapshot; the substantive guide files are identical.
- These are derivative edits to one underlying guide. They must not be counted as three independent applicant experiences or independent corroboration.

### Process knowledge extracted

The guide decomposes the applicant journey beyond the offer:

1. Find a funded PhD vacancy through European academic-position boards and Dutch university vacancy channels.
2. Receive and decide on an offer; confirm the response deadline and negotiate the decision date where possible.
3. Complete university registration and submit degree, transcript, identity, English-language and research documents.
4. Work with the university's immigration service and the Dutch IND process for MVV/residence authorization.
5. Complete university-specific supervision/planning forms and employment/registration steps.
6. Prepare embassy appointment, document legalization, travel, housing, municipal registration and local onboarding.

The Groningen-specific narrative mentions Horaf inita registration, the Train and Supervision Plan, the Graduate School of Science and Engineering, the university Immigration Service Desk and Individual Training Budget. These are useful workflow entities, not universal Netherlands procedures.

### Temporal and evidential limits

- The forks' latest content dates to 2022–2023. Embassy procedures, immigration timelines, fees, contact details, forms, housing availability and university portals may have changed.
- The guide mixes firsthand experience, institution-specific instructions and general advice without claim-level source dates or verification status.
- Some statements describe one person's successful route; they do not establish average processing times, guaranteed outcomes or universal eligibility.
- Current visa, legalization and employment claims must be replaced with official university and Dutch government sources before operational use.
- The user's target-country list does not include the Netherlands. The transferable value is the lifecycle decomposition and evidence checklist, not the country policy.
- No fork license was established in repository metadata; do not reproduce large portions of the prose.

Disposition: unique fork deltas reviewed as one dependent source family; preserve lineage edges and do not inflate applicant-experience counts.

Evidence: [AliAIOps job-search guidance](https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad/blob/6f836112c3acc66e2951714fb85b76ea3eec7319/Find%20a%20PhD%20Position.md) · [post-admission workflow](https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad/blob/6f836112c3acc66e2951714fb85b76ea3eec7319/After%20being%20admitted.md) · [immigration guide](https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad/blob/6f836112c3acc66e2951714fb85b76ea3eec7319/Immigration%20affairs.md) · [alirezazolanvari accommodation delta](https://github.com/alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad/blob/87f5dc76669472ed86adc80536aa283ceb7ed009/Accomodation.md)

## Cross-source conclusion

These sources provide three different evidence classes: a historical scholarship-recipient scraper, a CV/author entity-extraction prototype, and a first-person post-admission/relocation guide. They are not interchangeable. Preserve source type, date, author/fork lineage and the distinction between an extracted record, an applicant account and a current official requirement.