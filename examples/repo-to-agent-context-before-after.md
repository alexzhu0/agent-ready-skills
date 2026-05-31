# Example: repo-to-agent-context

Use this with `skills/repo-to-agent-context/SKILL.md`.

## Before

```text
Repo: repos/agent-ready-skills
Task: "Add a small documentation improvement and keep the existing structure."
Observed files: root README, 10 SKILL.md files, one validator script, example folder, release notes.
Unknowns:
- No CI config was shown.
- No typecheck or unit tests were provided.
- No known risk register or known issue template.
Request from user: keep changes focused and safe.
```

## After

```markdown
# Repository Context Brief

## Repository Snapshot

- Purpose: Public collection of AI-agent workflow Skills (10 total).
- Technology: Markdown-first docs + Python validator script.
- Safety posture: No external runtime requirements; examples are synthetic.

## Project Map

- `README.md`: usage guide, skill index, examples, install instructions.
- `skills/`: one folder per skill, each containing only `SKILL.md`.
- `scripts/validate_skills.py`: local structural validator.
- `examples/`: before/after inputs and outputs for onboarding.
- `highstar.yaml` / `LICENSE` / `CONTRIBUTING.md` / `SECURITY.md`: repo metadata and contribution policy.

## Entrypoints And Data Flow

- Human edits:
  - Update documentation in `README.md` and `CONTRIBUTING.md` first.
  - Edit individual `SKILL.md` only when workflow clarity needs direct improvement.
- Publishing flow:
  - Validate with the local script, then run highstar review and publish.
```

```markdown
## Commands

- `python3 scripts/validate_skills.py .`
- `python3 /Users/alex/HighStarRepo/tools/highstar.py review .`
- `python3 /Users/alex/HighStarRepo/tools/highstar.py publish --owner alexzhu0 repos/agent-ready-skills`

## Task-Relevant Files

- `README.md`
- `skills/repo-to-agent-context/SKILL.md`
- `scripts/validate_skills.py`
- `examples/*.md` (when adding onboarding demos)

## Risks And Constraints

- No tests for execution behavior beyond structural checks.
- Any change to examples should remain synthetic and non-sensitive.
- Avoid adding per-skill auxiliary docs, which breaks the repository style.

## Recommended First Steps

1. Re-run validator after documentation edits.
2. Confirm `main` remains clean and pushes cleanly.
3. If only clarity improved, keep a scoped PR with low merge risk.
```

