# Example: tool-permission-audit

Use this with `skills/tool-permission-audit/SKILL.md`.

## What This Shows

A broad autonomy policy becomes a least-privilege permission model with clear gates for local work, public writes, credentials, and destructive actions.

## Before

```text
Agent setup:

Tools:
- read and edit local repository files
- run shell commands
- browse the web
- use the GitHub connector
- create GitHub issues
- push commits
- publish releases
- read environment variables

Current policy:
"Move fast and complete the user request. Ask only when needed.
Do not bother the user for routine work."

Team concern:
The agent is useful, but we do not know which actions require approval.
We want autonomy for normal coding and documentation, but we do not want accidental public writes, release publishing, credential exposure, or destructive shell commands.
```

## After

````markdown
## Permission Matrix

| Capability | Side effect class | Risk | Default gate |
| --- | --- | --- | --- |
| Read local files | Local read | May expose unrelated private data | Allowed for task-relevant paths |
| Edit repository files | Local write | May overwrite user work | Allowed after checking git status and scope |
| Run read-only shell commands | Local read | May reveal secrets in logs | Allowed when command is task-relevant |
| Run mutating shell commands | Local write or destructive | May delete files, change services, or alter state | Allowed only when reversible and task-relevant; destructive commands need explicit approval |
| Browse the web | External read | May use stale or untrusted sources | Allowed; cite sources when facts matter |
| Use GitHub connector | External read/write depending on action | May expose or modify public state | Read allowed for task-relevant repos; writes need explicit authorization |
| Create GitHub issues | Public external write | Creates durable public artifact | Requires explicit user authorization |
| Push commits | External write | Publishes code changes | Requires explicit user authorization unless already delegated for this repo/task |
| Publish releases | Public external write | Creates public release artifact | Requires explicit user authorization |
| Read environment variables | Credential-sensitive read | May expose secrets | Deny by default unless exact variable is requested and needed |

## Risk Summary

- The phrase "ask only when needed" is too vague for public writes and credentials.
- Local reversible work and public irreversible work are currently mixed under one autonomy rule.
- Release publishing has a higher blast radius than normal code edits and needs its own gate.
- Environment variable access should be treated as credential-sensitive, not routine local read.

## Approval Gates

| Action | Gate |
| --- | --- |
| Local read-only inspection | No approval when task-relevant |
| Local file edits | No approval when scoped to the requested task and git status is checked |
| Tests, linters, validators | No approval unless they require credentials or production services |
| Public issue/comment creation | Explicit user authorization |
| Commit push or release publish | Explicit user authorization unless the user has already delegated publishing in the current task |
| Destructive commands such as `rm -rf`, `git reset --hard`, database deletes | Explicit user authorization |
| Secret or credential access | Explicit user authorization and exact variable/path scope |

## Overbroad Access

- "Use the GitHub connector" should be split into read-only inspection and write actions.
- "Run shell commands" should be split into read-only, mutating, destructive, and credential-touching commands.
- "Read environment variables" is overbroad without exact names and purpose.

## Recommended Policy Patch

Use this replacement policy:

```text
The agent may autonomously inspect task-relevant files, run read-only commands,
edit requested repository files, and run local verification.

The agent must request explicit user authorization before public external writes,
release publishing, credential access, destructive commands, production data changes,
or actions outside the requested repository/task scope.

When an action is public, irreversible, credential-sensitive, or destructive,
the agent must name the action, target, and expected effect before proceeding.
```

## Residual Risks

- The policy still relies on correct classification of shell commands.
- GitHub write authorization should be scoped to a specific repo and task.
- Web browsing can still introduce low-quality evidence; source quality must be reviewed separately.
````
