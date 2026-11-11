# mukesh14149/PhD-Admissions-Portal — pinned source investigation

- Revision: `c0eb4ee3c1a21669f1d66c57c1f7dfd433857e02`
- Inspected on: 2026-11-12
- State: **PRELIMINARY_PRIVACY_BOUNDED**
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
