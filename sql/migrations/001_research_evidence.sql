PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS research_repositories (
  repository_key TEXT PRIMARY KEY,
  canonical_url TEXT NOT NULL UNIQUE,
  github_id TEXT UNIQUE,
  owner TEXT NOT NULL,
  name TEXT NOT NULL,
  category TEXT,
  original_license TEXT,
  last_checked TEXT,
  current_screening_state TEXT NOT NULL CHECK (current_screening_state IN ('UNTRIAGED','SCREENED_INCLUDE','SCREENED_EXCLUDE','REVIEW_RECORDED')),
  exclusion_reason TEXT
);

CREATE TABLE IF NOT EXISTS repository_audits (
  id TEXT PRIMARY KEY,
  repository_key TEXT NOT NULL REFERENCES research_repositories(repository_key),
  snapshot_sha TEXT NOT NULL CHECK (length(snapshot_sha)=40),
  checked_on TEXT NOT NULL,
  review_state TEXT NOT NULL CHECK (review_state IN ('PRELIMINARY_FOCUSED','DEEP_REVIEW_DOCUMENTED','INDEPENDENTLY_VALIDATED')),
  review_path TEXT NOT NULL UNIQUE,
  empirical_execution TEXT NOT NULL DEFAULT 'NOT_TESTED',
  UNIQUE(repository_key, snapshot_sha, checked_on)
);

CREATE TABLE IF NOT EXISTS repository_findings (
  id TEXT PRIMARY KEY,
  audit_id TEXT NOT NULL REFERENCES repository_audits(id),
  summary TEXT NOT NULL,
  claim_class TEXT NOT NULL,
  original_file_url TEXT NOT NULL,
  source_locator TEXT,
  source_checked_on TEXT NOT NULL,
  current_applicability TEXT NOT NULL CHECK (current_applicability IN ('CURRENT','HISTORICAL','TRANSFERABLE_METHOD','CONFLICT','UNKNOWN')),
  verified_by TEXT
);

CREATE TABLE IF NOT EXISTS repository_relations (
  source_repo_key TEXT NOT NULL REFERENCES research_repositories(repository_key),
  destination_repo_key TEXT NOT NULL REFERENCES research_repositories(repository_key),
  relation_type TEXT NOT NULL CHECK (relation_type IN ('FORK_OF','DERIVED_FROM','REUSES_DATA','SHARES_SOURCE','LINKS_TO','SUPERSEDES','SAME_METHOD')),
  evidence_url TEXT NOT NULL,
  checked_on TEXT NOT NULL,
  PRIMARY KEY (source_repo_key,destination_repo_key,relation_type)
);

CREATE TABLE IF NOT EXISTS claim_register (
  id TEXT PRIMARY KEY,
  subject TEXT NOT NULL,
  predicate TEXT,
  value_text TEXT,
  units TEXT,
  applicable_cycle TEXT,
  status TEXT NOT NULL CHECK(status IN ('SUPPORTED_PRIMARY','SUPPORTED_SECONDARY','FIRSTHAND_SINGLE','CORROBORATED_FIRSTHAND','HISTORICAL','INFERENCE','CONFLICT','UNVERIFIED','CONDITIONAL_HISTORICAL')),
  checked_on TEXT NOT NULL,
  independently_checked_on TEXT,
  uncertainty TEXT,
  decision_effect TEXT
);

CREATE TABLE IF NOT EXISTS claim_sources (
  claim_id TEXT NOT NULL REFERENCES claim_register(id),
  source_id TEXT NOT NULL REFERENCES sources(id),
  locator TEXT,
  source_applicable_cycle TEXT,
  source_role TEXT NOT NULL CHECK(source_role IN ('SUPPORTS','CONTRADICTS','DISCOVERY_ONLY')),
  retrieval_status TEXT,
  PRIMARY KEY (claim_id,source_id)
);

