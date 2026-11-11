# Full inventory coverage: 404 PhD-research GitHub repositories

**Audit date:** 2026-11-11  
**Input:** [data/github_discovery_candidates.csv](../../data/github_discovery_candidates.csv)  
**Scope:** every repository name in this inventory, not every repository available on GitHub.  
**Method:** direct upstream README.md retrieval attempt and recursive Git file-tree request for all 404; focused implementation/test inspection where relevant.  
**Runtime execution:** no upstream runtime tests executed.  
**Independent official-source verification:** not implied by these checks.

## Audit-depth distinction

Repository-level screening is now performed across the full list. This **does not mean line-by-line review of every file**. For source-rich projects with thousands of files, reading only README, trees, and selected modules is **source sampling**, not exhaustive code review. Each row explicitly identifies that distinction. A missing README is not itself a missing repository. Git tree HTTP 409 means empty Git repository; Git tree HTTP 404 remains inaccessible/unresolved.

- Inventory entries: **404**
- Source-code or test files directly retrieved and analyzed during this pass: **90** across **56** named repositories (bounded samples, not complete projects; some modules only partially analyzed)
- Previously recorded in catalog: **35** (these are not all independently validated)
- Empty Git repositories confirmed through tree retrieval: **12**
- Git tree unresolved/404: **1**
- Heuristic category counts are only navigational; do not treat them as authoritative screening verdicts.

## High-signal implementation findings

