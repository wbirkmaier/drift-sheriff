# Examples

```bash
uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change
```

The shipped fixture correlates a target group health-check change with a matching CloudTrail management event and Config before/after state.
