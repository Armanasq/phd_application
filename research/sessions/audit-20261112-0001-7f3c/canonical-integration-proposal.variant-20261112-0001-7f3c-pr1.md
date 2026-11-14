# Canonical integration proposal — repository audit 2026-11-12

**Status:** proposal only. No shared inventory, global status, generated index, or canonical relation file was modified in this PR because other sessions have active branches and canonical-file ownership is not established.

## 1. Mainline state after PR #6

PR [#6](https://github.com/Armanasq/phd_application/pull/6) merged at commit fcbbb597b58f55b84fd517327dd341b3954e544f. It added session-specific investigations for simitii/CS-Grad-School-Applications-Reading-List and siddu1998/Graduate-Admissions, plus eight other supplements, under research/sessions/2cabbe82/.

The canonical CSV inventory was not updated by PR #6. The current main-branch candidate CSV still reports:
- 404 candidate identities;
- 63 REVIEW_RECORDED;
- 330 UNTRIAGED;
- 2 SCREENED_INCLUDE;
- 9 SCREENED_EXCLUDE.

The two SCREENED_INCLUDE entries are simitii and siddu1998 even though session-specific reports now exist on main. The canonical inventory and status summaries are therefore stale relative to the merged session research.

## 2. Proposed dispositions

| Repository | Proposed state | Proposed record |
|---|---|---|
| simitii/CS-Grad-School-Applications-Reading-List | PRELIMINARY_FOCUSED | Add review row pointing to research/sessions/2cabbe82/reviews/simitii-cs-grad-school-reading-list.md |
| siddu1998/Graduate-Admissions | PRELIMINARY_FOCUSED | Add review row pointing to research/sessions/2cabbe82/reviews/siddu1998-graduate-admissions.md |
| Ariaeimehr/PHD-Position-Finder | DEEP_REVIEW_DOCUMENTED (static; runtime NOT_TESTED) | Add review row pointing to this session's Ariaeimehr report |
| archna1212/PHD-OPENINGS | SCREENED_EXCLUDE | Reason: exact code mirror of Aghababaei/PhD-Seeker; no unique implementation |
| arbitan/ScholarshipWebsite | SCREENED_EXCLUDE | Reason: academic-publication keyword collision; no admissions/funding content |

## 3. Proposed relation

Add one repository relation:

- source_repo: archna1212/PHD-OPENINGS
- destination_repo: Aghababaei/PhD-Seeker
- relation: MIRROR_OF
- evidence: nine matching non-README file blob SHAs at the inspected revisions
- checked_on: 2026-11-12

This is a source-lineage relation, not an independent validation edge.

## 4. Proposed post-integration counts

If the two already-merged session reviews are recorded as preliminary, Ariaeimehr is recorded as one deep static review, and the two exclusions are added, the inventory should reconcile to:

- 404 total candidate identities;
- 66 review records: 9 deep static, 57 preliminary;
- 327 untriaged;
- 0 screened-in awaiting first review;
- 11 documented exclusions.

Check: 66 + 327 + 0 + 11 = 404.

These are proposed counts, not current main-branch counts. They must be recalculated from the canonical CSVs at integration time because other sessions may add findings before the reconciliation PR is prepared.

## 5. Canonical files requiring coordinated regeneration

1. data/github_discovery_candidates.csv — update the five candidate screening states and review paths.
2. data/repositories.csv — add the three review records (two prior session reviews and Ariaeimehr).
3. data/exclusions.csv — add the PHD-OPENINGS mirror and ScholarshipWebsite false-positive rationale.
4. data/repository_relations.csv — add MIRROR_OF lineage.
5. research/repositories/index.md — regenerate from the review register.
6. README.md, METHODOLOGY.md, RESEARCH_STATUS.md, quality/coverage-report.md, and synthesis/repository-systematic-review.md — reconcile counts and distinguish merged session reports from canonical deep-review status.

README.md, METHODOLOGY.md, and RESEARCH_STATUS.md currently disagree on review counts. Do not hand-edit generated files. Use the repository's generation/validation scripts after the shared-file owner and active sessions have been checked.

## 6. Integration controls

- Re-fetch main immediately before canonical integration.
- Inspect all active branches and PRs for overlapping edits.
- Assign one owner for each shared canonical file.
- Apply the smallest atomic change and preserve existing IDs/provenance.
- Run validate.py, unit tests, index check, source-ledger check, source validation, duplicate detection, and link checks in a controlled checkout.
- Do not merge if the current main diff conflicts with another session's pending work.
