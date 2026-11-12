# Swapnil-Gandhi/SoP-Template — deep review of research statement structure and provenance

**Reviewed:** 2026-11-12  
**Repository:** https://github.com/Swapnil-Gandhi/SoP-Template  
**Repository ID:** 559034119  
**Pinned source commit:** [98f6a25c59dd51a64859b029bbaea68b4adbef10](https://github.com/Swapnil-Gandhi/SoP-Template/commit/98f6a25c59dd51a64859b029bbaea68b4adbef10)  
**Review level:** DEEP_REVIEW_DOCUMENTED — all text sources and complete four-file inventory statically reviewed. Compiled example PDF **not** downloaded, rendered or compared.  
**Verdict:** ADAPT_STRUCTURE_ONLY. Do not copy example identities, assertions, findings, citations, dates or faculty preferences.

## 1. Purpose, boundaries, and evidence class

A four-file, CC0-licensed Computer Science PhD Statement of Purpose example. It contains a single article-class LaTeX source, its example PDF, README and CC0 license text. Its purpose is applicant writing and typesetting: it does not discover admissions calls, validate funding, contact faculty, provide evidence of acceptance, or predict admission outcomes. The source is authored from a historical fall-2022 application; its university and professor descriptions are not evidence of current availability in the 2026–27 cycle.

Source: [README](https://github.com/Swapnil-Gandhi/SoP-Template/blob/98f6a25c59dd51a64859b029bbaea68b4adbef10/README.md), [SoP.tex](https://github.com/Swapnil-Gandhi/SoP-Template/blob/98f6a25c59dd51a64859b029bbaea68b4adbef10/SoP.tex), [CC0 legal text](https://github.com/Swapnil-Gandhi/SoP-Template/blob/98f6a25c59dd51a64859b029bbaea68b4adbef10/LICENSE.md).

## 2. Structure and explicit writing method

The LaTeX source uses embedded editorial comments to describe a five-part narrative. It begins with a research motivation and a clearly delimited area; follows with three prior research contributions arranged as problem -> technical gap -> methodological intervention -> demonstrated/proposed result; then covers academic preparation and service; identifies the target institution, specific faculty and research fit; and concludes with a forward-looking research statement. The source is an example of **claim-to-contribution continuity**, not a universally applicable essay rubric.

Research contribution descriptions distinguish a conference-published result from an ongoing project; the reference section manually labels published and ongoing items. This distinction is valuable: a statement should not transform a currently evaluated prototype or preprint into a peer-reviewed accepted result. The original document also distinguishes demonstrated outcomes from a prospective integration plan. These statuses are author text, not independently confirmed publication metadata.

## 3. Document and formatting pipeline

`SoP.tex` is an article document using T1 font encoding, UTF-8, natbib, hyperref, xcolor, xspace and fancyhdr, with a custom two-sided header layout and manually shifted margins. A few source macros encapsulate the target institution, faculty names and project names, but most facts and entire paragraphs remain hard-coded. The README instructs direct `pdflatex SoP.tex` or Overleaf compilation. No Makefile, CI, automated count/length checker, bibtex build step, template-variable validation, unit tests or authoritative university-style validator exists in the four-file tree.

The source repeats the fancyhdr package include, sets coloured links, manually shifts page geometry, and uses alternate fancy header positions without explicitly setting a two-sided article class. These are portability/formatting review points; compilation warnings and final layout have **not** been reproduced here. No letterhead compliance, accessible PDF tagging, output page count or exact printed margin has been verified.

## 4. Hard-coded identity and staleness hazards

- The example header, program year and first-person history identify the **original author**, not the applicant using the template. Simply replacing the target-school macros does not anonymize the document.
- Faculty macros identify specific historic target professors; there is no real-time current-supervisor availability, funded slot, department affiliation or research-fit verification.
- The original project paragraphs contain named collaborators, past publications and strong performance claims. Those must be replaced with applicant-owned, verifiable work; copying them would fabricate credentials.
- Publication references are manually numbered [1]–[4], despite natbib being imported. Editing/reordering projects can silently break citation cross-references.
- The source includes institutional and project-specific external URLs as footnotes. An active or reputable link is not sufficient to verify that the associated claim is true, current or reusable.
- No word count or page-length enforcement is present, and the custom margins may conflict with school-specific page, spacing, minimum-font or anonymity rules.

## 5. Evidentiary and methodological limitations

This is one author's worked example, not a controlled study of admission decisions or proof that copying its style increases acceptance. The project supplies no applicant outcome dataset, controlled admissions assessment, document review by a committee or country-specific funding criteria. Writing quality depends on the actual applicant's research trajectory and the specific prompt, not on this repository's presentation alone. Cross-institution fit or scholarship-specific project proposals require separate official program instructions.

## 6. Source security, ethics and reproducibility

CC0 permits broad reuse of the template, but academic honesty separately requires that every purported personal contribution be true and supported. This review did **not** extract or redistribute the compiled PDF, download external linked papers, contact faculty, invoke Overleaf or compile LaTeX. The published text includes public first-person experiences; copying the phrasing risks misattribution even when the layout is reusable. Commit pinning supports future reproducibility but no local LaTeX version/engine output record has been captured.

## 7. Connections to repository research and an implementable template contract

Compared with [LimHyungTae/Awesome-PhD-CV](https://github.com/LimHyungTae/Awesome-PhD-CV), this serves the **research-narrative layer** rather than the structured accomplishments ledger. Its source should consume candidate-verified evidence from that ledger, not diverge from it.

A safe SoP pipeline is: applicant-owned project evidence -> structured claim/research-gap/novelty/outcome records -> university-specific research-fit facts supported by current authoritative pages -> written narrative -> factual contradiction check -> institution-specific length/anonymity/rubric check -> reproducible PDF render -> candidate approval. Keep accepted, submitted, under-review and ongoing outputs distinct, and distinguish aspiration from institution-confirmed supervisor availability.

## 8. Decision and incomplete verification

**DEEP_REVIEW_DOCUMENTED — ADAPT narrative method only.** Full `README.md`, `SoP.tex`, `LICENSE.md`, four-file repository tree and pinned commit were inspected; binary `SoP.pdf` was identified but not read. No TeX build, PDF visual QA, citation resolution, live faculty/program audit or application submission occurred. The supplied example is a historical writing aid, not evidence that any 2026/2027 PhD opening is valid, funded or available.
