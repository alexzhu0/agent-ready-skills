---
name: bug-report-to-repro
description: Use when converting bug reports, user complaints, screenshots, logs, or QA notes into a reproducible case with environment, steps, expected behavior, actual behavior, and missing evidence.
---

# Bug Report To Repro

## Purpose

Turn vague bug reports into a clear reproduction brief that engineering or QA can use.

## Fit

- Use when a bug report has enough symptom evidence to form a reproducible test path or triage brief.
- Do not use when the request is root-cause debugging without a concrete observed failure.

## Inputs

- Bug text, screenshot notes, logs, environment details, or user complaint.
- Version, browser, device, account role, feature area, and regression clues if available.
- Known expected behavior.

## Workflow

1. Extract symptom, environment, user role, and affected feature.
2. Draft the smallest plausible reproduction path.
3. Separate known facts from missing evidence.
4. Record expected versus actual behavior.
5. Add diagnostic questions that would reduce uncertainty fastest.

## Output

Produce Markdown with:

- Reproduction Brief
- Environment
- Repro Steps
- Expected Vs Actual
- Evidence
- Missing Data
- Triage Notes

## Validation

- Steps are ordered and executable.
- Expected behavior is not invented when unknown.
- Missing environment details are listed.
- Regression claims include the evidence source.
- The brief is short enough to paste into an issue tracker.
