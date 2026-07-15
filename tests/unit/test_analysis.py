from pathlib import Path

from drift_sheriff.analysis import analyze_resource
from drift_sheriff.fixtures import load_fixture


def test_analyze_resource_returns_expected_actor_and_event_ids() -> None:
    report = analyze_resource(
        load_fixture(Path("tests/fixtures/resource-change")),
        "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
    )

    assert report.actor_arn == "arn:aws:sts::111122223333:assumed-role/infra-admin/session-1234"
    assert report.event_ids == ["9bc0b580-35b1-4b72-94e4-5cb61191a001"]
    assert report.classification == "manual_console_change"


def test_analyze_resource_preserves_before_and_after_state() -> None:
    report = analyze_resource(
        load_fixture(Path("tests/fixtures/resource-change")),
        "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
    )

    assert report.before["healthCheckPath"] == "/healthz"
    assert report.after["healthCheckPath"] == "/readyz"
