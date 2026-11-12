# Rubaid-Ahmed/phd-tracker — deep static GitHub-backed applicant workspace audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/Rubaid-Ahmed/phd-tracker | **Pinned revision:** [`560cce95f13df12f89735e0e98eec8fabb08be7a`](https://github.com/Rubaid-Ahmed/phd-tracker/commit/560cce95f13df12f89735e0e98eec8fabb08be7a) | **State:** DEEP_REVIEW_DOCUMENTED (static) | **Decision:** adapt user-controlled university/professor modeling, reject current GitHub token and data privacy defaults.

## 1. Purpose and data model

A React/Vite browser app with university selection, 2024 QS ranking fixtures, professor interests, manually entered admission deadlines, scholarships/fellowships/internships and global search. It stores records in browser `localStorage` and optionally synchronizes the entire state to a GitHub repository using the GitHub Contents API. The 32-entry tree contains React components, a global context, GitHub service and compiled-asset build configuration. Latest source update: 2026-06-09. No tests/CI or authentication backend identified.

University ranking rows are static **QS 2024** examples; they are not current 2026 program or funding evidence.

## 2. Frontend dataflow and synchronization

`src/context/AppContext.jsx` initializes state from `phd_tracker_data` localStorage; actions add/remove/update universities with nested date/professor/opportunity lists. An effect persists all data on each state change. When `githubConfig` is set, a load action fetches `data.json` from the configured repository, and a debounced effect pushes the full JSON snapshot back to GitHub.

`src/services/githubService.js` uses `GET /repos/{owner}/{repo}/contents/data.json` and `PUT` with blob SHA, which is a useful optimistic-concurrency primitive. The client does not implement a three-way merge on a SHA conflict or durable synchronization queue; competing devices must resolve it manually. A `fileSha` from the state at save time can lag other device changes.

## 3. Critical credential and privacy boundary

`getGithubConfig()` loads a GitHub personal access token from the **browser's persistent localStorage** key `phd_tracker_github`, and `setGithubConfig()` serializes that config back to the same key. Browser script compromise, extension access or shared machine state can expose the token. The app does not use a server-side GitHub App consent model or short-lived scoped credential proxy.

`createRepo()` calls GitHub's authenticated repository-creation endpoint with `private: false` by default. This creates a **public repository** for applicant university preferences, professor contacts, deadlines and potentially personal notes if the user connects it without understanding visibility. There is no runtime privacy gate that forces private storage or warns about data visibility in the inspected service function.

`addCollaborator()` grants `push` access to a chosen username, affecting access to the application dataset. Proper permission review and confirmation are required before a personal study planner shares data.

## 4. Data correctness and Unicode handling

GitHub Contents API returns file content as base64. The writer encodes JSON via `btoa(unescape(encodeURIComponent(...)))`, producing UTF-8 bytes correctly. The reader, however, directly runs `JSON.parse(atob(json.content.replace(/\n/g,'')))` without decoding UTF-8 bytes to Unicode. Personal or institutional names containing accents/CJK characters can be restored as mojibake. Use `TextDecoder` over a Uint8Array constructed from decoded bytes or a consistent UTF-8 helper.

Records are identified with client-generated `uni_{rank}_{Date.now()}` keys; rank changes or separate device imports can duplicate the same university. The app uses QS rank as a duplicate guard, which fails when rankings change or alias lists differ. Use stable institution identifiers and keep rankings as dated third-party annotations.

## 5. Opportunity, funding and deadline semantics

`src/components/Opportunities.jsx` stores manually entered name/type/description/URL with no official source verification, funding amount, stipend guarantee or eligibility. `AdmissionDates.jsx` parses date-only strings with date-fns, subtracts `new Date()` to display days left and color codes 30/90-day windows; it does not capture the receiving institution's timezone, submission cutoff or intake cycle. Calendar dates entered by an applicant are hypotheses until supported by the program's current page.

Professors and expertise are user-maintained records, not proof of available funded doctoral supervision.

## 6. Deployment and operational gaps

The repository includes Vite/React and a broad QS 2024 static catalog but no backend source of verified offers, automated test suite, identity resolution, audit log, schema migration, encryption-at-rest policy, multi-device conflict resolution, receipt-backed submission workflow or versioned rankings provenance.

`loadFromGitHub` on mount may race with debounced save-on-state-change when config is present; a structured sync state machine should prevent uploading an old empty/local snapshot before remote state is loaded. No dynamic race reproduction was executed here; this is a source-level concurrency concern.

## 7. Transfer architecture and corrections

Reuse the concepts of explicit research-university lists, PI-methodology notes, distinct scholarship types, controlled sync and simple git-revision conflict protection. Require:
1. Private, encrypted applicant data by default and no persistent raw GitHub PAT in browser localStorage.
2. Explicit repository visibility and collaborator approvals, preferably a GitHub App authorization proxy.
3. Complete Unicode-safe JSON encoding/decoding.
4. Stable university and opportunity IDs independent of rankings and timestamps.
5. Source-verified deadline timezone, funding and eligibility claims.
6. Provenance-aware merge/conflict reconciliation and backup/restore tests.
7. Separate user-authored application status from institution-issued receipt/offer evidence.

## 8. Pinned implementation evidence

- [Global app state, local storage and sync](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/context/AppContext.jsx)
- [GitHub API, token and public repo defaults](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/services/githubService.js)
- [QS 2024 university fixtures](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/data/qsRankings.js)
- [University selection and duplicate handling](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/components/AddUniversityModal.jsx)
- [Deadline display](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/components/AdmissionDates.jsx)
- [Scholarship/fellowship manual entries](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/components/Opportunities.jsx)
- [Search](https://github.com/Rubaid-Ahmed/phd-tracker/blob/560cce95f13df12f89735e0e98eec8fabb08be7a/src/components/GlobalSearch.jsx)

**DEEP_REVIEW_DOCUMENTED — static source only.** No browser execution, GitHub token use, remote repository creation, private data sync, official program verification or source correctness tests were performed.
