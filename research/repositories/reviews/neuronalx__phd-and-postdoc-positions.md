# neuronalX/phd-and-postdoc-positions — historical vacancy source assessment

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/neuronalX/phd-and-postdoc-positions | **Pinned default-branch commit:** [`861f31226775d882303891ca877d7fd313a138e9`](https://github.com/neuronalX/phd-and-postdoc-positions/commit/861f31226775d882303891ca877d7fd313a138e9) | **State:** PRELIMINARY_FOCUSED; complete repository inventory but PDF body inspection NOT_PERFORMED | **Decision:** historical vacancy archive, not a verified open 2026 recruitment channel.

## 1. Scope and content identity

The repository is a very small archive of individual PhD/postdoctoral offer PDFs rather than a vacancy search service, applicant tracker or source-crawling implementation. The complete recursive tree has exactly three tracked files:
- `README.md` (192 bytes);
- `2023-05-14_PostDoc_Decoding-Transformers.pdf` (106,607 bytes);
- `2023-07-27_PhD-topic_AEx_BrainGPT.pdf` (109,365 bytes).

The README contains one described opportunity: `From Reservoir Transformers to BrainGPT`, labeled July 2023, and links to the Inria recruitment portal record `2023-06611` for more information and application. The repository's latest commit was 2023-07-31. It has no script, test, crawler, dataset, schema, package manifest, CI workflow, issues, PRs or license file.

## 2. Research value and provenance

The repository demonstrates a useful *primary offer artifact* pattern: retain an institution-specific archived PDF, an offer title, a dated source revision and the official recruitment-portal reference. It is useful for studying historical doctoral project framing, institutional posting conventions and the provenance chain from an external repository to the original employer application portal.

An externally linked employer URL is a candidate authority reference, not proof that an opportunity remains open. The 2023 year is historical relative to 2026-11-12; neither the GitHub record nor the file name establishes a live vacancy, a current funded contract or eligibility for a 2026/2027 intake.

The only topic that the README supports directly is the named BrainGPT/Reservoir Transformers PhD project. The postdoc PDF title suggests a related transformer research topic; do not infer detailed project methods, funding, supervisor or recruitment terms without reading the PDF and official employer record.

## 3. Source access limitation

GitHub provided the full repository file tree, commit history and binary PDF metadata. A container-based download attempt could not resolve GitHub; direct external raw-PDF retrieval also failed. The PDF bodies were **not** rendered, read or text-extracted. The Inria portal job text and current open/closed status were not verified.

This is therefore a preliminary source-identity and historical-classification review, **not** an analysis of the PDFs' technical content. The artifacts should not be promoted to deep review on the strength of filenames and README alone.

## 4. Evidence-led application to the repository

Represent the two items separately as `HISTORICAL_POSTING` observations with offer document URL, publisher/owner, original cycle (2023), archived-source revision and an explicit `CURRENT_AVAILABILITY_UNKNOWN` value. Add an `ORIGINAL_EMPLOYER_SOURCE` edge for the Inria recruitment URL, without claiming its current contents were fetched. Keep PhD and postdoc position types separate.

No application deadline, salary, funding, eligible citizenship, supervisor availability, official admissions policy or admission probability should be inferred from this source. A date in a filename is not a verified application deadline.

## 5. Evidence references

- [Readme and original Inria offer link](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/README.md)
- [Archived doctoral-offer PDF path](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/2023-07-27_PhD-topic_AEx_BrainGPT.pdf)
- [Archived postdoctoral-offer PDF path](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/2023-05-14_PostDoc_Decoding-Transformers.pdf)

**Disposition: PRELIMINARY_FOCUSED**, pending actual PDF-body review and employer-source verification if future historical research warrants it. This is not a current vacancy listing.
