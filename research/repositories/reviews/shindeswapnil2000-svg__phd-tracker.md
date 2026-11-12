# shindeswapnil2000-svg/PhD-Tracker. — deep static review

**Reviewed:** 2026-11-12. **Pinned upstream:** [4c93c22ce1a408a24cb002bfd70d4f3ce9c4c182](https://github.com/shindeswapnil2000-svg/PhD-Tracker./commit/4c93c22ce1a408a24cb002bfd70d4f3ce9c4c182).  
**State:** DEEP_REVIEW_DOCUMENTED; all five tracked files inspected, including state, seeded program records, app rendering and README. Browser/runtime NOT_RUN.  
**Verdict:** adapt local-first planning concepts after fixing migration and durability.

## 1. Scope

Fieldnotes is a static PhD workspace: programs and potential supervisors, application status/checklists, dashboard, preparation resources and web search links. The provided 22-program seed is predominantly sociology, political science, anthropology and humanities rather than AI/robotics. It is not a funded-vacancy verifier or admissions system.

## 2. Dataflow

app.js implements a Store wrapper over browser localStorage for programs, professors and applications, with separate keys. data.js contains SEED_PROGRAMS, empty SEED_PROFESSORS and preparation resources. The UI uses HTML string rendering plus event handlers. An optional Google Programmable Search Engine script brings external search results into the Explore view. There is no authenticated server, database or portable backup.

## 3. Destructive seed migration

When SEED_VERSION increases, app.js replaces the stored program list with new defaults plus only custom rows whose IDs start with prog_. **All user edits to preloaded programs**—including notes, status and verification details—are silently lost. The comment that custom programs are preserved does not extend to edited seed rows. Store.save catches quota errors and only logs to console, while Store.load treats corrupted JSON as an empty/fallback state. These are data-loss hazards.

## 4. Status and evidence semantics

The dashboard calls every application outside Researching and Preparing “submitted or beyond” without a portal receipt or status-event proof. It cannot distinguish user-edited intent from actual submission. Seed entries include narrative claims about funding and historical/generic department links, but lastVerified is empty. All begin as to-research, which correctly signals unverified source status. Deadlines are parsed into the device-local JavaScript Date and not tied to official source timezone.

## 5. Search and browser security

Application data are local plaintext readable to scripts sharing the origin; a malicious same-origin script or XSS could access them. Optional Google CSE and external fonts create network requests even though records are stored only locally. Many HTML templates escape text using escapeHtml, but source/user-provided link fields still require URL scheme allowlisting; HTML escaping is not sufficient for malicious href schemes.

## 6. Reliability and operations

No automatic source updates, per-claim citations, normalized institution/PI identifiers, receipt-backed submissions, cross-tab versioning or cloud recovery are built. A browser data clear destroys records. Multiple tabs can overwrite whole localStorage values. No tests or CI appear in the five-file tree, and no actual university current funding conditions were verified.

## 7. Pinned evidence and untested scope

[app.js](https://github.com/shindeswapnil2000-svg/PhD-Tracker./blob/4c93c22ce1a408a24cb002bfd70d4f3ce9c4c182/app.js), [data.js](https://github.com/shindeswapnil2000-svg/PhD-Tracker./blob/4c93c22ce1a408a24cb002bfd70d4f3ce9c4c182/data.js), [README](https://github.com/shindeswapnil2000-svg/PhD-Tracker./blob/4c93c22ce1a408a24cb002bfd70d4f3ce9c4c182/README.md). No browser test, live search, submission or official source recheck was performed.

## 8. Transfer to PhD Atlas

Keep separate program, professor, application and checklist entities. Implement seed-to-user overlays and non-destructive migrations, exported backups, controlled private storage, provenance/last-verified fields, real submission receipts, cycle-aware deadline timestamps and multi-session conflict handling. Distinguish the applicant's research notebook from verifiable admissions records.
