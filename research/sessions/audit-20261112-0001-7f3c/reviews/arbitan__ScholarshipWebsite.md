# arbitan/ScholarshipWebsite — false-positive screening review

- Repository ID: 123375259
- Default branch: master
- Inspected commit: 1d109c0b184a6e1cec1d5c71eda9cb722ad04928
- Created: 2018-03-01; last observed push: 2018-04-02
- Tree: 81 entries (67 files, 14 directories)
- Review disposition: SCREENED_EXCLUDE — academic-scholarship keyword collision, not a PhD admissions or funding resource
- Confidence: High for scope and structure; PDF body not inspected

## 1. Relevance determination

The repository description identifies this as a “Scholarship Articles Website for Owen Gottlieb PHD.” Its only substantive page is a faculty/research website featuring one academic article titled “You Can't Wrap Herring in an iPad: Digitization of Sacred Jewish Books, the Stripping of Embodied Ritual, and Implications for Jewish Education.”

The page describes the article's research topic and links to ScholarWorks for other downloadable scholarship by the faculty author. Here, “scholarship” means academic research/publications, not scholarships, doctoral funding, vacancies, or admissions advice.

No PhD opportunity discovery, application workflow, funding search, applicant experience, supervisor matching, or admissions guidance is implemented.

## 2. Repository structure

The recursive tree contains 81 entries: 67 blobs and 14 directories. The relevant application assets are:
- Scholarship/index.html — one static faculty article page.
- Scholarship/permission.html — a permission correspondence page.
- Scholarship/Gottlieb_Herring_in_an_iPad.pdf — the featured article PDF.
- Scholarship/css/stylesheet.css — custom page styles.
- Scholarship/img/* — institutional, publication, and project images.
- Scholarship/vendor/* — vendored Bootstrap, Font Awesome, jQuery, and jQuery Easing.
- Scholarship.zip — a 2 MB archive alongside the expanded site tree.

There is no README, application backend, structured data, database, tests, CI workflow, or package/build configuration. The site is static HTML/CSS with client-side JavaScript.

## 3. Functionality and implementation

The single index page presents the article title and abstract, links to the local PDF, and provides a link to the faculty author's ScholarWorks search. The footer links to external projects, institutional affiliations, and Google Scholar.

The upCount() JavaScript function increments localStorage.clickcount and logs it to the browser console. It is not a server-side download counter, analytics system, or persistent cross-user metric.

The page loads jQuery 1.12.4 and Bootstrap 3.3.7 from external CDNs and also vendors Bootstrap/Font Awesome locally. It has no data ingestion, search, authentication, user records, or application-state management.

Static markup defects include nested interactive anchors/button elements around the PDF link, incomplete metadata, and external target=_blank links without consistent rel protections. The stylesheet contains duplicate/inconsistent font declarations and malformed or ineffective declarations. These are maintenance issues in a legacy static site, not admissions-system defects.

## 4. Copyright and privacy boundary

permission.html contains a correspondence page recording permission to post the named article on a faculty website, with a copyright notice and explicit restrictions on reproduction, storage, distribution, and transmission without express written permission. It is not an open-source license or a general redistribution grant.

The correspondence also contains personal contact details. Those details are not reproduced here. The article PDF was not downloaded, quoted, or copied: its title and abstract in index.html are sufficient to establish that the repository is an academic publication page outside the admissions corpus. No license file was found in the repository tree.

Do not mirror the PDF or permission correspondence into the public PhD Atlas repository. Any separate scholarly use must be assessed against the rights notice and publisher permission.

## 5. Maintenance and validation

The repository has five commits, one branch, no reported issues or pull requests, and no license file. Its latest observed push dates to 2018. No runtime/browser test was performed; the source tree and relevant HTML/CSS were statically inspected. The PDF body and external link freshness were not inspected because they are unnecessary for the admissions-relevance decision and subject to the rights boundary above.

## 6. Final disposition

Exclude from the PhD admissions research corpus as a keyword collision. Retain the exclusion rationale and source URL so that future discovery passes do not repeatedly classify it as a funding or admissions resource.