| Upstream repository | Inspected file | Source-backed finding |
|---|---|---|
| [Aghababaei/PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker) | [`phdseeker/main.py`](https://github.com/Aghababaei/PhD-Seeker/blob/HEAD/phdseeker/main.py) | Uses `eval()` while processing time expressions derived from scraped content. Unsafe for arbitrary input; replace with a non-evaluating numeric parser. |
| [Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP) | [`scraper.py`](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP/blob/HEAD/scraper.py) | Makes HTTPS requests with `verify=False`, disabling certificate verification. |
| [zxcgzx/phd-application-tracker](https://github.com/zxcgzx/phd-application-tracker) | [`crawler/database/supabase_sync.py`](https://github.com/zxcgzx/phd-application-tracker/blob/HEAD/crawler/database/supabase_sync.py) | Includes a hard-coded credential carrying a `service_role` claim. Treat as exposed, rotate/revoke; do not reuse. |
| [fsuitoal-code/phd-application-command-center](https://github.com/fsuitoal-code/phd-application-command-center) | [`backend/alembic/versions/b6a3f0e27c58_deadline_source_verification.py`](https://github.com/fsuitoal-code/phd-application-command-center/blob/HEAD/backend/alembic/versions/b6a3f0e27c58_deadline_source_verification.py) | Backfills old deadlines with `confirmed_by_program` and `needs_human_verification=false`, without new corroboration. |
| [swadhinbiswas/fundmystudy-scraper](https://github.com/swadhinbiswas/fundmystudy-scraper) | [`src/deduper.ts`](https://github.com/swadhinbiswas/fundmystudy-scraper/blob/HEAD/src/deduper.ts) | Normalizes title/provider but scopes all three lookup keys to `source`; cross-source dedup is not automatic. |
| [Ariaeimehr/PHD-Position-Finder](https://github.com/Ariaeimehr/PHD-Position-Finder) | [`src/components/ScraperSimulator.tsx`](https://github.com/Ariaeimehr/PHD-Position-Finder/blob/HEAD/src/components/ScraperSimulator.tsx) | Frontend exposes simulated execution. A separate `phd_hunter.py` contains a real ingestion implementation; UI output alone cannot validate it. |
| [centrixsol/phd-applicant](https://github.com/centrixsol/phd-applicant) | [`src/app/api/apply/route.ts`](https://github.com/centrixsol/phd-applicant/blob/HEAD/src/app/api/apply/route.ts) | Application handling identifies the account via one `USER_EMAIL` fallback; examine authentication/authorization boundaries before any multiuser reuse. |
| [D2Simon/PhDHub](https://github.com/D2Simon/PhDHub) | [`phdhub/ai_services.py`](https://github.com/D2Simon/PhDHub/blob/HEAD/phdhub/ai_services.py) | Claude connection has a default third-party proxy base URL and can configure a local HTTP proxy. Applicant content routing requires explicit privacy scrutiny. |
| [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator) | [`scrape.py`](https://github.com/NimaaaAI/Position-Aggregator/blob/HEAD/scrape.py) | Separates broad sitemap/raw-source ingestion from downstream relevance filtering and handles rate limits; transferable source-first architecture. |
| [EydlinIlya/BlueSky-PhD-jobs](https://github.com/EydlinIlya/BlueSky-PhD-jobs) | [`src/dedup.py`](https://github.com/EydlinIlya/BlueSky-PhD-jobs/blob/HEAD/src/dedup.py) | Multi-stage dedup combines canonical application URLs and text-similarity logic; social-post vacancy claims need separate official validation. |
| [mdsamhussain1996/vidyasetu-scholarship-portal](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal) | [`scripts/discover.py`](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal/blob/HEAD/scripts/discover.py) | Distinguishes expected recurring dates from last-verified dates; tests cover rollover and duplicate/scam rules. |
| [dxeledx/PhdInfoHub](https://github.com/dxeledx/PhdInfoHub) | [`apps/workbench/services/import_sources.py`](https://github.com/dxeledx/PhdInfoHub/blob/HEAD/apps/workbench/services/import_sources.py) | Includes URL-import security boundaries using pinned connections; tests separately check source revalidation and ownership. |
| [SihengTao/phd-application-planner](https://github.com/SihengTao/phd-application-planner) | [`tests/test_data_quality.py`](https://github.com/SihengTao/phd-application-planner/blob/HEAD/tests/test_data_quality.py) | Contains tests for stable IDs, evidence conflicts, duplicate records, and SSRF/redirect protections. |
| [stealth-startup-2026/scholarship-scraper](https://github.com/stealth-startup-2026/scholarship-scraper) | [`usyd/usyd_scraper.py`](https://github.com/stealth-startup-2026/scholarship-scraper/blob/HEAD/usyd/usyd_scraper.py) | Official University of Sydney JSON-feed adapter, with separate eligibility/amount extraction. Broader scholarship data is not automatically a funded PhD vacancy. |
| [Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor) | [`skills/monitor-phd-scholarships/scripts/phd_tracker.py`](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor/blob/HEAD/skills/monitor-phd-scholarships/scripts/phd_tracker.py) | Explicit deadline-precision/funding/eligibility states, private state and deterministic validation; live official-source assertions still require checking. |
| [KhanShaheb34/profreach](https://github.com/KhanShaheb34/profreach) | [`app/api/gemini/lookup/route.ts`](https://github.com/KhanShaheb34/profreach/blob/HEAD/app/api/gemini/lookup/route.ts) | AI-assisted faculty lookup uses authorization and schema validation; model-provided facts must remain source-attributed. |
| [A-tavv/phd_position_tracker](https://github.com/A-tavv/phd_position_tracker) | [`scraper.py`](https://github.com/A-tavv/phd_position_tracker/blob/HEAD/scraper.py) | Two-source Netherlands vacancy parser with timeout, retry and source reports; geographical coverage is limited. |
| [zhoujasper/phd-atlas](https://github.com/zhoujasper/phd-atlas) | [`server/admissionInsights.js`](https://github.com/zhoujasper/phd-atlas/blob/HEAD/server/admissionInsights.js) | Separates deterministic entity matching from subjective model synthesis, and explicitly handles missing public award evidence conservatively. |
| [BaseLayerAI/academic-job-digest](https://github.com/BaseLayerAI/academic-job-digest) | [`src/index.ts`](https://github.com/BaseLayerAI/academic-job-digest/blob/HEAD/src/index.ts) | Structured multi-source vacancy pipeline with database and PI enrichment; upstream browser security settings require separate remediation. |
| [yongruiyu/CS_APP_Agent](https://github.com/yongruiyu/CS_APP_Agent) | [`agent.py`](https://github.com/yongruiyu/CS_APP_Agent/blob/HEAD/agent.py) | Tool-based program fact collection and incremental section completeness; no independent demonstration of source freshness in this pass. |

## Repeated or irrelevant source families

The inventory contains repeated MIT 6S191 course clones; several copies of the Farsi *Putting in for a PhD and moving abroad* guide; repeated academic-CV template trees; repeated personal application-material repositories; multiple `21-` repositories holding only `.gitignore` or unrelated Chinese political prose; and technology names whose `PHD`/`SOP` expansions are unrelated to doctoral admissions. Repeated source content must not count as independent corroboration. Publicly accessible personal records must not be copied into applicant datasets.

## Reproducible per-repository coverage ledger

Categories in this table are **navigation hypotheses** based on direct source reconnaissance, not endorsements. `README-path + tree` records have **no current claim of source-code testing**. The prior catalog state is preserved rather than overwritten.

| # | Repository | Preliminary group | Evidence depth | Pre-existing review |
|---:|---|---|---|---|
| 1 | [0612Leo/phd-application-tracker](https://github.com/0612Leo/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 2 | [0xshreyash/awesome-phd-scholarships](https://github.com/0xshreyash/awesome-phd-scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../docs/github/reviews/0xshreyash--awesome-phd-scholarships.md) |
| 3 | [1161316199/21-](https://github.com/1161316199/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 4 | [1171340562/21-](https://github.com/1171340562/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 5 | [1262241633/21-](https://github.com/1262241633/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 6 | [17337162621254271304/21-](https://github.com/17337162621254271304/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 7 | [A-tavv/phd_position_tracker](https://github.com/A-tavv/phd_position_tracker) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 8 | [abilcode/rag_task_pnu](https://github.com/abilcode/rag_task_pnu) | `OUT_OF_SCOPE` | README-path + tree | — |
| 9 | [abolfazl-yousefi/Academic-Job-Scraper-Project](https://github.com/abolfazl-yousefi/Academic-Job-Scraper-Project) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 10 | [abono200/phd-admissions-platform](https://github.com/abono200/phd-admissions-platform) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 11 | [abuhamoud237/phd-admissions](https://github.com/abuhamoud237/phd-admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 12 | [abusanny/cv](https://github.com/abusanny/cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 13 | [abusufyanvu/6S191_MIT_DeepLearning](https://github.com/abusufyanvu/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 14 | [adamrpah/CSSMA](https://github.com/adamrpah/CSSMA) | `OUT_OF_SCOPE` | README-path + tree | — |
| 15 | [AdewuyiDaniels/PhD-scholarship-search](https://github.com/AdewuyiDaniels/PhD-scholarship-search) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 16 | [aditirajnish/scholarship_web_scraper](https://github.com/aditirajnish/scholarship_web_scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 17 | [agandony/sop-cs-kirimkirim](https://github.com/agandony/sop-cs-kirimkirim) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 18 | [Aghababaei/PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | [record](../../docs/github/reviews/aghababaei--phd-seeker.md) |
| 19 | [AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo](https://github.com/AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo) | `OUT_OF_SCOPE` | README + tree + source sample | — |
| 20 | [Akshitha-03/Automating_PhD_Group4](https://github.com/Akshitha-03/Automating_PhD_Group4) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 21 | [AlanWang610/academic-cv-scraper](https://github.com/AlanWang610/academic-cv-scraper) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 22 | [AliAIOps/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 23 | [alimaher30119-cmd/ali.ibrahim](https://github.com/alimaher30119-cmd/ali.ibrahim) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 24 | [alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/alirezazolanvari/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 25 | [alistvt/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/alistvt/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 26 | [allen9408/Web-Application](https://github.com/allen9408/Web-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 27 | [alparslancay/New-Graduated-Recruitment-Application](https://github.com/alparslancay/New-Graduated-Recruitment-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 28 | [aluminium5/ScholarshipScraper](https://github.com/aluminium5/ScholarshipScraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 29 | [AnamikaRajendran/cv](https://github.com/AnamikaRajendran/cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 30 | [ankurhcu/6S191_MIT_DeepLearning](https://github.com/ankurhcu/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 31 | [Anu-Warrier/CV](https://github.com/Anu-Warrier/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 32 | [Anubhav-01-lang/software-review-dashboard](https://github.com/Anubhav-01-lang/software-review-dashboard) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 33 | [arbitan/ScholarshipWebsite](https://github.com/arbitan/ScholarshipWebsite) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 34 | [archna1212/PHD-OPENINGS](https://github.com/archna1212/PHD-OPENINGS) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 35 | [Ariaeimehr/PHD-Position-Finder](https://github.com/Ariaeimehr/PHD-Position-Finder) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 36 | [arunrathi9/Data-Science-Scholarships](https://github.com/arunrathi9/Data-Science-Scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 37 | [aryadegari/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/aryadegari/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 38 | [Atashi1990/FundBaMa](https://github.com/Atashi1990/FundBaMa) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 39 | [atomdbc/scholarship_scraper](https://github.com/atomdbc/scholarship_scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 40 | [ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 41 | [AybalaSenaHan/GraduateThesisProject](https://github.com/AybalaSenaHan/GraduateThesisProject) | `OUT_OF_SCOPE` | README-path + tree | — |
| 42 | [ayszbd/CSM.-SOP](https://github.com/ayszbd/CSM.-SOP) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 43 | [BaseLayerAI/academic-job-digest](https://github.com/BaseLayerAI/academic-job-digest) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | [record](../../docs/github/reviews/baselayerai--academic-job-digest.md) |
| 44 | [beepboopshru/scholarship-scraper](https://github.com/beepboopshru/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 45 | [benhichem/scholarships_scraper](https://github.com/benhichem/scholarships_scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 46 | [beric7/structural_inspection_main](https://github.com/beric7/structural_inspection_main) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 47 | [BillyGareth/6S191_MIT_DeepLearning](https://github.com/BillyGareth/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 48 | [binhu02/Collection-of-advice-for-PhD-application](https://github.com/binhu02/Collection-of-advice-for-PhD-application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 49 | [bodzioney/phd-applications](https://github.com/bodzioney/phd-applications) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 50 | [BokeLu/21-](https://github.com/BokeLu/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 51 | [borekda/phd-list](https://github.com/borekda/phd-list) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 52 | [buguen/PhD](https://github.com/buguen/PhD) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 53 | [bvbvbmnb/scholarship-scraper](https://github.com/bvbvbmnb/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 54 | [calogerobra/job_portal_scraper_simple_2](https://github.com/calogerobra/job_portal_scraper_simple_2) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 55 | [centrixsol/phd-applicant](https://github.com/centrixsol/phd-applicant) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 56 | [chaohuifeng/Academic_cv_phd](https://github.com/chaohuifeng/Academic_cv_phd) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 57 | [chapkovski/hnet](https://github.com/chapkovski/hnet) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 58 | [chinasaokolo/csGraduateApps](https://github.com/chinasaokolo/csGraduateApps) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 59 | [chinasatokolo/csGraduateApps](https://github.com/chinasatokolo/csGraduateApps) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 60 | [chinasatokolo/csGraduateFellowships](https://github.com/chinasatokolo/csGraduateFellowships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../docs/github/reviews/chinasatokolo--csgraduatefellowships.md) |
| 61 | [chuyaowang/nl-phd-tracker](https://github.com/chuyaowang/nl-phd-tracker) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 62 | [cirosantilli/-21-](https://github.com/cirosantilli/-21-) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 63 | [cirosantilli/21-](https://github.com/cirosantilli/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 64 | [cirosantilli/cirosantilli](https://github.com/cirosantilli/cirosantilli) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 65 | [cirosantilli/x86-bare-metal-examples](https://github.com/cirosantilli/x86-bare-metal-examples) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 66 | [CodeBoyPhilo/PhD-Application](https://github.com/CodeBoyPhilo/PhD-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 67 | [colonket/scholarship-scraper](https://github.com/colonket/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 68 | [CSC322-Grinnell/graduate-outcomes](https://github.com/CSC322-Grinnell/graduate-outcomes) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 69 | [curieuxjy/cv](https://github.com/curieuxjy/cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 70 | [cvorland/cvorland.github.io](https://github.com/cvorland/cvorland.github.io) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 71 | [cwc09262/clements-cv](https://github.com/cwc09262/clements-cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 72 | [D2Simon/PhDHub](https://github.com/D2Simon/PhDHub) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 73 | [D4vidHuang/PhD_scanner](https://github.com/D4vidHuang/PhD_scanner) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 74 | [DanialRamezani/PhD-Hunt](https://github.com/DanialRamezani/PhD-Hunt) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | [record](../../docs/github/reviews/danialramezani--phd-hunt.md) |
| 75 | [danieldrojas/gt-bootcamp-connect](https://github.com/danieldrojas/gt-bootcamp-connect) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 76 | [danielhafezi/ScholarshipScout](https://github.com/danielhafezi/ScholarshipScout) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../docs/github/reviews/danielhafezi--scholarshipscout.md) |
| 77 | [DataBizex/academic-application-tracker](https://github.com/DataBizex/academic-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 78 | [DataBizex/academic-positions-dashboard](https://github.com/DataBizex/academic-positions-dashboard) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 79 | [davidvossel/phd](https://github.com/davidvossel/phd) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 80 | [daytime001/Bulk-Email-Sender](https://github.com/daytime001/Bulk-Email-Sender) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 81 | [dbeinhauer/cv-phd](https://github.com/dbeinhauer/cv-phd) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 82 | [ddsuhaimi/scholarship_scraper](https://github.com/ddsuhaimi/scholarship_scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 83 | [deepak0004/PhD-Admission](https://github.com/deepak0004/PhD-Admission) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 84 | [DeepanshuGautam/phd_admissions](https://github.com/DeepanshuGautam/phd_admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 85 | [DefangChen/CS_Professors](https://github.com/DefangChen/CS_Professors) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 86 | [dhcoders/JobsACUK-WebScraper](https://github.com/dhcoders/JobsACUK-WebScraper) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 87 | [DianaJoseph08/phd-admissions-srm](https://github.com/DianaJoseph08/phd-admissions-srm) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 88 | [Dieselmarble/PhD-Application](https://github.com/Dieselmarble/PhD-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 89 | [dinglhmds/Search-PhD-Positions](https://github.com/dinglhmds/Search-PhD-Positions) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 90 | [dmstr/EOL-phd5-template](https://github.com/dmstr/EOL-phd5-template) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 91 | [dmstr/phd5-app](https://github.com/dmstr/phd5-app) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 92 | [do3-173/scholarship_scraper](https://github.com/do3-173/scholarship_scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 93 | [Drkkavita/kotte-kavita](https://github.com/Drkkavita/kotte-kavita) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 94 | [drPod/phd-application-tracker](https://github.com/drPod/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 95 | [dsj96/Application_Materials_For_PhD](https://github.com/dsj96/Application_Materials_For_PhD) | `REPEATED_RESOURCE` | README-path + tree | — |
| 96 | [dukee1213/Experience](https://github.com/dukee1213/Experience) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 97 | [durant42040/cs-sop](https://github.com/durant42040/cs-sop) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 98 | [DVT/rick-and-morty-app](https://github.com/DVT/rick-and-morty-app) | `OUT_OF_SCOPE` | README-path + tree | — |
| 99 | [dzkchen/ouinfo-scraper](https://github.com/dzkchen/ouinfo-scraper) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 100 | [EdZLau/scholarship-scraper](https://github.com/EdZLau/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 101 | [ekotwidodo/awesome-phd-positions](https://github.com/ekotwidodo/awesome-phd-positions) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 102 | [ElianPetkov/Graduate](https://github.com/ElianPetkov/Graduate) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 103 | [eparrainage/phd](https://github.com/eparrainage/phd) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../research/repositories/reviews/eparrainage__phd.md) |
| 104 | [evamaxfield/phd](https://github.com/evamaxfield/phd) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 105 | [EydlinIlya/BlueSky-PhD-jobs](https://github.com/EydlinIlya/BlueSky-PhD-jobs) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 106 | [fanleibo/21-](https://github.com/fanleibo/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 107 | [fanyi3017-stack/phd-application-research-agent](https://github.com/fanyi3017-stack/phd-application-research-agent) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/fanyi3017-stack--phd-application-research-agent.md) |
| 108 | [farahmahesar215-max/farah-akhtar](https://github.com/farahmahesar215-max/farah-akhtar) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 109 | [Fatemeh-J-RUG/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/Fatemeh-J-RUG/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 110 | [Fatemeh-J/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/Fatemeh-J/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 111 | [FBIResourse/cirosantilli](https://github.com/FBIResourse/cirosantilli) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 112 | [felker/doe_csgf_applications](https://github.com/felker/doe_csgf_applications) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 113 | [fengling9874/21-](https://github.com/fengling9874/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 114 | [Fengzhongzhihan/SDU-CS-Sophomore-Material](https://github.com/Fengzhongzhihan/SDU-CS-Sophomore-Material) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 115 | [Flookkie2540/cs-sop112](https://github.com/Flookkie2540/cs-sop112) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 116 | [Foly93/MD_FromBasicsToApplication](https://github.com/Foly93/MD_FromBasicsToApplication) | `OUT_OF_SCOPE` | README-path + tree | — |
| 117 | [fsuitoal-code/phd-application-command-center](https://github.com/fsuitoal-code/phd-application-command-center) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 118 | [G410725/21-](https://github.com/G410725/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 119 | [gabrieldim/Crypto-Trading-Graduate-Thesis](https://github.com/gabrieldim/Crypto-Trading-Graduate-Thesis) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 120 | [gederajeg/phd-scholarships](https://github.com/gederajeg/phd-scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 121 | [GEGE-5/CV](https://github.com/GEGE-5/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 122 | [gethonoraryphd/PHD](https://github.com/gethonoraryphd/PHD) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 123 | [gitstudy-2020/21-](https://github.com/gitstudy-2020/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 124 | [glavrentiadis/phd_position_aegis-r](https://github.com/glavrentiadis/phd_position_aegis-r) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 125 | [GraffamSophia/SophiaG](https://github.com/GraffamSophia/SophiaG) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 126 | [GSNCunha/PHD](https://github.com/GSNCunha/PHD) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 127 | [guravshubham12/ExcelR-Coaching-Courses](https://github.com/guravshubham12/ExcelR-Coaching-Courses) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 128 | [Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP](https://github.com/Gurudev517/AI-Driven-Academic-Opportunity-Portal-Using-Web-Automation-and-NLP) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 129 | [gwisk/gradguide](https://github.com/gwisk/gradguide) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/gwisk--gradguide.md) |
| 130 | [h000072/6S191_MIT_DeepLearning](https://github.com/h000072/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 131 | [hammadshaikhha/Causal-Inference-Mastery](https://github.com/hammadshaikhha/Causal-Inference-Mastery) | `OUT_OF_SCOPE` | README-path + tree | — |
| 132 | [Hao-Starrr/Graduate-Application-for-CUHKer](https://github.com/Hao-Starrr/Graduate-Application-for-CUHKer) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 133 | [hassony2/useful-computer-vision-phd-resources](https://github.com/hassony2/useful-computer-vision-phd-resources) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/hassony2--useful-computer-vision-phd-resources.md) |
| 134 | [HauLiang/PhD-Application-Template](https://github.com/HauLiang/PhD-Application-Template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 135 | [Hazrat-Ali9/PhD-Application](https://github.com/Hazrat-Ali9/PhD-Application) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 136 | [heitorrapela/awesome-phd-internships](https://github.com/heitorrapela/awesome-phd-internships) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 137 | [HelpLee/CV-Template-for-PhD-Student](https://github.com/HelpLee/CV-Template-for-PhD-Student) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 138 | [hemanth619/phd_admissions](https://github.com/hemanth619/phd_admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 139 | [hermmolly105/Awesome-PhD-CV](https://github.com/hermmolly105/Awesome-PhD-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 140 | [heyulanKiara/django-phd-scholarship](https://github.com/heyulanKiara/django-phd-scholarship) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 141 | [highwy/Application_Materials_For_PhD](https://github.com/highwy/Application_Materials_For_PhD) | `REPEATED_RESOURCE` | README-path + tree | — |
| 142 | [houwei1228/PhD_Fit](https://github.com/houwei1228/PhD_Fit) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 143 | [hqtang02/full-scholarship-phd](https://github.com/hqtang02/full-scholarship-phd) | `TREE_NOT_FOUND` | UNAVAILABLE (Git 404) | — |
| 144 | [hrithiksagar/PhD-fellowship-grants-and-Scholarships](https://github.com/hrithiksagar/PhD-fellowship-grants-and-Scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 145 | [hxkwan/PhDStudyTimer](https://github.com/hxkwan/PhDStudyTimer) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 146 | [ianouhi17-ctrl/phd-application-workbench](https://github.com/ianouhi17-ctrl/phd-application-workbench) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 147 | [ibrar-saeed-dev/scholarship_scraper](https://github.com/ibrar-saeed-dev/scholarship_scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 148 | [improvim/CV](https://github.com/improvim/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 149 | [imranbinyounos/PhdApply](https://github.com/imranbinyounos/PhdApply) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 150 | [imsankalp/phD-application-tracker](https://github.com/imsankalp/phD-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 151 | [Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | [record](../../docs/github/reviews/iran-open-source--putting-in-for-a-phd-and-moving-abroad.md) |
| 152 | [ishaanbahl6200/scholarship-scraper](https://github.com/ishaanbahl6200/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 153 | [j3551ca/phd_referee_package](https://github.com/j3551ca/phd_referee_package) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 154 | [JaccoSu/21-](https://github.com/JaccoSu/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 155 | [jaeminsjam/CV](https://github.com/jaeminsjam/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 156 | [Janjs/Web-Scraping-PhD-positions](https://github.com/Janjs/Web-Scraping-PhD-positions) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 157 | [JaykishanJ/PhD_Finder](https://github.com/JaykishanJ/PhD_Finder) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 158 | [JDCai200/21-](https://github.com/JDCai200/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 159 | [jedyang97/awesome-cs-phd-application-advice](https://github.com/jedyang97/awesome-cs-phd-application-advice) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/jedyang97--awesome-cs-phd-application-advice.md) |
| 160 | [JIAYING-ICE/interview](https://github.com/JIAYING-ICE/interview) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 161 | [jintonic-religion/academic-cv-portfolio](https://github.com/jintonic-religion/academic-cv-portfolio) | `OUT_OF_SCOPE` | README-path + tree | — |
| 162 | [jlmw19750422-sys/phd-admission-tracker](https://github.com/jlmw19750422-sys/phd-admission-tracker) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 163 | [joel-carlson/SophCS](https://github.com/joel-carlson/SophCS) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 164 | [johnwalle/scholarship-scraper](https://github.com/johnwalle/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 165 | [Joky02/AcademiaReach](https://github.com/Joky02/AcademiaReach) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 166 | [Jose-GREEN-TECH/Phd-mentor-app](https://github.com/Jose-GREEN-TECH/Phd-mentor-app) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 167 | [jspacco/sopp-analyzer](https://github.com/jspacco/sopp-analyzer) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 168 | [JVereeckenPEOCL/Jasper-Vereecken---PhD-in-Law](https://github.com/JVereeckenPEOCL/Jasper-Vereecken---PhD-in-Law) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 169 | [K-Graduate/application](https://github.com/K-Graduate/application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 170 | [KaiserWhoLearns/CS-PhD-Application-fee-waivers](https://github.com/KaiserWhoLearns/CS-PhD-Application-fee-waivers) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/kaiserwholearns--cs-phd-application-fee-waivers.md) |
| 171 | [Karshon/21-](https://github.com/Karshon/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 172 | [KeithBH/phd-positions](https://github.com/KeithBH/phd-positions) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 173 | [Khayrulbuet13/AcademicJobScraper](https://github.com/Khayrulbuet13/AcademicJobScraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 174 | [KieraTop/KieraLi-academic-cv](https://github.com/KieraTop/KieraLi-academic-cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 175 | [Kingjose05/physapp](https://github.com/Kingjose05/physapp) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 176 | [kirankaranth1/ApplicationStatusFetcher](https://github.com/kirankaranth1/ApplicationStatusFetcher) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 177 | [knockshore/6S191_MIT_DeepLearning](https://github.com/knockshore/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 178 | [KnowMe777/scholarship-scraper](https://github.com/KnowMe777/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 179 | [knwoke/ScholarshipWebScraper](https://github.com/knwoke/ScholarshipWebScraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 180 | [kody1126/English-Academic-CV-LaTeX-Template](https://github.com/kody1126/English-Academic-CV-LaTeX-Template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 181 | [kokomomo250/Awesome-Academic-CV](https://github.com/kokomomo250/Awesome-Academic-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 182 | [kruthikanmk/PhD-Scholarship-System](https://github.com/kruthikanmk/PhD-Scholarship-System) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 183 | [ktwu01/Awesome-Academic-CV](https://github.com/ktwu01/Awesome-Academic-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 184 | [ktwugoat/Awesome-Academic-CV](https://github.com/ktwugoat/Awesome-Academic-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 185 | [kumawatvinit/Scholarship-Management-System](https://github.com/kumawatvinit/Scholarship-Management-System) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 186 | [kxy716/21-----](https://github.com/kxy716/21-----) | `SEARCH_NOISE` | README-path + tree | — |
| 187 | [labri-progress/PHYsec_positions](https://github.com/labri-progress/PHYsec_positions) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 188 | [laoxiao29/21-](https://github.com/laoxiao29/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 189 | [ledmands/education_job_scraper](https://github.com/ledmands/education_job_scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 190 | [liaofangjie/21-](https://github.com/liaofangjie/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 191 | [liber145/CV](https://github.com/liber145/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 192 | [LimHyungTae/Awesome-PhD-CV](https://github.com/LimHyungTae/Awesome-PhD-CV) | `REPEATED_RESOURCE` | README-path + tree | [record](../../docs/github/reviews/limhyungtae--awesome-phd-cv.md) |
| 193 | [linyuqi/21-](https://github.com/linyuqi/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 194 | [Lukas-Vasionis/PhD_Positions](https://github.com/Lukas-Vasionis/PhD_Positions) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 195 | [m7mdramadandx/EVA-Scholarship](https://github.com/m7mdramadandx/EVA-Scholarship) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 196 | [MagedMYoussef/international-students-scholarships](https://github.com/MagedMYoussef/international-students-scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 197 | [MahdiAmrollahi/agentic-rag-persian](https://github.com/MahdiAmrollahi/agentic-rag-persian) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 198 | [MahdiRat/phd-application-tracker](https://github.com/MahdiRat/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 199 | [marcjoos-phd/dumses-hybrid](https://github.com/marcjoos-phd/dumses-hybrid) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 200 | [marly-marly/phd-admissions](https://github.com/marly-marly/phd-admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 201 | [Martin713/21-](https://github.com/Martin713/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 202 | [maruf009sultan/PHDeploy](https://github.com/maruf009sultan/PHDeploy) | `OUT_OF_SCOPE` | README-path + tree | — |
| 203 | [MaryleenAmaizu/ML-AI-Scholarships](https://github.com/MaryleenAmaizu/ML-AI-Scholarships) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../docs/github/reviews/maryleenamaizu--ml-ai-scholarships.md) |
| 204 | [MasonEdgar/DCT-Image-Steganography](https://github.com/MasonEdgar/DCT-Image-Steganography) | `OUT_OF_SCOPE` | README-path + tree | — |
| 205 | [mathieubray/JobScraper](https://github.com/mathieubray/JobScraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 206 | [mcnuttandrew/vis-phd-positions](https://github.com/mcnuttandrew/vis-phd-positions) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | [record](../../docs/github/reviews/mcnuttandrew--vis-phd-positions.md) |
| 207 | [mdsamhussain1996/vidyasetu-scholarship-portal](https://github.com/mdsamhussain1996/vidyasetu-scholarship-portal) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 208 | [mdsazzathossain1/GradResearch_AI](https://github.com/mdsazzathossain1/GradResearch_AI) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 209 | [merlick-netsi/netsi-phd-admissions-review](https://github.com/merlick-netsi/netsi-phd-admissions-review) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 210 | [mgoar/mtt-phd-filter](https://github.com/mgoar/mtt-phd-filter) | `OUT_OF_SCOPE` | README-path + tree | — |
| 211 | [Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor](https://github.com/Mhrnqaruni/ai-agent-skill-phd-scholarship-monitor) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 212 | [Michael110/Sopra12](https://github.com/Michael110/Sopra12) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 213 | [Michael110/Sopra2012](https://github.com/Michael110/Sopra2012) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 214 | [michaellennox/jobber](https://github.com/michaellennox/jobber) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 215 | [Mohamed-2030-M/scholarship-scraper](https://github.com/Mohamed-2030-M/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 216 | [monees007/phd_application_tracker](https://github.com/monees007/phd_application_tracker) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 217 | [MonikaTargosz/GraduateWorkANC](https://github.com/MonikaTargosz/GraduateWorkANC) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 218 | [MuhammadHammad26/ScholarshipScraper](https://github.com/MuhammadHammad26/ScholarshipScraper) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 219 | [mukesh14149/PhD-Admissions-Portal](https://github.com/mukesh14149/PhD-Admissions-Portal) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 220 | [muthyalanikhil/SimplySiamApplication](https://github.com/muthyalanikhil/SimplySiamApplication) | `OUT_OF_SCOPE` | README-path + tree | — |
| 221 | [n4t3rusch/ScholarshipWebScraper](https://github.com/n4t3rusch/ScholarshipWebScraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 222 | [NaichuanLuo/PhDAdmission](https://github.com/NaichuanLuo/PhDAdmission) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 223 | [natestemen/gradapps](https://github.com/natestemen/gradapps) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 224 | [NaughtFound/Go2Phd](https://github.com/NaughtFound/Go2Phd) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 225 | [NegarMirgati/6S191_MIT_DeepLearning](https://github.com/NegarMirgati/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 226 | [neuronalX/phd-and-postdoc-positions](https://github.com/neuronalX/phd-and-postdoc-positions) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 227 | [Nikhil-Rao20/phdbench](https://github.com/Nikhil-Rao20/phdbench) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 228 | [Nikhil9989/nikhil-portfolio](https://github.com/Nikhil9989/nikhil-portfolio) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 229 | [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 230 | [nishanchettri/PhD-positions-electronic-engineering](https://github.com/nishanchettri/PhD-positions-electronic-engineering) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 231 | [NoahH273/Scholarship-Scraper](https://github.com/NoahH273/Scholarship-Scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 232 | [nocilladoluis616-a11y/scholarships_scraper](https://github.com/nocilladoluis616-a11y/scholarships_scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 233 | [NoorMohammadTalukder/usa-masters-phd-scholarship-guide](https://github.com/NoorMohammadTalukder/usa-masters-phd-scholarship-guide) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 234 | [nurarif-png/SOP-CS-SOP-REFUND](https://github.com/nurarif-png/SOP-CS-SOP-REFUND) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 235 | [onlynayan/academic-cv-latex-template](https://github.com/onlynayan/academic-cv-latex-template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 236 | [OnRush1226/21-](https://github.com/OnRush1226/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 237 | [OpenSIST/OpenSIST.github.io](https://github.com/OpenSIST/OpenSIST.github.io) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 238 | [Orangeibro/CV](https://github.com/Orangeibro/CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 239 | [owenlikecoding/scholarship-scraper](https://github.com/owenlikecoding/scholarship-scraper) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 240 | [owenlikecoding/scholarship-scraper1](https://github.com/owenlikecoding/scholarship-scraper1) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 241 | [Panda-369/21-](https://github.com/Panda-369/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 242 | [PankidT/phd_tracker](https://github.com/PankidT/phd_tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 243 | [Parth-360/ACADEMIC-JOB-Scraper](https://github.com/Parth-360/ACADEMIC-JOB-Scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 244 | [ParthZanwar01/scholarship-scraper](https://github.com/ParthZanwar01/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 245 | [patsalvatore-draftly/scholarship-scraper](https://github.com/patsalvatore-draftly/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 246 | [PeiMu/findPhdPositions](https://github.com/PeiMu/findPhdPositions) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | [record](../../docs/github/reviews/peimu--findphdpositions.md) |
| 247 | [PhD-5/Hook_iOS_HTTP-s](https://github.com/PhD-5/Hook_iOS_HTTP-s) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 248 | [PhD-5/SSLWriteHook](https://github.com/PhD-5/SSLWriteHook) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 249 | [phd-cs/Search-Algorithms](https://github.com/phd-cs/Search-Algorithms) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 250 | [Philosohirinism/phd-tracker](https://github.com/Philosohirinism/phd-tracker) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 251 | [physical10086/phd-application-tracker](https://github.com/physical10086/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 252 | [pierrelux/rlbook](https://github.com/pierrelux/rlbook) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 253 | [pliang279/awesome-phd-advice](https://github.com/pliang279/awesome-phd-advice) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/pliang279--awesome-phd-advice.md) |
| 254 | [poloclub/awesome-grad-school](https://github.com/poloclub/awesome-grad-school) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/poloclub--awesome-grad-school.md) |
| 255 | [PremKumarKollabathula/CS396H-Support-Hand-off](https://github.com/PremKumarKollabathula/CS396H-Support-Hand-off) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 256 | [Prernamishra08/6S191_MIT_DeepLearning](https://github.com/Prernamishra08/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 257 | [psrana/Internation-Scholarships-for-UG-PG-PhD-students](https://github.com/psrana/Internation-Scholarships-for-UG-PG-PhD-students) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 258 | [pstone22/PhD](https://github.com/pstone22/PhD) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 259 | [psyho/ai-job-scraper](https://github.com/psyho/ai-job-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 260 | [pungkiilham/scholarship_master-phd](https://github.com/pungkiilham/scholarship_master-phd) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 261 | [PurpleKay/21-](https://github.com/PurpleKay/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 262 | [putrosm/scholarship-ummanitarian](https://github.com/putrosm/scholarship-ummanitarian) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 263 | [Rafnuss-PhD/ERT-surface-configuration](https://github.com/Rafnuss-PhD/ERT-surface-configuration) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 264 | [raganmd/touchdesigner-sop-points-to-csv](https://github.com/raganmd/touchdesigner-sop-points-to-csv) | `OUT_OF_SCOPE` | README-path + tree | — |
| 265 | [RahulShastri003/application-tracker](https://github.com/RahulShastri003/application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 266 | [randyob/csi_ops](https://github.com/randyob/csi_ops) | `OUT_OF_SCOPE` | README-path + tree | — |
| 267 | [ratulsaha2021/scholarship-agent](https://github.com/ratulsaha2021/scholarship-agent) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 268 | [RaveeshM/Scholarship-Web-Scraper](https://github.com/RaveeshM/Scholarship-Web-Scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 269 | [ravishchawla/GraduateRecommendationSystem](https://github.com/ravishchawla/GraduateRecommendationSystem) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 270 | [realrezi/Medical-PhD-Scraper](https://github.com/realrezi/Medical-PhD-Scraper) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 271 | [rednaxela2018/Application_Materials_For_PhD](https://github.com/rednaxela2018/Application_Materials_For_PhD) | `REPEATED_RESOURCE` | README-path + tree | [record](../../docs/github/reviews/rednaxela2018--application-materials-for-phd.md) |
| 272 | [Rehmanjeff/scrape-phd-positions](https://github.com/Rehmanjeff/scrape-phd-positions) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 273 | [renzoe/positions_internships_phd_postdoc](https://github.com/renzoe/positions_internships_phd_postdoc) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 274 | [repalash/PhD-Portal](https://github.com/repalash/PhD-Portal) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 275 | [restatedev/restate](https://github.com/restatedev/restate) | `OUT_OF_SCOPE` | README-path + tree | — |
| 276 | [RheoDesign/AAVS-Beijing](https://github.com/RheoDesign/AAVS-Beijing) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 277 | [Richard0047/aftcs](https://github.com/Richard0047/aftcs) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 278 | [rjalfa/PhDAdmission](https://github.com/rjalfa/PhDAdmission) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 279 | [royrada/scholarship-scraper](https://github.com/royrada/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 280 | [Rubaid-Ahmed/phd-tracker](https://github.com/Rubaid-Ahmed/phd-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 281 | [Ruib2021/6S191_MIT_DeepLearning](https://github.com/Ruib2021/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 282 | [RZFan525/NLP-PhD-Application-In-The-World](https://github.com/RZFan525/NLP-PhD-Application-In-The-World) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 283 | [s-lion-h/21-](https://github.com/s-lion-h/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 284 | [sainathss97/6S191_MIT_DeepLearning](https://github.com/sainathss97/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 285 | [saiPraveenMeda/phdAdmissions2019](https://github.com/saiPraveenMeda/phdAdmissions2019) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 286 | [salmanmaq/academic-cv-template](https://github.com/salmanmaq/academic-cv-template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 287 | [Samaritan735/Samaritan-purse-scholarship-](https://github.com/Samaritan735/Samaritan-purse-scholarship-) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 288 | [Scholars4Scholars/ScholarshipScraper](https://github.com/Scholars4Scholars/ScholarshipScraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 289 | [sci-freak/phd-tracker](https://github.com/sci-freak/phd-tracker) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 290 | [seanxuu/PhD-Seeker](https://github.com/seanxuu/PhD-Seeker) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 291 | [Sekilloda/FindMeAPhD](https://github.com/Sekilloda/FindMeAPhD) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 292 | [serdark/academic-jobs-scraper](https://github.com/serdark/academic-jobs-scraper) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 293 | [shahabkhan9380900/shahab-khan-academic-cv](https://github.com/shahabkhan9380900/shahab-khan-academic-cv) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 294 | [ShahriarAbir86/higher-study-analysis-skill](https://github.com/ShahriarAbir86/higher-study-analysis-skill) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 295 | [shaily99/advice](https://github.com/shaily99/advice) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/shaily99--advice.md) |
| 296 | [shakirul360/Awesome-PhD-CV](https://github.com/shakirul360/Awesome-PhD-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 297 | [shankar-taladra/Awesome-PhD-CV](https://github.com/shankar-taladra/Awesome-PhD-CV) | `REPEATED_RESOURCE` | README-path + tree | — |
| 298 | [shindeswapnil2000-svg/PhD-Tracker.](https://github.com/shindeswapnil2000-svg/PhD-Tracker.) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 299 | [ShowStopperTheSecond/Putting-in-for-a-PhD-and-moving-abroad](https://github.com/ShowStopperTheSecond/Putting-in-for-a-PhD-and-moving-abroad) | `REPEATED_RESOURCE` | README-path + tree | — |
| 300 | [shuaiwang88/Visualization-Scholarship-recommendation-system-at-a-college](https://github.com/shuaiwang88/Visualization-Scholarship-recommendation-system-at-a-college) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 301 | [shubhamGoswami/Phd](https://github.com/shubhamGoswami/Phd) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 302 | [shuijiaolou/cirosantilli](https://github.com/shuijiaolou/cirosantilli) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 303 | [SihengTao/phd-application-planner](https://github.com/SihengTao/phd-application-planner) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | [record](../../docs/github/reviews/sihengtao--phd-application-planner.md) |
| 304 | [sil24040/cse341-sophiesilveira1](https://github.com/sil24040/cse341-sophiesilveira1) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 305 | [sinass/graduate](https://github.com/sinass/graduate) | `OUT_OF_SCOPE` | README-path + tree | — |
| 306 | [siyahalp-prog/scholarship-scraper](https://github.com/siyahalp-prog/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 307 | [sjyttkl/21-](https://github.com/sjyttkl/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 308 | [SKWCTS/Kb_CSI](https://github.com/SKWCTS/Kb_CSI) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 309 | [SophiaRonquillo/SophiaRonquillo.github.io](https://github.com/SophiaRonquillo/SophiaRonquillo.github.io) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 310 | [SophieTestingClassroom/sophietestingclassroom-classroom-csvidtest-basics-of-git-test-github-starter-course](https://github.com/SophieTestingClassroom/sophietestingclassroom-classroom-csvidtest-basics-of-git-test-github-starter-course) | `OUT_OF_SCOPE` | README-path + tree | — |
| 311 | [sqykonwnothing/GDIIST-Admissions-2026](https://github.com/sqykonwnothing/GDIIST-Admissions-2026) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 312 | [sscardapane/tensorflow-for-ict-applications](https://github.com/sscardapane/tensorflow-for-ict-applications) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 313 | [ssine/willow](https://github.com/ssine/willow) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 314 | [sssail/academic-CV](https://github.com/sssail/academic-CV) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 315 | [stealth-startup-2026/scholarship-scraper](https://github.com/stealth-startup-2026/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 316 | [stevanoryan/scholarship-atlas](https://github.com/stevanoryan/scholarship-atlas) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 317 | [StudentTraineeCenter/chord-seq-ai-app](https://github.com/StudentTraineeCenter/chord-seq-ai-app) | `OUT_OF_SCOPE` | README-path + tree | — |
| 318 | [Sujan078BCT/Phd-Progress-Tracking-Application](https://github.com/Sujan078BCT/Phd-Progress-Tracking-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 319 | [sunjieyi/cirosantilli](https://github.com/sunjieyi/cirosantilli) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 320 | [sushil3710/PHD_Admission_Portal](https://github.com/sushil3710/PHD_Admission_Portal) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 321 | [swadhinbiswas/fundmystudy-scraper](https://github.com/swadhinbiswas/fundmystudy-scraper) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 322 | [Swapnil-Gandhi/SoP-Template](https://github.com/Swapnil-Gandhi/SoP-Template) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/swapnil-gandhi--sop-template.md) |
| 323 | [syedpeera/Phd-Admissions-NITPY](https://github.com/syedpeera/Phd-Admissions-NITPY) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 324 | [syfantid/Greek-CS-Student-Opportunities](https://github.com/syfantid/Greek-CS-Student-Opportunities) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 325 | [TahaM1/ScholarshipScraper](https://github.com/TahaM1/ScholarshipScraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 326 | [TalehMalikov/phd-application-tracker](https://github.com/TalehMalikov/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 327 | [Tang-heng-zhi/21-](https://github.com/Tang-heng-zhi/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 328 | [tarun14110/system-for-PhD-Admissions](https://github.com/tarun14110/system-for-PhD-Admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 329 | [tasseff/grfp](https://github.com/tasseff/grfp) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 330 | [temple-geography/gis-application-development](https://github.com/temple-geography/gis-application-development) | `OUT_OF_SCOPE` | README-path + tree | — |
| 331 | [theflyingrahul/fastai](https://github.com/theflyingrahul/fastai) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 332 | [TIYDC/iron-jobs](https://github.com/TIYDC/iron-jobs) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 333 | [tomjackson-tech/graduate](https://github.com/tomjackson-tech/graduate) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 334 | [TSTS09/Grad-Admission-Agent](https://github.com/TSTS09/Grad-Admission-Agent) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 335 | [ttvd/houdini-sop-attribute-csv-export](https://github.com/ttvd/houdini-sop-attribute-csv-export) | `OUT_OF_SCOPE` | README-path + tree | — |
| 336 | [Tyin-nn/phd-application-manager](https://github.com/Tyin-nn/phd-application-manager) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 337 | [tzsh1007/6S191_MIT_DeepLearning](https://github.com/tzsh1007/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 338 | [uan021112/personal-academic-cv-template](https://github.com/uan021112/personal-academic-cv-template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 339 | [ujjwal-kanodia/ap-project](https://github.com/ujjwal-kanodia/ap-project) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 340 | [Ujjwal21293/PhD-SOP-](https://github.com/Ujjwal21293/PhD-SOP-) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 341 | [ummanitarian/scholarship-ummanitarian](https://github.com/ummanitarian/scholarship-ummanitarian) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 342 | [Upsjyq/6S191_MIT_DeepLearning](https://github.com/Upsjyq/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 343 | [Usaid786467/Global-PhD-Scholarship-Finder-Application-Automator](https://github.com/Usaid786467/Global-PhD-Scholarship-Finder-Application-Automator) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 344 | [ut666/VolViewer](https://github.com/ut666/VolViewer) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 345 | [vaidhyesh1/scholarship-scraper](https://github.com/vaidhyesh1/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 346 | [varunj/PhD-Admissions](https://github.com/varunj/PhD-Admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 347 | [VenkatSBitra/phd-application-tracker](https://github.com/VenkatSBitra/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 348 | [vishal872002/PhD-admission](https://github.com/vishal872002/PhD-admission) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 349 | [VLazorykOOP/csharplab1-SoproniukAnna](https://github.com/VLazorykOOP/csharplab1-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 350 | [VLazorykOOP/csharplab10-SoproniukAnna](https://github.com/VLazorykOOP/csharplab10-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 351 | [VLazorykOOP/csharplab2-SoproniukAnna](https://github.com/VLazorykOOP/csharplab2-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 352 | [VLazorykOOP/csharplab3-SoproniukAnna](https://github.com/VLazorykOOP/csharplab3-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 353 | [VLazorykOOP/csharplab4-SoproniukAnna](https://github.com/VLazorykOOP/csharplab4-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 354 | [VLazorykOOP/csharplab6-SoproniukAnna](https://github.com/VLazorykOOP/csharplab6-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 355 | [VLazorykOOP/csharplab7-SoproniukAnna](https://github.com/VLazorykOOP/csharplab7-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 356 | [VLazorykOOP/csharplab8-SoproniukAnna](https://github.com/VLazorykOOP/csharplab8-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 357 | [VLazorykOOP/csharplab9-SoproniukAnna](https://github.com/VLazorykOOP/csharplab9-SoproniukAnna) | `OUT_OF_SCOPE` | README-path + tree | — |
| 358 | [vsitzmann/phd-master-application-docs](https://github.com/vsitzmann/phd-master-application-docs) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/vsitzmann--phd-master-application-docs.md) |
| 359 | [vsvarapriya/phd_admissions_portal](https://github.com/vsvarapriya/phd_admissions_portal) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 360 | [WagnerJon/application-atlas](https://github.com/WagnerJon/application-atlas) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 361 | [wangdepin/Application_Materials_For_PhD](https://github.com/wangdepin/Application_Materials_For_PhD) | `REPEATED_RESOURCE` | README-path + tree | — |
| 362 | [wijayantoap/scholarship-scraper](https://github.com/wijayantoap/scholarship-scraper) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 363 | [womanreading7/PhD-Application-Guide](https://github.com/womanreading7/PhD-Application-Guide) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/womanreading7--phd-application-guide.md) |
| 364 | [wonyly13/phd-application-prep](https://github.com/wonyly13/phd-application-prep) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 365 | [wukun2/sunyijie-phd-application](https://github.com/wukun2/sunyijie-phd-application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 366 | [Wuziyi616/Graduate_Application](https://github.com/Wuziyi616/Graduate_Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 367 | [xcreeperz/HFUT_CS_Sophomore](https://github.com/xcreeperz/HFUT_CS_Sophomore) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 368 | [xujingchen1996/research-app-toolkit](https://github.com/xujingchen1996/research-app-toolkit) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 369 | [xzxLeslie/phd-2027-admissions](https://github.com/xzxLeslie/phd-2027-admissions) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | — |
| 370 | [yanyuwei110/21-](https://github.com/yanyuwei110/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 371 | [yazabat/6S191_MIT_DeepLearning](https://github.com/yazabat/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 372 | [Yelk11/scholarship_scraper](https://github.com/Yelk11/scholarship_scraper) | `DISCOVERY_OR_GUIDANCE` | README + tree + source sample | — |
| 373 | [Yi-Lynn/cv-latex-template](https://github.com/Yi-Lynn/cv-latex-template) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 374 | [yi212212/6S191_MIT_DeepLearning](https://github.com/yi212212/6S191_MIT_DeepLearning) | `OUT_OF_SCOPE` | README-path + tree | — |
| 375 | [yiluyounizxx110/21-](https://github.com/yiluyounizxx110/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 376 | [yj-w-03/XMU-CS-sophomore-year](https://github.com/yj-w-03/XMU-CS-sophomore-year) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 377 | [yongruiyu/CS_APP_Agent](https://github.com/yongruiyu/CS_APP_Agent) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 378 | [yongsen/research_proposal](https://github.com/yongsen/research_proposal) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 379 | [you27-mohamed/PhD-Hunter](https://github.com/you27-mohamed/PhD-Hunter) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../docs/github/reviews/you27-mohamed--phd-hunter.md) |
| 380 | [yurtdisiphdrehberi/yurtdisiphdrehberi](https://github.com/yurtdisiphdrehberi/yurtdisiphdrehberi) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/yurtdisiphdrehberi--yurtdisiphdrehberi.md) |
| 381 | [zainebmb/ETSProgtest](https://github.com/zainebmb/ETSProgtest) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 382 | [zaohmeing/21-](https://github.com/zaohmeing/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 383 | [zarif98sjs/how-not-to-do-phd-application](https://github.com/zarif98sjs/how-not-to-do-phd-application) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 384 | [zhanglj37/Tutorial-on-PhD-Application](https://github.com/zhanglj37/Tutorial-on-PhD-Application) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../docs/github/reviews/zhanglj37--tutorial-on-phd-application.md) |
| 385 | [ZhangPeng123456aabb/21-](https://github.com/ZhangPeng123456aabb/21-) | `SEARCH_NOISE` | README-path + tree | — |
| 386 | [zhaohmng-outlook-com/21-](https://github.com/zhaohmng-outlook-com/21-) | `EMPTY_REPOSITORY` | EMPTY (Git 409) | — |
| 387 | [ZhenbangYou/University-Application--Computer-Science-Graduates-](https://github.com/ZhenbangYou/University-Application--Computer-Science-Graduates-) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 388 | [zhijing-jin/nlp-phd-global-equality](https://github.com/zhijing-jin/nlp-phd-global-equality) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../docs/github/reviews/zhijing-jin--nlp-phd-global-equality.md) |
| 389 | [zhoujasper/phd-atlas](https://github.com/zhoujasper/phd-atlas) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | [record](../../docs/github/reviews/zhoujasper--phd-atlas.md) |
| 390 | [zll-hust/Business2CEEPhD](https://github.com/zll-hust/Business2CEEPhD) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 391 | [zohairahmedai/uestc-scholarship](https://github.com/zohairahmedai/uestc-scholarship) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | — |
| 392 | [zxcgzx/phd-application-tracker](https://github.com/zxcgzx/phd-application-tracker) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | [record](../../docs/github/reviews/zxcgzx--phd-application-tracker.md) |
| 393 | [KhanShaheb34/profreach](https://github.com/KhanShaheb34/profreach) | `APPLICATION_OR_MATERIALS` | README + tree + source sample | [record](../../research/repositories/reviews/khanshaheb34__profreach.md) |
| 394 | [simitii/CS-Grad-School-Applications-Reading-List](https://github.com/simitii/CS-Grad-School-Applications-Reading-List) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 395 | [siddu1998/Graduate-Admissions](https://github.com/siddu1998/Graduate-Admissions) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 396 | [AakashKumarMissrani/Twinly-Applications-Assistant-](https://github.com/AakashKumarMissrani/Twinly-Applications-Assistant-) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 397 | [erikpsw/phd-application-pipeline](https://github.com/erikpsw/phd-application-pipeline) | `APPLICATION_OR_MATERIALS` | README-path + tree | [record](../../research/repositories/reviews/erikpsw__phd-application-pipeline.md) |
| 398 | [wenzi-researchlab/phd-fit-radar](https://github.com/wenzi-researchlab/phd-fit-radar) | `DISCOVERY_OR_GUIDANCE` | README-path + tree | [record](../../research/repositories/reviews/wenzi-researchlab__phd-fit-radar.md) |
| 399 | [BrainPhD-CN/handbook](https://github.com/BrainPhD-CN/handbook) | `NEEDS_TARGETED_REVIEW` | README-path + tree | [record](../../research/repositories/reviews/brainphd-cn__handbook.md) |
| 400 | [fengke808-hash/phd-radar](https://github.com/fengke808-hash/phd-radar) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |
| 401 | [dxeledx/PhdInfoHub](https://github.com/dxeledx/PhdInfoHub) | `NEEDS_TARGETED_REVIEW` | README + tree + source sample | — |
| 402 | [bchen002/Doctoral-Supervisor-Skill](https://github.com/bchen002/Doctoral-Supervisor-Skill) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 403 | [mjvar/CS-PhD-Application-Tips](https://github.com/mjvar/CS-PhD-Application-Tips) | `APPLICATION_OR_MATERIALS` | README-path + tree | — |
| 404 | [GuangLun2000/PhD-app-tutorial](https://github.com/GuangLun2000/PhD-app-tutorial) | `NEEDS_TARGETED_REVIEW` | README-path + tree | — |

## Limitations and next verification steps

This ledger documents all 404 upstream identities, their README-path investigation and their Git tree investigation; it does **not** claim the 404 full software projects were all exhaustively read. Source code reviews are targeted at admissions and research intelligence workflows. Large unrelated scientific/software projects were excluded from deep inspection only after source-level screening. Even well-designed projects require a pinned commit, dependency validation, runtime tests, network boundary checks, and fresh official-source corroboration before production reuse.

External repos and their live vacancy claims may change after the inspection date. No external repository was modified, application submitted, contact made, or upstream code executed. This document is a static evidence ledger, not a live admissions database.
