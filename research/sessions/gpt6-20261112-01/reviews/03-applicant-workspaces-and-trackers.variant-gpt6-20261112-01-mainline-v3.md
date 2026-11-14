# Applicant workspaces, trackers and preparation templates

Session: gpt6-20261112-01  
Review date: 2026-11-12  
Static inspection only; no app or test suite was executed.

## 1. imranbinyounos/PhdApply — GradKit Pro

- Upstream: https://github.com/imranbinyounos/PhdApply
- Snapshot: `091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e` (main)
- Inspected: README, SwiftUI views, `GradKitStore`, model definitions, CSV services, app entry point and test files.
- Review state: `STRUCTURED_SOURCE_REVIEW`; no runtime validation.

### Product and architecture

A local macOS graduate-application workspace with customizable tables, application stages, university/professor/scholarship sections, filtering, sorting, a Kanban board, dashboard summaries and CSV import/export.

The active visible UI is driven by `GradKitStore`, which stores section data as JSON-encoded dictionaries in `UserDefaults`. The project also declares SwiftData models and configures a SwiftData `ModelContainer`, but the inspected main UI does not use that model context. This creates two parallel persistence architectures, one of which appears unused by the current UI.

### Findings

- `GradKitStore` uses flexible `[[String:String]]` row dictionaries and custom column definitions. This is easy to customize but lacks stable relational IDs and typed field semantics.
- The table sorts/filters rows for display, then passes the displayed enumeration index to update/delete operations on the underlying unsorted array. After a filter or sort, editing/deleting a visible row can mutate a different stored row. This is a data-integrity defect.
- Column identity is derived from its display name. Renaming a column changes its identity; duplicate names are not consistently rejected and can overwrite row values.
- Custom columns can remove important fields unless mandatory columns are enforced centrally.
- CSV import processes line-by-line, so quoted multiline cells cannot round-trip safely. Exported text containing newlines can break subsequent imports.
- The SwiftData `ApplicationRecord` model and `GradKitStore` model duplicate application concepts. Status/stage fields can diverge if both are ever used.
- `UserDefaults` is local and simple, but it is not a database with transactions, indexed queries, robust migration or automatic backup. Frequent full-state writes can become expensive as the dataset grows.
- The app opens a `mailto:` draft rather than automatically sending email, which is a safer human-controlled boundary.
- No meaningful automated coverage of row identity, sorting/filtering mutation, CSV round-trip, migrations or persistence behavior was established.

### Adoption decision

Useful patterns: local-first operation, user-configurable columns, stage views, and exportability. Replace row-index addressing with stable row IDs; normalize core entities and relations; version the schema; test import/export round-trips; use a single authoritative persistence layer; add backup/restore and evidence fields for funding/deadlines.

