# houwei1228/PhD_Fit — pinned source investigation

- Revision: `947d73c2b6a1dbba4a94d7e28063bde6a97248b5`
- Inspected on: 2026-11-12
- State: **DEEP_STATIC_READY_FOR_CANONICAL_RECONCILIATION**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: PENDING (do not count this session report as a canonical audited candidate)

## 1. Purpose

PhD_Fit is a CV-aware Streamlit assistant for finding, scoring and monitoring PhD positions; self-reported match scores are not admissions probabilities.

## 2. Architecture

Root tree contains Streamlit app, SQLite db.py, scoring.py, security.py, opportunity monitoring module and targeted tests.

## 3. Data flow

SQLite user/opportunity database, profile handling and scoring are separated from externally retrieved vacancy evidence.

## 4. Critical correctness

services/opportunity_monitor.py compares official target URLs and retrieves status/funding/deadline evidence using search and model-mediated extraction; model output is not independently authenticated official funding proof.

## 5. Identity and state

db.py contains duplicate-evidence and merging procedures; protect institution-specific requisition identity and applicant links from fuzzy-merge errors.

## 6. Security and privacy

security.py includes PBKDF2 password and Fernet encryption primitives; private CV transmission to external search/model providers needs explicit user consent.

## 7. Validation boundaries

Test source exists for dedup and monitoring, but code, tests, institutional vacancy sites and scheduled jobs were NOT executed.

## 8. Transfer verdict

Adopt explicit VERIFIED/UNKNOWN/CONFLICTED source gates, employer and requisition identifiers, review evidence stamps, and applicant-private boundaries before using opportunities as current facts.

## Pinned upstream source paths

- [README.md](https://github.com/houwei1228/PhD_Fit/blob/947d73c2b6a1dbba4a94d7e28063bde6a97248b5/README.md)
- [services/opportunity_monitor.py](https://github.com/houwei1228/PhD_Fit/blob/947d73c2b6a1dbba4a94d7e28063bde6a97248b5/services/opportunity_monitor.py)
- [db.py](https://github.com/houwei1228/PhD_Fit/blob/947d73c2b6a1dbba4a94d7e28063bde6a97248b5/db.py)
- [security.py](https://github.com/houwei1228/PhD_Fit/blob/947d73c2b6a1dbba4a94d7e28063bde6a97248b5/security.py)
- [tests/test_deduplication.py](https://github.com/houwei1228/PhD_Fit/blob/947d73c2b6a1dbba4a94d7e28063bde6a97248b5/tests/test_deduplication.py)
