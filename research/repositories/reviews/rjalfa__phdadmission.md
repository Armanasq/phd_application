# rjalfa/PhDAdmission — eight-section static source investigation

**Snapshot:** 24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a; **checked:** 2026-11-12; **validation:** SOURCE_INSPECTION_ONLY; **runtime:** NOT_EXECUTED; **review state:** DEEP_REVIEW_DOCUMENTED.

## 1. Objective and ethical inspection boundary

Audit legacy PhD admissions web-app architecture and whether the publicly committed repository includes applicant records. Root README is only a short Java-web-project title. The tracked tree reports 2,495 entries, including 1,600 data/* files grouped across 800 applicant-like directories. The identities and authenticity of those records are not established; NO applicant record content was opened, extracted, exported, summarized or copied.

## 2. Source inventory and app behavior

Source tree contains Java servlet controllers, model classes for applicant personal/education information, web forms and JavaScript; 2,495 total tracked entries in the Git tree, of which 1,678 are blobs. Source paths include src/ap/adm/phd/Database.java, controller/AuthenticationFilter.java, UserController.java, AdminController.java and model/PersonalInformation.java. No CI, project test, security audit or release metadata was observed in the tracked tree sample.

## 3. Data model and collection surface

Database.fillUser maps request parameters into names, email, mobile number, address, date of birth, family member, gender, category and schooling/degree records. UserController processes applicant multipart submissions and writes CV and SOP files. Source data handling and publication of applicant-like data files are incompatible with the privacy standard required for the new applicant evidence vault. Even if the committed files prove to be synthetic fixtures, they must be explicitly classified and scrubbed before any reuse.

## 4. Concrete source-level concerns

UserController.doPost iterates submitted request parameters and writes every parameter name and value to System.out; this can expose personal information in application logs. AuthenticationFilter uses session flags to enforce some route access but embeds a fixed administrator email string in the admin conditional. The servlet filter rejects URLs ending in html and otherwise conditionally redirects; this is not a substitute for exhaustive authorization checks. Multipart submission iterates Parts using a second it.next() call for SOP after encountering PDF, which can incorrectly pair files if request ordering differs. These are source-level observations, not exploited vulnerabilities.

## 5. Evidence handling and privacy controls

Do not treat the publicly committed applicant-like directories as a research dataset. They may contain real personal records, sensitive academic materials or synthetic placeholders; the distinction requires a privacy-preserving maintainer review and data-protection assessment. Never read, mirror, index, quote or transplant those files into our repository or searchable training corpus. Only source paths and non-personal code patterns were inspected.

## 6. Architecture transfer and mitigations

The multi-stage applicant form, typed educational entities and role concept are transferable as abstract ideas. A modern system needs encrypted private storage, strict access control per applicant, file scanning and type validation, explicit consent and retention, safe audit logging without raw fields, no hard-coded administrator identity, and migrations with integrity tests. Treat status and communication records as confidential and separate them from public evidence citations.

## 7. Coverage and cross-project context

Compare with WagnerJon/application-atlas local-only persistence and Tyin-nn localStorage tracker: unlike those applications, this repository's committed data/ structure raises an immediate source-disclosure screening risk. It provides no verified 2026/27 international funded-vacancy evidence, nor an appropriate dataset for reproducing applicant claims. Test execution, deployment verification, privacy classification and ownership checks were NOT performed.

## 8. Verdict and citations

DEEP_REVIEW_DOCUMENTED (static code plus tree metadata). Reject as source material for any applicant profile or official application fact; investigate exposure responsibly without accessing contents. [README](https://github.com/rjalfa/PhDAdmission/blob/24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a/README.md), [Database fillUser](https://github.com/rjalfa/PhDAdmission/blob/24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a/src/ap/adm/phd/Database.java), [UserController logging and multipart](https://github.com/rjalfa/PhDAdmission/blob/24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a/src/ap/adm/phd/controller/UserController.java), [AuthenticationFilter](https://github.com/rjalfa/PhDAdmission/blob/24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a/src/ap/adm/phd/controller/AuthenticationFilter.java), [personal-information model](https://github.com/rjalfa/PhDAdmission/blob/24c08ffa203cdd73862cb1564aa6dbb1eb18fb3a/src/ap/adm/phd/model/PersonalInformation.java).
