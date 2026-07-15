import json
from pathlib import Path

from typer.testing import CliRunner

from drift_sheriff.cli import app


def test_account_command_matches_expected_output() -> None:
    fixture_dir = Path("tests/fixtures/account-snapshot")
    expected = json.loads((fixture_dir / "expected-account-report.json").read_text())

    result = CliRunner().invoke(app, ["account", "--fixtures", str(fixture_dir)])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == expected
