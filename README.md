# Agent Ready Skills

Ten practical AI-agent skills for turning messy work into clear context, evals, reviews, and launch-ready artifacts.

This repository is intentionally simple: copy one skill folder, read one `SKILL.md`, and use it with any agent workflow that supports skill-like instructions.

## Why

Agent builders repeatedly solve the same problems: compressing context, reviewing prompt drift, debugging traces, turning failures into evals, and preparing small tools for public launch.

These skills make those workflows explicit, inspectable, and easy to adapt.

## Install

Clone the repository and run the validator:

```bash
git clone https://github.com/alexzhu0/agent-ready-skills.git
cd agent-ready-skills
python3 scripts/validate_skills.py .
```

To use a skill, copy a folder from `skills/` into your local skill directory, or paste the relevant `SKILL.md` into your agent instructions.

## Quickstart

Validate the collection:

```bash
python3 scripts/validate_skills.py .
```

Use one skill directly:

```bash
sed -n '1,180p' skills/deck-to-agent-kb/SKILL.md
```

Then ask your agent:

```text
Use the deck-to-agent-kb skill on examples/sample-deck-notes.md and produce an agent knowledge base.
```

## Skill Index

| Skill | Job | Best input | Expected output |
| --- | --- | --- | --- |
| `deck-to-agent-kb` | Convert slides and deck notes into agent knowledge | PPT notes, screenshots, slide exports | Page analysis, key facts, risk/action index, answer boundaries |
| `meeting-to-action-brief` | Turn meeting notes into action briefs | Notes, transcripts, chat logs | Decisions, owners, deadlines, blockers, follow-up prompts |
| `repo-to-agent-context` | Compress a repo before agent coding | File tree, README, manifests | Repo map, entrypoints, test commands, risks |
| `prompt-drift-review` | Review prompt and instruction changes | Diff, old/new prompt, AGENTS.md | Removed guardrails, risky additions, regression checks |
| `agent-skill-lint-review` | Review a skill before publishing | `SKILL.md` draft | Trigger clarity, safety, validation, publish-readiness score |
| `eval-case-miner` | Turn failures into eval cases | Bugs, logs, bad outputs | Scenario, input, expected behavior, assertions |
| `agent-trace-debugger` | Summarize agent traces | JSONL traces, tool logs | Timeline, root-cause candidates, retry advice |
| `mcp-server-evaluator` | Compare MCP/tool connectors | Server docs, manifests, tool list | Capability table, trust boundary, integration recommendation |
| `llm-cost-risk-review` | Reduce token cost and latency risk | Prompt, workflow, context bundle | Cost drivers, trimming plan, budget assumptions |
| `devtool-launch-pack` | Prepare a small devtool for launch | Repo README, metadata, demo | README checklist, topics, launch copy, release notes |

## Examples

Before:

```text
Slide 7: UAT screenshots. Some failures around permission prompts.
Slide 8: Qwen comparison. Large model better but slower.
Slide 9: Need final KB for agent use.
```

After using `deck-to-agent-kb`:

```markdown
## Key Facts
- UAT found permission-prompt failures on slide 7.
- Model comparison on slide 8 favors quality over latency.

## Risk And Action Index
| Risk | Evidence | Action |
| --- | --- | --- |
| Permission prompts block automation | Slide 7 screenshots | Add approval boundary and fallback path |

## Answer Boundaries
- The agent may summarize observed slide evidence.
- The agent must not claim production readiness without UAT sign-off.
```

More examples live in `examples/`.

## API

This is a markdown-first skill collection. The only executable interface in v0.1.0 is the validator:

```bash
python3 scripts/validate_skills.py .
```

The validator checks frontmatter, section coverage, naming, and minimum skill count.

## FAQ

**Does this call external AI APIs?**

No. The repository is plain Markdown plus a standard-library Python validator.

**Are these only for one agent product?**

No. The folders use a simple `SKILL.md` convention that can be adapted for Codex, Claude-style skills, or internal agent runtimes.

**Why one repository instead of ten?**

One repository is easier to browse, clone, validate, and adapt. Each skill remains independently copyable.

## Contributing

Issues and pull requests are welcome when they include a concrete workflow, a sample input, and the expected artifact.

Run this before opening a pull request:

```bash
python3 scripts/validate_skills.py .
```

## License

MIT
