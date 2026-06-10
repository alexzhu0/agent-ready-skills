---
name: agent-handoff-brief
description: Use when handing work from one AI agent, developer, or session to another by summarizing current state, files touched, decisions made, blockers, verification, and next safe actions.
---

# Agent Handoff Brief

## Purpose

Create a compact handoff that lets another agent resume without redoing discovery.

## Inputs

- Current task, conversation notes, file changes, commands run, or partial results.
- Known blockers, validation status, and user constraints.
- Repository path or artifact locations.

## Workflow

1. State the objective and current status.
2. List files touched and decisions made.
3. Record commands run and their outcomes.
4. Capture blockers, risks, and unresolved questions.
5. Recommend the next safe action.

## Output

Produce Markdown with:

- Objective
- Current State
- Files And Artifacts
- Decisions
- Verification
- Blockers
- Next Actions

## Validation

- The handoff distinguishes facts from plans.
- File paths and artifact names are precise.
- Verification status includes what was not tested.
- Next actions are ordered and reversible when possible.
- The receiving agent should not need the full prior chat to continue.
