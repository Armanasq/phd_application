# Kingjose05/physapp — deployed-client-only preliminary audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/Kingjose05/physapp | **Pinned gh-pages commit:** [`16571ba5516d4a7a0405f050a3dd851d27e18df3`](https://github.com/Kingjose05/physapp/commit/16571ba5516d4a7a0405f050a3dd851d27e18df3) | **State:** PRELIMINARY_FOCUSED | **Decision:** potential physics-PhD program tracker; implementation behavior cannot be established from the published deployment bundle.

## Purpose and observable artifacts

The GitHub repository describes “PhysApp - Physics PhD Program Research Application Tracker.” Its default `gh-pages` branch contains nine tracked tree entries: `.nojekyll`, `index.html`, a minified JS bundle, compiled CSS, PDF worker, icons and favicon. No unminified source tree, tests, package manifest, backend implementation, documentation of program sources, CI workflow or license file is present in this default-branch tree. The latest observed update is 2026-09-11.

The `index.html` is a minimal app shell with a root element and bundled asset imports under `/physapp/`. This confirms a deployed static JavaScript single-page client, not which features work or whether it has a live university API, authoritative database, admissions-source verification, or authenticated users.

## Inspection coverage and limitations

The full tree, repository metadata and HTML entry were inspected. A request for the large minified JS asset returned no textual content in the available GitHub file-reading interface, so its program model, PDF functionality, local storage design, integration endpoints and UI behavior were **not inspected**. The presence of a PDF worker is not proof of a secure or correct document import pipeline.

No production frontend, remote API, user record, third-party code or PDF was executed or opened. Do not infer supported physics schools, current deadline accuracy, eligibility or applicant submission status.

## Transfer and next verification

Preserve as a candidate application-workspace reference but maintain `PRELIMINARY_FOCUSED`. For a deeper audit, retrieve the original source branch/project history or a readable source map, obtain and statically analyze the JS modules, verify data origins, and test any input/document functions in an isolated environment. Any university program data or physics-specific vacancy availability requires independent official sources.

The published bundle alone is not a source for funded PhD offers, supervisor availability, acceptance rates or successful application receipts.

## Pinned evidence

- [Entry document](https://github.com/Kingjose05/physapp/blob/16571ba5516d4a7a0405f050a3dd851d27e18df3/index.html)
- [Published JavaScript asset](https://github.com/Kingjose05/physapp/blob/16571ba5516d4a7a0405f050a3dd851d27e18df3/assets/index-DxjHFhNX.js)
- [Published stylesheet](https://github.com/Kingjose05/physapp/blob/16571ba5516d4a7a0405f050a3dd851d27e18df3/assets/index-BjCt8IiY.css)

**PRELIMINARY_FOCUSED** until accessible implementation-level source evidence is obtained.
