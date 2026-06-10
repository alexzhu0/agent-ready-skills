---
name: architecture-rfc-review
description: Use when reviewing architecture RFCs, system design docs, diagrams, proposals, or technical decision records for tradeoffs, missing constraints, risk, and decision readiness.
---

# Architecture RFC Review

## Purpose

Review architecture proposals for clarity, risk, tradeoffs, and readiness to decide.

## Fit

- Use when a technical proposal needs a decision-quality review before implementation.
- Do not use when the task is only code style cleanup or a small isolated bug fix.

## Inputs

- RFC, design doc, diagram, ADR, or proposal.
- Requirements, constraints, scale expectations, and non-goals if available.
- Existing system boundaries or migration context.

## Workflow

1. Restate the proposal in one paragraph.
2. Identify assumptions, constraints, and missing requirements.
3. Review tradeoffs across reliability, operability, cost, security, and complexity.
4. List decision blockers separately from nice-to-have improvements.
5. Recommend approve, revise, reject, or spike with rationale.

## Output

Produce Markdown with:

- Proposal Summary
- Strengths
- Risks And Tradeoffs
- Missing Information
- Decision Blockers
- Recommendation
- Follow-Up Checks

## Validation

- Critique is tied to the actual proposal.
- Alternatives are not invented unless clearly labeled.
- Decision blockers are distinct from polish.
- Recommendation includes confidence.
- Operational and security concerns are considered.
