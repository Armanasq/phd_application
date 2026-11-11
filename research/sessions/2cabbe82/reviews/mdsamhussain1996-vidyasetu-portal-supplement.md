# VidyaSetu Scholarship Portal — supplemental investigation

- Existing canonical pin: `fc11048d6488c86d9da373795d857f2019f88204`
- Files in canonical review: schema, discovery, validation, tests, scheduled workflow, source and search configuration.
- Status: supplemental static analysis; no scheduled workflow or model extraction executed.

## Additional synthesis

The most transferable concept is the separation between discovery, source freshness and verification. A recurring scholarship's next annual cycle is not a continuation of the prior confirmed date. A system must retain the historical verified record while moving the future cycle's deadline to Expected/Unknown until the new official announcement appears.

The implementation's hash-based cache is useful only if it is advanced after successful extraction and validation. If a failed model request marks a page as processed, a later run may incorrectly skip the same unchanged page. Hash updates should therefore be committed only after the extraction transaction reaches an explicit success state.

The existing canonical review identifies two independent trust bugs: URL substring checks can accept lookalike hosts, and evidence presence is used as a confidence proxy. An exact quote proves only that text appeared in a fetched page; it does not prove the page belongs to the official funder, that the claim applies to the target cycle, or that the applicant is eligible.

## Transfer

Adopt per-source content hashes, separate first-seen/last-checked/last-verified timestamps, cycle rollover, staged review queues, and automated pending-item pull requests. Require exact host validation, redirect checks, quote-to-source matching, explicit cycle/applicant scope, and independent verification before a public claim is marked confirmed.

## Validation gaps

No current scholarship pages were re-fetched, no workflow run was replayed, and no adversarial hostname, extraction failure, or date-rollover test was executed in this session.
