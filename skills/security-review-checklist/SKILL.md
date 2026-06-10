---
name: security-review-checklist
description: Use when reviewing feature specs, tool integrations, agent workflows, API changes, or launch plans for security concerns such as auth, secrets, data exposure, abuse paths, and approval gates.
---

# Security Review Checklist

## Purpose

Create a pragmatic security review checklist for a feature or workflow.

## Fit

- Use when a feature, tool, integration, or agent workflow can affect data, auth, secrets, or external actions.
- Do not use when the change is purely cosmetic and has no trust boundary or data-flow impact.

## Inputs

- Feature spec, tool list, API change, workflow description, or launch plan.
- Auth model, data handled, deployment surface, and user roles if available.
- Known security requirements or compliance constraints.

## Workflow

1. Identify assets, actors, trust boundaries, and sensitive data.
2. Review auth, authorization, secrets, logging, and external calls.
3. Look for abuse paths, privilege escalation, data leakage, and unsafe defaults.
4. Convert findings into checks and required approvals.
5. Separate blockers from follow-up hardening.

## Output

Produce Markdown with:

- Security Scope
- Assets And Trust Boundaries
- Risk Checklist
- Required Controls
- Approval Gates
- Blockers
- Follow-Up Hardening

## Validation

- Sensitive data paths are explicit.
- Auth and authorization are checked separately.
- Findings have practical controls.
- Public or external writes require approval gates.
- Unknown security context is not treated as safe.
