# repalash/PhD-Portal — deep static review

**Review date:** 2026-11-12. **Pinned upstream revision:** [c47f45e7efa2fb7a609560340c25d858f829e7c6](https://github.com/repalash/PhD-Portal/commit/c47f45e7efa2fb7a609560340c25d858f829e7c6).  
**Review state:** DEEP_REVIEW_DOCUMENTED — source-level review only, no application execution.  
**Category:** historical desktop admissions form and administration workflow.  
**Verdict:** reference historical domain decomposition, reject persistence mechanism.

## 1. Goal and scope

A JavaFX desktop prototype with distinct Applicant and Admin applications for PhD admission at IIIT Delhi, implemented around 2015. The applicant UI gathers education, research interests, identity, preferences and supporting document paths; the admin UI filters records by applicant attributes. The project has about 40 source/resource files and no verified current official deployment.

## 2. Data architecture

`PhDApplication` is a large mutable Java object storing applicant demographic, education, score, project and preference fields. The applicant controller converts form inputs to this object then appends JSON-like content to a local file. Administrator views parse the stored records into in-memory lists and filter by equality or numeric comparisons. The source does not demonstrate an RDBMS, entity uniqueness constraint, append-only outcome ledger or explicit admission-year relation.

## 3. Enrollment ID generation and concurrency

The applicant controller reads `./database/enrollno.dat`, increments the integer and rewrites it using `Files.write`. This is **not an atomic compare-and-swap transaction**: concurrent applicant processes can generate the same enrollment ID or overwrite one another's counter. There is no file lock, database sequence, idempotency key or conflict/retry path.

`PhDApplication.appendToFile` uses `Files.write(..., StandardOpenOption.APPEND)` to store a record, but an append does not by itself guarantee complete record integrity under interruption or concurrent appends. A malformed/truncated row could poison future reads.

## 4. Data interpretation and filtering

The administrative filter applies numerous hardcoded equality and percentage comparisons, with separate GPA/CGPA/marks handling and time/date fields. The code uses date strings and fixed year dropdown values ending at 2015. It is not safe to treat those enumerations as modern admissions criteria. Some applicant fields depend on toggle selection and may fail with missing input. Source-level tests should check country/nationality, marks units, date parsing and missing values before further use.

## 5. Privacy and document handling

The applicant flow stores full name, address, birth date, nationality, gender, category, phone, university/board history and preferences. It also writes uploaded SOP and CV file content into locally named paths based on enrollment ID. The inspected desktop code does not establish encrypted persistence, per-applicant access control, redaction/retention, file type validation, or authenticated staff review. Distribution of the local database file would expose personal data. No private applicant files were opened or redistributed in this audit.

## 6. Tests and operations

The repository has JavaFX FXML and application classes but no evidenced repeatable CI, tests, release pipeline or current license for production reuse. Local relative files and hardcoded dropdown options make cross-machine installation and administration brittle. No compilation or UI workflow was run.

## 7. Evidence boundaries

Reviewed the complete tree, `Application/src/.../PhDApplication.java`, `Applicant/src/.../Controller.java`, `Admin/src/.../AdminFilterController.java`, `Admin/src/.../Main.java` and project structure. Claims above derive from implementation; no live university admission rules, deployed application state, applicant outcome or identity data were verified.

Pinned evidence: [PhDApplication.java](https://github.com/repalash/PhD-Portal/blob/c47f45e7efa2fb7a609560340c25d858f829e7c6/Application/src/com/iiitd/ap/project/application/PhDApplication.java), [applicant controller](https://github.com/repalash/PhD-Portal/blob/c47f45e7efa2fb7a609560340c25d858f829e7c6/Applicant/src/com/iiitd/ap/project/applicant/Controller.java), [admin filter](https://github.com/repalash/PhD-Portal/blob/c47f45e7efa2fb7a609560340c25d858f829e7c6/Admin/src/com/iiitd/ap/project/admin/AdminFilterController.java).

## 8. Transfer decision

Useful domain ideas: separate applicant and administrator roles, normalized score types, structured school background, research preferences and explicit form-submission acknowledgement. Reject file-based enrollment counters, uncontrolled personal data, direct file appends, and current-policy assumptions derived from static 2015 form fields. Implement private event-backed per-user records, transactional unique IDs, academic cycle, verified requirements and review audit trails.

**Validation:** static source review; no tests or live application exercised.