Evidence: [GradKitStore](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/GradKitStore.swift) · [GradKit views](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/GradKitProViews.swift) · [models](https://github.com/imranbinyounos/PhdApply/blob/091cd1fe3517f0e1805d17cb5e0958e5cf50cd2e/PhdApply%20Final%20code/PhdApply/Models.swift)

## 2. ianouhi17-ctrl/phd-application-workbench

- Upstream: https://github.com/ianouhi17-ctrl/phd-application-workbench
- Snapshot: `4bece08790a727a9abce1e6eb400715234b0b731` (main)
- License: MIT.
- Inspected: README and 18 Markdown templates covering weekly plans, timelines, materials, school selection, advisor notes, CV, research summary, research narrative, outreach, meetings, SOP, recommendation packets, submission checks, interviews and offer comparison.
- The central XLSX workbook was identified in the tree but its binary contents were not inspected.
- Review state: `STRUCTURED_DOCUMENT_REVIEW`.

### Workflow methodology

The workbench follows a deliberate preparation sequence:

1. Establish the applicant's research identity and one-page research narrative.
2. Build a program/school list using selection principles.
3. Create structured advisor reading notes and research-fit records.
4. Prepare an academic CV and research summary.
5. Conduct supervisor outreach and prepare meeting notes.
6. Maintain a master SOP and reusable personal/diversity evidence bank.
7. Assemble recommender packets and reminder messages.
8. Run a submission checklist, then prepare interviews and offer comparisons.

### Transferable strengths

- It decomposes the application into durable artifacts rather than treating the SOP as the entire application.
- Advisor research notes, meeting preparation, recommender packets and offer comparisons are explicit, reusable work products.
- The central workbook is intended to act as an operational control surface for weekly planning and status tracking.

### Limitations

- The content is US-centric and explicitly oriented to Fall 2027 graduate applications. It must not be copied as policy for Canada, UK, Ireland, Luxembourg, Switzerland, Norway, New Zealand or Australia.
- Advice such as target-school counts, advisor outreach volume and weekly quotas is heuristic, not a validated universal standard.
- The templates do not require claim-level evidence, source dates, funding confirmation, international fee status, eligibility gates or deadline timezones.
- The binary workbook is not inspected, so formulas, data validation, conditional formatting and workbook-level integrity remain unknown.
- Templates are scaffolding, not evidence of successful admission or funding.

### Adoption decision

Adopt the lifecycle decomposition and artifact templates as a planning pattern. Rebuild the control workbook around country-specific opportunity types, evidence provenance, verified funding, cycle/year, timezone-aware deadlines, eligibility and explicit uncertainty. Do not inherit US deadlines or quotas.

Evidence: [README](https://github.com/ianouhi17-ctrl/phd-application-workbench/blob/4bece08790a727a9abce1e6eb400715234b0b731/README.md) · [advisor notes](https://github.com/ianouhi17-ctrl/phd-application-workbench/tree/4bece08790a727a9abce1e6eb400715234b0b731/01_%E9%80%89%E6%A0%A1%E4%B8%8E%E5%AF%BC%E5%B8%88) · [submission checklist](https://github.com/ianouhi17-ctrl/phd-application-workbench/tree/4bece08790a727a9abce1e6eb400715234b0b731/06_%E7%94%B3%E8%AF%B7%E6%8F%90%E4%BA%A4)

## Mainline overlap — drPod/phd-application-tracker

A source-level review is already present on `main` under `research/repositories/reviews/drpod__phd-application-tracker.md`. This session's exploratory notes are withdrawn from the PR to avoid duplication.

## 3. ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER

- Upstream: https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER
- Snapshot: `18b4c4a163bbd908ff434d47a7cf570686962e83` (main)
- Inspected: README, JS data and page modules, application/job/task logic, API wrapper and FastAPI backend.
- Review state: `PRELIMINARY_FOCUSED`.

### Architecture and actual behavior

A multi-module career/academic tracker with jobs, PhD-CS opportunities, applications, tasks, interviews, calendar, analytics and settings. The visible data is predominantly hard-coded demo data and browser `localStorage`; the FastAPI backend endpoints are placeholders returning empty/demo responses and are not the system of record for the UI modules.

### Findings

- The demo dataset explicitly labels itself as demonstration data. It contains static opportunity examples without vacancy-specific source links, source dates, funding evidence or eligibility verification.
- Application, job, PhD and task modules store records under separate localStorage keys. There is no normalized relation from a discovered job/program to an application record, so the lifecycle is not evidence-linked.
- User-entered fields are interpolated into `innerHTML` in several rendering paths. This creates stored DOM-XSS risk if untrusted/imported values are rendered.
- The page router contains duplicated/overlapping conditions; some later branches are unreachable after earlier conditions match.
- The API wrapper checks connectivity, but the application modules primarily use local demo state rather than the backend. The presence of a FastAPI directory should not be interpreted as a working persistence layer.
- No authentication, multi-user model, backup/export strategy, or source-verification lifecycle was established.

### Adoption decision

Useful as a broad information-architecture prototype. Do not use its static records as opportunity evidence. A mature implementation needs one normalized opportunity/application model, source lineage, secure rendering, migrations, export/backup and explicit API integration.

Evidence: [demo data](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/data.js) · [application module](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/applications.js) · [API wrapper](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/js/api.js) · [FastAPI entry point](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/blob/18b4c4a163bbd908ff434d47a7cf570686962e83/backend/app/main.py)

## Cross-repository conclusion

Applicant workspaces are strongest when they preserve user-owned decisions and evidence while separating them from external opportunity data. Local-first storage is useful, but it still needs stable IDs, migrations, backups, secure file storage and data-integrity tests. Static demo data must never be promoted to verified opportunity records.