CREATE TABLE IF NOT EXISTS research_publications (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  year INTEGER CHECK (year BETWEEN 1900 AND 2200),
  doi TEXT UNIQUE,
  publication_state TEXT NOT NULL CHECK(publication_state IN ('PEER_REVIEWED','PREPRINT','POSTER','SUBMITTED','UNDER_REVIEW','UNKNOWN')),
  source_id TEXT REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS supervisor_publications (
  supervisor_id TEXT NOT NULL REFERENCES supervisors(id),
  publication_id TEXT NOT NULL REFERENCES research_publications(id),
  relevance_basis TEXT,
  PRIMARY KEY (supervisor_id,publication_id)
);

CREATE TABLE IF NOT EXISTS opportunity_verification (
  opportunity_id TEXT PRIMARY KEY REFERENCES opportunities(id),
  verified_on TEXT NOT NULL,
  application_channel_status TEXT NOT NULL,
  individual_funding_status TEXT NOT NULL,
  international_tuition_status TEXT NOT NULL,
  offer_date_evidence TEXT NOT NULL,
  salary_or_stipend_terms TEXT,
  employer_status_discrepancy TEXT,
  action_blockers TEXT,
  source_id TEXT REFERENCES sources(id)
);

CREATE TABLE IF NOT EXISTS applicant_experience_cases (
  id TEXT PRIMARY KEY,
  source_url TEXT NOT NULL,
  posted_on TEXT,
  country_id TEXT REFERENCES countries(id),
  observed_process TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  survivorship_risk TEXT,
  external_recheck TEXT
);

CREATE TABLE IF NOT EXISTS communication_actions (
  id TEXT PRIMARY KEY,
  application_id TEXT REFERENCES applications(id),
  supervisor_id TEXT REFERENCES supervisors(id),
  state TEXT NOT NULL CHECK(state IN ('DRAFTED','APPROVED','SENT','RESPONDED','CANCELLED')),
  authorized_at TEXT,
  authorized_by TEXT,
  delivery_reference TEXT,
  sent_at TEXT,
  private_content_path TEXT,
  CHECK(state NOT IN ('SENT','RESPONDED') OR (authorized_at IS NOT NULL AND authorized_by IS NOT NULL AND delivery_reference IS NOT NULL AND sent_at IS NOT NULL))
);

CREATE TABLE IF NOT EXISTS recorded_discovery_searches (
  id TEXT PRIMARY KEY,
  channel TEXT NOT NULL,
  query TEXT NOT NULL,
  requested_page INTEGER NOT NULL CHECK (requested_page>=1),
  run_at TEXT NOT NULL,
  raw_returned INTEGER NOT NULL CHECK (raw_returned>=0),
  unique_new INTEGER NOT NULL CHECK (unique_new>=0),
  duplicate_count INTEGER NOT NULL CHECK (duplicate_count>=0),
  run_status TEXT NOT NULL,
  error_reason TEXT
);

CREATE INDEX IF NOT EXISTS idx_audit_repo ON repository_audits(repository_key,checked_on);
CREATE INDEX IF NOT EXISTS idx_repo_findings_audit ON repository_findings(audit_id);
CREATE INDEX IF NOT EXISTS idx_claim_sources_source ON claim_sources(source_id);
CREATE INDEX IF NOT EXISTS idx_supervisor_papers_paper ON supervisor_publications(publication_id);
CREATE INDEX IF NOT EXISTS idx_communication_application ON communication_actions(application_id,state);
CREATE INDEX IF NOT EXISTS idx_search_channel ON recorded_discovery_searches(channel,run_at);

CREATE TRIGGER IF NOT EXISTS guard_acceptance_without_evidence_insert
BEFORE INSERT ON applications
WHEN NEW.state='ACCEPTED' AND NOT EXISTS (
  SELECT 1 FROM application_events
  WHERE application_id=NEW.id AND event_type='ACCEPTANCE_RECEIPT' AND evidence_ref IS NOT NULL
)
BEGIN SELECT RAISE(ABORT,'ACCEPTED application requires an acceptance evidence event'); END;

CREATE TRIGGER IF NOT EXISTS guard_acceptance_without_evidence_update
BEFORE UPDATE OF state ON applications
WHEN NEW.state='ACCEPTED' AND NOT EXISTS (
  SELECT 1 FROM application_events
  WHERE application_id=NEW.id AND event_type='ACCEPTANCE_RECEIPT' AND evidence_ref IS NOT NULL
)
BEGIN SELECT RAISE(ABORT,'ACCEPTED application requires an acceptance evidence event'); END;

CREATE TRIGGER IF NOT EXISTS guard_critical_application_event_insert
BEFORE INSERT ON application_events
WHEN NEW.event_type IN ('APPLICATION_SUBMITTED','SUPERVISOR_CONTACTED','OFFER_ACCEPTED','ACCEPTANCE_RECEIPT')
AND (NEW.evidence_ref IS NULL OR trim(NEW.evidence_ref)='')
BEGIN SELECT RAISE(ABORT,'Critical action events require evidence_ref'); END;
