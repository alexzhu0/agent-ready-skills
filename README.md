# Agent Ready Skills

Twenty practical AI-agent skills for turning messy work into clear specs, evals, reviews, briefs, and launch-ready artifacts.

This repository is intentionally simple: each skill is one folder with one `SKILL.md`. Copy a folder into a compatible skills directory, or paste the selected `SKILL.md` into your agent instructions.

## Why

Agent builders repeatedly need the same workflows: turning docs into tool specs, turning incidents into evals, reviewing risk, compressing handoffs, and preparing small repositories for release.

These skills make those workflows explicit, readable, and easy to adapt.

## Why These 20

The set focuses on workflows that appear repeatedly in public agent-skill ecosystems and real agent operations:

- Product and planning work: PRDs, roadmaps, competitive briefs, telemetry insights.
- Quality and eval work: support-ticket evals, prompt rubrics, bug repros, incident postmortems.
- Engineering risk work: RFCs, dependency upgrades, database migrations, security and privacy reviews.
- Agent operations: handoffs, tool permissions, automation scouting, launch readiness.

The common pattern is not "make the agent smarter." It is "make repeated expert work reusable, inspectable, and safer."

## Quality Bar

Each skill is expected to:

- Trigger from a specific messy input, not a vague topic.
- State when to use it and when not to use it.
- Produce an artifact someone can paste into an issue, PRD, review, launch note, or eval suite.
- Preserve evidence, assumptions, and unknowns.
- Avoid unsafe external actions, credential exposure, and irreversible operations.

## Install

```bash
git clone https://github.com/alexzhu0/agent-ready-skills.git
cd agent-ready-skills
python3 scripts/validate_skills.py .
```

Use one skill:

```bash
mkdir -p ~/.codex/skills
cp -R skills/bug-report-to-repro ~/.codex/skills/
```

Or paste the selected `SKILL.md` into any agent that supports project instructions.

## Quickstart

1. Pick a skill from the index.
2. Read its `SKILL.md`.
3. Attach the messy source material.
4. Ask the agent to produce the output sections named by the skill.

Example:

```text
Use the bug-report-to-repro skill on this support complaint and produce a reproduction brief.
```

## Best First Trials

These are the fastest ways to see whether the repository is useful before reading all 20 skills:

| Try this first | Why it is useful | Example |
| --- | --- | --- |
| `bug-report-to-repro` | Turns a vague complaint into an issue-ready reproduction brief. | [Before/after](examples/bug-report-to-repro-before-after.md) |
| `prompt-to-eval-rubric` | Turns a loose prompt into a reusable eval rubric. | [Before/after](examples/prompt-to-eval-rubric-before-after.md) |
| `tool-permission-audit` | Turns broad agent autonomy into explicit approval gates. | [Before/after](examples/tool-permission-audit-before-after.md) |

## 30-Second Trial

Paste `skills/bug-report-to-repro/SKILL.md` into your agent with this input:

```text
The import button fails for CSV files over 20MB. User sees "Upload complete" but the file never appears. Browser: Chrome. Account: admin test tenant. It worked last week.
```

Expected output shape:

```markdown
## Reproduction Brief
- Symptom: CSV import appears complete but file does not appear.
- Scope: Chrome, admin test tenant, files over 20MB.
- Regression clue: worked last week.

## Repro Steps
1. Sign in as admin in the test tenant.
2. Upload a CSV file larger than 20MB.
3. Observe completion message.
4. Check whether the file appears in the import list.
```

## Skill Index

