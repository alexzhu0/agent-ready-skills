---
name: llm-cost-risk-review
description: Use when reviewing prompts, context bundles, agent workflows, or LLM product flows for token cost, latency risk, context bloat, repeated instructions, and budget guardrails.
---

# LLM Cost Risk Review

## Purpose

Find avoidable LLM cost, latency, and context-window risk before a workflow becomes expensive.

Use this skill for prompts, system instructions, retrieval packs, long context handoffs, and agent workflow plans.

## Inputs

- Prompt, context bundle, workflow description, or trace.
- Known model, token budget, latency target, or pricing if available.
- User-visible quality requirements.

## Workflow

1. Identify the cost drivers: repeated context, irrelevant files, verbose examples, long tool outputs, retries, and expensive model choices.
2. Separate essential context from convenience context.
3. Look for contradictions and stale instructions that increase reasoning load.
4. Recommend trimming, caching, summarization, retrieval, cheaper model routing, or eval gating.
5. State budget assumptions instead of pretending to know exact pricing when not provided.
6. Preserve quality-critical information even if it is long.

## Output

Produce Markdown with these sections:

- Cost And Latency Snapshot
- Main Cost Drivers
- Safe Trimming Plan
- Budget Assumptions
- Fallback Strategy
- Quality Risks

Keep recommendations operational: what to remove, keep, compress, cache, or test.

## Validation

- Cost estimates are labeled approximate unless exact pricing and token counts are provided.
- Trimming suggestions do not remove safety or correctness constraints.
- The fallback strategy says what to do when budget or latency is exceeded.
- Quality risks are listed next to cost savings.
- The review distinguishes one-time setup cost from per-run cost.
