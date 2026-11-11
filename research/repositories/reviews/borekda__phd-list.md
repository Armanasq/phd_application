# borekda/phd-list — preliminary review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [3691b05582ae3c64e32bf9262d518dc648dadc8c](https://github.com/borekda/phd-list/commit/3691b05582ae3c64e32bf9262d518dc648dadc8c)  
**Review state:** PRELIMINARY_FOCUSED. Static dataset and description review.  
**Category:** historical vacancy datasets.  
**Verdict:** reference historical schema and examples only.  
**Primary risk:** expired 2018–2019 positions presented as current opportunities.

## Purpose and structure

A small static directory of cognitive neuroscience, psychology, behavioral science and decision-making PhD/postdoctoral opportunities. It stores records in `websites.yaml` and longer descriptions in `descriptions.md`. The record shape includes title, short description, URL, source/repository link, supervisors, deadline, tags and location/use labels.

The repository's last observed commit is 20 December 2018. It includes a MIT license.

## Useful historical example

The Swiss working-memory PhD description records a funded four-year position, approximate CHF 47,000–50,000 annual salary, desired qualifications, application materials and an explicit 31 January 2019 deadline. This is a good example of how an advert can be decomposed into salary, duration, research topic, supervisor, qualifications and application procedure. The amount and deadline are strictly historical and must not be reused as current facts.

## Limitations

Most listed deadlines and start dates are from 2019. There is no cycle field, source snapshot, last-verified timestamp, status transition, funding component model or applicant-class eligibility. Some entries mix PhD and postdoc positions or use an aggregator as the destination URL. A free-text `until filled` deadline cannot be evaluated without a current official source.

## PhD Atlas decision

Use the YAML shape as a minimal historical vacancy schema example, not as an active feed. Atlas should add cycle, date timezone/cutoff, employer/institution, source class, award/funding components, applicant scope, exact evidence spans and verification state. Preserve archived opportunities separately from current open opportunities.

**Coverage boundary:** the YAML, descriptions and license were inspected; external source pages were not re-fetched.
