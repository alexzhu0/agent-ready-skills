# Example: agent-trace-debugger

Use this with `skills/agent-trace-debugger/SKILL.md`.

## Before

```jsonl
{"ts":"2026-05-31T10:00:00Z","type":"user","message":"Publish the skill repo and verify it."}
{"ts":"2026-05-31T10:00:03Z","type":"tool_call","tool":"validate_skills","input":"."}
{"ts":"2026-05-31T10:00:04Z","type":"tool_result","tool":"validate_skills","status":"ok","message":"validated 10 skills"}
{"ts":"2026-05-31T10:00:07Z","type":"tool_call","tool":"gh_auth_status","input":"github.com"}
{"ts":"2026-05-31T10:00:08Z","type":"tool_result","tool":"gh_auth_status","status":"error","message":"token in default is invalid"}
{"ts":"2026-05-31T10:00:12Z","type":"tool_call","tool":"publish_repo","input":"alexzhu0/agent-ready-skills"}
{"ts":"2026-05-31T10:00:13Z","type":"tool_result","tool":"publish_repo","status":"error","message":"GitHub CLI auth is not valid"}
{"ts":"2026-05-31T10:01:20Z","type":"tool_call","tool":"gh_auth_login","input":"device flow"}
{"ts":"2026-05-31T10:02:00Z","type":"tool_result","tool":"gh_auth_login","status":"ok","message":"Logged in as alexzhu0"}
{"ts":"2026-05-31T10:02:06Z","type":"tool_call","tool":"publish_repo","input":"alexzhu0/agent-ready-skills"}
{"ts":"2026-05-31T10:02:20Z","type":"tool_result","tool":"publish_repo","status":"ok","message":"Published https://github.com/alexzhu0/agent-ready-skills"}
```

## After

```markdown
# Agent Trace Debugger

## Run Snapshot

| Field | Value |
| --- | --- |
| Task | Publish the skill repo and verify it |
| Final state | Published successfully |
| First failure | Invalid GitHub CLI token |

## Failure Timeline

| Time | Event | Result |
| --- | --- | --- |
| 10:00:03 | Skill validator ran | Success: 10 skills validated |
| 10:00:07 | GitHub auth checked | Failure: default token invalid |
| 10:00:12 | Publish attempted anyway | Failure: GitHub CLI auth not valid |
| 10:01:20 | Device-flow login started | Recovery action |
| 10:02:00 | Login completed | Success: logged in as alexzhu0 |
| 10:02:06 | Publish retried | Success: repo published |

## First Failure

The first observed failure was authentication, not repository validation or publish logic.

Raw evidence:

```text
token in default is invalid
```

## Root-cause Candidates

| Candidate | Evidence | Confidence |
| --- | --- | --- |
| Expired or invalid `gh` token | `gh_auth_status` failed before publish | High |
| Repository content invalid | Validator passed before auth failure | Low |
| GitHub repo already existed | Publish later succeeded | Low |

## Retry Or Fix Plan

1. Run `gh auth login -h github.com`.
2. Re-run `gh auth status`.
3. Re-run the publish command only after auth is valid.
4. Verify remote README, release, topics, and issue state.

## Evidence To Preserve

- `validated 10 skills`
- `token in default is invalid`
- `Logged in as alexzhu0`
- `Published https://github.com/alexzhu0/agent-ready-skills`
```
