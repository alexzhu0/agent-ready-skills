---
name: prompt-to-eval-rubric
description: Use when converting prompts, system instructions, assistant behaviors, or policy requirements into eval rubrics with scoring criteria, test cases, assertions, and failure modes.
---

# Prompt To Eval Rubric

## Purpose

Turn desired model behavior into a reusable evaluation rubric.

## Fit

- Use when prompt behavior must be evaluated repeatedly or compared across model/prompt versions.
- Do not use when the task is only rewriting the prompt and no evaluation criteria are needed.

## Inputs

- Prompt, system instruction, policy, desired behavior, or bad output.
- User goals, safety requirements, and known failure modes if available.
- Preferred scoring scale if provided.

## Workflow

1. Extract expected behaviors and forbidden behaviors.
2. Convert each behavior into a measurable criterion.
3. Tie each criterion to prompt evidence, policy evidence, or a clearly labeled assumption.
4. Add representative test cases, including edge cases.
5. Define pass/fail assertions and scoring guidance.
6. Preserve uncertainty where behavior is underspecified.

## Output

Produce Markdown with:

- Eval Goal
- Rubric Table
- Test Cases
- Assertions
- Failure Modes
- Scoring Notes
- Missing Requirements

## Validation

- Criteria are observable in outputs.
- Assertions can be judged consistently.
- Safety and correctness are not traded away for style.
- Ambiguous prompt requirements become missing requirements.
- Test cases include at least one likely failure case.
