# Contributing

Contributions should make the skills easier to understand, safer to run, or more useful on real agent workflows.

Good contributions include:

- A new realistic example input.
- A clearer validation checklist.
- A tighter trigger description.
- A safety boundary for risky actions.
- A skill improvement backed by a concrete use case.

Before opening a pull request:

```bash
python3 scripts/validate_skills.py .
```

Keep each `SKILL.md` concise. Do not add per-skill README files unless the repository maintainers decide to change the structure.

## Natural Growth Checklist

If this collection is in quiet growth mode, treat each cycle as a low-risk maintenance pass:

- Check metrics every 24h, 72h, and 7d with `python3 tools/highstar.py metrics --owner alexzhu0 agent-ready-skills`.
- If there is no visible usage signal, keep improvements scoped to clarity and onboarding.
- Add behavioral changes only when there is a concrete report that usage failed due to unclear input/output.
- Keep structure stable: no new subdirectories for each skill, no new dependencies, no non-deterministic examples.
- Record any structural decision in a short release note before next publish.
