# CodeBoyPhilo/PhD-Application — source-pinned PhD proposal audit

**Checked:** 2026-11-12  
**Upstream:** https://github.com/CodeBoyPhilo/PhD-Application  
**Pinned revision:** [`d60d80990b828fbcd1b03154f5ea01d81d587d6a`](https://github.com/CodeBoyPhilo/PhD-Application/commit/d60d80990b828fbcd1b03154f5ea01d81d587d6a)  
**Status:** focused complete text-source/document audit; **NOT** an experiment, admission outcome, paper validation, bibliography fact-check or successful LaTeX build.  
**Verdict:** reference research-question and proposal-organization methods; independently rewrite and verify all specific content.  
**Risk:** proposal is aspirational and academically specific, with no benchmark outcomes or code execution; no license file identified.

## 1. Source inventory, history and reproducibility

The complete recursive tree has 26 blobs: seven directly relevant TeX files (`main.tex` and `contents/{abstract,introduction,related_works,objectives,methodology,future_plan}.tex`), a 54 KB BibLaTeX source (`references.bib`), eleven plus illustrated figures/assets, and gitignore/OS metadata. There is **no README, LICENSE, executable evaluation pipeline, test, result file, GitHub Actions workflow, or recorded application outcome** in the inspected tree. Six recent upstream commits were reviewed in GitHub history; latest 2024-09-13, editing narrative and methodology. No upstream PR or issue was listed.

The proposal's `main.tex` uses a 12pt article with `biblatex`/Biber, title page, independent chapter-like `\input` sections and author-year references. It is **a proposed research plan**, not a published scientific result. Its visual assets include drawings of knowledge graphs, prompts, RAG, KG-QA and architectures. The binary image bodies were only inventoried; figures have not been independently reproduced or scientifically validated. The TeX was not compiled and its full bibliography was not checked against publisher records.

Sources: [main.tex](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/main.tex), [abstract](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/abstract.tex), [literature review](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/related_works.tex).

## 2. Research problem, dependency graph and contributions actually proposed

**Focus:** knowledge-graph-augmented adaptation of LLMs for domain-specific question answering. The text identifies two broad failure modes: hallucination and lack of specialized knowledge; contrasts parameter fine-tuning against retrieving external knowledge; argues that irrelevant KG information and the graph/text modality gap create additional challenges.

Three research questions are explicitly traceable:
1. **RQ1 — retrieval:** find useful, question-relevant subgraphs from large/noisy KGs without misleading the language model.
2. **RQ2 — representation/fusion:** transform structured entity/relation information into language-model-compatible representations while preserving informative relations.
3. **RQ3 — data efficiency:** adapt general LLMs to specialist tasks with limited labeled domain data.

The causal dependency is important: a graph-text fusion experiment cannot be meaningfully interpreted if KG entity linking and subgraph retrieval quality are uncontrolled. Distinguish *retrieval recall/noise*, *relation preservation*, *fusion effectiveness* and *label-efficiency* with separate ablations, rather than attributing all improvement to a proposed hybrid architecture.

The literature section contrasts node-focused QAGNN, GreaseLM/Dragon and graph-prompt paths against triplet-level and contrastive learning strategies. The proposal intends “information theory based” multimodal fusion but **does not specify a formal objective, estimator, architecture, optimizer, graph sampling algorithm, or quantitative hypothesis**. These are research directions, not implemented algorithms.

Sources: [introduction](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/introduction.tex), [research questions](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/objectives.tex), [methods](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/methodology.tex), [related works](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/related_works.tex).

## 3. Planned evaluation and scientific gaps

The methodology names the biomedical QA benchmarks **MedQA-USMLE** and **PubMedQA**, envisages comparing existing baseline methods, varying labeled-data budget and testing different open-source LLM backbones and specialist domains. Those intentions are explicit. However, the checked repository has:
- No pinned dataset versions, split/contamination protocol, licensing/IRB boundaries or KG provenance;
- No model architecture or graph retrieval specification precise enough to reproduce;
- No choice of outcome metrics (e.g., correctness, calibration, factual attribution, retrieval grounding) or uncertainty reporting;
- No baseline configurations, parameter/compute parity or runtime cost budget;
- No result table, experimental artifact, trained weights or executable tests;
- No formal evaluation of KG extraction errors, missing knowledge, citation accuracy, source poisoning or clinical safety.

The proposal's rhetorical suggestion that labeled data requirements are often “one million tokens” must not be generalized as a fixed domain-adaptation requirement. Bibliography metadata in this repository was not externally verified; use official bibliographic sources before referencing any of its citations in an application.

## 4. Staged feasibility plan

The `future_plan.tex` prescribes:
- Months 1–12: coursework, literature survey, theory;
- Months 13–18: initial method prototype and benchmarks;
- Months 19–29: full model and robustness/efficiency evaluation;
- Months 30–36: generalization experiments;
- Months 37–48: finishing research and thesis.

This is a four-year **proposed** timetable, not demonstrated completion. For practical applicants, a short, phase-gated initial research proposal is preferable: define concrete hypotheses and measurable baselines in the first 3–6 months, then extend only upon empirical evidence. The original timetable is appropriate as an organization example, not an institutional funding or duration fact.

Source: [work plan](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/future_plan.tex).

## 5. Cross-repository and PhD strategy transfer

Useful interconnections to the current research program:
- **RAG/agentic medical QA:** replace vague “KG helps reasoning” with explicit entity-linking/graph-retrieval diagnostics, question-conditioned graph evidence, answer calibration and citation checks. Compare graph retrieval against SQL/full-text-only and other direct evidence retrieval; do not assume KG wins.
- **Robotics/SLAM:** general proposal pattern is “failure mode → research questions → constrained methods → baseline evaluation → milestone risks.” Do not transfer biomedical benchmarks into a navigation proposal without domain justification.
- **Admissions deliverables:** `Research Questions` articulates testable lines of work more clearly than a technology shopping list. Each question should map to a hypothesis, source of data, metric and fallback plan.
- **Source lineage:** authorship and PDF figure reuse must be handled separately from adopting generic section structure, especially since this repository has no visible LICENSE.

Decision: **focused research-proposal source audit, reference only, no admission success inference**. The proposal is distinct from live funded vacancies, verified supervisors and original publications in the global inventory.

## 6. Uninspected and validation boundary

TeX source for all six narrative sections and main document was fully inspected; the bibliography was inventoried but not line-by-line validated; images were inventoried by tree metadata; no PDF exists in this source snapshot. GitHub history, pull requests and issues were checked. No `biber`/`xelatex`/`pdflatex` compilation, independent paper checking, clinical QA benchmark or cross-source citation audit was performed. Upstream scientific claims, applicant identity and actual admissions outcome remain **UNVERIFIED**.
