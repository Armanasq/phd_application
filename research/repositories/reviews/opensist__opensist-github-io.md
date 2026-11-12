# OpenSIST/OpenSIST.github.io — source-pinned deep frontend admissions platform audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/OpenSIST/OpenSIST.github.io | **Pinned revision:** [`259b4b651a47a97c7d90d9d78ed5326b6ed5fd53`](https://github.com/OpenSIST/OpenSIST.github.io/commit/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53) | **State:** DEEP_REVIEW_DOCUMENTED (frontend static audit only) | **Verdict:** adapt provenance-aware applicant/program/outcome separation; require independent backend and privacy verification before adopting.

## 1. Audience, source and actual scope

An independently maintained overseas graduate admissions information-sharing platform created by ShanghaiTech University students. README describes helping ShanghaiTech applicants plan overseas postgraduate applications, rather than a funded PhD vacancy scraper. The repository contains a React/Vite browser client with program directories, applicant profiles, application result records, program descriptions, posts, favorites, authentication pages, user consent, and administration UI.

The pinned tree contains 229 files, including assets, React components, data/cache modules, Markdown/FAQ content, and static university rankings. The GitHub license is GPL-3.0, so redistributing derived implementation requires compatible licensing and obligations. Last observed source commit: 2026-10-23. No backend service implementation is present in the inspected frontend repository; runtime tests, server database and user permissions were not independently verified.

## 2. Data model and information architecture

`src/Data/Schemas.js` distinguishes `Master` and `PhD`, CS/EE and other majors, geographic regions, applicant degrees, publication states, research/evaluation categories and application outcomes `Admit`, `Reject`, `Waitlist`, `Defer`. The user can create a program description, applicant profile (often per application year), and application outcome record with `RecordID = ApplicantID|ProgramID`, year, semester, submission, interview, decision and status fields. The browser UI includes a global record table with program/applicant filtering and sorting.

This is a **self-reported graduate admissions intelligence and experience corpus**, not evidence of an individual institution's current recruiting capacity or scholarship offer. Personal background, admissions outcomes and program requirements are separate data types. The university list contains manually recorded rankings and aliases; no source version or ranking methodology is attached to each row in inspected client code.

## 3. End-to-end frontend/backend boundary

`src/APIs/APIs.js` maps programs, applicants, records, content/posts, favorites, files, account administration and login to a server URL defaulting to `https://opensist.tech/`; Vite config can override it. `src/Data/Common.js` performs credentialed fetch with `credentials: 'include'`; on a 401 it clears the local cache and redirects to login. Unlike single-user local-only dashboards, this frontend has distinct remote API read and write paths.

`ProgramData.js` obtains program lists and description batches from the remote backend; `ApplicantData.js` obtains applicant entries; `RecordData.js` normalizes records keyed by RecordID; mutating calls invalidate affected caches. The program UI supports additions and revisions, so facts may originate from user submissions rather than institution-signed documents. The trust/provenance of server-side records, anti-abuse moderation and privilege checks **cannot be established from this repository**.

## 4. Cache synchronization and privacy implications

`CacheStore.js` implements a localForage/IndexedDB-style cache with a one-hour TTL, schema versioning, per-key serialized writes, request generation/version checks, foreground/background priorities and explicit cache-epoch invalidation. `CoreCacheSync.js` periodically prefetches programs, descriptions, applicants, records and applicant metadata/avatars in batches. It avoids stale background writes overriding later foreground results, and clears caches on logout/unauthorized responses.

These are substantive transferable caching techniques, but applicant records and metadata are copied into persistent browser storage. Such offline retention increases confidentiality exposure on shared devices, especially if profiles include personal contact/education details. A browser cache is not a legal data-retention or encryption policy. Cache clearing on logout is useful but does not prove data deletion from other backups, browsers or server databases.

## 5. Consent and authorization evidence

