# Examples

```bash
uv run drift-sheriff resource arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change
uv run drift-sheriff account --fixtures tests/fixtures/account-snapshot
uv run drift-sheriff issue arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef --fixtures tests/fixtures/resource-change --format github
```

The shipped fixture correlates a target group health-check change with a matching CloudTrail management event and Config before/after state, then compares the actor path to the declared owning repository and automation role.
