from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from drift_sheriff.exceptions import DriftSheriffError
from drift_sheriff.fixtures import load_fixture
from drift_sheriff.models import FixtureBundle


class EvidenceAdapter:
    def load(self, source: Path) -> FixtureBundle:
        raise NotImplementedError


@dataclass(frozen=True)
class FixtureEvidenceAdapter(EvidenceAdapter):
    def load(self, source: Path) -> FixtureBundle:
        return load_fixture(source)


@dataclass(frozen=True)
class AwsEvidenceAdapter(EvidenceAdapter):
    profile: str | None = None

    def load(self, source: Path) -> FixtureBundle:
        raise DriftSheriffError(
            f"live AWS evidence loading is not implemented for {source}; "
            "use fixture-backed snapshots or add an AWS adapter implementation"
        )


def get_evidence_adapter(mode: str) -> EvidenceAdapter:
    if mode == "fixture":
        return FixtureEvidenceAdapter()
    if mode == "aws":
        return AwsEvidenceAdapter()
    raise DriftSheriffError(f"unsupported evidence adapter mode: {mode}")
