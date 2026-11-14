# Session cross-repository synthesis — 2026-11-12

## Scope
This synthesis connects two screened-in candidates investigated in session audit-20261112-0001-7f3c. It is additive session research, not a canonical global synthesis.

## Comparison

| Dimension | simitii reading list | siddu1998 Graduate-Admissions |
|---|---|---|
| Primary artifact | One-file curated link index | Institution-foldered personal SOP and LOR PDFs |
| Evidence type | Secondary links to advice, official guidance, and examples | Primary applicant-authored documents, but unverified authorship/consent and outcomes |
| Workflow | Discover, learn, prepare, compare, select faculty, prepare questions | Compare examples by institution/degree/cycle and adapt narrative |
| Data structure | No schema; links embedded in prose | Folder names and filenames only; no manifest |
| Currency | README last changed 2020 | Latest README change 2023; referenced examples largely 2020–2021 |
| Main risk | Historical, US/CS/NLP selection bias and source dependence | Personal-document privacy, consent, license, and copying risk |
| Adoption | Source discovery taxonomy only | Reference-only; do not ingest or redistribute personal PDFs |

## Combined methodological conclusions

1. Separate source discovery from evidence authority. A curated index is not itself primary evidence; a personal SOP is an example, not proof of what caused admission.
2. Carry source metadata and context with every claim: original author, date/cycle, field, geography, degree type, source class, consent/license, and last verification.
3. Do not count repeated links, copied lists, or derivative repositories as independent corroboration. Resolve each shared URL to one canonical source and preserve dependency edges.
4. Treat successful applicant examples as selected case material. Without rejected applicants, denominator, and outcome verification, do not infer causal factors or acceptance probabilities.
5. Convert narrative advice into testable preparation checks, not deterministic admissions rules. For example, research-fit claims should be checked against recent faculty publications, available supervision, and a funded position.
6. Protect document provenance and privacy. Public availability does not establish consent to copy recommendation letters, personal essays, signatures, contact details, or embedded metadata.
7. Separate historical narrative patterns from current program requirements. Current official department instructions override old examples.

## Integration proposal
For the canonical PhD Atlas, model external material as Source -> Claim -> Evidence Context -> Applicant Action. Keep source class, original author, date, geography, field, cycle, license/consent, verification state, and dependency relations as explicit fields. Store only links and minimal non-sensitive descriptions for applicant-specific examples unless explicit reuse rights and privacy review are established.

## Open questions
- Verify whether each external resource remains available and whether current official guidance supersedes it.
- Verify author/consent and license conditions before using any personal SOP or LOR as training/reference material.
- Independently assess applicant narratives and avoid counting repeated sources across curation lists.
- Extend the candidate inventory through the next eligible batch after these two screened-in repositories are recorded.
