# tarun14110/system-for-PhD-Admissions — legacy institutional applicant workflow audit

**Reviewed:** 2026-11-12  
**Repository:** https://github.com/tarun14110/system-for-PhD-Admissions  
**Repository ID:** 50530193  
**Pinned revision:** [afef1f602872a935ef207c66bfb8f9163d69015c](https://github.com/tarun14110/system-for-PhD-Admissions/commit/afef1f602872a935ef207c66bfb8f9163d69015c)  
**Review state:** DEEP_REVIEW_DOCUMENTED — Java source/dataflow and admin-filter static review; runtime and applicant archive contents NOT_TESTED.  
**Decision:** Reject as a deployed admissions system; reference only its applicant form and multi-criterion filtering concepts after redesign.

## 1. Problem and source truth

A 2015–2016 teaching prototype for submitting doctoral application details and screening applicants on attributes such as qualifications and background. The README describes a locally deployed JavaFX graphical interface, but the actual source contains annotated **Java HttpServlet** components; its implementation does not substantiate that architecture claim. It is not a 2026 admissions portal or a source of current funded openings.

## 2. Architecture and inventory

The pinned recursive tree contains 36 files: Java servlet source under src/Client and src/Admin; Eclipse web project settings; archived compiled .class outputs; import/conversion utility; screenshot samples; and bundled CSV/text application records. Main components include /Form, /Form2, /Form3 for applicant data capture, /Admin and /Filter for query form and request-session filters, /Filter2 for filtering, and /PerInfo and /EduInfo for applicant detail display/edits. There is no observed database connection in the inspected core; the design stores serialized personal fields in flat files at a Windows-specific absolute path.

Evidence: [README](https://github.com/tarun14110/system-for-PhD-Admissions/blob/afef1f602872a935ef207c66bfb8f9163d69015c/README.md), [Form2](https://github.com/tarun14110/system-for-PhD-Admissions/blob/afef1f602872a935ef207c66bfb8f9163d69015c/src/Client/Form2.java), [Filter2](https://github.com/tarun14110/system-for-PhD-Admissions/blob/afef1f602872a935ef207c66bfb8f9163d69015c/src/Admin/Filter2.java).

## 3. Applicant and reviewer dataflow

Applicant UI fields are read from HttpServletRequest in Form2 and Form3 and appended using FileWriter to one shared D://100.txt file. Fields are delimited by semicolons, without an observed schema/version, quoting policy or atomic record boundary. /Admin renders search criteria, /Filter stores submitted criteria in HttpSession, and /Filter2 inspects data fields and applies filters. The repository also contains an independent CSV importer that rearranges and normalizes columns to an output text file, using hard-coded Unix paths.

File scope and application identity are not bound to an independently authenticated applicant account. Distinguish these illustrative student records from any verified real application.

## 4. Source-supported security and correctness risks

- **Sensitive data in plaintext:** Applicant and academic data are written to a shared unencrypted local text file with absolute drive path. Concurrent appends and multi-step form writes are not transactional; an interruption can mix or truncate records.
- **No demonstrated access control:** Inspected admin and applicant servlet methods do not show authentication or row-level authorization for reading/editing applicant data. They are unsuitable for access from a shared network.
- **Fragile format:** Form2/Form3 manually append semicolon-delimited fields, while parts of Filter2 and the extra importer split on commas. There is no centralized parser or escaping for delimiters/newlines, so field offset and integrity assumptions can break.
- **Shared servlet mutable state:** Filter2 declares numerous filter values as servlet instance fields and sets them during request handling. Servlets may process requests concurrently, risking filter state bleed between users.
- **Null and bounds errors:** Source code calls .equals on potentially missing request parameters and indexes split record arrays with hard-coded positions; missing/short records can fail.
- **Path portability:** Hard-coded D://100.txt and /home/tarun/workspace/IIITD source paths prevent reproducible deployment on other machines.
- **Client-view mismatch:** README advertises JavaFX but the inspected source relies on HttpServlet and HTML string output, with old HTTP-linked browser assets. The correct deployment packaging and validation have not been established.

These findings are based on code paths; no file access, real applicant data processing, runtime exploit or remote deployment was attempted.

## 5. Testing and verification gaps

There are compiled artifacts and screenshots, but no verified automated CI, regression tests, privacy/redaction fixture corpus or transactional correctness tests in the inspected tree. It lacks dependency locking and a controlled build pipeline for a modern servlet server. GitHub repository history is from 2015–2016; its behavior cannot establish current PhD admissions criteria or acceptance outcomes.

## 6. Privacy and source governance

The repository tree contains applicant-like CSVs, archived text and PDFs. **None of their contents was read or reproduced.** They could include real personal identifiers and are not required to understand program logic. The absence of verified consent, rights, access control and retention terms blocks ingestion into the PhD application evidence corpus. Static review is sufficient to classify technical architecture without exposing records.

## 7. Comparative analysis and reusable elements

Relative to sushil3710/PHD_Admission_Portal (PostgreSQL and JWT roles), this early prototype uses flat-file persistence and weak per-session filter state. Relative to Willow (MongoDB and unprotected API), it has similarly insufficient access control but offers directly a multi-criterion applicant filtering surface. Reuse only the conceptual form taxonomy and reviewer-filter UX, not the source implementation.

A production architecture would use a normalized Applicant/Application/Document/Review schema, per-applicant identity and RBAC/row ownership; schema-validated typed input; private encrypted document storage; per-revision audited transitions; deterministic filter queries; CI fixtures using synthetic data; and explicit graduation/admissions cycle metadata.

## 8. Decision

**DEEP_REVIEW_DOCUMENTED — REJECT_AS_IS.** Inspected README, full recursive tree, applicant and admin servlet source, parsing/filters, import utility and source-referenced risk areas. Not done: recompile/build, deploy server, run tests, inspect applicant CSV/PDF content, verify historical outcomes or confirm current institutional policies. Source evidence supports software design claims only, not actual funded doctoral admissions.
