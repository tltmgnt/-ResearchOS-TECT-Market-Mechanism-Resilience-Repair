# ResearchOS TECT — Market Mechanism Resilience & Repair
Offline synthetic-market research integrated with [Grok-HedgeOps-DTI](https://github.com/tltmgnt/Grok-HedgeOps-DTI).

## Implemented
A browser lab and CLI compare baseline resource allocation with candidate deduplication, participant-cap and pro-rata repairs. Includes invariant checks, distribution trade-offs, source/review notes, local storage and study/report, CSV and Markdown exports. See [model contract](docs/MODEL.md).

## Run
Python 3.10+, standard library only:
```sh
python -m unittest discover -s tests -v
python server.py
```
Open http://127.0.0.1:8000. The loopback server evaluates the shared Python model; file:// and static-only hosting are unsupported.
```sh
python cli.py examples/study.json --output market-review-bundle.json
```
Output refuses overwrite.

## Grok-HedgeOps integration
Copy the exported bundle to a Grok-HedgeOps-DTI checkout and run:
```sh
python market_resilience_review.py market-review-bundle.json --output market-research-review.json
```
The adapter recomputes results, rejects tampering and creates an explicitly unverified research review. This requires the companion integration PR. It does not authorize or affect trading.

## Verification
Model tests, HTTP smoke tests, and Python 3.10/3.12/3.13 CI check the CLI and browser server endpoints. JavaScript syntax is checked separately. Interactive browser behavior is not verified here; no executor is available in the originating conversation. Hosting remains unconfigured.

Synthetic examples only. No live venue connection, attack execution, formal resilience proof, investment recommendation, government affiliation or empirical effectiveness claim. No live LLM provider is configured. Apache-2.0 license retained.

## Terrain and market connectivity lab

Start with the market lesson. Mask the central spread/depth observation and compare the 8 bp and 14 bp thresholds. In a repair review, document who supplied the cost assumptions and why each transition is plausible. [Standalone course and exercises](curriculum/terrain_market_resilience/README.md)