`Agreement.jsx` contains Chinese privacy statements claiming users may choose anonymity/contact exposure, that applicant information is for authorized ShanghaiTech academic email holders, and that backend storage is private. This is a published promise, **not** independent proof of server-side access controls. On the client, `isAuthApplicant()` compares the applicant ID's username portion with the current display name. This heuristic can control UI actions, but **must not be treated as server authorization**; the repository does not include the backend code needed to verify object-level access restrictions.

`UserData.js` handles login/logout, display names, anonymous toggle and metadata caching; credentials are sent as POST with included cookies, and the client shows no bearer token stored directly in localStorage. Security boundaries still depend on cookie flags, CSRF protection, rate limiting, email-domain proof, object-level authorization and server retention — all **NOT_VERIFIED** without backend inspection. Avoid harvesting or publishing applicant profiles and self-reported records.

## 6. Content quality, source dependence and runtime gaps

The program page permits human-edited Markdown descriptions, course requirements and admission preferences; `Markdown.jsx` renders with ReactMarkdown and a default URL sanitization transform, rejecting ordinary javascript: protocols and limiting permitted image data URLs to raster formats. This is a stronger rendering posture than direct raw `innerHTML`. Nevertheless, authorization of edits, attachment handling, content provenance and moderation remain backend-dependent.

Admissions results have known survivorship and disclosure biases: self-reporting, missing denominators, overrepresentation of particular universities/majors/cycles, inconsistent decisions/funding, anonymous identities, and lack of verified institutional confirmation. The platform does not make a current funded job offer merely because a historical applicant reported admission.

Repository `package.json` defines lint/typecheck/build scripts; it does not establish real deployment reliability, backend CI, full API integration coverage or a validated selection-rate estimation. No browser, live API, authentication or private user-data test was executed.

## 7. Transfer and integration design for PhD research

Adopt as references: applicant-year segmentation; program–applicant–outcome relational linkage; admission/decision timeline; provenance-aware comments; degree/region filters; explicit anonymous profiles; batched source-description reads; generation-safe cache invalidation; UI privacy agreement.

Before data/model reuse:
1. Identify separate `SELF_REPORTED_OUTCOME`, `OFFICIAL_PROGRAM_REQUIREMENT`, `OFFICIAL_VACANCY` and `PERSONAL_APPLICANT_PROFILE` evidence types.
2. Do not infer admission rates from convenience-sampled self-reports or conflate Admit with guaranteed full funding.
3. Verify official current program requirements and admissions cycles independently before making eligibility recommendations.
4. Require backend-verified user membership and row-level authorization; preserve consent, retention and deletion controls before any profile import.
5. Keep private applicant records out of public Git and avoid copying identifiable outcome records.
6. Evaluate GPL-3.0 compatibility before adapting any code.

## 8. Pinned implementation evidence and validation

- [API endpoint registry](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/APIs/APIs.js)
- [Authenticated request wrapper](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/Common.js)
- [Programs and source descriptions](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/ProgramData.js)
- [Applicant data and UI ownership check](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/ApplicantData.js)
- [Application outcome records](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/RecordData.js)
- [Status/degree and rank schemas](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/Schemas.js)
- [Cache safety](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/CacheStore.js)
- [Background cache prefetch](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/CoreCacheSync.js)
- [Auth/user cache](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Data/UserData.js)
- [Privacy agreement](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Components/Agreement/Agreement.jsx)
- [Outcome entry form](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Components/Modify/Record/AddModifyRecord.jsx)
- [Program edit form](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Components/Modify/Program/AddModifyProgram.jsx)
- [Markdown rendering](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/src/Components/Markdown/Markdown.jsx)
- [Build scripts](https://github.com/OpenSIST/OpenSIST.github.io/blob/259b4b651a47a97c7d90d9d78ed5326b6ed5fd53/package.json)

**DEEP_REVIEW_DOCUMENTED — frontend-only static inspection.** Selected primary implementation paths, file tree, privacy text and data structures reviewed. No backend code, production data, API requests, external applicant records or runtime tests were accessed; server privacy/security, admissions accuracy and funding coverage remain **UNVERIFIED**.
