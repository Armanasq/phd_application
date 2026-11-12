# fengke808-hash/phd-radar — focused source review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [9e97435ee527e79c0a8a5ef7752f8c5a198e15a3](https://github.com/fengke808-hash/phd-radar/commit/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3); latest commit observed 2026-08-18.
- **Category:** applicant-specific Chinese PhD radar / outreach CRM.
- **Review state:** DEEP_REVIEW_DOCUMENTED. Static inspection of data generation, matching, H5 pages and cloud functions; no cloud deployment or runtime tests.
- **License:** no explicit license metadata or license file confirmed.

## 1. Problem and intended user

A uni-app/WeChat mini-program and H5 dashboard tracks a single applicant's supervisor list, research directions, admissions windows, outreach status and daily activity. It is a personal pipeline rather than a reusable global opportunity service.

## 2. Architecture and data flow

A Python generator reads CSV, Markdown and Excel files from a sibling local directory named in the script, emits professors/admissions/daily JSON, and the front end consumes either bundled JSON or public H5 JSON files. An optional CloudBase path uploads JSON into a database and exposes two cloud functions.

Relevant files: [generator](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/scripts/generateData.py), [matching](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/src/utils/matchScore.js), [data service](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/src/utils/dataService.js), [detail page](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/src/pages/professors/detail.vue), [cloud status function](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/cloudfunctions/updateApplicationStatus/index.js).

## 3. Useful implementation ideas

- Separate generated read models from the mini-program UI.
- A lightweight admissions-window dashboard and supervisor follow-up view can be useful.
- The source-specific pipeline shows how a private working dataset can be transformed into a static client dataset, although the current repository does not provide the source directory needed to reproduce it.

## 4. Verified data-quality and logic defects

The generator hardcodes daily new-professor and high-match counts and includes fixed suggestion records rather than deriving these values from the current data. It also parses month/day strings using a fixed 2026 year. These fields make the dashboard look current while not representing actual daily measurements.

The match score is a domain-specific keyword heuristic: research-direction keyword hits contribute 60%, outreach status contributes 20%, and a manually fixed school-priority table contributes 20%. A professor can receive a higher score because the applicant has already contacted them or because the school is on a preferred list. This is not a measure of scientific fit, recruitment availability or funding probability. The keyword set is specific to clinical laboratory medicine and is not transferable to robotics/AI without replacing the ontology and scoring model.

## 5. Security and persistence findings

The generated JSON is served as public static data and contains identifiable supervisor contact information and applicant outreach/reply records; the daily suggestion payload also includes direct contact information. Do not mirror or import these records. The CloudBase status-write function accepts an ID, status and note and writes to the database without an authentication/ownership check or strict status validation. The read function returns requested data by key without a visible authorization check.

The detail page reads the static professor JSON. Its status control mutates only the in-memory object, while the note-save handler displays a local toast without persisting the note. The cloud status function is not called by this page, so the apparent CRM write path is not integrated in the inspected UI.

## 6. Testing and operational maturity

No automated test suite or source-data fixture was established in the inspected tree. The generator depends on files outside the repository, so output reproducibility and source lineage cannot be checked from this repository alone. No cloud permission or multi-user isolation test was run.

## 7. Adoption judgment

**REJECT AS-IS; ADAPT ONLY THE READ-MODEL CONCEPT.** Do not import the published personal dataset. If implementing a similar workflow, use a private tenant-scoped store, authenticated writes, event history, validated states, source URLs and field-level evidence. Compute daily metrics from event records, not constants.

## 8. Unresolved work

Audit cloud database rules and deployment configuration; inspect the missing source-data directory if the owner makes it available; validate public data exposure and deletion; add real event-backed metrics, research-fit evaluation and integration tests.

## Additional source-level code reinspection — 2026-11-12

Pinned upstream `9e97435ee527e79c0a8a5ef7752f8c5a198e15a3`: inspected `cloudfunctions/updateApplicationStatus/index.js` (32 lines), `cloudfunctions/getDailyData/index.js` (21), `scripts/generateData.py` (141), `src/utils/matchScore.js` (55), plus README, Git tree and application dataflow; intentionally **did not copy or print personal professor/contact datasets** in the tracked JSON. The update cloud function accepts `{id,status,note}`, queries `applications` by `professorId` and inserts/updates without validating caller identity, permitted status transitions, record ownership or tenancy in that function. The read function accepts arbitrary `key` and returns stored `phd_data` without filtering by caller in the handler. Whether cloud-provider role rules restrict invocation is **unverified**; do not claim a deployed public exploit.

The generator takes individualized applicant CSV/Markdown/Excel from an adjacent local `博士导师投递` folder and exports `professors.json`, `admissions.json` and `daily.json` into the public-facing `src/data` directory, with a corresponding H5 `docs/data` snapshot. These data are not neutral global admissions information and may contain outreach histories. The browser-scored `calcMatch(professor)` assigns 60 points for hard-coded keyword overlap, up to 20 for response/sent status and up to 20 for university priority. Thus the reported **0–100 matching score is an unvalidated heuristic**, not PI recruitment likelihood, funding entitlement or calibrated admission probability. No actual international-degree/visa or official 2026/27 vacancy verification is implemented by these modules.

**Transfer:** UI separation between supervisor directory, personal outreach and time-sensitive admissions-window monitoring, but require authenticated user-scoped data, record-level RLS, private datasets, clear provenance for official dates and explicit labeling of scores as heuristics. Tests to add: unauthorized cloud-function invocation, cross-user professor IDs, concurrent insert/update races, score-calibration fixtures, stale public exports and source-controlled PII detection. No cloud deployment, access test or runtime execution performed. [status function](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/cloudfunctions/updateApplicationStatus/index.js), [data function](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/cloudfunctions/getDailyData/index.js), [generator](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/scripts/generateData.py), [score](https://github.com/fengke808-hash/phd-radar/blob/9e97435ee527e79c0a8a5ef7752f8c5a198e15a3/src/utils/matchScore.js).
