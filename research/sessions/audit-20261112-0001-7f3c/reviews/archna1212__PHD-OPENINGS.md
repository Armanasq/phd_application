# archna1212/PHD-OPENINGS — source-lineage and implementation audit

- Repository ID: 1212713238
- Default branch: main
- Inspected commit: 1b2f558fe128d7d90c8c2323500a9e71fa945e77
- Created: 2026-04-16
- Latest observed change: README download-link update
- Review disposition: SCREENED_EXCLUDE as an independent implementation; retain as a derivative mirror of Aghababaei/PhD-Seeker
- Confidence: High for source identity and static code findings; no runtime validation

## 1. Purpose and scope

The repository describes itself as “PhD Seeker”, a Python scraper for doctoral positions advertised on ScholarshipDB and FindAPhD. Its actual scope is search-result collection and export, not a complete admissions workflow. It does not model applicant eligibility, funding components, supervisor fit, application stages, or submission evidence.

## 2. Complete structure and provenance

The recursive tree contains 11 entries: one package directory and ten files. The files are README.md, requirements.txt, setup.py, and the phdseeker package files __init__.py, __main__.py, constants.py, main.py, phdseeker_cli.py, repo.yaml, and rich_dataframe.py.

A content-address comparison against Aghababaei/PhD-Seeker found that all nine non-README file blobs are byte-identical to the upstream repository at the inspected revision. Every path in this repository also exists upstream; this repository has no unique implementation file. Its README differs, but the setup metadata still points to the original Aghababaei repository and retains the original author/maintainer attribution. GitHub reports fork=false, so this is a copied mirror rather than a GitHub fork relationship.

The upstream repository contains additional files absent from this copy, including its LICENSE, changelog, manifest and Makefile. The copied setup.py declares GPLv3, but this repository omits the license file. The absence of the upstream license and provenance metadata in the copy creates a redistribution/compliance ambiguity; do not assume the mirror has independently established reuse rights.

Evidence:
- [Inspected repository tree](https://github.com/archna1212/PHD-OPENINGS/tree/1b2f558fe128d7d90c8c2323500a9e71fa945e77)
- [Copied scraper implementation](https://github.com/archna1212/PHD-OPENINGS/blob/1b2f558fe128d7d90c8c2323500a9e71fa945e77/phdseeker/main.py)
- [Source configuration](https://github.com/archna1212/PHD-OPENINGS/blob/1b2f558fe128d7d90c8c2323500a9e71fa945e77/phdseeker/repo.yaml)
- [Packaging metadata](https://github.com/archna1212/PHD-OPENINGS/blob/1b2f558fe128d7d90c8c2323500a9e71fa945e77/setup.py)
- [Upstream implementation](https://github.com/Aghababaei/PhD-Seeker)
- [Existing canonical upstream review](../../../../research/repositories/reviews/aghababaei__phd-seeker.md)

## 3. Actual workflow

The package loads three YAML source configurations: ScholarshipDB, FindAPhD non-EU, and FindAPhD EU. It builds quoted keyword queries, requests up to a configurable number of pages per source, extracts title/country/date/link fields with BeautifulSoup, optionally filters by country, and exports CSV/XLSX through pandas. The CLI exposes keywords, countries, page limit, output format, and verbose display.

This is search-result collection, not a verified opportunity database. It does not extract or verify salary, stipend, tuition coverage, nationality restrictions, funding duration, deadline cut-off time, supervisor availability, or application outcome. The output schema is limited to Country, Date, Title and Link.

## 4. Implementation defects confirmed in the copied source

- **Unsafe date evaluation:** relative date text scraped from external HTML is transformed and passed to Python eval(). This is an arbitrary-code-execution boundary on untrusted source content.
- **TLS verification disabled for all configured sources:** the client sets verify=(repo == "findaphd"), but the actual configuration keys are findaphd-noneu and findaphd-eu. The condition is therefore false for every configured source. InsecureRequestWarning is also globally suppressed.
- **No explicit request controls:** no explicit timeout, retry policy, HTTP status validation, or response-content validation is implemented before parsing.
- **Brittle selectors:** source-specific CSS classes are hard-coded in repo.yaml and can silently stop matching after provider redesigns.
- **Silent record truncation:** titles, countries, dates and links are collected into separate lists and combined with zip(); unequal selector counts silently drop trailing values.
- **Misleading concurrency termination:** page tasks catch their own exceptions and return False, while asyncio.wait uses FIRST_EXCEPTION. Since errors are converted to return values, the early-exception behavior is ineffective and the tasks generally run to completion.
- **Event-loop lifecycle:** the object obtains an event loop at construction, runs it synchronously, then closes it. This is not safe to embed in an already-running asynchronous application.
- **Relative-date approximation:** months are converted to a fixed 30-day interval and all dates are reduced to a relative minute count. The result is not an absolute deadline and has no timezone/cut-off semantics.
- **Version-check race:** the CLI launches a background version-check thread using a shared dictionary; the check has no explicit timeout or status validation, and the CLI can finish before the result is written.
- **Weak deduplication:** pandas drops only identical full rows. Cross-source copies, changed URLs, changed titles, or the same vacancy with different provider metadata remain duplicates.

## 5. Maintenance and validation

The repository has four commits, one branch, no reported issues or pull requests, no tests, and no CI workflow. The last observed commit changes only a README download link. Dependencies are not pinned in requirements.txt. The README's installation/package instructions still describe the original project rather than a separately maintained implementation.

No upstream code was executed. The defects above are static findings; runtime behavior and exploitability were not tested.

## 6. Adoption decision

Do not count this repository as an independent project, method, or applicant evidence source. Its implementation is byte-identical to the already reviewed PhD-Seeker code. Retain the repository only as a provenance/rediscovery record and add a MIRROR_OF relation to Aghababaei/PhD-Seeker when the canonical relation ledger is reconciled.

The transferable concept is YAML-driven source adapters. Do not reuse the copied scraper without addressing untrusted eval, TLS verification, source parser tests, absolute date semantics, canonical opportunity identity, funding evidence, and source-level provenance.
