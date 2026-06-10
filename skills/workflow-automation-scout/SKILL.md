---
name: workflow-automation-scout
description: Use when reviewing repeated manual processes, team workflows, operational checklists, or task logs to identify automation candidates, required inputs, ROI, risks, and human approval points.
---

# Workflow Automation Scout

## Purpose

Find useful automation opportunities without automating unclear or risky judgment.

## Inputs

- Process notes, SOPs, task logs, checklists, or repeated manual work descriptions.
- Frequency, time cost, failure rate, and tools involved if available.
- Constraints around approvals, compliance, and user impact.

## Workflow

1. Break the workflow into repeatable steps and judgment-heavy steps.
2. Estimate value using frequency, time saved, error reduction, and user impact.
3. Identify required inputs, outputs, tools, and integration points.
4. Add safeguards, approval gates, and fallback paths.
5. Rank candidates by value, feasibility, and risk.

## Output

Produce Markdown with:

- Workflow Snapshot
- Automation Candidates
- Value Estimate
- Required Integrations
- Human Approval Points
- Risks And Safeguards
- Recommended First Automation

## Validation

- Automation candidates are tied to repeated work.
- Judgment-heavy steps keep human review.
- ROI is labeled approximate unless measured.
- External writes and customer-visible actions include gates.
- The first automation is small enough to pilot.
