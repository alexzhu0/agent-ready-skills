---
name: repo-launch-readiness-review
description: Use when reviewing a small repository before public launch for README clarity, examples, license, metadata, validation commands, issue hygiene, release notes, and obvious trust gaps.
---

# Repo Launch Readiness Review

## Purpose

Check whether a small repository is understandable, usable, and safe to publish.

## Inputs

- Repository README, file tree, metadata, examples, license, and release notes.
- Target audience, launch channel, and install path if available.
- Known validation commands and open issues.

## Workflow

1. Review whether a new visitor can understand the repo in under one minute.
2. Check install, quickstart, examples, license, security, and contribution paths.
3. Identify missing trust signals and confusing claims.
4. Score readiness and list launch blockers separately from polish.
5. Recommend the smallest changes before publishing.

## Output

Produce Markdown with:

- Readiness Score
- Visitor Summary
- Launch Blockers
- Trust And Metadata Checks
- Example Quality
- Polish Tasks
- Recommendation

## Validation

- Score rationale is visible.
- Blockers are separated from nice-to-have tasks.
- Claims in README are checked against files.
- Missing license or unsafe instructions are treated as blockers.
- Recommendations are small and release-oriented.
