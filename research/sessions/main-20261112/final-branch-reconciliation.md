# Published branch reconciliation — 2026-11-12

Base main: `59530807dcc6cb42ca6847b57f6c481fd7c7118f`. Audit method: list all published branches and PRs, compare each branch's recursively resolved Git blob tree against main by exact relative path and SHA; never equate different Git commit histories after squash merges with absent content.

## Results

- All published pull requests were closed at inspection; #19-#21 and the other merged PRs already contribute their durable work to main. #12 and #14 were closed without merge, and their relevant canonical findings were subsequently published via other paths.
- Across 25 non-main branches, only the five source-unique files listed below were absent on main. These were inspected and imported without changing any pre-existing main path:
- `research/sessions/audit-20261112-0001-7f3c/siddu1998__Graduate-Admissions.md` from `research/repository-audit-20261112-0001-7f3c`, blob `c114f57f3645283397554d4f9cd73612821980b6`
- `research/sessions/audit-20261112-0001-7f3c/simitii__CS-Grad-School-Applications-Reading-List.md` from `research/repository-audit-20261112-0001-7f3c`, blob `222dbf36f9b749d48f2b41a267cc24738dc4a6a2`
- `research/sessions/20261112-gpt6-7b61/manifest.md` from `research/repository-audit-20261112-gpt6-7b61`, blob `7ef641c1e5171259472331b8bbef6f6707552386`
- `research/sessions/20261112-k5e7b/manifest.md` from `research/repository-audit-20261112-k5e7b`, blob `d37ab826904ff611d53978ba02e70ed29e68f018`
- `research/sessions/gpt6-20261112-01/initial-investigations.md` from `research/session-gpt6-20261112-01`, blob `434891bcc42327fd817fcfa8d0583e9b75b0bffd`
- All conflicting files at existing paths—including CSV catalogs, review notes, index, README and session manifests—were left at their newer main version rather than force-merged.
- Historical manifests contain an `IN_PROGRESS` field recording their original session's state; this is a retrospective artifact and **does not** reserve a present task or imply any automation remains running.
- Branch refs are deliberately retained for provenance and to avoid interfering with concurrent users/agents. This is a selective content integration, **not** a claim that old branch heads have become Git ancestors of main.

## Scope and verification

The 404-candidate inventory has explicit review/exclusion dispositions, but static review depth varies and current university/funding eligibility remains unverified unless separately evidenced. This reconciliation did not run third-party repositories, resolve historical applicant PDF content, change issue state, update other agents' branches, send applicant emails or submit applications. No forced updates or branch deletions occurred.
