# DeepanshuGautam/phd_admissions — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [63cd39182ce9eebbd1065258c47ba3ac581b6d5e](https://github.com/DeepanshuGautam/phd_admissions/commit/63cd39182ce9eebbd1065258c47ba3ac581b6d5e).  
**State:** DEEP_REVIEW_DOCUMENTED; static source inspection, runtime NOT_TESTED.  
**Verdict:** reject direct code reuse. An educational case for admissions-year partitioning and filtering, not secure production software.

## 1. Purpose and scope

A 2015 PHP/MySQL departmental PhD admissions admin application with login, year/semester database creation, criteria-based candidate shortlisting, personal/academic detail views, attachments and password management. The tracked tree contains 88 files, mostly PHP, CSS, client JS and bundled jQuery. It is historical administration software, not an official current admissions policy source.

## 2. Architecture and data model

The admin interface creates one database per year/semester and maintains a master `db_list` directory. Generated tables cover registered users, personal details, qualifications, experience, email confirmation and password resets. An admin selects the active semester, sets discipline-specific CGPA/percentage/age thresholds and browses candidate records by application ID. The approach captures admission-cycle scope but physically partitioning data by year without migrations complicates governance, cross-cycle applicant identity and consistency.

## 3. SQL injection and input validation

The login route builds SQL by interpolating user-supplied username into `select adminUserName,adminPassword ... where adminUserName='${userName}'` and sends it to `mysqli_query`. The profile/qualification routes construct `... WHERE userId = ${appNo}` from raw `$_GET['app_no']` without parameterization. Application listings interpolate posted discipline text into a join query. Database creation and shortlisting use concatenated posted year/semester/criteria values in SQL.

This creates multiple source-level SQL injection surfaces. Neither a client UI dropdown nor an authenticated session makes SQL concatenation safe. The exact likelihood of exploitation in a live deployment was not tested. Replace dynamic SQL values with prepared statements and validate identifier names against server-owned allowlists.

## 4. Authentication and secrets

Database connection files contain static database credentials in tracked source. Their literal values are deliberately omitted. Admin authentication compares `hash('sha512', password)` with stored hashes, without a visible password-specific salted KDF; SHA-512 alone is inappropriate for password storage. Username is reflected into HTML error text without output escaping, introducing a potential HTML injection route. Admin pages depend on a `$_SESSION['adminUserName']` flag; no CSRF token or repeated server authorization policy was established across mutation routes.

## 5. Eligibility logic and scientific limits

Criteria include discipline, undergraduate/postgraduate grading schemes (percentage, CGPA, CPI4/CPI8), minimum age and submission/confirmation flags. Values are bare numeric fields and SQL predicates, not current institutional admissions requirements. There is no independently sourced evidence for the original thresholds, exception rules, target cycles, international eligibility or funding. Hardcoded filters cannot substitute for institution-specific, dated policies.

## 6. Persistence and operations

`create_database.php` performs several DDL `CREATE DATABASE` and `CREATE TABLE` queries as part of an admin HTTP request; it has no versioned migration plan, transaction across DDL/data registration or rollback ledger. Errors call legacy `mysql_error()` despite use of `mysqli_query`, obscuring diagnostics. Directly emitting database errors to the browser would be a separate information-disclosure risk if enabled. The attachment view constructs `upload/${appNo}_PP.jpg` from a query param and relies on filesystem naming rather than scoped document authorization. Personal/demographic records need a protected evidence and retention policy.

## 7. Evidence boundary

Read the full tree and selected source files `adminLogin.php`, database connection files, `create_database.php`, `select_database.php`, `set_criteria.php`, `view_applications.php`, `personal_info.php`, `academic_info.php`, `enclosures.php`, `change_password.php`. No PHP runtime, database, external API, password cracking, security exploit or source dataset was executed.

Pinned evidence: [login](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/adminLogin.php), [criteria](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/set_criteria.php), [personal info](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/personal_info.php), [database creation](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/create_database.php), [listing](https://github.com/DeepanshuGautam/phd_admissions/blob/63cd39182ce9eebbd1065258c47ba3ac581b6d5e/view_applications.php).

## 8. Transfer to PhD Atlas

Model admissions cycles, applicant records, qualification types, committee decisions, eligibility criteria and submission evidence as typed records rather than string-concatenated SQL. Use scoped role authorization, prepared SQL, password KDF, protected documents, schema migrations and immutable decision history. Criteria need official citations and review dates. Do not import credentials or applicant data.
