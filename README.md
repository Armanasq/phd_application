# PhD Admissions Intelligence & Execution

**Evidence snapshot:** 12 November 2026 · **State:** active systematic mapping and admissions research — **not complete**

A public, reproducible research workspace for fully funded doctoral admissions in **Canada, the United Kingdom, Ireland, Luxembourg, Switzerland, Norway, New Zealand, and Australia**, with **global** GitHub resource investigation. Scientific target areas: inertial and visual-inertial estimation, SLAM, navigation, robot perception, physics-informed learning and autonomous systems.

The objective is a credible **fully funded offer as early as possible**, screening specifically for offers that could occur by 31 December 2026 while building a realistic 2027-intake pipeline. An application deadline or scholarship application is **not an offer**.

## Research and decision entry points

| Purpose | Canonical artifact |
|---|---|
| **Actual research status and blockers** | [Research status](RESEARCH_STATUS.md) |
| 2026–27 application decisions and deadlines | [Corrected application campaign](strategy/2026-2027-corrected.md), [research-fit priority table](strategy/research-fit-priorities.md), [deadline/approval checklist](docs/operations/november-2026-readiness.md) |
| Country-specific institutional policy | [Eight country dossiers](docs/countries/README.md) |
| Officially sourced vacancies, scholarships, programs | [20 opportunity/route leads](data/opportunities.csv) and [individual funding, fee and offer-date gates](data/opportunity_assessments.csv) |
| Global GitHub reviews | [Canonical repository index](research/repositories/index.md), [67 reviewed record metadata](data/repositories.csv) |
| Global GitHub candidate inventory | [404 raw discovered identities](data/github_discovery_candidates.csv), [18 screened exclusions](data/exclusions.csv) |
| Transparent search/research method | [Protocol](METHODOLOGY.md), [source policy](SOURCE_POLICY.md), [discovery log](data/discovery_log.jsonl) |
| Verifiable claims and source independence | [26 claims](data/claim_register.jsonl), [21 canonical source records](data/sources.jsonl), [dependency crosswalk](synthesis/source-dependency-crosswalk.md) |
| Researcher and laboratory matching | [Three research-fit dossiers](research/supervisors/index.md) |
| Applicant experiences and contradictions | [Six evidence-classified public cases](research/applicant-experiences/index.md) |
| Cross-source findings | [Preliminary systematic mapping](synthesis/repository-systematic-review.md), [country comparison](synthesis/country-comparison.md) |
| Implementation and source QA | [Relational model](docs/architecture/data-model.md), [idempotent local importer](docs/architecture/importer.md), [coverage and limits](quality/coverage-report.md), [methodology critique](quality/methodology-audit.md) |

## Corpus boundaries

| Level | Count | Meaning |
|---|---:|---|
| Raw GitHub candidate identities | **404** | Unique repository strings from sampled queries and selected referrals; **includes noise** |
| Reviewed repositories | **67** | A dated, source-revision-specific individual record |
| Eight-section deep static reviews | **9** | Inspected relevant code/docs, provenance, method, comparisons and limitations; **runtime tests not executed** |
| Preliminary bounded reviews | **58** | Not yet satisfying the full research-review contract |
| Screened exclusions | **18** | Documented exclusion rationale and provenance |
| Included for subsequent review | **2** | Relevant initial screening, individual deep review pending |
| Untriaged discovery candidates | **319** | No inclusion determination made |
| Country dossiers | **8** | Official-source national assessments; not nationwide vacancy exhaustiveness |
| Program/position/scholarship leads | **20** | Heterogeneous opportunity classes; **not 20 verified funded offers** |
| Claim records / canonical sources | **26 / 21** | Claim-specific source references; independent semantic recheck still pending |
| Applicant experience cases | **6** | Source-classified anecdotes, **not representative admissions statistics** |

Search included 12 first-page broad repository queries, six GitHub code-search groups, and eight further multilingual/focused first-page repository queries. Query families include Chinese and Turkish, plus international research terms. **No discovery saturation has been demonstrated.**

## Immediate admissions interpretation

- [ETH Soft Robotics](https://jobs.ethz.ch/job/view/JOPG_ethz_d3lDgHgDI4ewDFQ1Fb): salaried and time-sensitive, 30 November 2026; a three-week **initial response aim** is not a guaranteed offer.
- [UZH Robotics and Perception Group](https://rpg.ifi.uzh.ch/positions.html): excellent scientific overlap and salaried PhD recruitment; original 27 October cutoff passed, continuing screening stated, **remaining vacancies and application-form acceptance unverified**.
- [ETH RobotX](https://robotx.ethz.ch/education/open-positions.html): fully funded November 2026 application round, but **final decisions by 15 February 2027**; not a defensible December 2026 offer promise.
- [Monash–NVIDIA PhD](https://vl4ai.erc.monash.edu.au/positions/distrobot-phd/): advertised funded international package; candidate's publication-venue eligibility unresolved.
- [Surrey international-funded computational vision PhD](https://www.surrey.ac.uk/postgraduate/vision-speech-and-signal-processing-phd): tuition waiver including overseas fees plus stipend, 17 January 2027, moderate topic fit.
- [Luxembourg SnT CVI2 computer vision](https://www.uni.lu/en/jobs/doctoral-researcher-in-computer-vision/): salaried doctoral advertisement with published gross pay; employer's external application portal status unverified.

No application has been submitted, professor contacted or offer received through this workspace. Preparation and research are not equivalent to external action.

## Repository architecture

```text
METHODOLOGY.md          research questions, inclusion criteria, screening, stop rule
SOURCE_POLICY.md        claim evidence, policy/financial gates, privacy
RESEARCH_STATUS.md      evidence-backed progress and blockers
data/                   machine-readable catalogues, claims, leads, searches, exclusions
research/
  repositories/         canonical index and eight extended source reviews
  supervisors/          publication/methodology-fit investigations
  applicant-experiences/ curated firsthand accounts with source class
docs/
  countries/            eight standalone country dossiers
  github/reviews/       retained original bounded review notes (historical)
  architecture/         entity design and append-only migrations
synthesis/              comparative and evidence-dependence analyses
strategy/               2026 and 2027 pipeline and research-fit portfolio
quality/                source and methodological QA, coverage limitations
sql/                    normalized SQLite schema and additive migrations
scripts/                discovery, validation, index, source ledger, bootstrap
tests/                  regression and data integrity checks
.github/workflows/      continuous structural validation
```

## Reproducibility and quality gates

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/generate_index.py --check
python3 scripts/build_source_ledger.py --check
python3 scripts/validate_sources.py
python3 scripts/detect_duplicates.py --fail-on-duplicates
python3 scripts/check_links.py
python3 scripts/bootstrap.py --db .local/phd_intelligence.sqlite
python3 scripts/import_research.py --dry-run
python3 scripts/import_research.py --db .local/phd_intelligence.sqlite
```

Optional discovery uses authenticated GitHub REST search only when explicitly run; credentials are read from `GITHUB_TOKEN` in the environment, never committed:

```sh
python3 scripts/discover_repositories.py --max-pages 2 --per-page 50
python3 scripts/discover_repositories.py --max-pages 2 --per-page 50 --write
```

The first command is **dry-run by default**, the second updates the research queue and appends a query log. Both are distinct from eligibility screening and independent review. Search quotas and partial API results are surfaced rather than hidden.

**This is a public repository.** Do not commit private applicant CVs, documents, scores, citizenship, references, passwords, email messages or credentials. Source links and verifiable public publication identifiers are acceptable. Application submissions, external outreach, and offer acceptance require explicit authorization and proof-backed state transitions.
