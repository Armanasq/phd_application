# DataBizex/academic-application-tracker — focused workbook review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [b135e25824b75926cbe5f0d5c9be14a4466775c9](https://github.com/DataBizex/academic-application-tracker/commit/b135e25824b75926cbe5f0d5c9be14a4466775c9); latest commit observed 2026-09-22.
- **Category:** offline Excel application tracker generated with openpyxl.
- **Review state:** PRELIMINARY_FOCUSED. Inspected README, both workbook generators and link-repair script; no Excel/LibreOffice recalculation or workbook runtime tests.
- **License:** MIT, confirmed in [LICENSE](https://github.com/DataBizex/academic-application-tracker/blob/b135e25824b75926cbe5f0d5c9be14a4466775c9/LICENSE).

## 1. Problem and intended use

A generated Excel workbook tracks PhD, Master's and postdoctoral applications. It provides a dashboard, application table, university/supervisor reference sheet, explorer, four-way shortlist radar and usage guide. It is designed to work offline without macros or external connections.

## 2. Architecture and data model

Python/openpyxl generates a blank template and a populated example. The workbook has a fact-like Applications sheet and a Universities & Supervisors lookup sheet. INDEX/MATCH formulas fill country, supervisor and funding; validation lists constrain statuses, priorities, degrees and research-fit values. Conditional formatting and native charts provide dashboards.

Relevant files: [blank generator](https://github.com/DataBizex/academic-application-tracker/blob/b135e25824b75926cbe5f0d5c9be14a4466775c9/generator/build_blank_template.py), [example generator](https://github.com/DataBizex/academic-application-tracker/blob/b135e25824b75926cbe5f0d5c9/generator/build_full_example.py), [README](https://github.com/DataBizex/academic-application-tracker/blob/b135e25824b75926cbe5f0d5c9/generator/../README.md).

## 3. Useful implementation ideas

- A self-contained, portable spreadsheet can serve applicants who do not want a hosted database.
- Separating institution reference data from per-program application rows reduces repeated entry.
- Dropdown validation, conditional formatting, charts and internal navigation are generated reproducibly.
- MIT licensing permits reuse subject to the license terms.

## 4. Formula and data-model defects

The blank generator pre-populates 30 application rows and writes formulas only through `A_LAST` (row 33). Data validation extends another 30 rows, but the calculated columns and dashboard/Explorer ranges remain bounded to the original 30 rows. Entering applications in those extra validated rows does not automatically make the derived fields or dashboard include them.

The radar's overall average combines research fit, funding strength, prestige, deadline urgency and supervisor responsiveness as if they were comparable positive suitability dimensions. The deadline formula assigns the maximum urgency score to an overdue deadline because negative days increase `10 - days/20` before it is clamped to 10. Urgency is an operational alert, not evidence of program quality, and should not increase a candidate's scientific or funding fit.

The funding-strength formula gives 10 to text containing “Fully”, 6 to “Partial”, and 7 to every other non-error value. Unknown, unfunded, self-funded or unrecognized funding text can therefore receive a relatively high score. The workbook needs explicit full/partial/tuition-only/unfunded/unknown categories and should not equate “scholarship” with a known coverage amount.

Prestige, responsiveness and research fit are manually entered subjective values. The resulting average is a user-defined shortlist heuristic, not an admission or offer probability. The workbook has no source ledger, eligibility gate or evidence freshness.

## 5. Compatibility and scale

The Explorer and dashboard use fixed ranges. Some nearest-deadline formulas use `MIN(IF(...))` array-style expressions; actual behavior across Excel 2016 and LibreOffice was not verified. The README's compatibility claim should be backed by a recalculation matrix rather than formula syntax inspection alone.

## 6. Testing and operational maturity

The scripts are straightforward and reproducible, but no automated workbook assertions, formula-cache validation, Excel/LibreOffice render tests or generated-file comparison were run. The populated sample is illustrative, not a verified admissions dataset.

## 7. Adoption judgment

**ADAPT AS AN EXPORT FORMAT, NOT AS THE SYSTEM OF RECORD.** A polished offline workbook is useful as a user export. Keep canonical evidence, status and source history in the application database; generate the workbook from validated records and label all manual subjective scores clearly.

## 8. Unresolved work

Extend formulas and dashboard ranges dynamically or use Excel Tables; separate urgency from fit; make unknown/unfunded funding score zero or unknown; validate all dates and currencies; test recalculation in Excel and LibreOffice; add workbook-level formula and data-integrity tests.