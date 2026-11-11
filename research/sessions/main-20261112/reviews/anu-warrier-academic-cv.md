# Anu-Warrier/CV — source-pinned academic CV artifact review

- Reviewed: 2026-11-12.
- Upstream: https://github.com/Anu-Warrier/CV
- Upstream commit: [de422fd238d5acd1901072c636702cf4c8c75741](https://github.com/Anu-Warrier/CV/commit/de422fd238d5acd1901072c636702cf4c8c75741)
- Git tree SHA: `de422fd238d5acd1901072c636702cf4c8c75741`.
- Scope: complete three-entry file inventory, full README, LaTeX source structure, six visible upstream commits, repository metadata, issues and pull requests. The sample PDF was inventoried but **not visually inspected**; LaTeX was not compiled.
- Screening recommendation: `REVIEW_RECORDED / PRELIMINARY_FOCUSED` as `application_documents`, pending coordinated canonical-register update. Not a current admissions or funding evidence source.
- Runtime verification: NOT_PERFORMED.

## Purpose and actual assets

This is a static academic CV example rather than an admissions pipeline. The upstream README offers a public-use academic CV template written in Overleaf, with a PDF preview. The tree contains exactly three tracked objects: `README.md` (442 bytes), `CV_LaTeX_Overleaf_code` (16,375 bytes), and `awarrier_cv_04_2022.pdf` (83,470 bytes). The LaTeX source is a 372-line article document; no build system, dataset, parser, API, test suite, CI configuration, or funding/vacancy aggregator is present.

The author explicitly credits https://github.com/NicDuquette/CV-Template as an earlier template source. The README calls the code permissively licensed, but the inspected tree contains **no LICENSE file or SPDX grant**. Verify upstream and derivative rights before copying substantial source or typography. The source includes a person's historical academic record, not verified applicant data for another candidate.

## Document structure and implementation

The explicit heading macro organizes **Education**, **Positions Held**, **Peer-Reviewed Publications**, **Other Publications**, **Honors and Awards**, **Presentations**, **Service & Leadership**, **Skills**, and **Research Interests**. The document separates publication categories, which is a useful evidence-control pattern: peer-reviewed articles, non-peer-reviewed materials, manuscripts and other outputs should not be conflated when adapting an academic CV.

The source uses `article` at 12 points with `geometry` on US-letter paper. Layout packages include `booktabs`, `fontawesome5`, `ETbb`, `parskip`, `hanging`, `calc`, `array`, and `hyperref`; it defines `heading`, `subheading`, and `X` macros and uses tabular alignment for part of the layout. These are source observations, **not evidence that the document compiles reproducibly** with any specified TeX distribution or available fonts.

## Provenance, history, maintenance

GitHub reported six commits on 2022-05-26, ending at the pinned tree. No pull requests or issues were returned. The repository is neither an actively maintained deadline policy reference nor a validated source of admissions outcomes. The author's original statements and institutional information are historical examples; do not transfer personal claims into the applicant's own profile.

## Transfer to the PhD application program

1. Treat the CV as a **document-structure reference**. Build the candidate-specific document only from verified transcripts, publication metadata, appointments, projects, awards, datasets and accepted artifacts.
2. Maintain explicit publication state (`published`, `accepted`, `under_review`, `preprint`, `in_preparation`) and separate peer-reviewed publications from other research outputs; never infer acceptance or impact metrics.
3. Connect each section to its authoritative evidence item (DOI/publisher, official appointment letter, transcript, conference record, or project artifact). Document visual design is not a substitute for source verification.
4. For robotics, navigation, SLAM and AI research applications, emphasize attributable scientific contribution, experimental validation, benchmarks, code/artifacts and research-fit. This is a candidate-specific editorial recommendation, not information demonstrated by this upstream CV.
5. Prefer abstract sectioning principles rather than copying the individual's personal academic record. Review template-chain licensing if source code reuse is contemplated.

## Gaps and evidence status

The PDF's rendered typography, whether the LaTeX matches the PDF exactly, package compatibility, build reproducibility, rights to underlying template code, and validity of individual academic claims remain **NOT_VERIFIED**. No application was submitted, no personal document was sent, and no third-party runtime was executed.

## Pinned evidence

- [README](https://github.com/Anu-Warrier/CV/blob/de422fd238d5acd1901072c636702cf4c8c75741/README.md)
- [LaTeX source](https://github.com/Anu-Warrier/CV/blob/de422fd238d5acd1901072c636702cf4c8c75741/CV_LaTeX_Overleaf_code)
- [PDF inventory](https://github.com/Anu-Warrier/CV/blob/de422fd238d5acd1901072c636702cf4c8c75741/awarrier_cv_04_2022.pdf)
- [Pinned tree](https://github.com/Anu-Warrier/CV/tree/de422fd238d5acd1901072c636702cf4c8c75741)

This session adds a unique review artifact only. Canonical counters and generated indexes must be reconciled against current `main` in a separate consistency-checked update.
