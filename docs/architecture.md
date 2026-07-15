# Architecture

DriftSheriff keeps event ingestion, ownership mapping, attribution logic, and output rendering separate.

## Planned flow

1. Adapters load CloudTrail, Config history, resource tags, and ownership metadata.
2. Normalizers convert source documents into typed evidence records.
3. Analysis classifies actor channel, ownership fit, and drift likelihood.
4. Renderers emit JSON, issue bodies, and concise investigation summaries.

The current shipped adapter is fixture-backed, with a dedicated boundary so AWS-backed evidence loaders can be added later without rewriting the analysis path.
