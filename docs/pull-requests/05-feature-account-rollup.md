## Problem

Resource-level attribution is useful, but operators also need a wider account view to see how many changes look manual, automated, or likely drift-related in one sweep.

## Approach

- added account-wide rollup analysis over all resources in a fixture bundle
- counted changes by classification and ownership-fit state
- exposed `drift-sheriff account --fixtures <dir>`

## Important decisions

- reused the resource-level attribution path rather than building a second account-specific classifier
- preserved the per-resource reports inside the account output so the summary remains traceable back to exact evidence
- aligned the account-level counts with the existing coarse classification logic rather than inventing a separate taxonomy

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff account --fixtures tests/fixtures/account-snapshot`

## Known limitations

- rollups are still fixture-backed and do not yet page live AWS evidence
- no GitHub issue output yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- corrected the account-level expected classification counts to match the actual automation classification logic instead of weakening the classifier
