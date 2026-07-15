from __future__ import annotations

from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.models import FixtureBundle, ResourceAttributionReport


def _source_channel(user_agent: str) -> str:
    if "console.amazonaws.com" in user_agent:
        return "console"
    if "aws-sdk" in user_agent:
        return "sdk"
    return "unknown"


def _classify_change(actor_arn: str, source_channel: str) -> str:
    if source_channel == "console":
        return "manual_console_change"
    if ":assumed-role/" in actor_arn and "automation" in actor_arn:
        return "expected_automation_change"
    if ":assumed-role/" in actor_arn:
        return "unknown_actor"
    return "unknown_actor"


def _ownership_fit(
    actor_arn: str,
    source_channel: str,
    owner_tag: str | None,
    bundle: FixtureBundle,
) -> tuple[str | None, str]:
    if owner_tag is None:
        return None, "unknown_owner"
    ownership = next((item for item in bundle.ownership if item.owner_tag == owner_tag), None)
    if ownership is None:
        return None, "unknown_owner"
    if actor_arn in ownership.approved_role_arns:
        return ownership.repository, "expected_automation_change"
    if source_channel == "console":
        return ownership.repository, "likely_iac_drift"
    return ownership.repository, "ownership_mismatch"


def analyze_resource(bundle: FixtureBundle, arn: str) -> ResourceAttributionReport:
    resource = next((item for item in bundle.resources if item.arn == arn), None)
    if resource is None:
        raise DriftSheriffError(f"resource not found in fixture: {arn}", exit_code=3)

    matching_events = [item for item in bundle.trail_events if item.resource_arn == arn]
    if not matching_events:
        raise DriftSheriffError(f"no trail events found for resource: {arn}", exit_code=4)

    latest_event = sorted(matching_events, key=lambda item: item.event_time)[-1]
    source_channel = _source_channel(latest_event.user_agent)
    owner_tag = resource.tags.get("Owner")
    likely_owner_repository, ownership_fit = _ownership_fit(
        latest_event.actor_arn,
        source_channel,
        owner_tag,
        bundle,
    )
    return ResourceAttributionReport(
        arn=resource.arn,
        resource_type=resource.resource_type,
        actor_arn=latest_event.actor_arn,
        session_name=latest_event.session_name,
        source_channel=source_channel,
        classification=_classify_change(latest_event.actor_arn, source_channel),
        likely_owner_repository=likely_owner_repository,
        ownership_fit=ownership_fit,
        event_ids=sorted(event.event_id for event in matching_events),
        before=resource.before.attributes,
        after=resource.after.attributes,
        tags=resource.tags,
    )
