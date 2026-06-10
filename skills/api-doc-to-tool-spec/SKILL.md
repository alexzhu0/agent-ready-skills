---
name: api-doc-to-tool-spec
description: Use when converting API documentation, endpoint notes, OpenAPI snippets, or integration docs into an agent-ready tool specification with capabilities, inputs, auth, examples, and operational risks.
---

# API Doc To Tool Spec

## Purpose

Turn API documentation into a compact tool specification an agent can safely use or hand to an implementer.

## Fit

- Use when source docs describe API behavior but an agent needs a safer tool contract before implementation or automation.
- Do not use when the source is only product intent with no endpoint, auth, or data-shape evidence.

## Inputs

- Endpoint docs, OpenAPI snippets, SDK examples, or integration notes.
- Auth requirements, rate limits, scopes, and sample requests if available.
- The intended agent workflow or user task.

## Workflow

1. Identify each capability the API exposes in plain language.
2. Extract required inputs, optional inputs, output shape, auth scopes, and errors.
3. Mark unclear fields as assumptions instead of guessing.
4. Separate read-only operations from write or destructive operations.
5. Add one minimal example request and one expected response shape per core operation.

## Output

Produce Markdown with:

- Tool Summary
- Capability Table
- Inputs And Outputs
- Auth And Rate Limits
- Example Calls
- Risks And Approval Gates
- Open Questions

## Validation

- Every capability maps back to evidence in the source docs.
- Required inputs are not mixed with optional inputs.
- Auth scopes and write operations are explicit.
- Unknown behavior is listed under open questions.
- Examples are small and do not include real secrets or private data.
