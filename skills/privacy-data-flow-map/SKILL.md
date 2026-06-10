---
name: privacy-data-flow-map
description: Use when mapping product flows, event tracking, forms, integrations, or agent workflows into a privacy data-flow map covering collected data, purpose, retention, sharing, consent, and risk.
---

# Privacy Data Flow Map

## Purpose

Map what data a workflow collects, where it goes, and which privacy questions need review.

## Fit

- Use when a product or agent workflow handles user, customer, employee, or sensitive operational data.
- Do not use when no data collection, storage, sharing, or retention decision is involved.

## Inputs

- Product flow, form fields, event names, integration docs, or agent workflow.
- User roles, jurisdictions, retention requirements, and policy constraints if available.
- Known third-party processors or storage destinations.

## Workflow

1. Inventory data fields and classify sensitivity.
2. Map collection, processing, storage, sharing, and deletion.
3. Identify purpose, consent, retention, and access-control questions.
4. Flag unnecessary collection or unclear data use.
5. Recommend privacy review items and minimization options.

## Output

Produce Markdown with:

- Data Inventory
- Flow Map
- Purpose And Retention
- Third Parties
- Privacy Risks
- Minimization Options
- Open Questions

## Validation

- Data fields are specific, not vague categories.
- Sensitive data is marked clearly.
- Retention and deletion gaps are visible.
- Third-party sharing is not assumed safe.
- Recommendations reduce data where possible.
