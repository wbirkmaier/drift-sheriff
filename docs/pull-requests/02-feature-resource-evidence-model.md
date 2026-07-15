## Problem

DriftSheriff had a repository baseline but no working attribution path for a single resource change.

## Approach

- added typed fixture models for resources, before/after state, and CloudTrail-style events
- correlated one resource ARN to matching evidence events
- exposed `drift-sheriff resource <arn> --fixtures <dir>` with deterministic JSON output

## Important decisions

- kept the first slice focused on one resource ARN rather than a whole-account view so the evidence model could be exercised end to end
- preserved exact event IDs and actor/session metadata in the first report instead of collapsing everything into a higher-level classification prematurely
- treated missing trail evidence as a distinct error condition rather than silently returning partial attribution

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change`

## Known limitations

- no ownership mapping or drift classification yet
- source channel detection is still coarse in this slice

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- no material findings after local self-review
