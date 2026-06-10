---
name: dependency-upgrade-risk-review
description: Use when reviewing dependency upgrades, package-lock diffs, SDK version changes, release notes, or migration guides for breaking changes, security impact, tests, and rollout risk.
---

# Dependency Upgrade Risk Review

## Purpose

Assess whether a dependency upgrade is safe, risky, or needs a staged rollout.

## Fit

- Use when a dependency version change needs impact, test, and rollout review.
- Do not use when choosing between unrelated packages; use a dependency-selection workflow instead.

## Inputs

- Current and target versions.
- Changelog, release notes, migration guide, lockfile diff, or package manifest.
- Local usage patterns and test coverage if available.

## Workflow

1. Identify version jump size and release date distance.
2. Extract breaking changes, security fixes, deprecations, and runtime changes.
3. Map changes to likely local usage.
4. Recommend tests, canary scope, and rollback.
5. Call out whether more source inspection is required.

## Output

Produce Markdown with:

- Upgrade Snapshot
- Breaking Changes
- Local Impact
- Security And Maintenance Notes
- Test Plan
- Rollout Recommendation
- Open Questions

## Validation

- Version numbers are exact.
- Changelog claims are not mixed with guesses.
- Test plan matches likely local impact.
- Security fixes are visible.
- Recommendation includes confidence and remaining unknowns.
