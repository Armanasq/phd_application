# neuronalX/phd-and-postdoc-positions — partial document-archive triage

- Inspected on 2026-11-12 at [commit 861f31226775d882303891ca877d7fd313a138e9](https://github.com/neuronalX/phd-and-postdoc-positions/commit/861f31226775d882303891ca877d7fd313a138e9).
- Provisional state: SCREENED_INCLUDE, **PDF_CONTENT_NOT_REVIEWED**; do not count as a completed source-level document audit.
- Contents: [README](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/README.md) and two binary PDFs: [2023 postdoc Transformers offer](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/2023-05-14_PostDoc_Decoding-Transformers.pdf), [2023 PhD BrainGPT offer](https://github.com/neuronalX/phd-and-postdoc-positions/blob/861f31226775d882303891ca877d7fd313a138e9/2023-07-27_PhD-topic_AEx_BrainGPT.pdf).

## Available evidence

The 192-byte README references a doctoral topic "From Reservoir Transformers to BrainGPT" with July 2023 date and an Inria 2023 recruitment URL (https://recrutement.inria.fr/public/classic/en/offres/2023-06611). The tree additionally contains a PostDoc Decoding Transformers PDF (106,607 bytes) and a PhD BrainGPT PDF (109,365 bytes). Git history shows additions between April and July 2023; no more recent vacancy update was observed and issue/PR listings were empty. A historic 2023 opportunity is not a November 2026 open call.

The README alone cannot establish actual thesis scope, contract duration, supervisor, compensation, application process, nationality restrictions, current recruiting or official offer status. The two PDFs could contain these details, but their bodies were **not parsed**: the GitHub plaintext fetch path raised UnicodeDecodeError on the PhD PDF, and a separate raw PDF lookup returned a cache-miss failure. Neither failure is evidence of a corrupt source PDF.

## Follow-up and review boundary

Retain this as an AI/neuroscience recruitment-method lead and retrieve both PDF bytes through a working binary download route. Render and inspect their text/layout before claiming a completed investigation, then compare their claims to current primary Inria documentation if a current lead is needed. No 2023 data should be carried forward as current. No PDF contents, live Inria employer link, applicant submission, tests or private files were accessed.

**Decision:** leave canonical completion status pending independent PDF-content extraction; classify only at the screened-in discovery gate. Do not fabricate source evidence or infer current funding.
