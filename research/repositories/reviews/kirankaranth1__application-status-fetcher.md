# Focused source investigation — Kirankaranth1/ApplicationStatusFetcher

**Upstream revision:** `cfd458d41efb93670faa712d7ed9b1a038753b2f` dated 2016-04-01; reviewed 2026-11-12. **Class:** PRELIMINARY_FOCUSED, historical application-status browser automation; no current institutional portal validation or code execution.

The [README](https://github.com/Kirankaranth1/ApplicationStatusFetcher/blob/cfd458d41efb93670faa712d7ed9b1a038753b2f/README.md) defines a config-driven Selenium routine for checking graduate application statuses on several older US university portals, not a scholarship database or doctoral opportunity discovery source. The inspected 3-file tree comprises `GetMyStatus.py`, a campus-specific `MyUnivs.config` and README. The credentials-bearing configuration file was **not opened or reproduced**. [`GetMyStatus.py`](https://github.com/Kirankaranth1/ApplicationStatusFetcher/blob/cfd458d41efb93670faa712d7ed9b1a038753b2f/GetMyStatus.py) is a 125-line Python 2-era script. It starts Firefox or PhantomJS at module scope, parses labeled config lines, enters usernames/passwords through XPath, clicks optional intermediate fields, prints a status string, captures screenshots on error and clears cookies.

### Source-established reliability and security risks

1. **Credential handling:** the documented configuration format stores usernames and passwords as readable key/value text. A debug helper `get_status_test()` passes a password as a parameter and prints it; the helper is not called in the inspected normal path, so do **not** claim the default flow logs credentials. Never put live account details into a shared repo or CLI logs.
2. **Obsolete automation:** PhantomJS and `find_element_by_xpath`/old Selenium APIs, static institution-specific XPaths and arbitrary sleeps are not durable against modern dynamic login, multi-factor authentication, CAPTCHA, authentication changes and consent boundaries.
3. **Error-state ambiguity:** extensive bare `except:` handlers print generic messages; failed login, missing status label, browser incompatibility and portal denial cannot be distinguished from no status change.
4. **Unredacted screenshots:** on a failure in silent mode, screenshot files may contain private applicant/portal details; static filenames may overwrite each other, and no retention controls are visible in the main script.
5. **CLI argument bug:** one exception handler in `get_status()` evaluates `sys.argv[2]` without checking argument count, although the README makes `silent` optional. For a regular invocation with only one config argument, a downstream UI failure can raise `IndexError` inside error recovery.
6. **No source officiality contract:** the config identifies portal URLs, not a current protected API. Login automation is unsuitable without explicit user authorization and institution portal terms; this investigation did not attempt to log in, test accounts, or read any real applicant status.

### Engineering synthesis and verdict

The reusable abstraction is **per-institution adapter interface with explicit state, timestamps and error provenance**. Replace browser scraping of credentials with user-mediated status entry or an authorized institution API, store private tokens in a secrets manager, scope per-applicant data, persist screenshot/redaction policies, and treat `application_status` as unknown until an authorized receipt is verified. Compared with local-first [PhD Fit](https://github.com/houwei1228/PhD_Fit), this legacy script offers narrower portal automation and much weaker secret hygiene; it should not be incorporated into a production multi-country admissions intelligence system.

**Verdict: REJECT AS AN OPERATIONAL PORTAL CONNECTOR.** Static confidence is high for the five named code-level issues; deployment, live portal functionality and legal permissions remain untested. No use of credentials, application submission, email or external service was performed.
