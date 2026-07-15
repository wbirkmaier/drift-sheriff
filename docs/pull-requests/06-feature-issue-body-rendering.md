## Problem

Attribution reports are useful, but investigators often want a ready-to-file issue body that preserves the same evidence and ownership context.

## Approach

- added GitHub issue body rendering for a single attributed resource report
- exposed `drift-sheriff issue <arn> --fixtures <dir> --format github`
- kept the issue content aligned with the existing resource report instead of inventing a second narrative path

## Important decisions

- rendered issue output from the existing report model so the JSON report remains the source of truth
- kept the format intentionally concise and evidence-first
- did not include auto-remediation steps because the tool does not perform or validate reverts

## Test evidence

- `uv run ruff check .`
- `uv run mypy src`
- `uv run pytest`
- `uv run pytest --cov=src --cov-report=term-missing`
- `uv build`
- `uv run drift-sheriff issue arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change --format github`

## Known limitations

- only GitHub markdown issue rendering is supported in this slice
- no account-level report rendering yet

## Self-review

- [x] Security reviewed
- [x] No write operations introduced
- [x] Output ordering is deterministic
- [x] Attribution claims are evidence-based

## Review findings

- no material findings after local self-review
