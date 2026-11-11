# Independent repository investigation — Ontario undergraduate scraping, legacy PhD admissions and applicant artifacts

Date: 2026-11-12. Target: https://github.com/Armanasq/phd_application. This report is source-pinned and additive on `main`; it does not change shared screening, exclusions, generated indexes, or concurrent session documents. At assignment, the three target identities were UNTRIAGED and not listed in inspected published session ownership manifests. Unpublished work of other conversations remains unobservable.

## 1. dzkchen/ouinfo-scraper — undergraduate domain mismatch

- Repository: https://github.com/dzkchen/ouinfo-scraper
- Snapshot: [37fb9cc4daa1ac6b60eb644e565a2c3518fe5bd9](https://github.com/dzkchen/ouinfo-scraper/commit/37fb9cc4daa1ac6b60eb644e565a2c3518fe5bd9), 2026-03-27.
- Inspected: 12-entry tree, [README](https://github.com/dzkchen/ouinfo-scraper/blob/37fb9cc4daa1ac6b60eb644e565a2c3518fe5bd9/README.md), `scrape_programs.py`, `scrape_scholarships.py`, `csv_convert.py`, metadata, commits and issue listing.
- Proposed disposition: **SCREENED_EXCLUDE — UNDERGRADUATE_ADMISSIONS_SCOPE_MISMATCH**. No code or source data was run.

OUInfo covers Ontario secondary-school applicants and undergraduate university programme/scholarship applications: OUAC codes, Grade 12 prerequisites, admission averages and undergraduate supplementary applications. Those are not doctoral positions, tuition commitments or postgraduate research admissions. The scholarship script produces undergraduate award records, not international funded PhD vacancy evidence. The README describes its outputs as a work in progress with possible errors.

The programme crawler uses HTTPS, `requests.Session`, a bounded timeout, HTTP status checks and paginated catalogue discovery; programme IDs include collision disambiguation. Yet its link acceptance condition tests whether `ouinfo.ca` is a substring of the hostname rather than exact or properly suffixed hostname, so lookalike hosts could be admitted. Supplementary-application detection uses heuristic text matches; missing text becomes a negative boolean rather than an independently evidenced determination. These source-level observations are not claims that any external exploit was run. Transferable source parsing techniques require redesign for doctoral intake, verified cycle-specific eligibility and permitted source URLs.

## 2. DeepanshuGautam/phd_admissions — historical institutional PhD admissions portal

- Repository: https://github.com/DeepanshuGautam/phd_admissions
- Snapshot: [63cd39182ce9eebbd1065258c47ba3ac581b6d5e](https://github.com/DeepanshuGautam/phd_admissions/commit/63cd39182ce9eebbd1065258c47ba3ac581b6d5e), 2015-04-20.
- Inspected: 96-entry tree, Git history and issue list; representative PHP files `adminLogin.php`, `create_database.php`, `view_applications.php`, `set_criteria.php`, `personal_info.php`, `change_password.php`, `master_database_connection.php`, `select_database.php`.
- Proposed disposition: **PRELIMINARY_FOCUSED — historical architecture reference only; reject deployment or code reuse without security redesign**.

This is a PHP + MySQLi administrator-oriented admissions workflow, with semester/year-specific databases, applicant and qualification tables, application lists and shortlisting criteria. It models a university-side process rather than an applicant's opportunity discovery, supervisor match, private document readiness or funding entitlement.

Direct code inspection found SQL constructed using string concatenation and user-controlled inputs: [adminLogin.php](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/adminLogin.php) interpolates an admin username into a SQL SELECT; [view_applications.php](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/view_applications.php) interpolates a submitted discipline; [personal_info.php](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/personal_info.php) concatenates a request `app_no` into a query. The [password changer](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/change_password.php) writes a direct SHA-512 password hash instead of a modern slow salted password KDF and also dynamically concatenates its SQL UPDATE. The database builder creates table names from interpolated variables. These are serious source-level security anti-patterns, **not a demonstrated live exploit**.

The fetched tree contains no visible current test/CI suite, independent credential audit or licensing proof. Avoid moving its PHP authentication code into a contemporary application. Transfer only independently redesigned concepts: intake-cycle entities, role-scoped access, validated screening criteria, privacy-preserving record custody and immutable decision history.

## 3. Dieselmarble/PhD-Application — applicant writing resources and personal-artifact corpus

- Repository: https://github.com/Dieselmarble/PhD-Application
- Snapshot: [d007ea157200c5a8eb8a1c10f973b70dcdafbab6](https://github.com/Dieselmarble/PhD-Application/commit/d007ea157200c5a8eb8a1c10f973b70dcdafbab6), 2025-10-08.
- Inspected: [README](https://github.com/Dieselmarble/PhD-Application/blob/d007ea157200c5a8eb8a1c10f973b70dcdafbab6/README.md), complete 56-entry tree, licensing presence, upstream history and issue listing.
- Proposed disposition: **PRELIMINARY_FOCUSED — historical writing/structure reference; do not ingest personal documents**.
- Content boundary: no GRE books, CV PDFs, recommendation letters, personal statements, ZIPs or private artifacts were opened, reproduced or incorporated.

The README curates resources for CVs, personal statements, statements of purpose, research proposals, prospective-supervisor contact, GRE requirements and graduate applicant advice. It distinguishes applicant personal narrative from research-focused SOP framing while warning that a programme may combine or separate such documents. The tree contains named personal application files, referee letters and third-party GRE PDFs. An Apache-2.0 repository license file exists, but this does not establish separate rights or consent for personally identifying material or externally authored copyrighted documents. A past closed issue concerned a broken supervisor-contact link. External official requirements and link freshness were not verified in this review.

Adopt only the public README's document taxonomy and links as historical leads. Recheck official per-programme 2026–27 prompts/word limits and consent for any original artifact. An example SOP is not admission-success evidence.

## Cross-repository synthesis and explicit limits

- **Scope gate:** undergraduate scholarships and Grade 12 records do not satisfy PhD research opportunity selection, regardless of shared terms like “university” or “scholarship”.
- **Authority gate:** 2015 institution-side application software is not a trustworthy modern applicant-private platform; parameterized SQL, safe password KDFs, authenticated role boundaries and server-side audit trails are prerequisites.
- **Evidence gate:** historical SOP/PS/letter examples and repository license metadata cannot prove effectiveness, current admissions rules, publication rights or permission to process personal documents.
- **Workflow model:** source observation -> date/cycle-scoped claim -> primary official verification -> candidate-specific eligibility/funding -> authorized submission evidence.
- **Validation:** static source inspection only; no third-party runtime testing, real authentication, external applications, live scholarship sources or unpublished session activity verification.

Canonical CSVs and generated review indexes are not changed by this session report; reconcile the proposed dispositions atomically and only if the identities remain unclaimed at a fresh main-branch snapshot.
