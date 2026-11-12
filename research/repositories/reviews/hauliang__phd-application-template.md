# HauLiang/PhD-Application-Template — LaTeX CV/research-plan source audit

**Review date:** 2026-11-12 | **Upstream:** https://github.com/HauLiang/PhD-Application-Template | **Pinned revision:** [`8094b0809493e061d118b853af4733f72267f985`](https://github.com/HauLiang/PhD-Application-Template/commit/8094b0809493e061d118b853af4733f72267f985) | **State:** DEEP_REVIEW_DOCUMENTED (LaTeX source review, compilation not tested) | **Verdict:** adapt typesetting and research-plan framing with attribution; replace all example personal content.

## 1. Scope and document assets

A 2022 PhD application document repository containing an English academic CV, Chinese CV and research plan as LaTeX source, PDF renders, preview PNGs, bibliography and Apache-2.0 license. The default-branch tree contains 19 entries. The README directs users to XeLaTeX compilation and attributes the CV and proposal templates to other Overleaf sources. This is an editable writing artifact, not a current scholarship opportunity, student application API, or verified acceptance-outcome dataset.

## 2. CV source architecture

`CV/cv.tex` uses ModernCV with `banking` style, customizable color, a compact two-column header, bespoke `customcventry` and `customcvproject` macros, research interests, education, awards, projects and outputs. The use of `moderncv`, Font Awesome, geometry, custom tables and page spacing offers a practical modular academic CV example.

The published source contains the original example applicant's contact details and academic history. Do not reuse the sample identity, achievements or publication assertions. Replace them with independently verified personal facts before compiling a private applicant CV.

## 3. Research-plan source architecture

`RP/rp.tex` assembles a title, introduction, related work, research objectives, methodology, candidate experience and bibliography. `RP/structure.tex` defines A4 page geometry, packages for math/algorithms/listings, fonts and framed environments. `RP/ref.bib` contains cited references, while the main RP includes substantial placeholder text and topic-specific applicant history.

The proposal template helps structure argument, but placeholders like “Methodology 1” and “Objective 1” are not scientifically complete research questions. The candidate-experience section must be rewritten with accurate and current outputs. The source does not automatically enforce institution-specific word counts, formatting or CV requirements.

## 4. Bilingual and portability limits

Both `CV/cv.tex` and `CV_CN/cv_cn.tex` are provided, facilitating bilingual document drafting. However Chinese and English application variants require institution-specific source terminology, degree equivalence and name representation. XeLaTeX dependencies and historical Font Awesome/ModernCV macros may vary across environments; reproducible compilation, font fallback and bibliography generation were not tested here.

The PNG/PDF previews demonstrate an intended layout, but this audit did not open the PDFs, visually inspect rendered pages or validate word/line overflow. A screenshot is not a guarantee of accessible PDF tagging.

## 5. Licensing and source lineage

GitHub identifies Apache-2.0, but the README explicitly states that the CV and research proposal are based on two external Overleaf templates and instructs readers to inspect accompanying licenses. The repository's license cannot automatically transfer permissions over external derivatives; derivative code reuse must respect the original authors' terms and any font package licenses.

No external Overleaf source comparison, compilation, or license legal opinion was undertaken.

## 6. Scientific and admissions-validity boundary

The embedded candidate accomplishments and sample paper citations are example applicant content, not generalized eligibility evidence or verified self-reported results. A research plan structure does not establish a funded PhD vacancy, supervisor fit, admission probability, or the likelihood of receiving a scholarship.

The best content-evaluation standard remains the user's own research problem, methods, independent contributions and reproducible evidence, tailored to target supervisor papers and program requirements.

## 7. Transferable implementation details

Reuse the modular `moderncv`/LaTeX architecture, citation management, multilingual document versions and academic section hierarchy after rights checks. For a production application-document workflow, maintain a structured factual CV store (degrees, contributions, outputs, DOI), generate destination-specific layouts, keep private data off public Git, and render/verify every PDF output with a reproducible toolchain.

Source lineages and institution-specific instructions should be recorded as separate metadata instead of silently inheriting template defaults.

## 8. Pinned source and validation

- [README and upstream template credits](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/README.md)
- [English CV LaTeX](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/CV/cv.tex)
- [Chinese CV source](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/CV_CN/cv_cn.tex)
- [Research plan](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/RP/rp.tex)
- [Research-plan structure](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/RP/structure.tex)
- [Bibliography](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/RP/ref.bib)
- [Repository license](https://github.com/HauLiang/PhD-Application-Template/blob/8094b0809493e061d118b853af4733f72267f985/LICENSE)

**DEEP_REVIEW_DOCUMENTED — editable sources inspected.** No source compilation, PDF rendering, third-party license verification, applicant identity reuse, admission verification or external academic claim validation. Personal sample details were not reproduced.
