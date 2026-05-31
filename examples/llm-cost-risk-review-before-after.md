# Example: llm-cost-risk-review

Use this with `skills/llm-cost-risk-review/SKILL.md`.

## Before

```text
Input:
- The agent is asked to review full git history, full README, all skills,
  and every issue when summarizing repo quality.
- Suggested model: large-context variant for all tasks.
- Response template always includes "comprehensive deep analysis" plus full path list.
- Workflow target: every user asks should be answered "carefully and completely".
- Latency budget: < 4s for first reply.
- No cost budget or token limit has been assigned.

Observed issues:
- Retrieving every issue and README path per run increases noise.
- Prompt asks for always-on full-depth analysis.
- No explicit fallback for latency miss.
```

## After

```markdown
# Cost and Latency Snapshot

- Workflow risk: High prompt/context bloat risk due to over-inclusive input requirements.
- Main constraint conflict: asks for "comprehensive" while expecting <4s.
- Uncertainty: no explicit token budget or pricing constants.

## Main Cost Drivers

- Full-history and full-repo scans for routine summaries.
- "Always use large-context model" instruction without task tiering.
- Mandatory exhaustive output format requirements.

## Safe Trimming Plan

- Keep repo checks narrow by trigger:
  - For review requests: `README.md`, `highstar.yaml`, changed `SKILL.md`, and last 3 issues.
  - For style checks: `SKILL.md` + `README.md` only.
- Add model routing:
  - Cheap model for first-pass summary and candidate extraction.
  - Large model only when output requires risk synthesis.
- Replace "comprehensive" with evidence-scoped defaults:
  - "comprehensive within provided scope" unless user explicitly asks for deep expansion.

## Budget Assumptions

- Assume a soft per-run context ceiling before switching to cheap model.
- Treat token estimates as approximate; count only provided context fields as budget drivers.

## Fallback Strategy

- If token budget exceeds expected bounds, truncate to latest context and open issues only.
- Return an explicit warning: "Output is a scoped summary; request expand for full history."

## Quality Risks

- Skipping full history may miss older context. Keep this as a tradeoff, not a silent fallback.
- Model switch may change style but should preserve required constraints.
- Scoped summaries must still include guardrails and missing-evidence markers.
```

