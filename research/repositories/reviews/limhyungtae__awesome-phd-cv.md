# LimHyungTae/Awesome-PhD-CV — research CV and industry resume template deep audit

**Reviewed:** 2026-11-12  
**Repository:** https://github.com/LimHyungTae/Awesome-PhD-CV  
**GitHub repository ID:** 1190195126  
**Pinned upstream commit:** [c95e5c286988cabcfdb9279e27f924368b90ad8e](https://github.com/LimHyungTae/Awesome-PhD-CV/commit/c95e5c286988cabcfdb9279e27f924368b90ad8e)  
**Review state:** DEEP_REVIEW_DOCUMENTED — source-level audit of the README, guidance, three LaTeX layouts, research-CV section modules, class files, reference bibliography and preview generation; binary previews/fonts and LaTeX execution NOT_TESTED.  
**Decision:** Adapt research CV taxonomy and evidence discipline, not a one-size-fits-all scholarship CV or validated ATS performance claim.

## 1. Goal and audience segmentation

This repository packages three structurally distinct application documents: a multi-page academic CV based on Awesome-CV, Jake's single-column software-industry resume, and Deedy's dense two-column resume. The README and GUIDELINES explicitly distinguish academic research achievements and service from recruiter/ATS-oriented engineering impact. These layouts address document presentation, not admission probability, scholarship eligibility, source discovery, or confirmed supervisor recruitment.

## 2. Source inventory and architecture

The pinned recursive tree contains 65 entries, including LaTeX source, root README and GUIDELINES, three compiled example PDFs, associated preview images, embedded fonts, a bibliography style and BibTeX references. The active academic entrypoint is research-cv/cv.tex, which invokes research-cv/awesome-cv.cls (Awesome-CV v1.6.1 declared) and modular sources under research-cv/cv/. Its rendered section graph includes summary, education, work experience, research projects, publications, teaching, honors and academic services. The academic source uses fontspec, unicode-math, fontawesome5, geometry, hyperlinks and custom section environments, and declares XeLaTeX.

Jake's resume is a separate article-class/single-column template with pdfLaTeX-friendly text extraction conventions. Deedy uses a custom class with fontspec, textpos and dense two-column layout. A bash utility generates PNG previews from the first page of each prebuilt PDF using ImageMagick. The files are not a unified document-generation API; customization is through LaTeX edit/compile workflows.

Primary sources: [README](https://github.com/LimHyungTae/Awesome-PhD-CV/blob/c95e5c286988cabcfdb9279e27f924368b90ad8e/README.md), [GUIDELINES](https://github.com/LimHyungTae/Awesome-PhD-CV/blob/c95e5c286988cabcfdb9279e27f924368b90ad8e/GUIDELINES.md), [academic entry](https://github.com/LimHyungTae/Awesome-PhD-CV/blob/c95e5c286988cabcfdb9279e27f924368b90ad8e/research-cv/cv.tex), [CV class](https://github.com/LimHyungTae/Awesome-PhD-CV/blob/c95e5c286988cabcfdb9279e27f924368b90ad8e/research-cv/awesome-cv.cls), [industry resume](https://github.com/LimHyungTae/Awesome-PhD-CV/blob/c95e5c286988cabcfdb9279e27f924368b90ad8e/jakes-format/resume.tex).

## 3. Research-content schema and dataflow

The academic CV separates education degrees, dissertation and advisor references; project experience and technical contributions; peer-reviewed journal/conference publications; academic teaching; honors/awards; and scholarly service. Publication source entries appear in research-cv/cv/publication_journals.tex and publication_conf.tex as manually maintained text. A BibTeX file is present but the parent CV's bibliography include is commented out, so updating ref.bib alone will not necessarily regenerate published entries.

Several existing section files are **inactive** because the parent cv.tex comments out their input directives: skills, presentation, certificates and writing. Merely editing one of those files will not make it appear in the built CV. Individual status macros signal accepted or under-review manuscript states; those are source-authored labels, not a substitute for verifying publication acceptance, DOI, journal indexing or award date.

## 4. Reproducibility and correctness findings

- **Broken README directory command:** The documented Awesome-CV setup says to change directory into awesome-cv-format, but the tracked entrypoint is under research-cv. A verbatim local build command from the README will fail without adapting the path.
- **Engine and package dependence:** Research CV and Deedy need XeLaTeX and optional system fonts/icon packages; compiled example PDFs do not demonstrate that a fresh system can rebuild from source. No TeX Live lockfile or CI smoke compilation is evidenced.
- **Different layouts and ATS claims:** README presents Jake's format as ATS-safe, but neither an ATS test fixture nor vendor compatibility results are present. This is design intent, not a verified acceptance rate for automated CV readers.
- **Invisible sections:** Commented-out input commands hide source modules; users may think editing skills.tex or certificates.tex has affected the final artifact when it has not.
- **Manual citation maintenance:** Publication entries are hardcoded, with separate BibTeX references; these can drift. In particular, under-review and accepted status qualifiers need owner verification at application time.
- **LaTeX portability:** The awesome-cv class defines numerous customized social links/headers and relies on third-party font packages. Porting it to pdfLaTeX or to automated one-page export cannot be assumed to work without changes.
- **Prior work and licensing:** The research-cv class identifies the Awesome-CV original and an LPPL 1.3c class license; the README cites CC BY-SA 4.0 for the original template. The Deedy and Jake components derive from other templates, each with potentially distinct licensing obligations. Confirm licenses for each reused component rather than treating all files as one uniform license.

No runtime compilation or ATS parser was executed; no upstream defects were patched.

## 5. Application-quality method that transfers

An evidence-based robotics/AI PhD CV should prioritize research questions, contributions/methods, peer-reviewed work with precise statuses, projects/results, advisor/collaborator links, teaching and relevant technical skills. Every institution, degree, project, award, publication claim, patent, collaboration, date and metric must be supported by the candidate's private evidence records. Verifiable first-author/co-first-author or corresponding-author status cannot be inferred from typography alone.

A separate industry engineering resume can condense the same evidence to system impact and measurable engineering outcomes. Do not use industry ATS guidance as a universal rule for academic faculty-led or committee-reviewed admissions.

## 6. Data integrity and privacy

The project includes an example researcher's personal CV, photo, self-descriptions and research achievements. They are template **examples**, not the applicant's identity, and must not be copied into other users' CVs or used as empirical admissions outcomes. The code inspection did not reuse the personal details; binary CV/image assets were not downloaded or analyzed.

No verification was performed for linked papers, citation counts, author affiliations, institution status or professional histories. Hyperlinks are authored references rather than source-of-truth accreditation.

## 7. Cross-repository synthesis

Compared with Swapnil-Gandhi/SoP-Template, this provides a typed section/document structure rather than narrative research motivation. Compared with application trackers, it is the **document rendering layer**: there is no submission receipt, deadline metadata, eligibility gate or revision-proof state. In PhD Atlas, store a typed academic profile and artifact provenance, render CV and engineering resume variants from approved facts, keep a separate publication-status ledger, and validate generated PDFs through a reproducible compile + visual QA pipeline.

## 8. Final disposition and limitations

**DEEP_REVIEW_DOCUMENTED — ADAPT** academic structure, avoid direct copying. Inspected README, GUIDELINES, both resume source templates, Deedy class, research CV class/entrypoint, active and inactive section modules, publication text and bibliography, and preview script at the pinned revision. Not inspected: binary PDFs/fonts/images or the full bibliography style internals. Not run: local XeLaTeX/pdfLaTeX compilation, link check, font availability, PDF accessibility/ATS parsing, CI, or any admissions outcome evaluation. The repository is a reusable presentation reference, not authoritative funding or scholarship information.
