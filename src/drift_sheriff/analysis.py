from __future__ import annotations

from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.models import FixtureBundle, ResourceAttributionReport


def _source_channel(user_agent: str) -> str:
    if "console.amazonaws.com" in user_agent:
        return "console"
    if "aws-sdk" in user_agent:
        return "sdk"
    return "unknown"


def analyze_resource(bundle: FixtureBundle, arn: str) -> ResourceAttributionReport:
    resource = next((item for item in bundle.resources if item.arn == arn), None)
    if resource is None:
        raise DriftSheriffError(f"resource not found in fixture: {arn}", exit_code=3)

    matching_events = [item for item in bundle.trail_events if item.resource_arn == arn]
    if not matching_events:
        raise DriftSheriffError(f"no trail events found for resource: {arn}", exit_code=4)

    latest_event = sorted(matching_events, key=lambda item: item.event_time)[-1]
    return ResourceAttributionReport(
        arn=resource.arn,
        resource_type=resource.resource_type,
        actor_arn=latest_event.actor_arn,
        session_name=latest_event.session_name,
        source_channel=_source_channel(latest_event.user_agent),
        event_ids=sorted(event.event_id for event in matching_events),
        before=resource.before.attributes,
        after=resource.after.attributes,
        tags=resource.tags,
    )
