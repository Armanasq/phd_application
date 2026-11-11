# siddu1998/Graduate-Admissions — source-level investigation

- Review date: 2026-11-12
- Repository ID: 426370062
- Default branch: main
- Inspected snapshot: 71d1750175b1cca2bca78fe738765b0c42c58c0a
- Repository: https://github.com/siddu1998/Graduate-Admissions
- Review state: PRELIMINARY_FOCUSED — structure, README, history, and risk inventory inspected; PDF contents not inspected
- Confidence: High for tree/README/history; low for SOP/LOR content and quality.

## 1. Problem and intended use

The author publishes personal graduate application statements for other applicants to use as examples. The README describes multiple application cohorts and institutions, notes repetition, and says the materials show how statements were adapted across universities and between MS/PhD applications. It invites others to contribute documents by pull request. This is a public document repository, not an admissions management application.

## 2. Complete repository structure

The recursive tree contains 40 entries: 16 directories and 24 files (one README plus 23 PDFs). The directories comprise 15 institution folders and one Recommendations folder:
- Brown: one SOP.
- CMU: two SOPs, including a Fall 2021 version.
- Columbia: one SOP.
- Cornell: two statements, including an MS IT+Health statement.
- EPFL: one SOP.
- Imperial College London: one SOP.
- MIT: one SOP.
- Oxford: one SOP.
- Purdue: two statements, one explicitly PhD-labelled.
- UBC: one statement of intent whose filename notes supervisor contact.
- UCSC: one PhD SOP.
- UIUC: one SOP.
- UMCP: one CS SOP.
- UNC-Chapel Hill: one SOP.
- USC: three statements, including an MS CS version and a 2021 version.
- Recommendations: three recommendation-letter PDFs.

The README also links to a Reddit graduate-admissions guide and three YouTube resources.

## 3. Data model and implied workflow

No machine-readable data model or application code exists. The directory structure encodes institution labels. Filenames provide limited metadata (institution, degree level, and sometimes cycle), but there is no consistent manifest of author, degree, research area, submission year, document type, consent, or outcome.

The implied workflow is to select examples for a target institution, compare statements across MS and PhD applications, observe repeated content and institution-specific changes, adapt structure to the target program, and optionally contribute additional applicant documents. This is informal reference material with no current-policy validation, provenance checks, quality rubric, or safeguards against copying.

## 4. Development history and maintenance

The repository has 11 commits, from the initial commit on 2021-11-09 to the latest README update on 2023-03-06. Most changes are README updates and bulk SOP additions. The only branch is main. No open issues or pull requests were found. No license file is present in the inspected tree. Do not assume personal documents may be redistributed or reused beyond their intended reference purpose.

## 5. Privacy and document-handling risk

The public tree contains three recommendation-letter PDFs under Recommendations/, with a person's name in filenames. Recommendation letters may contain personal data, referee identities, contact details, signatures, confidential evaluations, and information supplied with an expectation of restricted circulation. The tree also contains applicant-specific SOPs. This is a material privacy and consent concern.

I did not retrieve, reproduce, quote, or extract personal details from these binary documents. Their content and embedded metadata remain uninspected. Their presence is not evidence that they were submitted with consent for public redistribution. Do not mirror this repository into the PhD application workspace.

## 6. Evidence and methodological limitations

The README says the statements cover different cohorts and programs in 2020 and 2021, but filenames are not a reliable provenance record. The examples cannot establish that a particular SOP caused admission, nor can outcomes be inferred from institution-labelled filenames. There is no denominator, rejection set, reviewer feedback, or standardized document-quality assessment.

The documents are historical. Their structure may illustrate narrative variation, but prompts, length limits, selection criteria, and funding processes must be checked against current official sources.

## 7. Reusable lessons and adoption decision

Reference-only, with privacy restrictions. Potential high-level lessons inferred from the stated purpose and directory structure: maintain separate versions for distinct degree types and prompts; tailor research fit to the actual department and faculty; preserve a truthful, consistent research narrative; inspect whether repeated paragraphs add program-specific evidence; and track application cycle and document type explicitly.

These lessons are not validated against the PDF contents. Do not copy text, identifying details, referee letters, or personal narratives. Prefer public, author-approved examples or official university guidance.

## 8. Cross-repository relationships

This repository overlaps with simitii/CS-Grad-School-Applications-Reading-List in the broad theme of SOP examples and application guidance, but source roles differ: simitii is a curated link directory, while siddu1998 stores applicant-specific SOP and recommendation PDFs. Curated links can be indexed as source records; personal application documents require consent and should not be copied into a public research corpus.

The README’s external Reddit link is a separate community resource and should be assessed independently from the personal PDF collection.

## 9. Coverage and verification

Inspected: complete recursive tree (32 entries); full README; repository metadata, default branch, and latest commit; eleven-commit history; branch list; issues and pull requests.

Not performed: binary PDF extraction or semantic review; embedded metadata inspection; runtime tests (no executable software); consent, authorship, or license verification; current-policy validation of listed institutions; or admission-outcome verification.

Final disposition: repository-level structural investigation complete; substantive document review blocked by binary-access and privacy constraints. Keep at PRELIMINARY_FOCUSED until authorized, privacy-safe document review is possible. Do not upgrade based on filenames or README descriptions.
