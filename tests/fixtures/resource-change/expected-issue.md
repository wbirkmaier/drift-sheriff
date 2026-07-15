## Drift investigation: `arn:aws:elasticloadbalancing:us-west-2:111122223333:targetgroup/payments-blue/1234567890abcdef`

Resource type: `AWS::ElasticLoadBalancingV2::TargetGroup`
Classification: `manual_console_change`
Ownership fit: `likely_iac_drift`
Likely owner repository: `github.com/example/platform-live`

### Evidence
- Actor: `arn:aws:sts::111122223333:assumed-role/infra-admin/session-1234`
- Session: `session-1234`
- Source channel: `console`
- Event IDs: `9bc0b580-35b1-4b72-94e4-5cb61191a001`

### State change
- Before: `{'healthCheckPath': '/healthz', 'healthyThreshold': '3'}`
- After: `{'healthCheckPath': '/readyz', 'healthyThreshold': '5'}`

### Suggested investigation
- Confirm whether the actor and session were expected for the owning repository.
- Compare the observed state change with the last intended IaC change for this resource.
