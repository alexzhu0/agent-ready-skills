# Example: tool-permission-audit

Use this with `skills/tool-permission-audit/SKILL.md`.

## Before

```text
Agent tools:
- read files
- edit files
- run shell commands
- create GitHub issues
- publish releases

Policy: move fast, complete the user request, and ask only when needed.
```

## After

```markdown
## Permission Matrix

| Tool | Risk | Default gate |
| --- | --- | --- |
| Read files | May expose unrelated private data | Allowed for task-relevant paths |
| Edit files | May overwrite user work | Allowed after checking scope |
| Run shell commands | May mutate state or leak secrets | Read-only allowed; writes need task relevance |
| Create GitHub issues | Public external write | Requires explicit user authorization |
| Publish releases | Public external state change | Requires explicit user authorization |

## Required Clarifications

- Define what "ask only when needed" means for external writes.
- Separate local reversible actions from public irreversible actions.

## Recommended Policy Patch

Allow local read-only inspection by default. Require explicit approval for public GitHub writes, release publishing, destructive commands, and credential changes.
```
