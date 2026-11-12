# syfantid/Greek-CS-Student-Opportunities — deep static content review

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/syfantid/Greek-CS-Student-Opportunities | **Pinned revision:** [`3b7e4337eaf69e697dc61bc406801333d103342a`](https://github.com/syfantid/Greek-CS-Student-Opportunities/commit/3b7e4337eaf69e697dc61bc406801333d103342a) | **State:** DEEP_REVIEW_DOCUMENTED (content audit only) | **Decision:** historical source taxonomy; do not treat as current funding or PhD vacancy evidence.

## 1. Intended audience and evidence type

A manually curated, Greek-CS-student-oriented opportunity directory. It groups paid internships, general graduate employment, travel grants, conferences, hackathons, summer programs, scholarships, funded master's programs, and doctoral programs. The complete 11-file repository consists of README, nine topical Markdown lists, and a Jekyll theme config. It is a reference catalogue, **not** an admissions platform, verified eligibility engine, crawler, supervisor tracker, or official funding database. Latest upstream update observed: 2023-04-10.

## 2. Full inventory and classification

The `README.md` links nine topic files; all were read at the pinned revision:

| File | Actual content | Admissions role |
|---|---|---|
| `phd-programmes.md` | One PhD/postdoc ML/NLP opportunity, University of Lisbon, deadline **December 2017** | Historical PhD example only |
| `graduate-positions.md` | Two professional jobs: Booking.com software engineering and Google AI Residency 2018 | Not a doctoral admission listing |
| `scholarships.md` | Various degree-level educational grants with criteria and sponsors | Funding leads requiring current official verification |
| `master-programmes.md` | Ten MSc/Erasmus-style programs, some described fully or partially funded | MSc, not PhD programs |
| `paid-interships.md` | CERN, Vulcanus, World Bank, and product-school placements | Internships, some open to enrolled doctoral students |
| `summer-programmes.md` | ETH, EPFL, Google Summer of Code, Outreachy and other programs | Mostly training/internship |
| `travel-grants.md` | Two travel-support references | Ancillary grant programs |
| `conferences.md` | Two event-support references, including a 2017 conference link | Event funding, not admission |
| `hackathons.md` | Two hackathon entries and an empty row | Non-degree opportunity |

The scholarship and program pages use manually edited HTML tables embedded in Markdown. There are no machine-readable source snapshots, retrieval timestamps, official-source claim annotations, refresh jobs, schema validation, or outcome records.

## 3. Source lineage and temporal coverage

The only explicit PhD-opportunity row links to a faculty-managed job page and gives a December 2017 close date. Its “Full” funding label is not supported by a recorded contract, amount, offer letter, or contemporary official confirmation. Several additional links explicitly reference 2017 or 2018 award cycles, and scholarship deadlines use approximate labels such as “Beg Mar”, “Mid Apr”, or no year. The repository's 2023 modification does not refresh these records into a 2026/27 recruitment cycle.

The scholarship list mixes institutional, philanthropic, government, and industry providers; URLs include historical pages and legacy HTTP links. Each entry is a **discovery pointer**, not a currently active funding entitlement. No live linked-source pages were independently rechecked in this audit.

## 4. Eligibility, funding and decision semantics

The scholarship table records heterogeneous constraints: degree level, demographic requirements, grades, nationality, age ceilings, or student status. It also mixes distinct financial benefits: tuition coverage, cash award, travel/lodging support, and professional development. These categories must never be compressed into a single binary funded/unfunded flag.

A travel grant or conference-registration reimbursement does not finance doctoral tuition or living expenses. Several records are for master's or undergraduate study. The Chinese Government Scholarship row includes eligibility text inconsistent with its abbreviated degree-level column, demonstrating why normalized typed eligibility is required.

## 5. Architecture and maintenance

As a plain Markdown/Jekyll collection, it has no extraction code, API, tests, CI, database, user authentication, or automated integrity check in the inspected tree. A website-oriented grouping is useful for human browsing but cannot support complete search, live deadlines, duplicate reconciliation, renewal-cycle disambiguation, or provenance-aware scoring without an importer and a canonical source model.

No license grant was found in the 11-file tree. Do not assume permission to redistribute external content or copy other providers' logos, essays, or award text.

## 6. Bias, verification and operational risks

- **Geographic selection:** explicitly oriented to Greek CS students; not a representative international scholarship universe.
- **Historical drift:** 2017/2018 postings and approximate deadlines must not be promoted to 2026 vacancies.
- **Funding conflation:** internship pay, tuition waiver, fellowship stipend, travel support, and research employment are different instruments.
- **Eligibility mismatch:** per-item degree/age/citizenship conditions may differ from editorial column summaries.
- **Source dependency:** links to an original provider are references to verify, not independent confirmations.
- **Missing outcomes:** no award recipients, rejection denominator, current application windows, or calibrated selection data.
- **Incompleteness:** a single PhD entry does not support global discovery saturation or broad inference.

## 7. Transferable lessons

Reuse only the broad source taxonomy and separate funding dimensions. For a scientific admissions tracker, normalize each item as an event, program, award or vacancy with an original owner, cycle, official URL, observed date, last verified date, eligibility terms, funding components, degree type and documented unknowns. Preserve the original 2017 doctoral posting as `HISTORICAL`; never mark it open. Treat future scholarship renewal as a new version requiring its own evidence.

Link the catalogue to applicant readiness only after independently validating the official institution/provider page. Funding eligibility and guaranteed funding are separate assertions.

## 8. Pinned evidence and validation boundary

- [README](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/README.md)
- [Doctoral programs](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/phd-programmes.md)
- [Scholarships](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/scholarships.md)
- [Master's programs](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/master-programmes.md)
- [General graduate positions](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/graduate-positions.md)
- [Paid internships](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/paid-interships.md)
- [Summer programs](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/summer-programmes.md)
- [Travel grants](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/travel-grants.md)
- [Conferences](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/conferences.md)
- [Hackathons](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/hackathons.md)
- [Jekyll config](https://github.com/syfantid/Greek-CS-Student-Opportunities/blob/3b7e4337eaf69e697dc61bc406801333d103342a/_config.yml)

**DEEP_REVIEW_DOCUMENTED — static repository content.** All tracked textual source files were read. External funding portals, recruitment status, current grant conditions and applicants were **NOT independently validated**. No empirical runtime or admission-outcome claim is made.
