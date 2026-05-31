---
name: mcp-server-evaluator
description: Use when comparing MCP servers, tool connectors, plugin capabilities, or agent integrations by capability, auth needs, trust boundary, maintenance risk, and integration fit.
---

# MCP Server Evaluator

## Purpose

Help an agent team decide whether and how to adopt an MCP server or connector.

Use this skill for MCP server lists, connector docs, tool manifests, marketplace entries, and internal integration proposals.

## Inputs

- Server or connector names, docs, manifests, repository links, or tool descriptions.
- Target use case and environment.
- Security, privacy, or deployment constraints if known.

## Workflow

1. Identify each candidate and its primary job.
2. Compare capabilities, transports, auth model, data access, write operations, and maintenance signals.
3. Map the trust boundary: what data leaves the agent, what credentials are required, and what external systems can be changed.
4. Separate read-only use from write-capable or destructive use.
5. Identify setup complexity, local dependencies, hosted services, rate limits, and failure modes.
6. Recommend adopt, trial, defer, or reject with a short reason.

## Output

Produce Markdown with these sections:

- Evaluation Snapshot
- Capability Table
- Trust And Auth Boundary
- Operational Risks
- Integration Recommendation
- Trial Plan

Use tables for comparisons and concise prose for the final recommendation.

## Validation

- Each recommendation is tied to the target use case.
- Auth and write boundaries are explicit.
- Unknown maintenance or security facts are labeled unknown.
- No connector is recommended only because it is popular.
- The trial plan has a reversible first step.
