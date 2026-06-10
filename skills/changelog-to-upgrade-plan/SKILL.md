---
name: changelog-to-upgrade-plan
description: Use when reviewing changelogs, release notes, migration guides, or dependency announcements to create a practical upgrade plan with impact, tests, rollback, and owner-ready tasks.
---

# Changelog To Upgrade Plan

## Purpose

Convert release notes into an actionable upgrade plan without losing breaking changes or operational risk.

## Inputs

- Changelog, migration guide, release announcement, or dependency diff.
- Current version and target version.
- Known app usage, test commands, deployment path, and rollback constraints.

## Workflow

1. Extract breaking changes, deprecations, security fixes, and behavior changes.
2. Map changes to affected code paths, config, users, and runtime environments.
3. Classify each item as required, optional, risky, or informational.
4. Define test coverage needed before rollout.
5. Create rollback and monitoring notes for the first deployment.

## Output

Produce Markdown with:

- Upgrade Snapshot
- Impact Map
- Required Changes
- Test Plan
- Rollout And Rollback
- Open Questions

## Validation

- Version numbers and dates are copied exactly from evidence.
- Breaking changes are not buried under optional improvements.
- Test recommendations match the affected surfaces.
- Rollback is realistic for the repository or service.
- Unknown local usage is labeled as an assumption.
