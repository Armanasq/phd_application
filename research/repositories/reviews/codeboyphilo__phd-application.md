# CodeBoyPhilo/PhD-Application — research-proposal method and validation audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/CodeBoyPhilo/PhD-Application | **Pinned source:** [`d60d80990b828fbcd1b03154f5ea01d81d587d6a`](https://github.com/CodeBoyPhilo/PhD-Application/commit/d60d80990b828fbcd1b03154f5ea01d81d587d6a) | **State:** DEEP_REVIEW_DOCUMENTED (static proposal source review) | **Decision:** adapt research-question → method → evaluation structure, not its unverified scientific claims as results.

## 1. Purpose and document inventory

A 2024 LaTeX PhD research proposal titled “Knowledge Graph-Augmented LLM Adaptation For Domain-Specific Question-Answering.” The 26-entry tree contains a root `main.tex`, modular `contents/abstract.tex`, `introduction.tex`, `related_works.tex`, `objectives.tex`, `methodology.tex`, `future_plan.tex`, a bibliography and explanatory figures. The repo is application/document source, not a running KG/LLM model, production agent platform, admissions pipeline or funded doctoral program list.

## 2. Problem representation and research questions

The proposal states two high-level problems with domain-adapted LLMs: knowledge gaps and hallucination. It posits external domain knowledge graphs as structured evidence but acknowledges that large KGs contain irrelevant/noisy edges and that graph representations do not naturally align with text-only LLM embeddings. It formulates three research questions:
1. Retrieve relevant subgraphs from large, noisy domain knowledge graphs.
2. Bridge structured graph and textual representation spaces.
3. Adapt general LLMs with limited supervised domain-specific labels.

This is a coherent method-oriented decomposition: retrieval selection, heterogeneous representation fusion, and low-resource transfer are independently testable axes. The proposal's statements are hypotheses, not established method outcomes.

## 3. Planned computational methods

The methodology proposes a landscape survey, joint KG/LLM knowledge representation learning and information-theoretic multimodal feature fusion. It plans domain QA evaluations beginning with MedQA-USMLE and PubMedQA, plus cross-domain tests, variable labeled-data budgets and multiple open LLM backbones.

It does not specify the eventual graph encoder, retrieval objective, precise fusion architecture, training budget, leakage prevention or statistical test in the inspected abstract/objectives/methodology sections. Such details require explicit protocol design before empirical replication.

## 4. Evaluation and scientific validity gaps

A convincing benchmark requires:
- Datasets split by question, source and graph provenance to avoid answer leakage from KG construction.
- Equal training/evaluation budgets and comparable context token budgets for retrieval-only, fine-tuning-only, KG-augmented and no-KG baselines.
- Retrieval quality measurements (support recall, relevance, citation groundedness) separate from final answer accuracy.
- Ablation of graph structure, noisy/incomplete edges, corpus coverage and modality fusion.
- Multiple seeds, confidence intervals, model and data versioning, safety/reliability assessments.
- Hallucination/error criteria measured against traceable source evidence, not a model's self-rated confidence.

The PDF proposal source contains plans, not executed experiments, actual datasets or verified state-of-the-art improvements. Do not attribute results or funded doctoral admission to it.

## 5. Writing and argument architecture

The root LaTeX document assembles abstract → introduction → related work → research objectives → methodology → multi-year work plan → references. Equations, algorithms, figures and BibLaTeX references are available for expressing a technical research case. The proposal connects prior problems, specific research questions and method families, then assesses feasibility through staged milestones.

The writing is topic-specific: directly copying the KG research framing into an inertial navigation, SLAM or robotics proposal would not demonstrate scientific fit. Reuse only the structural mapping from problem/evidence to tractable hypothesis and evaluation.

## 6. Planning and feasibility

The `future_plan.tex` allocates months 1–12 to survey/theory, 13–18 to prototype and preliminary tests, 19–29 to full implementation/robustness, 30–36 to cross-domain transfer and 37–48 to dissertation/defence. This is a conventional, internally phased roadmap rather than an institutional guarantee of a four-year offer or detailed resource plan.

The code does not present an explicit data-governance, compute budget, ethical review or supervisor work package. Proposal feasibility depends on institutional support and verified data access.

## 7. Transferable research design for PhD application

A strong application can reuse the logical frame: document a concrete failure of existing approaches, define independent discriminating hypotheses, propose a method with baseline alternatives, identify datasets and metrics, plan ablations, articulate failure modes, and map work to reproducible milestones. Explain what evidence already exists (publications/experiments) versus work merely proposed.

For robotics/SLAM, analogous questions might concern sensor noise, out-of-distribution motion, uncertainty and reproducibility; do not claim this repository proves any such method.

## 8. Source citations and validation boundary

- [Root LaTeX structure](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/main.tex)
- [Abstract](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/abstract.tex)
- [Research objectives](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/objectives.tex)
- [Methodology and benchmarks](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/methodology.tex)
- [Timeline](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/contents/future_plan.tex)
- [References source](https://github.com/CodeBoyPhilo/PhD-Application/blob/d60d80990b828fbcd1b03154f5ea01d81d587d6a/references.bib)

**DEEP_REVIEW_DOCUMENTED — static research proposal review.** LaTeX content and assembly inspected. Bibliographic claims, benchmark actual results, scientific novelty, admissions outcome, supervision commitment and applicant-specific eligibility were **NOT independently verified**; no LaTeX compilation or research model execution occurred.
