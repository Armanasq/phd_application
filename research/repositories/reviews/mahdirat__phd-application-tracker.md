# MahdiRat/phd-application-tracker — preliminary source review

**Reviewed:** 2026-11-12. **Pinned upstream:** [014a6bba1aea38961cee136746218b9343da25c9](https://github.com/MahdiRat/phd-application-tracker/commit/014a6bba1aea38961cee136746218b9343da25c9).  
**State:** PRELIMINARY_FOCUSED, full four-file source tree; runtime not executed.  
**Disposition:** unfinished learning exercise; not a functional application-management product.

The entire application is a short Python CLI at `src/main.py` with a menu for Add/View/Update/Delete/Search/Exit. Only Add and View are implemented. Update/Delete/Search print placeholders without modifying records. Data are an in-memory `applications = []` list and are lost on process exit. There is no stable application identity, funding source, deadline, current-cycle state, status history, external source evidence, retry or durable storage.

**Execution blocker:** `src/main.py` imports `from models import Application`, but the complete Git tree has **no `models.py`**. The module therefore cannot run as checked out without external/unpublished files or code added elsewhere. The `requirements.txt.txt` file is empty and misnamed. No tests or README implementation instructions are present. The script constructs an example record before showing the menu; it is not an imported data source.

**Transfer:** at most an introductory CLI menu idea, not an implementation reference. A production tracker needs a typed application model, persistent unique key, per-applicant ownership, deadlines, evidence provenance, audit events and tested CRUD operations.

**Evidence:** [source](https://github.com/MahdiRat/phd-application-tracker/blob/014a6bba1aea38961cee136746218b9343da25c9/src/main.py).
