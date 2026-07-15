from __future__ import annotations

import json
from pathlib import Path

from pydantic import ValidationError

from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.models import FixtureBundle


def load_fixture(fixtures_dir: Path) -> FixtureBundle:
    path = fixtures_dir / "snapshot.json"
    try:
        return FixtureBundle.model_validate(json.loads(path.read_text()))
    except FileNotFoundError as error:
        raise DriftSheriffError(f"fixture file not found: {path}") from error
    except ValidationError as error:
        raise DriftSheriffError(f"invalid fixture file: {path}: {error}") from error
