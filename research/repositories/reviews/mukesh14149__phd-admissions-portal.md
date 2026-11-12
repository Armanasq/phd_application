# mukesh14149/PhD-Admissions-Portal — pinned source investigation

- Revision: `c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02`
- Inspected on: 2026-11-12
- State: **DEEP_REVIEW_DOCUMENTED — static source only; private records not inspected**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: RECORDED (source-level, not independently validated)

## 1. Purpose

JavaFX applicant/admin desktop admission demo; README claims grade/category-based applicant filters.

## 2. Architecture

Root contains sizeable CSV files Data_to_Import_with.csv and Feedback.csv, plus local CV/SOP folders. Their contents were NOT opened due to possible applicant PII.

## 3. Data flow

Application Controller.java copies user-uploaded CV and SOP into hard-coded /home/mukesh/... filesystem paths; code logs selected local file paths.

## 4. Critical correctness

Server Controller.java has input filtering and admission-selection rules, but no authoritative 2026/27 funding or institutional vacancy provenance.

## 5. Identity and state

Reuse only abstract applicant/admin state design after access controls, secure file storage and data validation. Runtime/DB and private CSV analysis not performed.

## Pinned upstream source paths

- [README.md](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/README.md)
- [src/application/Controller.java](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/src/application/Controller.java)
- [src/server/Controller.java](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/src/server/Controller.java)

## Deep static investigation — 2026-11-12

**Review status:** DEEP_REVIEW_DOCUMENTED — risk-focused complete inspection of the first-party Java controllers, launcher code, data model, README and tree metadata, without opening historical applicant CSV/PDF records or executing software. **Decision:** REJECT_AS_IS; reuse only conceptual form/filter workflow.

### 1. Research purpose and documentary boundary

