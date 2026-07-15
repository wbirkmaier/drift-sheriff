# Threat Model

## Assets

- CloudTrail and Config evidence
- repository ownership mappings
- generated issue and report content

## Risks

- exposing credentials or session tokens in reports
- overstating drift from incomplete evidence
- attributing a change to the wrong repository or actor

## Mitigations

- fixture-first evidence modeling
- explicit evidence IDs in conclusions
- clear separation between ownership hints and confirmed source evidence
