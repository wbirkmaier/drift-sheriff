# Security

DriftSheriff is intended for read-only attribution and IaC ownership analysis.

## Reporting

Use GitHub security reporting for sensitive issues.

## Guardrails

- Do not log credentials, assumed-role tokens, or raw CloudTrail event payloads that contain secrets.
- Do not attempt automatic remediation.
- Keep fixtures sanitized and public-safe.
