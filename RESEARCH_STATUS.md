# Research execution and evidence status

**Current snapshot:** 12 November 2026. This project is an **ongoing research program**, not a completed systematic review or an accepted admissions application.

| Workstream | State | Evidence accomplished | Completion blocker |
|---|---|---|---|
| Global repository discovery | INITIAL_SCREENING_COMPLETE | 404 unique discovered candidates; all classified (reviewed or excluded) | discovery saturation, broader pagination/topic/fork coverage and live-source rechecks remain unproven |
| Individual GitHub repository audits | IN PROGRESS | 228 source-pinned review records: 124 deep static reviews, 104 preliminary; 176 documented exclusions | upgrade 104 preliminary investigations; run/verify independent source and methodology checks |
| Source/repository dependence | EVIDENCE_COLLECTED | 6 evidenced relationships, 21-source ledger, 26 claim records | canonicalize more shared guides and verify original claims independently |
| Eight country dossiers | EVIDENCE_COLLECTED | All eight source-linked national assessments, including policy and funding contrasts | national lab/vacancy coverage, visas, tuition and 2027 recruiting completeness |
| Funding and available programs | IN PROGRESS | 78 leads (20 + 58 added 14 Nov by seven parallel search agents) with official-source and tuition/offer gates; 57-lab supervisor radar; see [search synthesis](synthesis/opportunity-search-2026-11-14.md) | employer form rechecks, offer terms and candidate-specific fee/eligibility |
| Scientific supervisor matching | EVIDENCE_COLLECTED | Three method/paper-based target lab dossiers; 2023 *Measurement* article externally source-verified | PI availability, verified degree/English, recent papers and novelty audit |
| Applicant firsthand accounts | IN PROGRESS | Six classified cases, contradictory UK and Norwegian experiences preserved | longitudinal, international multi-source review and population limitations |
| Cross-source systematic mapping | IN PROGRESS | comparative repo taxonomy, dependence, empirical limits and source-based best practices | more qualified independent studies, formal screening-yield statistics |
| Immediate 2026 offer analysis | IN PROGRESS | ETH/UZH/Monash employer leads differentiated from 2027 decision cycles | no published guaranteed 2026 offer, interview/document/eligibility bottlenecks |
| 2027 portfolio and documents | IN PROGRESS | EPFL/UK/UBC/Monash/NZ cases and explicit scientific-fit plan | accepted/eligible package, personal official transcripts, scholarship commitments |
| Structural QA | VERIFIED (structural only) | GitHub Actions **17 tests passed**, local links, schema/migrations, source generation, idempotent importer with application state preservation | third-party implementation and semantic source verification **not tested** |

## Evidence boundary

The public [source ledger](data/sources.jsonl) contains 21 distinct URLs supporting 26 recorded claim items. **Every ledger record currently reads `independent_recheck: NOT_PERFORMED`**. Primary-official retrieval is a stronger source type than an anecdote, but the dual-source independently confirmed stage is not met.

**Canonical CSV screening states (recomputed 12 November 2026):** 0 untriaged; 0 screened-in awaiting review; 176 excluded with reasons; 228 review records (124 deep static and 104 preliminary). Exactly 404 discovered identities; initial inventory disposition is complete, independent testing and discovery saturation are not.

## Offer and communication status

No application submissions, supervisor emails, funded offers, interviews, or acceptance evidence has been recorded by the workspace. An open admissions channel is not a funding offer. Applicant's published *Measurement* 2023 DOI has been verified at publisher; official degree equivalence, present language scores, accepted-paper ranking, national immigration eligibility and reference willingness are **not formally established**.

## Immediate deadline-driven priorities

- **Before 27 November 2026:** ETH RobotX application and three-group research-fit packet; [official RobotX page](https://robotx.ethz.ch/education/open-positions.html) says final decisions by **15 February 2027**, so remove from the 2026-offer probability group.
- **Before 30 November 2026:** ETH Soft Robotics employer call, conditional on documented hardware/robot-learning relevance and degree evidence; response aim ≠ offer.
- **Urgent verification:** UZH Robotics and Perception Group initial deadline passed, states review until positions filled; obtain actual remaining-spot/form status before any classification as open.
- **1–2 December:** EPFL EDIC central route and Oxford funding consideration. Oxford full international coverage is not guaranteed by program admission.
- **15 December:** UBC CS application for September 2027, with separately dated transcript and referee requirements.
- **2027 preparation:** Surrey funded international visual design Jan 17, Monash R1 Feb 28 and Wellington doctoral scholarship March 1; Luxembourg salaried CVI2 portal status still unverified.
- **Research first:** review any top-ranked-publication requirement against **specific documented rank**, not merely existence of a journal DOI.

See [deadline-specific readiness and authorization gates](docs/operations/november-2026-readiness.md), [public research importer](docs/architecture/importer.md), and [research method](METHODOLOGY.md), [current opportunity records](data/opportunities.csv), [quality scope report](quality/coverage-report.md), and [candidate-specific plan](strategy/2026-2027-corrected.md).
