CREATE TRIGGER IF NOT EXISTS guard_submission_without_evidence_insert
BEFORE INSERT ON applications
WHEN NEW.state='SUBMITTED' AND NOT EXISTS (
  SELECT 1 FROM application_events
  WHERE application_id=NEW.id AND event_type='APPLICATION_SUBMITTED'
    AND evidence_ref IS NOT NULL AND trim(evidence_ref)<>''
)
BEGIN SELECT RAISE(ABORT,'SUBMITTED application requires a submission evidence event'); END;

CREATE TRIGGER IF NOT EXISTS guard_submission_without_evidence_update
BEFORE UPDATE OF state ON applications
WHEN NEW.state='SUBMITTED' AND NOT EXISTS (
  SELECT 1 FROM application_events
  WHERE application_id=NEW.id AND event_type='APPLICATION_SUBMITTED'
    AND evidence_ref IS NOT NULL AND trim(evidence_ref)<>''
)
BEGIN SELECT RAISE(ABORT,'SUBMITTED application requires a submission evidence event'); END;

CREATE TRIGGER IF NOT EXISTS guard_application_events_immutable_update
BEFORE UPDATE ON application_events
BEGIN SELECT RAISE(ABORT,'Application events are append-only'); END;

CREATE TRIGGER IF NOT EXISTS guard_application_events_immutable_delete
BEFORE DELETE ON application_events
BEGIN SELECT RAISE(ABORT,'Application events are append-only'); END;
