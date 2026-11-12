# pungkiilham/scholarship_master-phd — bounded source review

**Source:** https://github.com/pungkiilham/scholarship_master-phd; **Git tree SHA:** `26b4418efca8b410905ae2564c47b4d4425e2baa` ([snapshot inventory](https://api.github.com/repos/pungkiilham/scholarship_master-phd/git/trees/26b4418efca8b410905ae2564c47b4d4425e2baa)); inspected 2026-11-12. **Execution:** NOT_TESTED. **Official eligibility/funding:** NOT_INDEPENDENTLY_VERIFIED.

## 1. Material and boundary

[src/components/ApplicationTracker.jsx](https://github.com/pungkiilham/scholarship_master-phd/blob/master/src/components/ApplicationTracker.jsx), [src/data/trackerData.js](https://github.com/pungkiilham/scholarship_master-phd/blob/master/src/data/trackerData.js). Other files were inventoried in the Git tree, but large binary artifacts, or code not linked above, were not fully inspected.

## 2. Source-level observations

React application tracker stores docsReady/applied and status flags in localStorage; seed scholarship dates in trackerData.js include many dates from 2025/2026, ambiguous rolling awards and notes not checked against current issuer websites.

## 3. Use and interconnections

Capture simple status and docs checklist without treating seeded dates as current verified deadlines. Preserve source authority and distinguish illustrative templates/individual cases from official current admissions and funding evidence.

## 4. Verification gaps

**STATIC_PAST_DEADLINES_AND_LOCAL_ONLY_STATUS (P1).** No live code execution or independently verified university/scholarship policy, and no binary evidence validation, took place. This is a preliminary focused review, not a completed deep review.
