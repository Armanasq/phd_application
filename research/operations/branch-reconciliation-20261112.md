# Main-branch reconciliation of research branches and pull requests

**Audit date:** 2026-11-12. **Repository:** https://github.com/Armanasq/phd_application  
**Baseline:** main@583e214fa9477ce67fcfa52191de0e302b6f7cc5.  
**Method:** GitHub branch/PR inventory, Git tree blob comparisons against main, canonical register and manifest inspection. No branch rewrites/deletion and no untrusted third-party execution.

## Pull-request disposition

All 16 previously opened pull requests are now closed. Fourteen were merged. PR #12 and PR #14 were closed without merging. Their proposed canonical work was already reconciled independently on main: dinglhmds/heyulanKiara screening for #12, and fsuitoal-code/phd-application-command-center for #14. Neither should be reopened or merged blindly.

## Remaining branches

At baseline, 25 research branches still existed. Most contain **older versions** of shared files: candidate/review CSVs, generated index, status summaries, tests, and manifests. The source branch's commit ancestry can diverge even when the same review content has already been merged, squashed, or independently integrated.

A full Git-tree path comparison found six branch-only paths:
- Two additional session-local notes for siddu1998/Graduate-Admissions and simitii/CS-Grad-School-Applications-Reading-List. Both identities already have source-pinned canonical records on main. These notes are supplementary rather than independently new reviewed repositories.
- Two unmerged manifests for sessions 20261112-gpt6-7b61 and 20261112-k5e7b. Both describe IN_PROGRESS scope and overlap already reviewed Lukas-Vasionis and Mhrnqaruni sources. They are retained in their branches as historical coordination context.
- An older session initial-investigations note, whose principal repository findings overlap existing mainline reports.
- A deeper source-pinned report for aluminium5/ScholarshipScraper. This was selectively copied to main, verified against the pinned upstream ingest code, and promoted to DEEP_REVIEW_DOCUMENTED in canonical metadata.

No broad branch merge was attempted. It would risk reverting later work. No branch was force-pushed, rebased, deleted or modified. No open PR remained at the audited checkpoint.

## Verified integration

Commit [f588959](https://github.com/Armanasq/phd_application/commit/f58895930918700efa9b4f1531c2ef19588f5883) atomically integrates the aluminium5 upgrade and two independent deep source reviews, with the candidate CSV, review CSV, generated index and RESEARCH_STATUS.md synchronized in one Git commit.

This is **content reconciliation**, not a claim that every historical branch's commits are ancestors of main. Additional branch artifacts require case-by-case source and duplication checks, not blanket merge. Issues #1–#5 remain open where evidence or applications are incomplete.

## Merge policy for parallel agents

Read the current main head and the exact candidate state before preparing new work. Inspect manifests and competing source-pinned reviews. Preserve each session's files. Integrate only verified, non-duplicate content. Update the canonical CSV and generated index in one snapshot-based commit; use a fast-forward, expected-head lease and refuse force pushes. Require a successful post-push research-integrity workflow; structural success does not establish live scholarship correctness.
