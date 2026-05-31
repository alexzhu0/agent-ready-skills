---
name: agent-skill-lint-review
description: Use when reviewing an agent Skill or SKILL.md draft before publishing to check trigger clarity, scope, safety boundaries, progressive disclosure, validation, and publish readiness.
---

# Agent Skill Lint Review

## Purpose

Review a skill draft before it is shared, installed, or published.

Use this skill for `SKILL.md` files, skill folders, prompt packs, and agent workflow instructions.

## Inputs

- Skill folder or `SKILL.md` content.
- Intended users and target workflow if known.
- Any repository or platform conventions the skill must follow.

## Workflow

1. Check frontmatter: name, description, trigger specificity, and mismatch with body.
2. Check scope: what the skill does, when to use it, and when not to use it.
3. Check workflow: steps should be clear without overloading context.
4. Check safety: credentials, destructive operations, external writes, privacy, and production actions.
5. Check progressive disclosure: move bulky examples or reference material out of the main body when needed.
6. Check validation: the skill should tell the agent how to know the work is complete.
7. Assign a publish-readiness score from 0 to 5.

## Output

Produce Markdown with these sections:

- Publish Readiness Score
- Trigger And Scope Findings
- Workflow Findings
- Safety Findings
- Validation Findings
- Minimal Fix List

Prefer concrete edits over broad advice.

## Validation

- Findings cite specific skill sections or missing sections.
- The score is justified by actionable blockers.
- Safety issues are separated from clarity issues.
- The fix list is short enough for a maintainer to apply in one pass.
- No new skill behavior is invented without labeling it as a suggestion.
