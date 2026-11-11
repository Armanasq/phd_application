# siddu1998/Graduate-Admissions — session investigation

- Repository: https://github.com/siddu1998/Graduate-Admissions
- Inspected revision: `71d1750175b1cca2bca78fe738765b0c42c58c0a`
- Last observed commit: 2023-03-06
- Default branch: `main`
- Issues / pull requests / releases: none returned by inspected API queries
- Review status: repository structure and artifact inventory inspected; PDF content not independently analyzed
- License: no license file or metadata was established in this pass

## Nature and structure

A personal archive of application materials, mainly statements of purpose and statements of intent, organized by institution and degree/application cycle. README states that the examples include multiple application cohorts, repeated content, and MS-to-PhD evolution. It invites others to contribute materials in named folders.

Repository inventory includes application documents for Brown, CMU, Columbia, Cornell, EPFL, Imperial College London, MIT, Oxford, Purdue, UBC, UCSC, UIUC, University of Maryland, UNC-Chapel Hill and USC. The corpus also contains recommendation-letter PDFs. Those personal documents are not reproduced or summarized here.

## Research value

The repository provides a useful comparative corpus for studying:
- how one applicant adapts a research narrative across programs;
- how MS and PhD statements differ in research depth and future direction;
- how program-specific fit is articulated;
- how repeated experiences are reframed without changing underlying facts;
- how a statement of intent may reference prior supervisor contact.

The strongest methodological use is a controlled comparison of the author's own statement versions across institutions and cycles. A proper study would code each document for research question, prior-work evidence, methods, contribution, future agenda, faculty/lab fit, institutional fit, and prompt compliance.

## Evidence boundary

The README's description establishes the author's stated intent and document organization, not admissions outcomes. A PDF stored under an institution folder is not evidence of acceptance, interview, scholarship or offer. No inference about admission success should be made without separate firsthand evidence.

## Privacy and licensing

Recommendation letters and personal application materials may contain names, contact details, academic records and confidential referee statements. Do not extract or republish those details in a public research report. Use only materials that are clearly intended for public methodological study, and respect the repository's rights and any third-party confidentiality. No license was established; public visibility does not automatically grant permission to reuse or redistribute the PDFs.

## Transfer to PhD Atlas

Add a private `ApplicationArtifact` model:
- applicant profile version;
- institution/program/cycle;
- artifact type (SOP, research proposal, CV, writing sample, statement of intent);
- prompt/version;
- draft version and timestamp;
- evidence references to factual claims;
- reviewer feedback;
- final-submission checksum and portal evidence.

Support a comparison view across versions, but separate factual claims from rhetorical changes. A document's claims should be traceable to the applicant's verified profile and research record. Keep recommendation letters and sensitive personal documents private and outside public Git.

## Provenance and coverage

Inspected the complete top-level repository listing and README, including institution folders and PDF inventory. Checked recent commit history and empty issue/PR/release results. Individual PDF bodies were not fetched or analyzed, and no admissions outcome was verified. The review is a structural and methodological assessment, not a full document-content audit.

## Canonical classification

**PRELIMINARY_FOCUSED** — the README and full document inventory were inspected; personal PDF content and referee materials were deliberately not ingested or reproduced. Original session evidence: [source review](../../sessions/2cabbe82/reviews/siddu1998-graduate-admissions.md). No admissions outcome is verified.
