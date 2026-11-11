# Independent 16-repository screening and source-review batch

**Reviewed:** 2026-11-12. **Parent:** https://github.com/Armanasq/phd_application. **Execution:** GitHub source inspection only, no third-party code or SMTP execution, no personal PDFs read. Canonical CSVs are not changed by publishing this supplemental evidence. Reconcile with live `main` before changing state counts.

## Deep static bounded code review — daytime001/Bulk-Email-Sender

Pinned upstream: [dc910caf400a27a17a7534bdb1bb4b5ad504d227](https://github.com/daytime001/Bulk-Email-Sender/commit/dc910caf400a27a17a7534bdb1bb4b5ad504d227), 2026-07-12. The complete 120-entry tree, README, GitHub metadata/history, issue listing, MIT license presence, Python project manifest, core engine/SMTP/recipient/message/template/worker/sent-store source, selected Tauri Rust source and tests were inspected. Rust/UI and dependency lockfile not exhaustively reviewed. The intended audience is applicants contacting graduate supervisors, not a verified professor directory or scholarship platform.

The [recipient loader](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/recipients_loader.py) parses JSON and XLSX/XLSM, checks names/emails and reports duplicates/invalid rows. The [engine](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/engine.py) personalizes messages, validates attachment existence, sends with retries and pauses, emits worker progress events and appends sent status. The [SMTP client](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/smtp_client.py) implements SSL and STARTTLS but also allows an unencrypted SMTP configuration. [SentStore](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/sent_store.py) records names/emails/job IDs in local plaintext JSONL/text and reloads email addresses to suppress repeat sends.

**Critical behavior:** The send success and local sent-log append are separate operations, so crashing after mail acceptance but before log append can cause duplicate retries. A retry after ambiguous SMTP acknowledgement cannot guarantee exactly-once delivery. Recipients' consent, faculty identity, eligible funding, sender authorization, attachment sensitivity, record retention and actual mail delivery are not independently verified by the inspected code. The sender creates email Message-ID but has no provider-side idempotency guarantee. Python [SMTP tests](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/tests/test_smtp_integration.py) include a local debug server; they were read, not run. No external email was sent.

**Transfer:** Reimplement typed recipient validation, preview/cancel, structured delivery state and audit logs behind per-recipient approval, verified supervisor evidence, data-retention controls and an uncertainty-aware provider receipt workflow. Verdict: relevant *transport pattern*, not an admissions intelligence or success-rate evidence source. Proposed state: DEEP_REVIEW_DOCUMENTED for bounded critical-path static review only; empirical execution NOT_TESTED.

## Preliminary, relevant document-source reviews

1. **[Anu-Warrier/CV@de422fd238d5acd1901072c636702cf4c8c75741](https://github.com/Anu-Warrier/CV/commit/de422fd238d5acd1901072c636702cf4c8c75741)** — Three-file academic CV LaTeX template for a PhD candidate, declared as derived from NicDuquette/CV-Template. README and LaTeX source inspected; binary CV not opened, no LaTeX compilation or repository license confirmed. PRELIMINARY_FOCUSED, transferable formatting template only; derivative-code rights and individual target-program requirements unknown.
2. **[GEGE-5/CV@092d18541fc656219c2cd42fec9a2f4f5706c562](https://github.com/GEGE-5/CV/commit/092d18541fc656219c2cd42fec9a2f4f5706c562)** — Fork of liber145/CV, historical academic CV, LaTeX writing samples and PDF files. Complete tree and sample LaTeX type inspected, no personal PDF text extracted. PRELIMINARY_FOCUSED, useful only as historical artifact taxonomy; no admissions outcome, independent replication or redistribution rights established.

## Thirteen scope exclusions

Each decision is backed by the pinned upstream git tree and source README when present. This is **screening**, not code audit. Exclude for the doctoral admissions resource research question; a separate ML/robotics literature study may have different boundaries.

| Repository at pinned commit | Reason / proposed exclusion |
|---|---|
| [alimaher30119-cmd/ali.ibrahim@ad4678b38edde76883185d766bdc902db6d2fcca](https://github.com/alimaher30119-cmd/ali.ibrahim/tree/ad4678b38edde76883185d766bdc902db6d2fcca) | Two-file personal academic profile site; PERSONAL_PROFILE_ONLY |
| [AnamikaRajendran/cv@2472103e0028981c0cb9b903df45391c1ae327fa](https://github.com/AnamikaRajendran/cv/tree/2472103e0028981c0cb9b903df45391c1ae327fa) | One personal CV PDF; no inspectable reusable guidance; PERSONAL_CV_BINARY_ONLY |
| [AybalaSenaHan/GraduateThesisProject@4515e127e059791835362e0645c088c7f3c0a077](https://github.com/AybalaSenaHan/GraduateThesisProject/tree/4515e127e059791835362e0645c088c7f3c0a077) | C# graduate-thesis catalog CRUD rather than doctorate admissions; THESIS_DATABASE |
| [ayszbd/CSM.-SOP@02a48043cd105eeb61db97052da0094a5ce7a031](https://github.com/ayszbd/CSM.-SOP/tree/02a48043cd105eeb61db97052da0094a5ce7a031) | HTML business customer-success operating plan; SOP_ACRONYM_COLLISION |
| [beric7/structural_inspection_main@591fca811e0529b8693fd280b893109879e5fbbb](https://github.com/beric7/structural_inspection_main/tree/591fca811e0529b8693fd280b893109879e5fbbb) | Research papers and CV/structural inspection datasets; RESEARCH_METHODS_NOT_ADMISSIONS |
| [cirosantilli/cirosantilli@50739dade7f2bccbec4888463e6ccbf437b514d0](https://github.com/cirosantilli/cirosantilli/tree/50739dade7f2bccbec4888463e6ccbf437b514d0) | Public profile/action repository; PROFILE_COLLISION |
| [cirosantilli/x86-bare-metal-examples@528ab2becc4992218ca0b7e297f3e1f1674268de](https://github.com/cirosantilli/x86-bare-metal-examples/tree/528ab2becc4992218ca0b7e297f3e1f1674268de) | BIOS/operating-system assembly tutorials; UNRELATED_SYSTEMS_TUTORIAL |
| [CSC322-Grinnell/graduate-outcomes@6bd692ecd06bb9cad2c12938642d28af8b4e179c](https://github.com/CSC322-Grinnell/graduate-outcomes/tree/6bd692ecd06bb9cad2c12938642d28af8b4e179c) | Rails college alumni/graduate-outcome visualization, not PhD applications; ALUMNI_OUTCOMES |
| [cvorland/cvorland.github.io@d9fc153b4154cd9192c5165b512a1bcd33e7b734](https://github.com/cvorland/cvorland.github.io/tree/d9fc153b4154cd9192c5165b512a1bcd33e7b734) | Personal research website and publication catalogue; PERSONAL_RESEARCH_SITE |
| [danieldrojas/gt-bootcamp-connect@ee628f1d1dbef44b4cf0beae8e4bce2f04b823f8](https://github.com/danieldrojas/gt-bootcamp-connect/tree/ee628f1d1dbef44b4cf0beae8e4bce2f04b823f8) | Coding-bootcamp alumni networking, not doctoral recruitment; BOOTCAMP_NETWORK |
| [FBIResourse/cirosantilli@6df8844c4020b5036b9f800946ebc14187480be2](https://github.com/FBIResourse/cirosantilli/tree/6df8844c4020b5036b9f800946ebc14187480be2) | Single-file fork of profile repository, not independent admissions evidence; PROFILE_FORK_DUPLICATE |
| [guravshubham12/ExcelR-Coaching-Courses@0d234c437064f14d77eda3d0c49bd92164f3caae](https://github.com/guravshubham12/ExcelR-Coaching-Courses/tree/0d234c437064f14d77eda3d0c49bd92164f3caae) | Commercial analytics-training advertisement using PhD instructor keyword; TRAINING_MARKETING_COLLISION |
| [hammadshaikhha/Causal-Inference-Mastery@cd709afff1170f9c5cdcb144ee69a9ed92a2fe48](https://github.com/hammadshaikhha/Causal-Inference-Mastery/tree/cd709afff1170f9c5cdcb144ee69a9ed92a2fe48) | Graduate causal inference notes and PDFs, not doctoral admissions; GRADUATE_METHODS_NOT_ADMISSIONS |

## Synthesis and boundary

- Sixteen identities: **one** bounded deep static software review, **two** preliminary source reviews, **thirteen** justified screening exclusions. Do not count all sixteen as deep.
- A sending tool is downstream of *verified supervisor identity and authorization*, not a replacement for independent university opportunity research. An email log is not a reply, consent record or funded offer.
- Template/CV forks, profile pages and unrelated courseware are search noise or historical writing examples, not independent current admissions evidence.
- No third-party runtime, live mail transport, private PDFs, funding-source verification, official policy validation or security penetration test was performed.
- Integration into canonical CSVs remains a separate, guarded transaction; recheck the latest queue to avoid duplicating parallel-session work.
