# Preliminary systematic mapping of open PhD-admissions resources

**Date:** 11 November 2026. **Not a completed systematic literature review.** This is a structured evidence mapping of public repositories and selected official admissions processes. Research questions, retrieval selection and limits: [METHODOLOGY.md](../METHODOLOGY.md).

## Corpus and evidence independence

The global discovery inventory currently contains **404 unique raw candidate names**, including irrelevant names. Direct screening has found **9 excluded** and **7 included-but-not-deep-reviewed**. There are **35 dated repository assessments**: **8** detailed, eight-part static reviews and **27** preliminary inspection notes. These are a small examined subset, not an exhaustive global sample. [Canonical status-tagged index](../research/repositories/index.md) · [Structured candidate queue](../data/github_discovery_candidates.csv) · [Full limitations](../quality/coverage-report.md).

Eight detailed investigations cover:
[PhD-Seeker](../research/repositories/reviews/aghababaei__phd-seeker.md),
[evidence-aware planner](../research/repositories/reviews/sihengtao__phd-application-planner.md),
[academic-job-digest](../research/repositories/reviews/baselayerai__academic-job-digest.md),
[PhD XML feed](../research/repositories/reviews/eparrainage__phd.md),
[ProReach CRM](../research/repositories/reviews/khanshaheb34__profreach.md),
[PhD application/outreach pipeline](../research/repositories/reviews/erikpsw__phd-application-pipeline.md),
[Supervisor Fit Radar](../research/repositories/reviews/wenzi-researchlab__phd-fit-radar.md),
and [Chinese neuroscience PhD handbook](../research/repositories/reviews/brainphd-cn__handbook.md).

## Functional taxonomy

| Resource class | Examples in investigated inventory | Evidence of actual utility | Critical limitation |
|---|---|---|---|
| Firsthand application stories | gwisk, zhanglj37, BrainPhD-CN, womanreading7 | Context, preparation tactics, interview process | Success selection bias, stale/US-focused policy, anecdote ≠ causal inference |
| Curated guidance and Awesome lists | pliang279, shaily99, poloclub, zhijing-jin | Cross-reference discovery, original faculty advice links | Recycled sources and unverified 2026 deadlines |
| Writing materials and templates | Swapnil-Gandhi, LimHyungTae, vsitzmann | Real LaTeX/copy-edit structures | Example text could fabricate candidate achievements if copied |
| Scrapers and recruitment monitors | PhD-Seeker, ScholarshipScout, PhD-Hunter, PeiMu | HTML extraction and author/position search concepts | Unsafe code, source churn, weak international funding and dedup |
| Published vacancy feeds | eparrainage/phd | Current Atom vacancy URLs, broad search awareness | Generator not published; date/funding/fee eligibility unverified |
| Persistent automated monitoring | BaseLayerAI/academic-job-digest | Site-specific adapters, stored state, duplicate detection, PI enrichment | US biomedical coverage; TLS, SQL, privacy and silent PI-drop risks |
| Applicant systems and AI workspaces | SihengTao planner, ProReach, zhoujasper Atlas, zxcgzx | Program/PI entities, state tracking, evidence QA, document/export workflows | Actual AI claims, private data, authorization, backups not independently run |
| Prompt/skill workflows | erikpsw pipeline, fanyi3017 agent | Structured evidence selection, draft-only authorized outreach | Host capabilities needed; a prompt is not executable app or verified source |
| Scientific-fit frameworks | wenzi PhD Fit Radar | Methods, equipment, recent output and proposal feasibility beyond keywords | Uncalibrated 0–5 scoring, no live PI availability or outcome data |

## Evidence-backed cross-resource comparison

**Reused sources are not independent evidence.** [PhD-Hunter](https://github.com/you27-mohamed/PhD-Hunter) credits [PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker) and an upstream LinkedIn scraper. ScholarshipScout and PhD-Seeker target ScholarshipDB/FindAPhD, so they may report the same employer vacancy. Awesome Lists repeat original faculty SOP and application advice; number of backlinks does not count as observed successful applicants. See [source-dependency crosswalk](source-dependency-crosswalk.md).

**A scraper's “fully funded” label cannot be trusted alone.** The author/editor interface must distinguish original employer, current live portal, tuition category, international award, stipend/salary term, actual PI funding and expected **offer** date. For example, [Reading home-fee-only studentship](https://www.jobs.ac.uk/job/DTP262/phd-studentship-in-soft-robotics-and-embodied-intelligence) is technically relevant but not automatically fully funded for an overseas-fee applicant. The [Surrey project](https://www.surrey.ac.uk/postgraduate/vision-speech-and-signal-processing-phd) explicitly covers both overseas tuition and the stipend, albeit with weaker SLAM fit.

**Strongest implementation lesson: field-level evidence gates.** SihengTao defines claim/source paths with independent checks, but the checker cannot verify semantic truth solely from a JSON badge or HTTP 200. Compare [official ETH employment](https://jobs.ethz.ch/job/view/JOPG_ethz_d3lDgHgDI4ewDFQ1Fb), [EPFL EDIC committee funding](https://www.epfl.ch/education/phd/edic-computer-and-communication-sciences/edic-computer-and-communication-sciences/edic-how-to-apply/) and [Oxford scholarship consideration](https://www.ox.ac.uk/admissions/graduate/courses/dphil-computer-science): they represent genuinely distinct admission/funding relations.

**Code quality and ethical risks change adoption decisions.** The PhD-Seeker source calls `eval` on scraped text and disables TLS verification for configured boards; executable code is **rejected** even though adapter ideas are transferable. Public applicant-document repositories can contain transcripts and identity scans; don't mirror. A historical Chinese handbook includes an advice to misrepresent a US address; explicitly reject. A CRM's generated outreach draft never constitutes contact or permission to send.

**Research-fit matching needs publication-level methods and formal supervisor capacity.** The Wenzi rubric helps ask rigorous alignment questions but has no performance calibration. Actual lab targets [UZH RPG, ETH RSL and Monash VL4AI](../research/supervisors/index.md) require empirical paper match, applicant-research DOI, funded role, online portal status, and field-specific eligibility before scoring fit.

## What can be integrated responsibly

Build an original **adapter → source snapshot → claim evidence → canonical vacancy → employer/current portal → international fee and salary gate → scientific publication match → authorized application state** pipeline. Track contradiction and temporal scope explicitly; preserve raw leads even if a PI is unresolved. Program-status and proof data is modeled by [additive SQLite migration](../sql/migrations/001_research_evidence.sql). Third-party code must be separately license-reviewed, tested and sandboxed; no unsafe tool or credentials are copied.

## Unresolved review work

Full listing source recrawl/precision tests, 27 further substantive repository audits, screening 353 raw names, more GitHub topic and code/maintainer searches, historical + contemporary applicant accounts from all eight target countries, 2027 scholarship funding decisions, and independent semantic source checking. Until completed, the broad systematic synthesis remains **preliminary**.
