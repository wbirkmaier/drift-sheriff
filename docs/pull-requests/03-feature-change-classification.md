## Problem

Exact evidence is necessary, but reviewers also need an initial classification that explains whether the change looks like console activity or an automation path.

## Approach

- added source-channel and classification fields to the resource report
- classified console-driven changes separately from assumed-role automation and unknown actor paths
- preserved the underlying event evidence while adding the higher-level label

## Important decisions

- based classification on actor and channel evidence already present in the event rather than ungrounded naming heuristics
- kept the classification set intentionally small in the first pass so meanings stay clear
- left ownership and drift-likelihood for a later slice instead of overloading the first classifier

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change`

## Known limitations

- classification is still evidence-driven but coarse
- no repository ownership or approval mapping yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- no material findings after local self-review