| Skill | Job | Best input | Expected output |
| --- | --- | --- | --- |
| `api-doc-to-tool-spec` | Convert API docs into agent tool specs | Endpoint docs, OpenAPI notes | Capabilities, inputs, auth, examples, risks |
| `changelog-to-upgrade-plan` | Turn release notes into upgrade plans | Changelogs, migration notes | Impact map, tasks, tests, rollback |
| `support-ticket-to-eval` | Convert support tickets into eval cases | Tickets, complaints, transcripts | Scenario, expected behavior, assertions |
| `customer-call-to-prd` | Turn customer calls into product requirements | Call notes, interview notes | Problems, requirements, non-goals, risks |
| `incident-log-to-postmortem` | Summarize incidents into postmortems | Logs, timelines, status notes | Timeline, impact, root causes, actions |
| `messy-notes-to-decision-log` | Extract decisions from rough notes | Notes, chat dumps, scratch docs | Decision log, evidence, owners, questions |
| `roadmap-to-release-plan` | Convert roadmap ideas into release plans | Roadmap notes, feature lists | Milestones, scope, dependencies, risks |
| `telemetry-to-product-insights` | Translate product metrics into insights | Events, funnels, dashboards | Findings, hypotheses, experiments |
| `bug-report-to-repro` | Turn bug reports into reproducible cases | Bug text, screenshots, logs | Repro steps, expected/actual, missing data |
| `competitive-research-brief` | Summarize competitor research | Notes, pages, feature comparisons | Positioning, gaps, claims, watchlist |
| `architecture-rfc-review` | Review architecture proposals | RFCs, diagrams, design docs | Risks, tradeoffs, questions, decision advice |
| `database-migration-risk-review` | Review data migration plans | SQL, migration docs, schemas | Risk map, checks, rollback, rollout plan |
| `dependency-upgrade-risk-review` | Review dependency upgrade risk | Package diffs, release notes | Breaking changes, tests, rollout advice |
| `security-review-checklist` | Build a pragmatic security review | Feature spec, threat notes | Assets, trust boundaries, checks |
| `privacy-data-flow-map` | Map data collection and privacy risk | Product flow, events, forms | Data inventory, retention, consent risks |
| `prompt-to-eval-rubric` | Turn prompts into eval rubrics | Prompt, expected behavior | Rubric, cases, scoring, failure modes |
| `agent-handoff-brief` | Create a handoff for another agent | Task state, files, blockers | Current state, next steps, risks |
| `tool-permission-audit` | Audit agent tool permissions | Tool list, policy, commands | Permission matrix, risks, approval gates |
| `workflow-automation-scout` | Find automation opportunities | Repeated process notes | Automation candidates, ROI, safeguards |
| `repo-launch-readiness-review` | Review a repo before public launch | README, metadata, examples | Readiness score, blockers, polish tasks |

## Examples

Each example starts with realistic messy input, then shows the artifact the skill should produce.

| Skill | Example | Output you should expect |
| --- | --- | --- |
| `bug-report-to-repro` | [Bug report to repro brief](examples/bug-report-to-repro-before-after.md) | Issue-ready repro steps, evidence, missing data, and triage notes |
| `prompt-to-eval-rubric` | [Prompt to eval rubric](examples/prompt-to-eval-rubric-before-after.md) | Rubric, test cases, assertions, failure modes, and missing requirements |
| `tool-permission-audit` | [Tool policy to permission audit](examples/tool-permission-audit-before-after.md) | Permission matrix, approval gates, policy patch, and residual risks |

## API

```bash
python3 scripts/validate_skills.py .
python3 scripts/validate_skills.py . --score
```

The validator checks skill count, folder naming, YAML frontmatter, required sections, and optional quality scores.

This is a Markdown-first repository. There is no runtime API and no external service dependency.

## FAQ

**Does this call an LLM API?**

No. The repository contains Markdown skills and a standard-library Python validator.

**Are these tied to one agent runtime?**

No. The skills use a plain `SKILL.md` convention and can be adapted to folder-based skill runtimes or pasted into project instructions.

**Why replace the original 10 skills?**

The new set is broader and more practical for repeatable agent-builder work: specs, evals, risk reviews, privacy, security, handoffs, automation scouting, and launch readiness.

## Contributing

Issues and pull requests are welcome when they include a concrete workflow, a sample input, and the expected artifact.

Keep each skill self-contained. Do not add per-skill README files unless the repository structure intentionally changes.

## License

MIT
