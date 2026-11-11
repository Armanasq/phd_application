# Preliminary systematic mapping of open PhD-admissions resources

**Initial mapping:** 11 November 2026; **canonical ledger reconciled:** 12 November 2026. **Not a completed systematic literature review.** This is a structured evidence mapping of public repositories and selected official admissions processes. Research questions, retrieval selection and limits: [METHODOLOGY.md](../METHODOLOGY.md).

## Corpus and evidence independence

The global discovery inventory currently contains **404 unique raw candidate names**, including irrelevant names. Direct screening has found **22 excluded** and **0 screened-in without registered review**. There are **88 dated repository assessments**: **20** detailed, eight-part-or-longer static reviews and **68** preliminary inspection notes. These are a small examined subset, not an exhaustive global sample. [Canonical status-tagged index](../research/repositories/index.md) · [Structured candidate queue](../data/github_discovery_candidates.csv) · [Full limitations](../quality/coverage-report.md).

The first eight structured investigations cover (see the canonical index for all 20):
[PhD-Seeker](../research/repositories/reviews/aghababaei__phd-seeker.md),
[evidence-aware planner](../research/repositories/reviews/sihengtao__phd-application-planner.md),
[academic-job-digest](../research/repositories/reviews/baselayerai__academic-job-digest.md),
[PhD XML feed](../research/repositories/reviews/eparrainage__phd.md),
[ProReach CRM](../research/repositories/reviews/khanshaheb34__profreach.md),
[PhD application/outreach pipeline](../research/repositories/reviews/erikpsw__phd-application-pipeline.md),
[Supervisor Fit Radar](../research/repositories/reviews/wenzi-researchlab__phd-fit-radar.md),
and [Chinese neuroscience PhD handbook](../research/repositories/reviews/brainphd-cn__handbook.md).



## Additional focused repository inspections — 11 November 2026

Twenty more source-pinned investigations have now been added across the latest two batches. These were **preliminary focused reviews when initially registered**; several additional audits have since been upgraded through source-level assessment:

- [0612Leo/phd-application-tracker](../research/repositories/reviews/0612leo__phd-application-tracker.md): local daily journal; imported JSON can inject markup through unescaped history rendering.
- [A-tavv/phd_position_tracker](../research/repositories/reviews/a-tavv__phd-position-tracker.md): Netherlands vacancy monitor; marks jobs seen before Telegram delivery and has no retryable delivery state.
- [AakashKumarMissrani/Twinly-Applications-Assistant](../research/repositories/reviews/aakashkumarmissrani__twinly-applications-assistant.md): planning documents only; no runnable implementation.
- [fengke808-hash/phd-radar](../research/repositories/reviews/fengke808-hash__phd-radar.md): personal mini-program; exposes applicant/supervisor data, uses hard-coded metrics and has an unauthenticated cloud write path.
- [bchen002/Doctoral-Supervisor-Skill](../research/repositories/reviews/bchen002__doctoral-supervisor-skill.md): useful explicit memory write-gate and session-routing design; tests are manual prompts, not executable tests.
- [mjvar/CS-PhD-Application-Tips](../research/repositories/reviews/mjvar__cs-phd-application-tips.md): qualitative US/CS applicant experience; not representative or current policy evidence.
- [abono200/phd-admissions-platform](../research/repositories/reviews/abono200__phd-admissions-platform.md): static US-CS dossiers; unsourced funding guarantees and an uncalibrated probability calculator.
- [AdewuyiDaniels/PhD-scholarship-search](../research/repositories/reviews/adewuyidaniels__phd-scholarship-search.md): fuzzy field matching over an unpinned external CSV; no funding/eligibility/deadline verification.
- [D2Simon/PhDHub](../research/repositories/reviews/d2simon__phdhub.md): broad local applicant CRM; plaintext credentials, unauthenticated network exposure and SSRF/prompt-injection concerns block public deployment.
- [DataBizex/academic-application-tracker](../research/repositories/reviews/databizex__academic-application-tracker.md): useful MIT-licensed offline workbook; fixed ranges and misleading composite scoring require correction.

At the 12 November 2026 main snapshot, the screening register records 88 reviewed repositories, 22 exclusions, 0 screened-in candidates awaiting registration and 294 untriaged candidates. Across the latest two batches, 20 additional repositories were individually inspected: 4 previously screened-in candidates and 16 untriaged candidates. The latest batch includes a five-repository duplicate-fork family. No upstream tests were executed.

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


## Additional source-level implementation lessons — 12 November 2026

- [Joky02/AcademiaReach](../research/repositories/reviews/joky02__academiareach.md) exposes useful evidence-first bilingual draft composition but the inspected send endpoints have no direct authorization/approval dependency and SMTP delivery state is not an atomic idempotent claim. Adapt only the verified-human-review workflow and test delivery safety under concurrency.
- [drPod/phd-application-tracker](../research/repositories/reviews/drpod__phd-application-tracker.md) demonstrates user-scoped Supabase queries but produces public object URLs, deletes previous files before a replacement transaction, and lacks tracked RLS-policy proof. Avoid processing private applicant documents with this storage path.
- [DianaJoseph08/phd-admissions-srm](../research/repositories/reviews/dianajoseph08__phd-admissions-srm.md) implements institutional stages and capacity gates while its inspected authentication path uses plaintext password comparison, predictable bearer tokens and public file mounting. Never copy account or upload mechanisms; no applicant DB or private documents were opened.
- [Gurudev517 academic-opportunity portal](../research/repositories/reviews/gurudev517__academic-opportunity-portal.md) disables TLS and records placeholder deadlines/contacts; [Janjs legacy MSCA scraper](../research/repositories/reviews/janjs__web-scraping-phd-positions.md) provides no 2026 vacancy/funding verification. Treat both as anti-patterns rather than live data sources.
- [zhoujasper/PhD Atlas](../research/repositories/reviews/zhoujasper__phd-atlas.md) offers source-grounded discovery and default-deny agent scopes in a large, self-hosted workspace; review finds browser local-storage HMAC is not confidentiality protection. [zxcgzx supervisor tracker](../research/repositories/reviews/zxcgzx__phd-application-tracker.md) illustrates multi-level crawling but has credential, RLS, import-schema and source-integrity concerns. Both were integrated from an independently authored source audit without modifying that session's branch.

These are source-pinned **static** findings. No third-party source tests, credential probes or current employer vacancy verification were performed. Generated counts derive from the canonical CSV index and will change as parallel sessions add verified work.

## What can be integrated responsibly

Build an original **adapter → source snapshot → claim evidence → canonical vacancy → employer/current portal → international fee and salary gate → scientific publication match → authorized application state** pipeline. Track contradiction and temporal scope explicitly; preserve raw leads even if a PI is unresolved. Program-status and proof data is modeled by [additive SQLite migration](../sql/migrations/001_research_evidence.sql). Third-party code must be separately license-reviewed, tested and sandboxed; no unsafe tool or credentials are copied.

## Unresolved review work

Full listing source recrawl/precision tests, 68 further substantive preliminary-review upgrades, screening 294 untriaged candidate names, more GitHub topic and code/maintainer searches, historical + contemporary applicant accounts from all eight target countries, 2027 scholarship funding decisions, and independent semantic source checking. Until completed, the broad systematic synthesis remains **preliminary**.
