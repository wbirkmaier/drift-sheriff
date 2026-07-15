from __future__ import annotations

from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.models import ResourceAttributionReport


def render_issue(report: ResourceAttributionReport, output_format: str) -> str:
    if output_format != "github":
        raise DriftSheriffError(f"unsupported issue format: {output_format}")

    lines = [
        f"## Drift investigation: `{report.arn}`",
        "",
        f"Resource type: `{report.resource_type}`",
        f"Classification: `{report.classification}`",
        f"Ownership fit: `{report.ownership_fit}`",
        f"Likely owner repository: `{report.likely_owner_repository or 'unknown'}`",
        "",
        "### Evidence",
        f"- Actor: `{report.actor_arn}`",
        f"- Session: `{report.session_name}`",
        f"- Source channel: `{report.source_channel}`",
        f"- Event IDs: `{', '.join(report.event_ids)}`",
        "",
        "### State change",
        f"- Before: `{report.before}`",
        f"- After: `{report.after}`",
        "",
        "### Suggested investigation",
        "- Confirm whether the actor and session were expected for the owning repository.",
        "- Compare the observed state change with the last intended IaC change for this resource.",
    ]
    return "\n".join(lines)
