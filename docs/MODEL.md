# Synthetic market mechanism model
This is an offline resource-admission/allocation lab, not a financial exchange or market attack tool. The example allocates fictional cloud capacity. No prices, securities, strategic agents, live interfaces, exploits or broker actions are modeled.

## Exact semantics
Requests are ordered entries with id, participant and integer units. Duplicate IDs may repeat; they are deliberately allowed as a stress fixture. Baseline aggregates all submissions per participant and allocates by first participant appearance. It is participant-priority FIFO, not exchange order-price-time matching.
A deduplicating candidate retains the first declaration per request ID and ignores later repeats, recording conflicting repeats. A participant cap limits admitted total units across IDs; identity labels are assumed, not authenticated or resistant to identity splitting.
Pro-rata allocates available capacity in integer shares proportional to admitted units. Floors are followed by largest-remainder allocation, ties by participant ID. All candidates use the same declared input; there is no automatic deployment or candidate selection.

Metrics: allocated units, unused capacity, participant allocations, served participant count and sum of squared allocation shares. Requested/unserved totals include repeated declarations and must not be interpreted as verified economic demand. No welfare, fairness, profit, equilibrium or systemic-risk guarantee follows.
Capacity and admitted-demand conservation checks validate finite examples only. Empty demand has undefined concentration (null).

## Cross-repository contract
The portable bundle contains study and report. Report schema is researchos-market-resilience/v1. The Grok-HedgeOps-DTI adapter recomputes the report with an identical evaluator and compares the entire canonical JSON; a SHA-256 digest binds input bytes after canonicalization, not identity or truth. Both repositories vendor the same standard-library module; changes require synchronized updates and golden-vector checks. This is offline file exchange, not a remote service dependency.

## Research and LLM boundaries
The Grok adapter can pass bounded synthetic study and report text to an explicitly supplied ask callback for a proposed research critique. Model prose remains unverified, cannot change rules or execute code, and requires independent human review. No API key, live LLM provider, automatic market-design extraction, formal proof, exploit discovery or repair deployment is configured.

## Evaluation plan
Use synthetic cases; vary capacity, requests, ordering, duplicate and conflicting IDs, participant caps and allocation rule. Inspect admitted and rejected demand and distribution trade-offs. Independently validate any economic interpretation before applying findings. Future work includes richer market models, causal validation and reviewed proposal schemas. No DARPA affiliation or IMR program participation is claimed.
