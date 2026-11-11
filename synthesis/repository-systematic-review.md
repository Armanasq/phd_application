# Preliminary systematic mapping — global GitHub PhD admissions resources
**Date:** 2026-11-11. **Not a completed systematic review.** Scope and selection protocol in [METHODOLOGY.md](../METHODOLOGY.md). Raw discovery ≠ qualified corpus.

## Research corpus and audit boundary
12 first-page broad repository queries yielded 392 unique raw records, including false matches. Six additional code-search query families identified further projects and extreme noise; 8 direct metadata-screened exclusions are logged. 30 earlier initial individual notes remain **PRELIMINARY**, not complete deep audits. **5** full-structured evidence-linked source review files now exist: [PhD-Seeker](../research/repositories/reviews/aghababaei__phd-seeker.md), [phd-application-planner](../research/repositories/reviews/sihengtao__phd-application-planner.md), [academic-job-digest](../research/repositories/reviews/baselayerai__academic-job-digest.md), [eparrainage/phd](../research/repositories/reviews/eparrainage__phd.md), [profreach](../research/repositories/reviews/khanshaheb34__profreach.md). They are deep *static*, not independently runtime-certified reviews.

## Evidence-based taxonomy
| Class | Directly inspected examples | Defensible capability | Dominant risk |
|---|---|---|---|
| Firsthand applicant essays | gwisk, zhanglj37, womanreading7 | process and narrative examples | outcome/survivorship, US-specific practice |
| Curated source guides | pliang279, shaily99, zhijing-jin, poloclub | source discovery/citation chaining | repeated same links, stale or unverified underlying contents |
| Application material templates | LimHyungTae, Swapnil-Gandhi, vsitzmann | LaTeX academic CV and program-tailored SOP forms | plagiarism/fabricated candidate achievements, personal PDF privacy |
| Vacancy/PI scrapers | Aghababaei, ScholarshipScout, PhD-Hunter, PeiMu | basic extraction and field-PI leads | unsafe evaluation/TLS, site churn, false funded labels, inaccurate affiliations |
| Contemporary vacancy feeds | eparrainage/phd | current Atom links to boards | hidden scraper code, no financial or eligibility screening |
| Persistent research monitors | BaseLayerAI academic-job-digest | site adapter, dedup/upsert, PI enrichment, digest | US biomedical bias, TLS/schema and unauthorized email |
| Candidate planning/CRM | SihengTao planner, ProReach, zhoujasper Atlas, zxcgzx | status, program/PI entities, document management, claim references | private data exposure, ungrounded AI, missing independent confirmation |
| Prompt-only assistants | fanyi3017 agent | research workflow and authorization questions | prompts do not execute workflow or prove data correctness |

## Cross-repository dependence and canonicalization
1. [PhD-Hunter](https://github.com/you27-mohamed/PhD-Hunter) explicitly acknowledges [PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker) and [joeyism/linkedin_scraper](https://github.com/joeyism/linkedin_scraper). They are algorithmic relatives, not independent support for extraction accuracy.
2. [ScholarshipScout](https://github.com/danielhafezi/ScholarshipScout) and PhD-Seeker share ScholarshipDB and FindAPhD data targets; their “coverage” must be de-duplicated by original employer URL.
3. [pliang279](https://github.com/pliang279/awesome-phd-advice), [shaily99](https://github.com/shaily99/advice), [jedyang97](https://github.com/jedyang97/awesome-cs-phd-application-advice) and [poloclub](https://github.com/poloclub/awesome-grad-school) link overlapping CMU/Stanford admissions writing advice. Repeated link is one original source, not 4 independent observed applicant successes.
4. ProReach implements an authenticated Gemini advisor CRM. SihengTao implements claim schema/validator; PhD Atlas has comprehensive dossier/backup. These are **complementary modules**, not benchmarked competitors for a common test.
5. [eparrainage/phd](https://github.com/eparrainage/phd) is an output-only Atom feed (no generator code in inspected tree). Its [Reading robotics posting](https://www.jobs.ac.uk/job/DTP262/phd-studentship-in-soft-robotics-and-embodied-intelligence) is restricted to Home fee status; keyword relevance does not imply international financial eligibility.

## Research-methods comparison
**Supervisor search**: venue-centric methods from PeiMu retrieve authors and pages, good recall but stale HTML and name collision. A stronger hybrid requires recent papers, institution disambiguation, actual PIs and verified call, then a qualitative scientific contribution match.

**Funding**: scraper titles that contain “funded” are insufficient; source must prove salary or tuition waiver and stipend for an **international applicant**. EPFL EDIC formally funds admitted students; Oxford only provides funding *consideration* in December 2026; Monash DistRobot has an explicit open project, package and top-ranked publication requirement. That difference is the central screening layer.

**Evidence design**: SihengTao shows explicit source/claimPaths and provenance statuses, more principled than prose-only prompts. But even its checker cannot prove that model-created 'verified' claims are semantically correct. Require independent primary-source retrieval before using that label.

**Engineering trust**: PhD-Seeker has actual `eval` on scraped announcement times and disables HTTP TLS peer verification for every configured source. This materially changes the previous “adapt scraper” verdict to **reject executable code**. BaseLayerAI job-digest has weak TLS and raw database schema interpolation. ProReach controls API input and auth but still passes private context to a model; preserving only verified source IDs is essential.

## Evidence gaps / negative controls
Observed search-result false positives include “Houdini SOP” and repository-owner “PhD” prefixes. Eight were explicitly screened and excluded with reasons. Many similar raw hits are untriaged; 392 is not denominator of admitted resources. No full pagination or sample-based precision, no global recall and no saturation.

## Resulting architecture recommendation
Keep raw leads separate from independently verified opportunities. Use entity registry and source/claim database with qualified data extraction. Implement adapter→canonical job→current employer status→international funding and eligibility→recent PI papers→applicant evidence→authorization before action. Abstract ideas may be adapted with license review; **do not vendor unsafe upstream implementations**.

## Next review criteria
Screen remaining raw candidates; verify whether newly included projects pass the threshold. Audit linked source domains and upstreams, inspect substantive GitHub issues/PRs and code of each qualified project, run non-network fixtures safely, then repeat independent discovery until new qualified-yield falls.
