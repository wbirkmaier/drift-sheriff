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

Repository scaffolding and CLI baseline are in place. Attribution and ownership slices land next.
