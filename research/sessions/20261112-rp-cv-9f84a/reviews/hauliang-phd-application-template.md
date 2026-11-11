# HauLiang/PhD-Application-Template — bilingual CV and research-plan template audit

**Checked:** 2026-11-12  
**Upstream:** https://github.com/HauLiang/PhD-Application-Template  
**Pinned revision:** [`8094b0809493e061d118b853af4733f72267f985`](https://github.com/HauLiang/PhD-Application-Template/commit/8094b0809493e061d118b853af4733f72267f985)  
**Status:** source-complete text/layout inspection for LaTeX sources, **PDFs NOT_READ** and compilation **NOT_EXECUTED**.  
**Verdict:** adapt layout/section structure carefully, not applicant claims or original wording.  
**Risk:** reused external Overleaf templates and a broad “all rights reserved” note require source-level license/provenance checking despite the Apache-2.0 LICENSE in this repository.

## 1. Scope, history, licensing and runtime contract

The complete main tree contains 16 file blobs: English academic CV (`CV/cv.tex` plus `cv.pdf`), Chinese CV (`CV_CN/cv_cn.tex` plus `cv_cn.pdf`), research-plan template (`RP/rp.tex`, `RP/structure.tex`, `RP/ref.bib`, `RP/rp.pdf`), image previews, README and Apache-2.0 LICENSE. The source is an example populated with the original candidate's achievements, references and professional contacts, not an anonymous blank template.

The README explicitly says to use **XeLaTeX**, demonstrates the TeXstudio compiler setting, attributes the CV to an external Overleaf CV article and the RP to a separate Overleaf environmental-studies template, and asks readers to inspect the license. Apache-2.0 is present; the additional README phrase “All rights are reserved by the authors” and the external provenance leave uncertainty about rights in third-party portions. Do not treat the top-level SPDX label as verified permission to copy every borrowed asset. Source links:
- [README](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/README.md), [LICENSE](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/LICENSE);
- [English CV source](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/CV/cv.tex), [Chinese CV source](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/CV_CN/cv_cn.tex);
- [Research-plan source](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/RP/rp.tex), [style/structure source](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/RP/structure.tex).

The last upstream commit is 2022-12-18; no open upstream issue or PR was returned, and no test/CI or compilation script was found in the full tree.

## 2. English and Chinese academic CV implementation

Both CV variants use `moderncv` document class, `fontawesome`, `tabularx`, `ragged2e`, `multicol`, `import`, custom tabular-entry commands and page geometry. The Chinese version additionally imports `ctex`. Both include a research-focused section structure rather than only an industry software resume:
- Research interests and educational trajectory;
- Research experience with objectives and algorithmic methods;
- Awards and honors;
- Technical skills;
- Publications and under-review work;
- Chinese variant also shows coursework and referees.

The English original presents publications with a “rank/impact factor” label and marks submissions as under review. These are **historical self-reported example statements**, not current verified bibliometrics. Reusing a CV should preserve exact author order, DOI, venue, publication status and applicant's contribution, while omitting unverified or obsolete impact-factor rankings. Under-review items must never be elevated to published.

The source has tight spacing (including large negative `\vspace` near title), manually arranged custom entries and hard-coded footer update dates. Such layout can become fragile under longer international names, many works, multilingual fonts and longer URLs. Recompile and inspect page overflows and link functionality after replacing all personal content. The source's original populated CV must never be included in the user's personal applicant profile or proof of credentials.

## 3. Research-plan structure, scientific value and gaps

`RP/rp.tex` is an academic **Research Plan** sample laid out as:
1. Introduction and related work;
2. Research objectives (three enumerated placeholders);
3. Research methodology (four enumerated placeholders);
4. Candidate experience / published research record;
5. Bibliography.

The concrete model-development and results content is intentionally a sequence of `xxx`/“Methodology 1...” placeholders. It is **not** a scientifically complete proposal; no evaluation dataset, precise hypotheses, baseline, metrics, feasibility risks, validation method, timeline or prospective host-supervisor fit is specified. The first-person candidate history is not reusable.

Useful adaptation for an actual PhD application: keep scientific motivation and coherent experience-to-plan traceability, but add:
- Defined research question and original hypothesis;
- Data source, representative benchmark, controlled baseline and success criterion;
- Risks, failure modes, ethical/privacy/IP boundaries and contingency;
- Time-bounded milestones and realistic computation/data access;
- Host laboratory/recruitment call alignment, exact specified word/page limits, and funding requirements.

The RP uses a custom boxed `pgfpages` page design and imports a separate style file. `RP/structure.tex` sets A4 page margins, font stack, mathematical and algorithm environments and optional framed boxes. Such dense decoration may be inappropriate when an institution supplies a required proposal form or strict page count. XeLaTeX requirement and user-controlled font/Chinese support should be validated per target institution.

## 4. Interconnections and transfer decision

- Compared with [CodeBoyPhilo's KG/LLM proposal](https://github.com/CodeBoyPhilo/PhD-Application): this repository is primarily *typesetting and application package structure*, whereas CodeBoyPhilo supplies actual research questions, literature positioning and staged methodology. Combining the generic strengths requires original writing; source imitation or copying personal claims is inappropriate.
- Compared with [Awesome-PhD-CV](https://github.com/LimHyungTae/Awesome-PhD-CV): both emphasize academic research, but a concise applicant-specific CV, verifiable publications and lab-fit priorities are more important than a visual template.
- For AI/robotics applicants, replace broad “skills” and journal metric labels with reproducible methods, specific engineering/research contributions, publications at verifiable status and evidence of independently executed work.
- Program portal instructions override all generic CV/Research Plan templates.

**Decision:** useful academic CV + proposal format exemplar; source-level text/template review complete; PDF rendering and license-chain reconciliation outstanding. Does **not** provide independent admission success, active opportunities or up-to-date university requirements.

## 5. Validation and privacy boundary

All four `.tex` files and README, LICENSE reference, history and file tree were inspected. Binary PDFs and image previews were enumerated but not opened; LaTeX dependencies were not installed; no XeLaTeX build or PDF QA executed; no original candidate's names, addresses, phone numbers or referee contact details are reproduced in this audit. Exact rights of upstream Overleaf components remain **NEEDS_CONFIRMATION**.
