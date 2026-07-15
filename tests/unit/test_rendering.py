from pathlib import Path

from drift_sheriff.analysis import analyze_resource
from drift_sheriff.fixtures import load_fixture
from drift_sheriff.rendering import render_issue


def test_render_issue_matches_expected_markdown() -> None:
    report = analyze_resource(
        load_fixture(Path("tests/fixtures/resource-change")),
        "arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef",
    )

    rendered = render_issue(report, "github")

    assert rendered == Path("tests/fixtures/resource-change/expected-issue.md").read_text().rstrip(
        "\n"
    )
