from pathlib import Path

from typer.testing import CliRunner

from drift_sheriff.cli import app


def test_issue_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/resource-change")
    expected = (fixture_dir / "expected-issue.md").read_text().rstrip("\n")

    result = CliRunner().invoke(
        app,
        [
            "issue",
            "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
            "--fixtures",
            str(fixture_dir),
            "--format",
            "github",
        ],
    )

    assert result.exit_code == 0
    assert result.stdout == expected + "\n"
