# shubhamGoswami/Phd — deep static review

**Review date:** 2026-11-12. **Pinned upstream revision:** [94f6e9beea373f0b499ac821d4e967fc288fb11d](https://github.com/shubhamGoswami/Phd/commit/94f6e9beea373f0b499ac821d4e967fc288fb11d).  
**Review state:** DEEP_REVIEW_DOCUMENTED — static source inspection, no runtime tests.  
**Category:** historical institution-specific admissions administration.  
**Verdict:** reject direct reuse; limited workflow-domain learning.

## 1. Purpose and scope

A 2015 Java Servlet/JSP IIIT Delhi PhD admissions prototype accepting applicant data, supporting multi-tab submission and administration/search. A 50-file Eclipse web project with form JSPs, servlet handlers, web.xml mappings, and Java entity/filter components. Not a live official application or funding source.

## 2. Architecture and dataflow

Applicant views collect educational history, board scores, category, nationality, date of birth, email, stream, GATE scores, and preferences. The server stores and filters XML records through `Entry` and several tab-specific servlets. The admin filter reads entries marked submitted, materializes them into an in-memory list, applies request-field filters and forwards the result to `table.jsp`. Uploaded file handling is limited to a session flag in the inspected `upload` servlet, not a verified secure file pipeline.

## 3. Authentication and session risk

The admin `cred` servlet compares submitted username/password to hardcoded literals and sets `admin=1` in the HTTP session. The OAuth Google Plus integration contains a hardcoded client secret in source. Secret values are deliberately not copied here. There is no evidenced credential rotation, secure externalized configuration, rate limiting, role permission model or current OAuth provider support. A prototype authentication route must not be exposed to applicants.

## 4. Concurrency and data integrity

`filter` extends `HttpServlet` but stores `list`, `finalList`, `rmList`, `dates` and many request-specific filter fields as mutable **instance variables**. Servlet instances are typically shared across requests, so concurrent administrators can overwrite each other's filter state and race over applicant result lists. This is a direct source-level thread-safety defect. Make all request-specific data local rather than servlet fields.

The filter hardcodes an absolute workstation XML location (`/Users/.../Desktop/tmp/temp.xml`); source handling has no configured deployment storage contract or DB-level transaction/uniqueness. Several field checks dereference `.isEmpty()` without a consistent null guard; failures are frequently caught broadly and transformed to HTTP 404, masking actual server and schema errors.

## 5. Privacy and verification

Admissions rows include contact details and protected/sensitive demographic and academic fields. `show` searches XML by applicant email; the inspected path does not demonstrate robust object authorization for each email lookup. An old session flag alone is insufficient for access control. XML parser creation does not show a secure-XML feature policy, making external-entity and external-document resolution worth testing before any migration. These are static design observations; no live exploit performed.

## 6. Functional consistency

The recorded applicant fields use raw strings rather than typed score units and cycle-specific requirements. Filtering by GATE, board percentages, dates and categories is hardcoded to 2015-era forms and may no longer align with current admission categories or policy. There are no source-backed funding awards, supervisor hiring statements, current deadline notices or international eligibility claims.

## 7. Evidence and validation

Inspected the recursive tree and `web.xml`, `Entry.java`, `filter.java`, `show.java`, `cred.java`, `upload.java`, selected tab handlers and legacy OAuth component. No automated test suite/CI or deployable environment was established; source was not compiled and no applicant submission was performed. Do not treat historical code as active institution infrastructure.

Pinned evidence: [web.xml](https://github.com/shubhamGoswami/Phd/blob/94f6e9beea373f0b499ac821d4e967fc288fb11d/WebContent/WEB-INF/web.xml), [filter](https://github.com/shubhamGoswami/Phd/blob/94f6e9beea373f0b499ac821d4e967fc288fb11d/src/com/iiitd/filter.java), [admin credentials handler](https://github.com/shubhamGoswami/Phd/blob/94f6e9beea373f0b499ac821d4e967fc288fb11d/src/com/iiitd/cred.java), [application entity](https://github.com/shubhamGoswami/Phd/blob/94f6e9beea373f0b499ac821d4e967fc288fb11d/src/com/iiitd/Entry.java), [applicant lookup](https://github.com/shubhamGoswami/Phd/blob/94f6e9beea373f0b499ac821d4e967fc288fb11d/src/com/iiitd/show.java).

## 8. Transfer decision

Retain only the distinction between applicant form, submission confirmation, administrative review and filtered decision queue. Build a modern typed schema with authorization per applicant, privacy-preserving documents, configurable source-specific requirements and deadline/cycle data. Do not reuse hardcoded credentials, global servlet state, workstation XML files or historical categorical assumptions.

**Runtime validation boundary:** none; deep refers to source inspection only.
