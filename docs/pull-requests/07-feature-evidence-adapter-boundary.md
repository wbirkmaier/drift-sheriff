## Problem

DriftSheriff still coupled its commands directly to the fixture loader, which would make later AWS-backed evidence loading unnecessarily invasive.

## Approach

- added a small evidence adapter interface
- implemented a fixture-backed adapter as the current shipped path
- added an explicit future AWS adapter stub that fails clearly rather than pretending live loading works

## Important decisions

- kept the adapter boundary narrow with one `load()` method returning the existing fixture bundle
- routed all three commands through the adapter now so later live integration can reuse the same analysis path
- made the future AWS adapter fail loudly with a targeted message instead of silently downgrading behavior

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff account --fixtures tests/fixtures/account-snapshot --adapter fixture`

## Known limitations

- the `aws` adapter mode is intentionally not implemented yet
- live CloudTrail, Config, and repository metadata loading are still fixture-first in this cycle

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- no material findings after local self-review
