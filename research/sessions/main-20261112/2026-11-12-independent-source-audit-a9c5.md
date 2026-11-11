# Independent source audit — four GitHub discovery candidates

**Date:** 2026-11-12  
**Repository:** https://github.com/Armanasq/phd_application  
**Integration:** direct `main` addition under a session-specific, non-overlapping path.  
**Evidence:** connected GitHub repository metadata, complete recursive trees, upstream commits, issues and file contents. No third-party executable or crawler was run, no credentials were used, and linked destination sites were not independently checked.

The four identities below were UNTRIAGED in the inspected 404-candidate inventory and were absent from the published assignment manifests available at review time. Work in other sessions that is not published cannot be observed. The canonical source-of-truth CSVs are intentionally not modified by this session-specific source report; the integration owner should reconcile them with concurrent work.

## 1. ekotwidodo/awesome-phd-positions — portal discovery source

- **Source:** https://github.com/ekotwidodo/awesome-phd-positions
- **Pinned commit:** [1482cb17635e35246ed69cd28648e8ed77d39075](https://github.com/ekotwidodo/awesome-phd-positions/commit/1482cb17635e35246ed69cd28648e8ed77d39075), dated 2026-07-05.
- **Tree inspected:** exactly two tracked files, `README.md` and `CONTRIBUTING.md`; both read in full.
- **Disposition:** useful curated *discovery* guide, not a confirmed funded-vacancy dataset.

The README groups university hiring and PhD pages under Austria, Belgium, Denmark, Estonia, Finland, France, Germany, Ireland, Italy, Luxembourg, Netherlands, Norway, South Korea, Sweden, Switzerland and the United Kingdom. Additional leads include EURAXESS, EURES, EuroSys, INOMICS, Nature Careers, EGU, Marie Skłodowska-Curie Actions and institutional doctoral programme pages. Ireland, Luxembourg, Norway, Switzerland and the UK match target-country workstreams. The pinned document has no first-class Canada, Australia or New Zealand country sections.

There is no scraper, structured position ID, funded-status determination, tuition or nationality eligibility model, employer-source snapshot, deadline cycle, rate-limited monitor, de-duplication, field-level claim evidence or test suite. A directory link is not proof that a vacancy exists, remains open, is funded, or admits a specific applicant.

The README declares CC0 1.0 and links the Creative Commons deed, but its two-file tree contains no standalone license file; this author statement does not govern linked third-party sites. Contributions are encouraged through PRs, but `CONTRIBUTING.md` does not impose verifiable source-freshness gates. No published issues were returned by the inspected listing. External URLs and their current redirects/eligibility were not validated.

Evidence: [README](https://github.com/ekotwidodo/awesome-phd-positions/blob/1482cb17635e35246ed69cd28648e8ed77d39075/README.md) · [Contributing](https://github.com/ekotwidodo/awesome-phd-positions/blob/1482cb17635e35246ed69cd28648e8ed77d39075/CONTRIBUTING.md).

**Transfer:** retain a country-to-portal lead crosswalk with source-owner and last-inspected fields; independently verify individual opportunities and funding terms on authoritative employer pages. The repository itself is fully inspected at the two-file level; external source chains remain unverified.

## 2. glavrentiadis/phd_position_aegis-r — doctoral interview task

- **Source:** https://github.com/glavrentiadis/phd_position_aegis-r
- **Pinned commit:** [6fc9cf3971a517d6bc04aaaafb38142a6fef2c14](https://github.com/glavrentiadis/phd_position_aegis-r/commit/6fc9cf3971a517d6bc04aaaafb38142a6fef2c14), dated 2025-11-24.
- **Tree:** `README.md`, `problem_statement.md`, `Analysis/preprocessing/compute_ba18_residuals.py`, input CSV and derived residual CSV. Prompt and Python code inspected; numerical CSV bodies not inspected.
- **Disposition:** relevant historical example of a research-intensive PhD selection assessment, *not* an active vacancy or current funding offer.

The README identifies a University at Buffalo AEGIS-R Lab Ph.D. interview exercise in structural/earthquake engineering. The prompt requires a ground-motion model of at least five 0.25–5 Hz frequencies, using earthquake magnitude, rupture distance, shear-wave velocity `Vs30`, earthquake/station UTM locations, and frequency correlation. It explicitly permits linear methods, Gaussian processes, neural networks or other justified models. Expected output is a 10-minute presentation documenting modeling assumptions, diagnostic evaluation and scenario predictions.

The Python preprocessing script reads an NGA-West2 tabular dataset with pandas, extracts `freq*` columns, constructs `pygmm.model.Scenario`, evaluates `BaylessAbrahamson2019`, interpolates log spectral amplitudes and derives log residuals. The filename is labeled `ba18` while the imported GMM class is labeled 2019, making benchmark attribution a point requiring independent scientific verification. File paths are relative to the current working directory, and code executes at import time without a main guard. No test suite, pinned environment file or data validation run was observed. The source tree has no visible license file; upstream issue list returned no reported issues.

**Transfer:** useful template for constructing bounded robotics/SLAM research interviews around model assumptions, scenario tests, evaluation plots and concise defenses. Do not copy datasets or state that this lab is currently hiring. No runtime tests, residual analysis or independent verification of scientific results were performed.

Evidence: [prompt](https://github.com/glavrentiadis/phd_position_aegis-r/blob/6fc9cf3971a517d6bc04aaaafb38142a6fef2c14/problem_statement.md) · [preprocessing script](https://github.com/glavrentiadis/phd_position_aegis-r/blob/6fc9cf3971a517d6bc04aaaafb38142a6fef2c14/Analysis/preprocessing/compute_ba18_residuals.py) · [README](https://github.com/glavrentiadis/phd_position_aegis-r/blob/6fc9cf3971a517d6bc04aaaafb38142a6fef2c14/README.md).

## 3. ddsuhaimi/scholarship_scraper — historical ingestion reference

- **Source:** https://github.com/ddsuhaimi/scholarship_scraper
- **Pinned commit:** [f87946acd027be753dbbd11704efef8fbecfbbb3](https://github.com/ddsuhaimi/scholarship_scraper/commit/f87946acd027be753dbbd11704efef8fbecfbbb3), dated 2019-08-17.
- **Tree:** three tracked text files: `readme.md`, `scraper.py` and `export/scholarship.csv`; all inspected.
- **Disposition:** historical methodological example with substantive correctness problems; not usable as current scholarship evidence.

The Python script fetches one page only (`range(1, 2)`) from an `http://` scholars4dev.com URL, parses fixed CSS selectors with BeautifulSoup, extracts scholarship name, university, degree, country, deadline and start period, then writes a pandas CSV. It has no request timeout, HTTP status validation, retry, content-type checks, HTTPS/TLS guarantee, source URL per row or provenance hash. Six broad bare `except` clauses silently transform extraction failures into `None`. Hard-coded page limits and fixed layout assumptions prevent any coverage guarantee. Its README does not list the imported `requests` dependency.

The checked-in 12-row CSV contains a mixture of undergraduate, master's, MBA, doctoral and postdoctoral awards, with dates from 2019/2020 and ambiguous compound deadline strings. Some fields are missing. It lacks cycle-specific eligibility, salary/stipend, international tuition, sponsor verification and per-field authoritative source URLs. It has no observed tests, CI or license file; no published issues were returned in the inspected list.

**Transfer:** a small example of adapter-to-table extraction, but not implementation code to reuse unmodified. Replace with bounded HTTPS fetching, explicit typed nulls/errors, source snapshots, raw source ID, cycle-aware deadline parsing, applicant-class eligibility and independent official-award validation. Historical date strings must never be promoted to 2026–27 facts.

Evidence: [scraper](https://github.com/ddsuhaimi/scholarship_scraper/blob/f87946acd027be753dbbd11704efef8fbecfbbb3/scraper.py) · [README](https://github.com/ddsuhaimi/scholarship_scraper/blob/f87946acd027be753dbbd11704efef8fbecfbbb3/readme.md) · [historical CSV](https://github.com/ddsuhaimi/scholarship_scraper/blob/f87946acd027be753dbbd11704efef8fbecfbbb3/export/scholarship.csv).

## 4. DVT/rick-and-morty-app — evidence-based exclusion

- **Source:** https://github.com/DVT/rick-and-morty-app
- **Pinned commit:** [d43da45c04afd796c9d9849e211fee4afbaef715](https://github.com/DVT/rick-and-morty-app/commit/d43da45c04afd796c9d9849e211fee4afbaef715).
- **Tree:** 96 entries, Angular application and testing/deployment configuration. Root README and complete file paths inspected, not all application code.
- **Disposition:** `SCREENED_EXCLUDE` — false positive for "graduate projects"; unrelated to doctoral admissions.

The [README](https://github.com/DVT/rick-and-morty-app/blob/d43da45c04afd796c9d9849e211fee4afbaef715/README.md) explicitly describes an Angular Rick and Morty demonstration using the public Rick and Morty API, Firebase and CircleCI. The source tree concerns character/episode UI, not opportunities, scholarships, supervisors, application evidence or graduate-school process. Dependency-update PRs do not change this subject classification.

A README+tree relevance inspection is sufficient for exclusion; a line-by-line code audit would not improve the admissions research question. Do not add this as an independent admissions research source.

## Cross-repository conclusions and status

1. A source directory, one lab's historical interview prompt, a 2019 scraper and an unrelated graduate-course demo are **four different evidence classes**. An inventory must distinguish screening, preliminary research, deep static source inspection, independent validation and exclusion.
2. A portal link does not establish a current eligible funded doctoral opening; a historical scholarship CSV cannot be used as a live deadline source; a technical interview exercise is not a confirmed vacancy.
3. Useful architecture for PhD application intelligence: `source registry -> permitted acquisition -> immutable observation -> field-level claim -> independent source verification -> candidate-specific funding/eligibility gate -> authorized action`.
4. The three substantive sources provide no independently confirmed 2026–27 vacancy, stipend, tuition or visa facts. No external code execution, live scraping, employer portal interaction or admissions application submission was performed.

**Pending canonical integration:** the four source-level dispositions should be reconciled with `data/github_discovery_candidates.csv`, `data/repositories.csv`, `data/exclusions.csv` and generated indexes by a single owner after checking current `main` and concurrent work. They are not counted as new canonical rows merely because this note has been committed.
