---
name: tool-permission-audit
description: Use when auditing AI-agent tool permissions, command policies, connector access, GitHub actions, file-system scopes, or automation rules for risk, approval gates, and least-privilege controls.
---

# Tool Permission Audit

## Purpose

Review an agent's tools and permission policy for unsafe access, unclear gates, and least-privilege gaps.

## Fit

- Use when an agent can read/write files, call connectors, run commands, publish, or touch credentials.
- Do not use when the agent has no tool access and only produces plain text.

## Inputs

- Tool list, command allowlist, connector scopes, system instructions, or policy text.
- User expectations for autonomy, external writes, destructive actions, and credentials.
- Known environment restrictions.

## Workflow

1. Inventory tools and classify their side effects.
2. Separate read-only, local write, external write, credential, and destructive actions.
3. Check whether approval gates match the risk.
4. Identify overbroad scopes and ambiguous wording.
5. Recommend a least-privilege policy patch.

## Output

Produce Markdown with:

- Permission Matrix
- Risk Summary
- Approval Gates
- Overbroad Access
- Policy Gaps
- Recommended Patch
- Residual Risks

## Validation

- Public or external writes are clearly gated.
- Destructive commands are not treated as normal execution.
- Credential handling is explicit.
- Local reversible actions are separated from irreversible actions.
- Recommendations preserve useful autonomy where risk is low.
