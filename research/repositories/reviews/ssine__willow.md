# ssine/willow — historical admissions-statistics platform static audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/ssine/willow  
**Repository ID:** 207145615  
**Pinned upstream SHA:** [62638c154593689c57ab28bf3e93cec535112c39](https://github.com/ssine/willow/commit/62638c154593689c57ab28bf3e93cec535112c39)  
**Review state:** DEEP_REVIEW_DOCUMENTED (source-level static audit; third-party code/test execution NOT_TESTED).  
**Disposition:** BLOCK public deployment or unfiltered applicant-data reuse; adapt only aggregate visualization and source-specific program metadata ideas.

## 1. Purpose and source scope

Willow is a 2019 Chinese-language US graduate-application information and visualization prototype. Its README describes categorizing more than 6,000 historic CS applicant records from two online communities by institution and program; this is an **author claim**, not an independently verified underlying dataset. The application models universities, programs, GRE/TOEFL/GPA score distributions and applicant outcomes. It is not a verified 2026 doctoral offer directory, scholarship database or evidence of current international funding.

## 2. Architecture and source inventory

The pinned recursive tree contains 38 tracked files: a React 16/TypeScript 3.6 client with Material-UI and Recharts, and an Express 4/TypeScript 3.6 server using MongoDB 3.x. The server's only application source and its manual test harness are server/src/index.ts and server/src/test.ts. The client includes page components for university/program views, numeric score charts, application comments and typed university/application objects. No migration framework, model validation schema, authentication middleware, production test suite or license file was present in the inspected tree.

The server loads credentials.json locally at startup (not tracked in the pinned tree), loads config.json, then connects to a MongoDB database called go_abroad and four collections: applicant, application, university and program. The client uses a literal HTTP API endpoint for the backend, so deployment is tied to a specific host. No live connection or personal dataset was accessed.

Evidence: [README](https://github.com/ssine/willow/blob/62638c154593689c57ab28bf3e93cec535112c39/README.md), [server](https://github.com/ssine/willow/blob/62638c154593689c57ab28bf3e93cec535112c39/server/src/index.ts), [typed models](https://github.com/ssine/willow/blob/62638c154593689c57ab28bf3e93cec535112c39/client/src/util/type.ts).

## 3. Pipeline and historical analysis model

The API exposes GET /applicant, /application, /university and /program, plus batch POST read endpoints. Each request accepts a serialized MongoDB filter. The frontend requests universities/programs, then applications and associated applicants by university or program. It classifies OFFER and AD as positive outcomes and all other values as negative, splits applicants into cohorts and renders GPA, GRE and TOEFL histograms, background cards and comments.

This is a descriptive visualization of **selected historic self-reported cases**, not an accepted-student probability model. There is no sampling denominator for all applicants, no reported verification of individual outcomes, no adjustment for repeated/duplicate identities, no 2026 application-cycle recrawl, and no scholarship/funding fields in the interface. The undergraduate GPA formats are stored as 4/4.3/100 scales, but cross-scale equivalence cannot be presumed.

## 4. Critical security and data-integrity findings

- **No authentication or authorization:** The Express server installs app.use(cors()) and exposes both read and write endpoints without any authentication middleware. GET endpoints can disclose all applicant documents; PUT /applicant, /application, /university and /program can insert or update records. If reachable outside an explicitly isolated trusted network, unauthorized access and data tampering are possible.
- **Client-controlled MongoDB queries:** The backend passes JSON.parse(req.query.filter) or JSON.parse(f) directly to collection.find(). Server-side allowlists, type checks, query complexity restrictions and MongoDB operator filtering are absent. This is an untrusted query-control boundary, not a safe search API.
- **Unvalidated writes:** The PUT handlers parse arbitrary JSON from req.body.data and merge it into existing documents through Object.assign(exist, data), then issue $set. There is no typed schema, ownership relation, field-level restriction, data provenance, revision/ETag check, or audit trail.
- **HTTP endpoint:** client/src/config.ts hardcodes a non-TLS HTTP service URL. Credentials may be absent, but historic applicant data transmitted through that connection would have no application-layer transport confidentiality guarantee.
- **Data quality:** Positive cohort labels use AD/OFFER, while all other outcomes—including wait-list—are treated as negative. This conflates distinct admissions stages. No validated funding/offer semantics, time-dependent outcomes or degree-specific subgroup inference are implemented.

No exploit was attempted; findings are limited to the static source contract and declared API.

## 5. Operational, error-handling and test limitations

The server loads credentials.json using fs.readFileSync at startup; that file is not in the inspected Git tree. Production configuration and dataset provenance therefore cannot be reconstructed from this checkout. The app makes MongoDB calls without explicit per-request try/catch in many routes. Returned error objects, malformed query JSON or unreachable database may cause rejected requests without controlled error responses. The TypeScript helper manually interpolates names/IDs into JSON filter strings, which can break with quotes or unusual characters.

The only server/src/test.ts is an imperative HTTP smoke harness containing actual PUT requests that mutate DB collections. It is **not a safe read-only test** and was not executed. There are no observed unit tests for histogram correctness, authorization, data import, source freshness or data security. Legacy dependency pins remain dated; the repository's five open Dependabot PRs target old library versions and do not constitute a current security assessment.

## 6. Privacy, source provenance and validity boundaries

The README names online forum sources and a historic cohort of approximately 6,000 records. There is no independently verified data license, consent scope, pseudonymization protocol, collection timestamp per case, source-content checksum, opt-out method or permission to republish raw applicant profiles. Public forum data are not automatically safe to expose in a searchable personal-profile database.

The repository shows historical score distributions and comments, not a reliable sample of rejected/non-applying candidates. The visualization can amplify survivorship and self-reporting bias. Do not use its histograms to estimate admission probability or to infer eligibility or funding for an individual applicant.

## 7. Comparison and transfer to PhD Atlas

Reusable aspects are a clean distinction between university, program, applicant and application entities; support for multiple GPA scoring conventions; explicit application-stage visualization; and cohort comparison.

A production replacement needs: authenticated and least-privilege access; filter schema validation with a strict allowable-operator set; suppression or aggregation of applicant-level PII; verified consent/source permission; deduplicated date-stamped cases; canonical program identity; explicit admission-state taxonomy (OFFER, AD, WL, REJ, UNKNOWN); separated scholarship/fee eligibility and actual offer dates; an auditable import/source manifest; independent validation against official current policies. Empirical admissions-rate inference requires a defined population denominator and a measurement design, not a frontend percentage.

Compared with institution-side portal sushil3710/PHD_Admission_Portal, Willow is a community admissions-history dashboard rather than a live administrative application system. Both demonstrate that convenience CRUD and dashboard components do not establish a secure evidence system. Unlike the source-first planner tools, Willow has no verified claim-to-source traceability.

## 8. Decision and verification limits

**DEEP_REVIEW_DOCUMENTED — reject as a deployed or applicant-specific decision engine.** The 38-entry tree, README, client/server manifests, entire core server, manual test harness, typed interfaces, query helpers, API configuration, application statistics and representative UI components, and recent issue/PR history were inspected. No MongoDB connection, historical applicant record, live deployment, browser build, unit test or vulnerability exploit was executed. The claimed 6,000+ source records and admission results remain unverified.
