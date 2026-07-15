from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer

from drift_sheriff.analysis import analyze_account, analyze_resource
from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.fixtures import load_fixture

app = typer.Typer(
    help="Explain AWS resource changes without mutating infrastructure.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)


@app.callback()
def callback() -> None:
    """DriftSheriff command group."""


@app.command("version")
def version() -> None:
    typer.echo("drift-sheriff 0.1.0")


@app.command("resource")
def resource(
    resource_arn: Annotated[str, typer.Argument(help="Resource ARN to attribute.")],
    fixtures: Annotated[
        Path,
        typer.Option(
            "--fixtures",
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
            help="Directory containing snapshot.json fixture data.",
        ),
    ],
) -> None:
    try:
        report = analyze_resource(load_fixture(fixtures), resource_arn)
    except DriftSheriffError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(report.model_dump_json(indent=2))


@app.command("account")
def account(
    fixtures: Annotated[
        Path,
        typer.Option(
            "--fixtures",
            exists=True,
            file_okay=False,
            dir_okay=True,
            readable=True,
            help="Directory containing snapshot.json fixture data.",
        ),
    ],
) -> None:
    try:
        report = analyze_account(load_fixture(fixtures))
    except DriftSheriffError as error:
        raise typer.Exit(code=error.exit_code) from error

    typer.echo(report.model_dump_json(indent=2))


def main(argv: Annotated[list[str] | None, typer.Argument(hidden=True)] = None) -> None:
    app(args=argv)
