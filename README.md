# DriftSheriff

DriftSheriff explains who changed an AWS resource, through what channel, and whether the change still lines up with declared ownership.

## Current focus

- offline evidence correlation from sanitized fixtures
- exact actor and repository attribution where the input supports it
- read-only issue and report generation

## Deliberate limits

- no automatic reverts
- no mutation of AWS resources
- no drift claim without source evidence and ownership context

## Running modes

- Offline: fixture-backed CloudTrail, Config, and ownership analysis
- Live: planned read-only adapters for AWS APIs and repository metadata sources

## Safety

- read-only by default
- deterministic JSON output
- evidence IDs preserved in every conclusion

## Status

```bash
uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change
uv run drift-sheriff account --fixtures tests/fixtures/account-snapshot
```

The current slice correlates one resource or an account fixture from offline evidence and returns exact event IDs, actor/session details, ownership hints, and drift-fit classification. Issue rendering lands in later slices.
