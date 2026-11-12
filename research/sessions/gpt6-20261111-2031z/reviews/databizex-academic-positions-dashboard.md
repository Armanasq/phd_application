# Repository review: DataBizex/academic-positions-dashboard

## Review disposition
- Depth: preliminary; blocked on native Power BI binary inspection.
- Pinned upstream commit: 7472058b0c0e704c676eb4be45de207fcc5f1f43.
- Repository has 5 tracked files: README.md, screenshot.png, LICENSE, a Power BI .pbix report, and an Excel .xlsx dataset.
- Last pushed: 2026-10-05. MIT license; no issues or pull requests.

## Purpose and visible claims
The README describes an interactive Power BI dashboard of more than 3,000 PhD/postdoc vacancies across 20+ countries. These figures are unverified claims, although the repository does include an Excel dataset. The dashboard is presented as an exploratory analytics layer for academic job opportunities, with filters and visual summaries.

The screenshot is a visual preview, not a source of verified metrics. An Excel dataset is included, but no independently readable API, SQL schema, ETL code, data dictionary, or validation report is published separately.

## What could be verified
- Repository file inventory and metadata.
- README's claimed data scope and intended analytics.
- Presence of native Power BI report and spreadsheet dataset artifacts.
- No source-level extraction or independent validation of the Power Query M steps, DAX measures, model relationships, refresh configuration, source connectors, or raw vacancy records was possible in this session.

## Blocking reason
The report is packaged in a .pbix binary, and the dataset is supplied as an .xlsx workbook. The available GitHub file-reading interface is text-oriented, and the execution environment cannot clone/download and inspect those files. Consequently, this repository must not be classified as deeply investigated.

## Required follow-up
1. Download the pinned .pbix and .xlsx artifacts into an isolated workspace.
2. Extract the Power BI model metadata, tables, relationships, calculated measures, and Power Query M expressions.
3. Trace the actual source of the 3,000+ jobs, country coverage, timestamps, duplicate policy, and update cadence.
4. Validate measures against underlying data and check missing/expired vacancy records.
5. Inspect whether the template leaks credentials or contains private source paths.
6. Reproduce representative dashboard metrics in an independent query and compare with visuals.

## Reusable ideas pending verification
A dashboard could help monitor opportunity volume by country, discipline, funding, and deadline status, but no source-backed metric from this repository should be imported into the canonical admissions framework yet.

## Evidence
- https://github.com/DataBizex/academic-positions-dashboard/tree/7472058b0c0e704c676eb4be45de207fcc5f1f43
- README and Git tree; native Power BI artifacts not inspected.
- Status: BLOCKED_PRELIMINARY, not deep review.