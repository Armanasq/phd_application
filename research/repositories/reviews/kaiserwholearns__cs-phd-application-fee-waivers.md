# KaiserWhoLearns/CS-PhD-Application-fee-waivers — source, eligibility and time-validity audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/KaiserWhoLearns/CS-PhD-Application-fee-waivers  
**GitHub repository ID:** 424778889  
**Pinned commit:** [4a7b9401d37356badb038eacb6255e3b914214ea](https://github.com/KaiserWhoLearns/CS-PhD-Application-fee-waivers/commit/4a7b9401d37356badb038eacb6255e3b914214ea)  
**Review state:** DEEP_REVIEW_DOCUMENTED — all single-README content and recursive file inventory inspected; 50 outbound links identified and structurally checked, but **none independently recrawled**.  
**Verdict:** ADAPT_DISCOVERY_AND_ELIGIBILITY_TAXONOMY_ONLY; all 2026/27 fee policies require fresh primary verification.

## 1. Purpose and scope

A community-maintained list of application **fee waivers** for CS doctoral and other graduate programs, predominantly United States and Canada, plus organization-based assistance programs. A fee waiver reduces a university **application charge**; it is not evidence of tuition remission, doctoral stipends, funded research contracts, admission or eligibility to study. The README says institutional rules and waiver eligibility differ by citizenship/permanent residency and the affected program. It explicitly states that absence from the list does not prove a school offers no waiver.

Source: [README](https://github.com/KaiserWhoLearns/CS-PhD-Application-fee-waivers/blob/4a7b9401d37356badb038eacb6255e3b914214ea/README.md).

## 2. Repository structure, materials and source classes

The repository consists of a concise Markdown-led catalogue rather than a crawler or automated qualification engine. Its README includes five headings: introduction, general fee waivers, institutional waivers, United States and Canada. The pinned README contains **50 Markdown links, 49 distinct destinations** (including contextual references, not 50 discrete fee-waiver offers). Links point to university graduate-admissions pages, department-specific instructions, event/association funding organizations, one Google Form, and advice/social resources. The file contains explanatory limitations such as domestic-only restrictions and in-application request procedures. There is no normalized CSV, JSON database, release-specific snapshot ledger, source change watcher, validity timestamp per policy, or private applicant record.

## 3. Task-to-evidence pipeline and derived eligibility fields

The intended operator flow is: identify applicant's target department -> inspect a list entry -> open the institution's primary fee policy or program office -> determine whether category, academic cycle and residence/nationality constraints apply -> request the waiver via official process -> record a written response/portal status. Common policy classes present in the README are financial need, approved program or association affiliation, sponsored diversity initiative, department discretion, waiver code, and separate graduate school versus CS department routes.

For a usable PhD application planner, each waiver claim requires at least `institution`, `department`, `program`, `admissions_cycle`, `fee_type=APPLICATION`, `applicant_class`, `eligible_nationalities_or_residencies`, `criteria`, `request_method`, `request_deadline`, `official_source_url`, `checked_at`, `source_excerpt`, `approval_state`, and `waiver_confirmation`. A list entry with an old link is a **lead** only, not a confirmed application budget reduction.

## 4. Source-backed freshness and correctness failures

- **Explicitly expired examples:** one UCSD CSE supplemental route cites **15 November 2021**, a Georgetown item references **fall 2022**, an NY/Northeastern entry refers to code `NUExperience24`, and another states a **2024** admission fee policy. These phrases are historical and cannot establish a 2026/27 waiver.
- **Latest commit does not refresh the catalogue:** the inspected head was committed on **23 October 2025** to add a Utah waiver; previous head history includes 2023 changes. One recent entry does not validate the ages of the other claims.
- **Broken relative link:** one UMass Amherst CICS Markdown destination is `cics.umass.edu/admissions/application-instructions` without scheme. It is not a robust absolute canonical URL. A separate absolute HTTPS UMass CICS item already exists.
- **Duplicate target identity:** Cornell Graduate School appears with distinct historical URL forms, UMass Amherst CICS appears in two entries; without canonicalization these can be counted as separate offers even if they describe the same policy.
- **General versus department mismatch:** the catalogue mixes general graduate fee waivers, engineering- or department-specific waivers and aid from applicant organizations, as well as non-CS/Master's-related pages. A waiver for one degree, program or school is not evidence for another.
- **Conditional international eligibility:** some notes explicitly exclude or restrict non-U.S. applicants while one Utah Kahlert entry labels international PhD applicants as a target class. These assertions have not been reverified at their official websites for 2026/27.
- **Variable trust tier:** one USC Viterbi note points to an individual researcher's FAQ and instructs emailing documents; such advice cannot replace an official written department confirmation. A 2021 Google Form is not automatically an approved ongoing university application method.
- **Availability versus approval:** a page saying applicants may request a waiver does not establish that the individual applicant satisfies requirements or that a fee has been waived. The original README has no request receipt/decision records.

These are direct observations of Markdown and history; no conclusion is asserted about current program rules or whether the historic links remain live.

## 5. Reproducibility, validation and data-quality model

A repeatable audit should snapshot official pages, follow redirects, preserve normalized policy dates, document per-URL fetch status and prove the claim using precise excerpts. It must distinguish `not_checked`, `possible`, `official_policy_found`, `eligible_on_current_terms`, `requested`, `approved`, `denied` and `expired`. Missing official evidence cannot be silently inferred from a third-party list. Each new cycle needs recheck, and any code/exception should carry a date range and eligible applicant class.

No CI, automated URL validator, timeline or tests are present in this Markdown-only repository. Static link counts and occurrence of historical years were verified at the pinned source, but no live HTTPS responses or source document bodies were fetched in this inspection.

## 6. Bias, ethics and uncertainty

The list is heavily North American; it does not represent a statistically complete global sample of universities or measure the proportion offering waivers. Community contributors select entries opportunistically. Fee-waiver eligibility may involve sensitive personal circumstances or documented membership: disclose or send records only after independently confirming the authorized official channel and lawful data handling. Organizational benefit lists, graduate school waivers and special scholarships cannot be pooled as interchangeable awards.

## 7. Connections and adoption into PhD Atlas

Compared with fee, funding and tuition data from `yongruiyu/CS_APP_Agent` and `dxeledx/PhdInfoHub`, this README is **fee-relief discovery**, not authoritative claim extraction. It complements a budget planner but should never mark a stipend-backed opening as funded or alter application-ready status on its own. The reusable design is a typed eligibility taxonomy and a per-target checklist that separates request date, institutional decision and financial outcome. For an international applicant, explicit non-U.S. eligibility and program-cycle matching are mandatory, rather than treating a general fee-waiver page as eligible.

## 8. Disposition and verification boundaries

**DEEP_REVIEW_DOCUMENTED — REFERENCE_ONLY pending official verification.** Inspected complete README, Markdown link inventory, GitHub commit dates and repository shape at the pinned commit. Did not inspect linked university pages or organization rules, call an application portal, submit requests, send emails, test external links, collect personal documents, or confirm an active 2026/27 waiver. Recheck official program policies before making cost or eligibility decisions.
