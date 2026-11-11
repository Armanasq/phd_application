# hemanth619/phd_admissions — source-lineage and implementation-delta review

**Reviewed:** 2026-11-12. **Pinned upstream:** [06f5ab5bd2ff7d2225117cd0da143e1d677c959a](https://github.com/hemanth619/phd_admissions/commit/06f5ab5bd2ff7d2225117cd0da143e1d677c959a).  
**State:** PRELIMINARY_FOCUSED — complete recursive tree/duplicate-blobs comparison and selected critical PHP code, no runtime execution.  
**Verdict:** derivative/related source; do not count shared implementation as independent engineering evidence.

The 2016 PHP admissions app uses the same PHP/MySQL administrator login, semester DB, candidate selection, grading criteria and personal/academic views as `DeepanshuGautam/phd_admissions` (2015). Direct Git tree comparisons found **86 identical relative file paths**, of which **76 have identical Git blob SHA-1 identifiers** across the repositories, despite different overall sizes (368 versus 88 files). This verifies extensive shared code, not formal Git fork ancestry. The extra files contain additional assets and library code that have not received an exhaustive diff review; use a source-lineage marker rather than treating this as an independent validated implementation.

Identical code files include `adminLogin.php`, `personal_info.php`, `academic_info.php` and connection configuration. Their shared SQL-query construction and database-credential patterns carry forward. In a directly inspected changed file `view_applications.php`, the list query still interpolates `$_POST['discipline']` into SQL; file changes do not establish improved SQL safety. The `set_criteria.php` source differs in size but retains posted numeric thresholds in dynamically constructed SQL statements. Applicant records include sensitive data and no current official institution source was verified.

**Transfer decision:** deduplicate at source/commit/blob level, preserve the 2016 branch as a separate candidate identity but link `shares-implementation-with` `DeepanshuGautam/phd_admissions`. Do not add independent confidence to a design conclusion merely because the same code occurs under two owners. Conduct a bounded diff review of added files before any claims of new functionality or remediation.

**Evidence:** [2016 repository](https://github.com/hemanth619/phd_admissions/tree/06f5ab5bd2ff7d2225117cd0da143e1d677c959a), [2016 listing](https://github.com/hemanth619/phd_admissions/blob/06f5ab5bd2ff7d2225117cd0da143e1d677c959a/view_applications.php), [2016 criteria](https://github.com/hemanth619/phd_admissions/blob/06f5ab5bd2ff7d2225117cd0da143e1d677c959a/set_criteria.php), [2015 baseline](https://github.com/DeepanshuGautam/phd_admissions/tree/63cd39182ce9eebbd1065258c47ba3ac581b6d5e).

**Validation:** Git blob/source comparison only; no test suite executed, no applicant data accessed or reproduced.
