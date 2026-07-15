import json
from pathlib import Path

from typer.testing import CliRunner

from drift_sheriff.cli import app


def test_resource_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/resource-change")
    expected = json.loads((fixture_dir / "expected-resource-report.json").read_text())

    result = CliRunner().invoke(
        app,
        [
            "resource",
            "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
            "--fixtures",
            str(fixture_dir),
        ],
    )

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected


def test_resource_command_returns_distinct_exit_code_for_missing_resource() -> None:
    fixture_dir = Path("tests/fixtures/resource-change")
    result = CliRunner().invoke(
        app,
        [
            "resource",
            "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/missing",
            "--fixtures",
            str(fixture_dir),
        ],
    )

    assert result.exit_code == 3
