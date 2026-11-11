# imsankalp/phD-application-tracker — pinned source investigation

- Revision: `073d96280e045d2dff25ba1906956e5f181a949a`
- Inspected on: 2026-11-12
- State: **DEEP_STATIC_READY_FOR_CANONICAL_RECONCILIATION**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: RECORDED (source-level, not independently validated)

## 1. Purpose

Express/Mongoose personal application tracker with optional Gmail OAuth inbox synchronization and mobile frontend.

## 2. Architecture

ApplicationController scopes CRUD and inbox imports by JWT user; GmailService reads subject:PhD messages, ScrapingService parses bodies into application status.

## 3. Data flow

src/utils/emailParser.js matches /Status: (\w+)/, truncating 'Under Review' to 'Under'; enum permits 'Under Review', not 'Under'.

## 4. Critical correctness

Email list defaults maxResults=25 and ScrapingService.processEmails does not follow nextPageToken, so it does not produce a complete historical ledger.

## 5. Identity and state

Controller defaults a missing parsed status to Submitted, which is not evidence a user actually submitted an application. Message sender and issuer are not validated in the parser.

## 6. Security and privacy

Application.sourceEmailId has an index but lacks a (user,sourceEmailId) unique compound index; concurrent upserts may duplicate receipts.

## 7. Validation boundaries

docs/FLOW.md describes OAuth, API and user journeys; runtime tests, OAuth account access, Gmail reads and live app operations were NOT executed.

## 8. Transfer verdict

Adapt Gmail only as an opt-in private receipt source with MIME/sender authentication, typed statuses, explicit unknown, pagination, unique identity, reconciliation and immutable provenance.

## Pinned upstream source paths

- [README.md](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/README.md)
- [src/utils/emailParser.js](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/src/utils/emailParser.js)
- [src/controllers/applicationController.js](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/src/controllers/applicationController.js)
- [src/services/gmailService.js](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/src/services/gmailService.js)
- [src/models/Application.js](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/src/models/Application.js)
- [docs/FLOW.md](https://github.com/imsankalp/phD-application-tracker/blob/073d96280e045d2dff25ba1906956e5f181a949a/docs/FLOW.md)