Pinned upstream commit: [c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02](https://github.com/mukesh14149/PhD-Admissions-Portal/commit/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02). The README expressly states this is a **2015 assignment** to build local, non-web JavaFX applicant and administrator forms, rather than a current institutional recruitment service. Its filtering example combines marks, degree, and department; it neither discovers universities nor establishes funding, applicant eligibility, scholarship calls, tuition/fee coverage or confirmed offers.

### 2. Source topology and implementation model

The 23-file tree has two JavaFX application entrypoints (applicant `src/application/Main.java`, administrator `src/server/Main.java`), corresponding `Controller.java` classes and FXML views, a three-property `Expense` table-row class, archived CSV/backup files, an assignment PDF, and IDE metadata. The source stores applicant profiles as comma-delimited rows in a fixed local `src/Feedback.csv` file. The administrative controller copies and repeatedly filters those rows using temporary `template.csv` and `helper.csv`, renders filtered results in a table, and generates one text summary per row under a local `src/files/` path.

The application file attachment controls use JavaFX `FileChooser` and copy selected CV/SOP bytes to author-specific absolute folders with incrementing counters. This is a local machine prototype: no authenticated applicant account, server/database transaction model, remote application submission receipt, access policy or official source-claim ledger was established.

Sources: [README](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/README.md), [applicant controller](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/src/application/Controller.java), [administrator controller](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/src/server/Controller.java), [table record model](https://github.com/mukesh14149/PhD-Admissions-Portal/blob/c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02/src/server/Expense.java).

### 3. Dataflow and cross-component relationships

Applicant fields are read from FXML controls, validated through several nested if/try blocks, concatenated into CSV by manual string joining, then added to a temporary file copied from the prior ledger. `Enrollment_id` derives from the last row's fixed column index (59), not a transactional sequence. The controller then deletes the original ledger and renames the temporary output. Administrative `Result` performs serial exact-value and numeric comparisons over individual hard-coded CSV column indices; it materializes human-readable text files and populates the table with apparent enrollment identifiers, names and local file paths. A table click launches a local text editor to open the generated text file.

This single CSV serves simultaneously as the applicant write store and administrative search data source. The code does not distinguish *submitted to an official university* from *saved locally*; the success label says only “Database updated.”

### 4. Verified defects and safety failures

- **PII and repository artifact exposure:** The tracked tree contains two large applicant-like CSVs (`src/Feedback.csv` and `src/Data_to_Import_with.csv`) plus backups. Their contents were **not opened** because they may contain identifiable candidate data. Review scope intentionally avoids reproducing such records.
- **Non-atomic writes and lost-data risk:** Applicant saves rebuild `template.csv`, then call `f1.delete()` and `f.renameTo(f1)` without checking either return value; the code closes its writer **after** the rename attempt. An interrupted process, buffered writes, rename failure or concurrent save can leave stale, missing or corrupted data.
- **Unsafe CSV encoding:** Applicant strings are concatenated with commas and no quoting or escaping. Administrator parsing uses `line.split(",")` and fixed offsets through at least `c[59]`. A name/address with comma, quoted text or embedded newline can shift fields, truncate records and misapply filter results. The generated per-applicant text artifacts reuse those brittle indices.
- **Non-unique identity under contention:** The enrollment number is derived from the last stored record and incremented, with no file lock or database uniqueness constraint. Two concurrent saves may read the same previous ID or race replacing the same CSV.
- **Faulty numeric validation:** Several paths invoke `Double.parseDouble` then `Integer.parseInt` on the same marks/CGPA field, so valid fractional scores can be rejected. In the administrative filter, one tenth-percentage parsing check accidentally uses the twelfth-percentage text field, creating inconsistent validation.
- **Unverified attachments:** `upload`/`upload1` rename copied bytes to `.pdf` but do not verify the selected file is a PDF, its size, or its original MIME signature. `FileChooser.showOpenDialog` may return null and `getAbsolutePath` then fails; the source prints private local file paths in logs.
- **Destructive fixed-path cleanup:** Administrator `back` blindly iterates and deletes files from a hard-coded directory and then deletes other hard-coded folders. There is no scoped temporary-directory ownership marker, user confirmation or check whether `listFiles()` returned null. Misconfigured folders may result in unrelated local file deletion.
- **External editor invocation without structured argument control:** The table-click handler passes a local path assembled from data to `Runtime.getRuntime().exec("gedit " + k)`. This does **not** use a shell by default; nevertheless it exposes an unvalidated file path to a subprocess and can break for filenames containing spaces or options. Avoid interpreting it as verified arbitrary shell execution.
- **No multi-user authorization or audited transitions:** There is no source-supported login, document access policy, object ownership check, applicant consent/retention scheme, encrypted candidate store, or canonical source proof for any vacancy/funding assertion. Admin selection results are simply a local filter, not admissions decisions.

### 5. Operational and test coverage

The project is tied to local JavaFX/FXML and author-specific filesystem paths. The source tree lacks a formal dependency lock/build/test suite, concurrency test, input-fuzzing corpus, invariant checker or privacy redaction fixture; the IDE project descriptors do not substitute for reproducible CI. No JavaFX UI launch, compilation, CSV import, file copy, editor process, deletion, PDF rendering, or source-link web visit was executed. The README's grade and deadline examples are desired behavior, not verified runtime test results.

### 6. Privacy, provenance and time validity

No attempt was made to inspect or enumerate the contents of the historical `Feedback.csv`, `Data_to_Import_with.csv`, their backup, or the assignment PDF. Only names and file sizes from the public tree were used to assess the risk boundary. The 2015 test data and workflow have no standing as proof that any university will accept a 2026/27 application, and there are no authoritative admissions-policy or funding-source snapshots.

### 7. Cross-repository comparison and transfer to PhD research operations

Compared with `tarun14110/system-for-PhD-Admissions` (another legacy servlet/flat-file application-filtering assignment), this repo is a genuine local JavaFX GUI, but both rely on positional delimiters, hard-coded local paths and weak identity/integrity guarantees. Compared with `saiPraveenMeda/phdAdmissions2019`, it lacks the latter's Django domain entities and roles while avoiding a networked server. None is a valid source for current scholarship eligibility or funded vacancies.

For PhD Atlas, retain only the idea of a structured applicant form, source-specific evidence checklist, and compound filter conditions. Replace the file pipeline with a typed transactional schema, stable opaque candidate/application keys, role-scoped storage, private encrypted documents, input and PDF MIME checks, idempotent submitted-state transitions, non-destructive import/export, and authenticated document retrieval. Preserve an official submission confirmation separately from the local form's save status.

### 8. Disposition and verification boundary

**DEEP_REVIEW_DOCUMENTED — BLOCK operational adoption.** Static inspection of the full first-party Java controllers and codebase shape is complete enough to establish architecture, decision flow, critical risks and transfer principles. The archived personal data and binary PDF were intentionally not read. No build, security experiment, live employer verification, current policy lookup, application action, or third-party runtime test occurred; this is an engineering audit rather than a claim that the real system was deployed or compromised.
