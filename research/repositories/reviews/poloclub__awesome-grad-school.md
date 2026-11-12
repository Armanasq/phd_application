# poloclub/awesome-grad-school — deep evidence and advice-network audit

**Reviewed:** 2026-11-12  
**Source:** https://github.com/poloclub/awesome-grad-school  
**Repository ID:** 426762768  
**Pinned revision:** [7f0d5d9deac3c3e7837f51b93b22448864233c8a](https://github.com/poloclub/awesome-grad-school/commit/7f0d5d9deac3c3e7837f51b93b22448864233c8a)  
**Review state:** DEEP_REVIEW_DOCUMENTED — entire Markdown guide, contribution policy, licensing, CI and generated-TOC configuration inspected statically. Linked external articles/videos/PDFs and CI **not independently executed**.  
**Disposition:** ADAPT_ADVICE_TAXONOMY_WITH_SOURCE_LEVEL_TRUST_CLASSIFICATION.

## 1. Purpose and limits

A broad curated resource for applying to, working within and graduating from research-oriented doctoral programs. It is not an admissions database, a funded-position list, an official programme handbook, or longitudinal outcome evidence. The README is divided into application preparation, statements, recommendation letters, prospective advisor choice, general PhD life, research/paper writing and peer review, academic and industry job searches, talks, fellowship preparation, mental health/help, and lab handbooks. Its usefulness lies in organizing methods and first-person scholarly advice across a research career rather than verifying any 2026–27 application eligibility or supervisor capacity.

Evidence: [README](https://github.com/poloclub/awesome-grad-school/blob/7f0d5d9deac3c3e7837f51b93b22448864233c8a/README.md).

## 2. Information architecture and source inventory

The pinned tree has 11 files, principally a ~20 KB README, MIT license, CONTRIBUTING, Makefile and a Node/Docker DocToc workflow. The README has **159 Markdown link occurrences, 157 distinct targets**, but this count includes *internal table-of-contents anchors and the badge*: there are **129 absolute external HTTP(S) link occurrences and 127 distinct external targets**. Therefore neither number represents independently reviewed articles or verified scholarships. Its headings form a three-stage knowledge map: pre-application research fit and materials; in-program scholarship production, communication and community practices; post-PhD transitions.

Examples of source genres include individual researcher blogs, university graduate advisories, community videos, industry advice, conference tutorials, fellowship collections and lab handbook repositories. These heterogeneous genres should retain source-level authority and date metadata when imported to a research knowledge graph. Content descriptions are short pointers; most linked original documents are not reproduced or epistemically checked by the index.

## 3. Discovery, collection and maintenance workflow

The repository is a manually curated list. CONTRIBUTING instructs contributors to avoid duplicates, provide succinct descriptions, add individual suggestions by PR, place them into a relevant category and use informative commits. The GitHub `LinkChecker` action runs Markdown link checks on pushes. A separate workflow uses Docker/Yarn DocToc and auto-commits a regenerated table of contents on `main`.

This makes navigation and syntactic link upkeep more reliable than an unmaintained pastebin, but it is not a scientific evidence validator: external content can change while retaining the same URL. The linked advice has not been assessed for validity under different countries, departments, programme cycles, citizenship categories or job contract types.

Sources: [CONTRIBUTING](https://github.com/poloclub/awesome-grad-school/blob/7f0d5d9deac3c3e7837f51b93b22448864233c8a/CONTRIBUTING.md), [CI](https://github.com/poloclub/awesome-grad-school/blob/7f0d5d9deac3c3e7837f51b93b22448864233c8a/.github/workflows/ci.yml), [linkcheck config](https://github.com/poloclub/awesome-grad-school/blob/7f0d5d9deac3c3e7837f51b93b22448864233c8a/mlc_config.json), [TOC workflow](https://github.com/poloclub/awesome-grad-school/blob/7f0d5d9deac3c3e7837f51b93b22448864233c8a/.github/workflows/generate_toc.yml).

## 4. Source-level quality findings and blind spots

- **A link checker is not factual validation.** The configuration ignores Twitter links and considers statuses 403, 429, 206 and 0 in addition to 200 acceptable/alive. It cannot prove that the material behind those URLs is accessible to a new reader, endorses its label, is current, or applies to a funded international PhD.
- **Explicit dead and expired material:** the conference section annotates one first-conference advice link as “URL currently not accessible”; the fellowship section notes the Ada Lovelace Fellowship was discontinued. These are deliberate historical tips, not current grant opportunities.
- **Category contamination:** faculty job talks, postdoc/faculty searches, PhD research methods and pre-PhD statements all appear in one list. A recommender that indexes it without lifecycle-stage tags would return inapplicable advice or falsely classify a faculty fellowship as a doctoral admission.
- **Historical advice:** many linked articles are visibly dated 2014–2022 or reference past conferences. Their scholarly writing principles can remain useful, but funding procedures and selection rules should be current-cycle verified.
- **Advice source heterogeneity:** a professor's blog, social thread, academic resource center, training guide and a university's official admissions requirement do not carry equivalent authority. The README does not assign a structured trust tier or evidence confidence.
- **No career outcomes model:** anecdotes and tips do not provide a controlled sample of admissions decisions, supervisor availability, funding success rates or expected returns. The repository cannot support quantitative claims about which tactic causally improves admissions.
- **Action/CI portability:** the linked workflow uses `actions/checkout@master`, a moving ref; reproducibility depends on its upstream action state. The TOC workflow auto-commits Markdown, so an updated last commit need not indicate a human source-content verification.

All observations are static. No current link-target content, external source accessibility or specific admission result was independently checked.

## 5. Method extraction and interconnections

The guide supports an interconnected advising workflow: identify scientific fit and researcher/lab culture -> prepare field-specific research contributions in an SOP -> coordinate credible recommendation letters -> interview potential supervisors using transparent questions -> evaluate lab norms/mentorship fit -> plan fellowships and scholarly output. The following stages—paper planning, rebuttals, research novelty, reviewing, conference talks, collaboration and academic career search—are useful to estimate long-term fit but are not part of any university's legal admission criteria.

The review found a direct reference to `pliang279/awesome-phd-advice` in its “Other Grad School Advice” section, and related resources in the same link graph include researcher-website design, peer-review tutorials and group handbooks. A graph representation should deduplicate the same underlying articles across collections using canonical URL/author/title rather than counting each aggregator endorsement as independent evidence.

## 6. Reliability, privacy, licenses and verification

The repository has MIT-licensed organization-specific text and tooling; third-party linked content retains separate copyright and rights. It does not contain applicant identity, application submission receipts or private dossiers in the inspected tree. The site provides no collection timestamp per external source, immutable copy of the original, retraction ledger or editorial peer-review method for advice. Reproducing a third-party PDF, figures or full essays requires individual permission/licensing analysis. The link-check workflow and action badges were **read as configuration, not executed or treated as an attested status**.

## 7. Transfer to PhD Atlas and complementary repositories

Compared with `Swapnil-Gandhi/SoP-Template`, which is one worked written artifact, this is a navigation taxonomy of many advice sources. Compared with `pliang279/awesome-phd-advice`, its coverage includes similar early-career material but also structured subcategories for rebuttals, research-paper acceptance, conference posters, mentor practices and job search. Compared with `dxeledx/PhdInfoHub` and funding crawlers, it supplies **methods**, not executable eligibility or deadline verification.

A viable use is a source-linked research checklist with evidence-kind tags: candidate-authored accomplishments, opinionated tactics, official program requirement, financial eligibility rule, public faculty bio, and confirmed application event. Keep outbound source URLs, last-checked, copyright scope, intended geography and relevance cycle. Never promote advice to a verified funding claim or overwrite candidate-supplied profile data.

## 8. Decision, uninspected surfaces and next tests

**DEEP_REVIEW_DOCUMENTED — ADAPT navigation and advice taxonomy.** README link graph, original repository structure, license and CI/TOC/contribution rules inspected at the pinned commit. No original source articles, embedded videos, downloadable PDFs, link checker runtime, source recrawl, admissions records, applicant data, employer outreach or official 2026/27 funding verification. Further adoption requires selecting a specific advice item, opening its primary source and verifying source date/attribution and audience before relying on the conclusion.
