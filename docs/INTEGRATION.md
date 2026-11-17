# Grok-HedgeOps-DTI compatibility anchor
Counterpart repository: https://github.com/tltmgnt/Grok-HedgeOps-DTI
Counterpart commit used in cross-repository CI: 2e4a25e96e08f88ef92bd7fe92e1e2e60f1bad6d

The contract job checks byte equality of the evaluator, exports a study/report bundle with this repository's CLI, runs the counterpart review CLI, and verifies human-review-required status with no execution authorization or evidence verification.

This proves compatibility only for that pinned public source state and tested fixture. It does not establish integration with trading, TECT assurance, a live LLM or production deployment. Updating the counterpart requires an explicit source pin update and passing contract checks. Both repos' related PRs must be merged for default-branch users to have the feature.
