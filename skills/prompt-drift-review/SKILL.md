---
name: prompt-drift-review
description: Use when reviewing changes to prompts, system instructions, AGENTS.md files, safety policies, agent rules, or workflow instructions for behavior drift and missing regression checks.
---

# Prompt Drift Review

## Purpose

Review prompt and instruction changes for behavioral regressions before they reach users or agents.

Use this skill for diffs, old/new prompts, policy edits, agent role files, and workflow instruction updates.

## Inputs

- Old and new prompt text, or a git diff.
- Intended behavior change.
- Known safety, compliance, or workflow constraints.

## Workflow

1. Identify the intended change in one sentence.
2. List removed guardrails, weakened wording, new ambiguity, new authority, and new tool permissions.
3. Check whether the new text changes priority, scope, refusal behavior, data handling, or destructive-action boundaries.
4. Identify contradictions between old and new instructions.
5. Convert high-risk drift into regression scenarios.
6. Separate must-fix issues from style suggestions.

## Output

Produce Markdown with these sections:

- Drift Summary
- Removed Or Weakened Guardrails
- Risky Additions
- Contradictions
- Regression Checks
- Recommended Patch Notes

Lead with the highest-risk behavior changes.

## Validation

- Every finding references a specific old/new phrase or diff area.
- Safety and authority changes are called out explicitly.
- Regression checks are actionable and can be run by a human or agent.
- Style comments do not distract from behavior risk.
- If no material drift exists, say so clearly and note residual test gaps.
