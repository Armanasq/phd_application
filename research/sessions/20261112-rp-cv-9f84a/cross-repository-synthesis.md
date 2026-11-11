# Cross-repository synthesis — proposal, CV and admissions guidance

**Session:** 20261112-rp-cv-9f84a  
**Scope:** three independently selected UNTRIAGED candidate repositories, pinned and source-inspected 2026-11-12.

| Resource | What exists | Verified transfer | Evidence confidence |
|---|---|---|---|
| [CodeBoyPhilo/PhD-Application](reviews/codeboyphilo-phd-application.md) | Real KG+LLM research questions, bibliography, method and 48-month planned work stages in editable TeX; 2024 | Research-question decomposition and methodological dependency structure | Full narrative source inspection; no reproducible model or admission result |
| [HauLiang/PhD-Application-Template](reviews/hauliang-phd-application-template.md) | 2022 bilingual moderncv examples, Research Plan TeX with placeholders, PDFs and previews | Research CV sectioning, typed publication status, proposal document structure | Text source inspected; PDF and XeLaTeX build unverified; upstream template rights need review |
| [ZhenbangYou/University-Application--Computer-Science-Graduates-](reviews/zhenbangyou-university-application.md) | 2022 first-person admissions advice, mostly professional master's and Peking University context | Early source collection, programme selection, coherent CV/SOP workflow, referee lead time | Entire article corpus inspected; current policy and outcomes not independently corroborated |

## Key linkages

1. **Different document layers, never interchangeable:** A PhD research plan explains unresolved scientific questions; a CV proves past work and publications; an SOP explains trajectory and future fit; the live employer/admissions portal defines current eligibility, deadline and funding. Each has a separate evidence source.
2. **Research proposal must be experimentally credible:** From CodeBoyPhilo, extract a dependency chain (retrieval quality -> graph/text fusion -> data-efficiency adaptation) and supply individual baselines/metrics/risks. Do not invent completed model outcomes.
3. **LaTeX form is not content validity:** HauLiang's bilingual CV structure is useful but its 2022 bibliometrics and populated claims cannot be reused. User-specific achievements require primary evidence, no inferred publication status.
4. **Historical anecdotes are not official policy:** ZhenbangYou is mostly an MSCS account. Its 2022 admissions cycles, GPA/test assumptions, estimated yields, and recommendation-weight priorities must never populate current 2026/27 program fields.
5. **Separate source rights from layout inspiration:** CodeBoyPhilo and ZhenbangYou have no visible license; HauLiang has an Apache-2.0 file but names reused external templates and an “all rights reserved” warning. Only adopt abstract structure without copying authors' original writing or identifiable records.
6. **Provenance graph:** Proposed relations are `ADMISSIONS_WORKFLOW_CONTEXT` (ZhenbangYou) -> `DOC_STRUCTURE_EXAMPLE` (HauLiang) -> `RESEARCH_HYPOTHESIS_EXAMPLE` (CodeBoyPhilo). These are different evidence categories, **not duplicate sources** or independent validation of application success.

## Integration checklist

- [x] Pinned upstream default-branch commits, trees, history, issues, PRs and relevant text-source files for all three.
- [x] Findings documented under session-only paths, with no overwrites of concurrent agent output.
- [x] No external pages, academic benchmarks, LaTeX dependencies, applicant credentials, application submissions or recommendation materials executed/accessed.
- [x] No claims of funding, offer success or current 2026/27 admissions requirements inferred from these projects.
- [ ] Canonical `data/repositories.csv` and `data/github_discovery_candidates.csv` reconciliation **NOT PERFORMED** by this isolated session. The global counts remain those of the refreshed canonical register until an integration owner updates them.
- [ ] Full validation scripts/LaTeX compilation **NOT EXECUTED**, because the available GitHub API workflow does not provide a local checkout or installed TeX dependencies.

## Suggested canonical dispositions (proposal only)

- `CodeBoyPhilo/PhD-Application` -> `PRELIMINARY_FOCUSED`, category `application_documents`, verdict `reference`, risk `unlicensed_research_proposal_without_experimental_results`.
- `HauLiang/PhD-Application-Template` -> `PRELIMINARY_FOCUSED`, category `application_documents`, verdict `adapt`, risk `template_rights_and_unverified_compilation`.
- `ZhenbangYou/University-Application--Computer-Science-Graduates-` -> `PRELIMINARY_FOCUSED`, category `firsthand_guides`, verdict `reference`, risk `2022_ms_specific_heuristics`.

Treat these as **text-source-complete but preliminary** review records, not software deep audits or externally validated PhD admissions research. Register them only in a coordinated transaction against the latest main.