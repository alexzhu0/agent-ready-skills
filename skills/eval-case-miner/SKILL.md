---
name: eval-case-miner
description: Use when converting bugs, user complaints, support tickets, logs, bad model outputs, or incident notes into reusable evaluation cases with inputs, expected behavior, assertions, and tags.
---

# Eval Case Miner

## Purpose

Turn real failures into reusable eval cases that prevent regressions.

Use this skill when a team has examples of bad model behavior but no structured eval yet.

## Inputs

- Bug report, user complaint, support ticket, log excerpt, trace, or bad model output.
- Product behavior expectation if known.
- Existing eval format if provided.

## Workflow

1. Identify the failure mode in plain language.
2. Extract the minimum input needed to reproduce the failure.
3. Write expected behavior as observable output, not vague intent.
4. Add assertions: must include, must not include, refusal condition, tool condition, or scoring rubric.
5. Tag the case by product area, risk type, model behavior, and priority.
6. Note privacy redactions or synthetic replacements needed before storing the case.
7. Group duplicate failures into one representative eval when possible.

## Output

Produce Markdown or JSON-like blocks with these sections:

- Eval Case Summary
- Input
- Expected Behavior
- Assertions
- Tags
- Source Evidence
- Redactions Needed

If the user provides an eval schema, match it.

## Validation

- The eval can fail or pass deterministically enough to be useful.
- Expected behavior is testable.
- Sensitive source data is redacted or marked for redaction.
- Tags support later filtering.
- The case preserves the original failure evidence.
