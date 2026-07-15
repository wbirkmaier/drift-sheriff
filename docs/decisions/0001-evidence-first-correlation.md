# ADR 0001: Start With Fixture-Backed Evidence Correlation

## Status

Accepted

## Context

Attribution logic depends on CloudTrail, Config, and ownership metadata that are not always available in local or CI environments.

## Decision

Start with fixture-backed evidence correlation and layer live AWS adapters later.

## Consequences

- tests stay deterministic
- attribution logic can mature before live API integration is added
