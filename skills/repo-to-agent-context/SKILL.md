---
name: repo-to-agent-context
description: Use before coding-agent implementation work to compress a repository into a concise context brief covering project purpose, layout, entrypoints, dependencies, tests, risks, and first commands.
---

# Repo To Agent Context

## Purpose

Give a coding agent enough repository context to make a safe first edit without reading everything.

Use this skill before implementation, debugging, onboarding, code review, or refactoring in an unfamiliar repo.

## Inputs

- Repository path or file tree.
- README, manifests, package files, build files, and test files.
- User's intended task if known.

## Workflow

1. Inspect the README, top-level files, manifests, and likely entrypoints.
2. Map the main subsystems, runtime, package manager, tests, generated files, and local conventions.
3. Identify files likely relevant to the user's task.
4. Record commands for install, lint, test, typecheck, build, and demo when discoverable.
5. Flag risk areas: migrations, generated code, destructive commands, flaky tests, missing docs, or broad shared modules.
6. Recommend the smallest safe next exploration or implementation step.

## Output

Produce Markdown with these sections:

- Repository Snapshot
- Project Map
- Entrypoints And Data Flow
- Commands
- Task-Relevant Files
- Risks And Constraints
- Recommended First Steps

Keep it compact. Prefer facts from files over guesses.

## Validation

- Commands are copied from repo evidence or clearly labeled as inferred.
- Relevant files are named with paths.
- Risks distinguish repo facts from assumptions.
- The brief is short enough to fit in a coding-agent context handoff.
- The next step is reversible unless the user requested otherwise.
