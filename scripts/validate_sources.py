#!/usr/bin/env python3
import csv
from datetime import date
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ALLOWED_CLAIM = {
    "SUPPORTED_PRIMARY", "SUPPORTED_SECONDARY", "FIRSTHAND_SINGLE",
    "CORROBORATED_FIRSTHAND", "HISTORICAL", "INFERENCE",
    "CONFLICT", "UNVERIFIED", "CONDITIONAL_HISTORICAL",
}
VALID_STATUS = {"open_verified", "rolling", "upcoming_confirmed", "verification_needed", "closed", "expired"}


def audit(data: Path = DATA) -> tuple[list[str], list[str], dict[str, int]]:
    errors = []
    warnings = []
    counts = {"claims": 0, "leads": 0, "unrechecked": 0, "undated_decisions": 0}
    try:
        with (data / "claim_register.jsonl").open(encoding="utf-8") as stream:
            claims = [json.loads(line) for line in stream if line.strip()]
        with (data / "opportunities.csv").open(encoding="utf-8", newline="") as stream:
            opportunities = list(csv.DictReader(stream))
    except (OSError, json.JSONDecodeError, csv.Error) as exc:
        return [f"Input load failed: {exc}"], [], counts
    counts["claims"] = len(claims)
    counts["leads"] = len(opportunities)
    seen = set()
    for idx, claim in enumerate(claims, 1):
        identity = claim.get("id")
        if not identity or identity in seen:
            errors.append(f"claim {idx}: duplicated/missing id")
        seen.add(identity)
        if claim.get("status") not in ALLOWED_CLAIM:
            errors.append(f"claim {identity}: invalid claim status")
        parsed = urlsplit(claim.get("source_url", ""))
        if parsed.scheme != "https" or not parsed.hostname:
            errors.append(f"claim {identity}: non-HTTPS or absent source")
        try:
            checked = date.fromisoformat(claim.get("checked_on", ""))
            if checked > date.today():
                warnings.append(f"claim {identity}: check date in the future relative to host")
        except ValueError:
            errors.append(f"claim {identity}: invalid check date")
        if claim.get("independent_recheck") in ("NOT_PERFORMED", None, ""):
            counts["unrechecked"] += 1
        if claim.get("status") == "CONFLICT":
            warnings.append(f"claim {identity}: unresolved source disagreement")
    ids = set()
    for row in opportunities:
        key = row.get("id")
        if not key or key in ids:
            errors.append(f"lead {key}: duplicated/missing id")
        ids.add(key)
        if row.get("status") not in VALID_STATUS:
            errors.append(f"lead {key}: invalid status")
        if not row.get("funding_verification"):
            errors.append(f"lead {key}: missing financing gate")
        if not row.get("offer_before_2027"):
            errors.append(f"lead {key}: missing offer-date evidence state")
        if not row.get("decision_date"):
            counts["undated_decisions"] += 1
        if row.get("status") == "open_verified" and row.get("funding_verification") in ("COMPETITIVE_UNAWARDED", "PROGRAM_FUNDING_PACKAGE_NOT_A_PERSONAL_AWARD"):
            warnings.append(f"lead {key}: application channel open but individual funding unawarded")
    if not claims:
        warnings.append("no claims to audit")
    if not opportunities:
        warnings.append("no opportunities to audit")
    return errors, warnings, counts


def main():
    errors, warnings, counts = audit()
    print(json.dumps({"structural_audit": "passed" if not errors else "failed", "counts": counts, "warnings": warnings, "errors": errors}, ensure_ascii=False, indent=2))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
