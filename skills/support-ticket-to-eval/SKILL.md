---
name: support-ticket-to-eval
description: Use when turning support tickets, user complaints, helpdesk transcripts, or failed assistant responses into reusable eval cases with expected behavior, assertions, and failure modes.
---

# Support Ticket To Eval

## Purpose

Turn real support pain into repeatable eval cases for product, support, or agent behavior.

## Fit

- Use when support evidence should become a reusable regression or model-behavior eval.
- Do not use when the ticket only needs a one-off human reply and no future check is useful.

## Inputs

- Support ticket, complaint, chat transcript, or failed assistant output.
- Product area, user role, and known expected behavior if available.
- Any sensitive details that must be redacted.

## Workflow

1. Redact private data while preserving the failure pattern.
2. Identify the user goal, current behavior, expected behavior, and severity.
3. Convert the case into a minimal input that reproduces the behavior.
4. Write assertions that can be checked by a human or automated judge.
5. Record variants that should be tested later.

## Output

Produce Markdown with:

- Eval Scenario
- Source Evidence
- Test Input
- Expected Behavior
- Failure Mode
- Assertions
- Variants

## Validation

- The eval preserves the original user pain without exposing secrets.
- Assertions are concrete enough to judge.
- Expected behavior is not invented when product intent is unknown.
- Severity is justified by evidence.
- The case can be reused without the full ticket context.
