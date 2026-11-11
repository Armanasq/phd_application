# Global GitHub repository intelligence

**Snapshot:** 2026-11-11 · **Audit type:** repository documentation and targeted implementation review, NOT complete execution/security audit.

- **Discovery**: 12 broad/multilingual first-page query passes produced 392 distinct candidate names after deduplication, including irrelevant matches.
- **Review**: 30 selected resources received individual, source-revision-pinned assessment records; 362 records remain UNTRIAGED.
- **Scope**: global resources, not limited to the target countries. Some highly relevant programs are discovered through non-country-specific repositories.
- **No saturation claim**: no repository-code search, deep issue chaining across all candidates, or subsequent page coverage has yet been completed.

## Reviews (all selected records)
| Repository | Class | Inspection | Verdict | Next action |
|---|---|---|---|---|
| [0xshreyash/awesome-phd-scholarships](reviews/0xshreyash--awesome-phd-scholarships.md) | funding lists | readme root | reject_as_current | BLOCK |
| [Aghababaei/PhD-Seeker](reviews/aghababaei--phd-seeker.md) | vacancy scrapers | focused code review | adapt | P1 |
| [BaseLayerAI/academic-job-digest](reviews/baselayerai--academic-job-digest.md) | job monitoring | focused code review | adapt | P1 |
| [chinasatokolo/csGraduateFellowships](reviews/chinasatokolo--csgraduatefellowships.md) | funding lists | readme root | reference | P2 |
| [DanialRamezani/PhD-Hunt](reviews/danialramezani--phd-hunt.md) | ai discovery | focused code review | adapt | P1 |
| [danielhafezi/ScholarshipScout](reviews/danielhafezi--scholarshipscout.md) | vacancy scrapers | notebook code review | reject_as_is | BLOCK |
| [fanyi3017-stack/phd-application-research-agent](reviews/fanyi3017-stack--phd-application-research-agent.md) | ai workflows | prompt review | adapt | P1 |
| [gwisk/gradguide](reviews/gwisk--gradguide.md) | firsthand guides | readme root | reference | P1 |
| [hassony2/useful-computer-vision-phd-resources](reviews/hassony2--useful-computer-vision-phd-resources.md) | research guides | focused documents | reference | P2 |
| [Iran-Open-Source/Putting-in-for-a-PhD-and-moving-abroad](reviews/iran-open-source--putting-in-for-a-phd-and-moving-abroad.md) | firsthand guides | focused documents | reference | P2 |
| [jedyang97/awesome-cs-phd-application-advice](reviews/jedyang97--awesome-cs-phd-application-advice.md) | curated guides | readme root | reference | P2 |
| [KaiserWhoLearns/CS-PhD-Application-fee-waivers](reviews/kaiserwholearns--cs-phd-application-fee-waivers.md) | funding lists | readme root | reference | P1 |
| [LimHyungTae/Awesome-PhD-CV](reviews/limhyungtae--awesome-phd-cv.md) | application documents | focused code review | adapt | P0 |
| [MaryleenAmaizu/ML-AI-Scholarships](reviews/maryleenamaizu--ml-ai-scholarships.md) | funding lists | readme sampled | reject_as_current | BLOCK |
| [mcnuttandrew/vis-phd-positions](reviews/mcnuttandrew--vis-phd-positions.md) | vacancy datasets | focused code data | reference | P2 |
| [PeiMu/findPhdPositions](reviews/peimu--findphdpositions.md) | supervisor discovery | focused code review | reference | P2 |
| [pliang279/awesome-phd-advice](reviews/pliang279--awesome-phd-advice.md) | curated guides | readme root | reference | P1 |
| [poloclub/awesome-grad-school](reviews/poloclub--awesome-grad-school.md) | curated guides | readme workflow | reference | P1 |
| [rednaxela2018/Application_Materials_For_PhD](reviews/rednaxela2018--application-materials-for-phd.md) | application documents | readme root | reject_as_template | BLOCK |
| [shaily99/advice](reviews/shaily99--advice.md) | curated guides | readme root | reference | P1 |
| [SihengTao/phd-application-planner](reviews/sihengtao--phd-application-planner.md) | research planning | focused code tests | adapt_priority | P0 |
| [Swapnil-Gandhi/SoP-Template](reviews/swapnil-gandhi--sop-template.md) | application documents | latex code review | adapt | P0 |
| [vsitzmann/phd-master-application-docs](reviews/vsitzmann--phd-master-application-docs.md) | application documents | readme only | reference | P2 |
| [womanreading7/PhD-Application-Guide](reviews/womanreading7--phd-application-guide.md) | firsthand guides | readme sampled | reference | P2 |
| [you27-mohamed/PhD-Hunter](reviews/you27-mohamed--phd-hunter.md) | vacancy scrapers | focused code review | reject_as_is | BLOCK |
| [yurtdisiphdrehberi/yurtdisiphdrehberi](reviews/yurtdisiphdrehberi--yurtdisiphdrehberi.md) | firsthand guides | readme root | reference | P2 |
| [zhanglj37/Tutorial-on-PhD-Application](reviews/zhanglj37--tutorial-on-phd-application.md) | firsthand guides | focused documents | reference | P1 |
| [zhijing-jin/nlp-phd-global-equality](reviews/zhijing-jin--nlp-phd-global-equality.md) | curated guides | focused documents | reference | P1 |
| [zhoujasper/phd-atlas](reviews/zhoujasper--phd-atlas.md) | application trackers | architecture focused | reference | P1 |
| [zxcgzx/phd-application-tracker](reviews/zxcgzx--phd-application-tracker.md) | application trackers | focused code review | reject_as_is | BLOCK |

## Highest-value methodological transfers
1. **Claim-level evidence and independent checks:** SihengTao/phd-application-planner.
2. **Source-specific, deduplicated ingestion and notification:** BaseLayerAI/academic-job-digest, with security hardening.
3. **Research-project-driven CV:** LimHyungTae/Awesome-PhD-CV; adapt research-cv, not industry ATS guidance.
4. **Technical SOP narrative:** Swapnil-Gandhi/SoP-Template (never copy author claims).
5. **Supervisor-first publication exploration:** PeiMu/findPhdPositions, but replace legacy scraping with supported academic bibliographic data.
6. **Application execution and backup domain:** zhoujasper/phd-atlas, architecture reference only.
7. **Community/admissions source chasing:** pliang279, shaily99, zhijing-jin, gwisk; deduplicate and verify at primary sources.

## Critical blockers
- Published credentials appear in source files of two tracker/scraper projects. Never copy, use or test them.
- A scholarship scraping notebook uses placeholder extraction while describing fully funded search; do not mark results funded.
- Historical scholarship tables contain observed country attribution errors and outdated dates.
- A position dataset is explicitly deprecated and covers 2024/25 applications; not an operational source.
See [failure register](failure-register.md) for precise observations and link targets.

## Inspection semantics
**README_ONLY / README_ROOT** means documentation and repo shape; **FOCUSED_CODE_REVIEW** means selected code and/or configuration files were actually read; **FOCUSED_DOCUMENTS** means selected relevant documents were read; **ARCHITECTURE_FOCUSED** means a subset of architecture docs and tree was reviewed. No verdict here implies full source audit, tests passed, legal compliance or ongoing maintenance.

The [discovery queue](../../data/github_discovery_candidates.csv) contains untriaged results. Do not infer relevance from appearance in the queue. The [reviewed register](../../data/repositories.csv) contains only resources with a dated individual review.
