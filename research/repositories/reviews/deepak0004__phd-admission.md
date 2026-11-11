# Deep static audit — deepak0004/PhD-Admission

**Inspected:** 2026-11-12. **Upstream commit:** [`7adbc3582e88f81bf8e73babe6283c9645b1598f`](https://github.com/deepak0004/PhD-Admission/commit/7adbc3582e88f81bf8e73babe6283c9645b1598f). **Git tree:** `453a32d34a08973586a765fedcc4bf22b6267519`. **Review state:** DEEP_REVIEW_DOCUMENTED for static architecture, endpoints, persistence, identity, applicant data and project scope; no runtime, OAuth or exploit test. **Adoption:** REJECT_SOURCE_AS_PRODUCTION; architectural and privacy anti-pattern reference only.

## 1. Identity, history, architecture and inspection coverage

The repository is an **Eclipse/Tomcat 8 course project**, not an operating university admissions system. Its [README](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/README.txt) instructs an applicant to log in, fill mandatory fields and submit; a separate servlet filters submitted entries. The last inspected commit was **16 December 2015**, so the source provides historical implementation evidence, not current admission dates, scholarships or policies.

The pinned Git tree contains two Eclipse Java web projects, `GLogin/` and `adminfinal/`, compiled Java `.class` files, HTML forms, servlet descriptors, and tracked plain-text sample files under paths named `Data`, `Cv` and `Sop`. Reviewed all six Java servlet source files and the admin `WEB-INF/web.xml` in relevant detail, plus README, tree, metadata and reported issue/PR state. Embedded sample files were **not read or republished** because they may contain applicant information. HTML form bodies were inventoried rather than exhaustively parsed. No authenticated or private service was accessed.

## 2. Actual dataflow, workflow and persistence model

The `GLogin` project implements an applicant-facing Google sign-in redirect ([Login.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/Login.java)) and a callback ([Verify.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/Verify.java)). The callback exchanges an authorization code, obtains identity data, scans a local text-based identity register and loads the matching application record. `WriteData.java` reads many separate HTTP form fields, assembles delimited text, assigns application-style record identifiers, writes files and accepts applicant file uploads. These are local submission-record writes, not confirmed receipts from a university portal.

The `adminfinal` project contains a separate sign-in implementation, another callback, and [filteredcontent.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/adminfinal/src/admin/filteredcontent.java), which scans delimited application records and applies request-supplied filters across demographics, programme/education metrics and date fields. The admin [deployment descriptor](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/adminfinal/WebContent/WEB-INF/web.xml) exposes distinct servlet paths including `/filteredcontent`. There is no relational schema, transaction or official admissions API in the inspected project.

## 3. Authentication, authorization and credential boundary

The two [verification handlers](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/Verify.java) contain literal OAuth client-identification/secret configuration embedded in source code. **No credential values are reproduced here; validity was not tested.** The callback extracts OAuth response fields using positional `split` and substring operations rather than a structured parser and does not visibly implement a login-state nonce binding or dedicated authenticated principal validation for downstream file access.

[filteredcontent.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/adminfinal/src/admin/filteredcontent.java) creates an HTTP session but does not independently check an authenticated administrator role before reading the applicant index. The admin `web.xml` does not declare a servlet `security-constraint`, `login-config`, or authentication filter mapping. Therefore the observed implementation lacks a demonstrated **server-enforced route authorization boundary** for the applicant index. This is a source-based access-control gap, **not** proof of a live exploit, functional credential, or publicly running system.

Adopt neither the committed OAuth configuration nor presumed admin access control. Use delegated OAuth/OIDC libraries with nonce/state/PKCE as applicable, server-side verified sessions, authorization policies on every read/write and private secret management.

## 4. Applicant data storage, upload and confidentiality

[WriteData.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/WriteData.java) writes applicant fields to a plain-text file derived from a generated ID, and its multipart handler extracts an uploaded filename from `content-disposition` before constructing file destinations. No canonical path containment, extension/MIME allowlist, application byte-size limit or cryptographic document storage boundary was identified in those operations. The repository itself tracks sample files under the admin web application's `WebContent/Data`, `Cv`, and `Sop` directories, and application data are persisted in or referenced from web-application paths instead of a separate protected candidate-data store.

This makes it unsuitable for transferring to a public research repository: applicant records, transcripts, CVs, statements of purpose, identities and references must stay in private access-controlled storage, not static web content or Git history. We did not inspect the contents of sample applicant records and cannot establish whether any identify real persons. Before adopting this type of design, add upload stream limits, randomized server filenames, path containment, scoped ACLs, retention/deletion policy, encryption as required and private backups.

## 5. Consistency, correctness and output integrity

In [Verify.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/Verify.java), the next record identifier is calculated after scanning the current text register and incrementing the last observed number. This is not atomic: concurrent applicant sessions could produce duplicate IDs or overwrite records. `WriteData.java` performs multiple file operations without a shared transaction/rollback, so index and document files may diverge on failure. The filter servlet parses delimited text by positional array indexing and converts numeric inputs via `Float.parseFloat` without a typed schema or systematic malformed-record recovery.

Both applicant and administrator handlers emit fragments of identity/application values into HTML with `out.println`; robust HTML context encoding was not established. No versioned applicant events, immutable document snapshots, independently evidenced submission receipts, or authoritative university status feed exists. Avoid treating a local **submit** button as an institutional application receipt.

For production use, require relational constraints or transactionally consistent event storage, idempotency keys, safe text rendering, validated typed fields, database isolation, and append-only proof-backed application transitions.

## 6. Source-quality, maintenance and empirical verification

The inspected snapshot contains Eclipse project metadata, compiled Java binaries and Tomcat 8 web content; no build-system lockfile, continuous integration, reproducible test suite, threat model or evidence-provenance fixtures were found in the tree. No upstream issue or pull-request result appeared in the inspected repository searches. Historical project documentation is minimal and does not establish modern OAuth interoperability, authorization, concurrency, deployment hardening or current support.

The audit is **static**: no Tomcat server, OAuth authentication, private applicant data, upload test, browser security test, admin access bypass, or production endpoint was executed. Security concerns describe source logic and missing controls, not confirmed exploitation.

## 7. Transferability and relationship to other PhD tooling

**Reusable concept only:** separate applicant form completion, document collection, and administrator-facing screening. The broad data fields suggest a workflow that distinguishes identity, educational history, funding requests and stage. However these need privacy-preserving schemas and clear applicant/administrator responsibility, not the source's delimited-file implementation.

Compared with [PhDBench source findings](https://github.com/Armanasq/phd_application/blob/main/research/sessions/20261112-phdbench-keith-4e23/reviews/nikhil-rao20-phdbench.md), this project lacks modern multi-user authorization even at the level of Firestore rules. Compared with the [local-first command center](https://github.com/Armanasq/phd_application/blob/main/research/sessions/20261112-0031z-gpt6-b/fsuitoal-command-center.md), it lacks atomic migrations, fail-closed private paths and tested domain models. All three still require independently verifiable applicant action and official-source evidence.

For `phd_application`, enforce a strict separation: public opportunity/source intelligence → private candidate record → explicit application approval → external portal action → immutable verified receipt. Do not store or expose candidate inputs within the public Git repository.

## 8. Final decision, evidence and outstanding limitations

**Decision: REJECT_SOURCE_AS_PRODUCTION.** This is a genuine PhD application-course implementation, not a false-positive repository: it demonstrates a two-role applicant/admin interface and enough code to identify security, privacy and consistency limitations. It also does **not** provide open vacancies, funding, updated admission requirements, deployment-quality software or evidence of actual university submissions.

Evidence: pinned [README](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/README.txt), [GLogin/Verify.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/Verify.java), [GLogin/WriteData.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/GLogin/src/WriteData.java), [adminfinal/filteredcontent.java](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/adminfinal/src/admin/filteredcontent.java), [admin deployment descriptor](https://github.com/deepak0004/PhD-Admission/blob/7adbc3582e88f81bf8e73babe6283c9645b1598f/adminfinal/WebContent/WEB-INF/web.xml). Source-level findings remain untested under live authentication or concurrent requests; old commit date and no CI preclude any current-software guarantee.
