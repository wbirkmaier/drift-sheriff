from pathlib import Path

from drift_sheriff.analysis import analyze_account, analyze_resource
from drift_sheriff.fixtures import load_fixture


def test_analyze_resource_returns_expected_actor_and_event_ids() -> None:
    report = analyze_resource(
        load_fixture(Path("tests/fixtures/resource-change")),
        "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
    )

    assert report.actor_arn == "arn:aws:sts::111122223333:assumed-role/infra-admin/session-1234"
    assert report.event_ids == ["9bc0b580-35b1-4b72-94e4-5cb61191a001"]
    assert report.classification == "manual_console_change"
    assert report.likely_owner_repository == "github.com/example/platform-live"
    assert report.ownership_fit == "likely_iac_drift"


def test_analyze_resource_preserves_before_and_after_state() -> None:
    report = analyze_resource(
        load_fixture(Path("tests/fixtures/resource-change")),
        "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
    )

    assert report.before["healthCheckPath"] == "/healthz"
    assert report.after["healthCheckPath"] == "/readyz"


def test_analyze_account_rolls_up_classifications() -> None:
    report = analyze_account(load_fixture(Path("tests/fixtures/account-snapshot")))

    assert report.classification_counts == {
        "expected_automation_change": 1,
        "manual_console_change": 1,
    }
    assert report.ownership_fit_counts == {
        "expected_automation_change": 1,
        "likely_iac_drift": 1,
    }
