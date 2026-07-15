## Problem

Actor and channel evidence are necessary, but drift review also depends on whether the change lines up with the resource's declared owner and approved automation path.

## Approach

- added ownership mapping records to the fixture bundle
- computed likely owner repository and first-pass ownership fit classification
- surfaced likely drift when a console change touches a resource that appears to belong to an IaC-managed repository

## Important decisions

- kept ownership fit distinct from the lower-level actor/channel classification so the report can show both the raw signal and the higher-level interpretation
- used explicit owner-tag to repository mapping in the first slice rather than inventing repository guesses from the ARN alone
- treated missing ownership data as an unknown-owner state rather than silently forcing a drift conclusion

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change`

## Known limitations

- ownership fit still relies on fixture mappings and tag presence
- no account-wide rollup or issue rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- no material findings after local self-review
