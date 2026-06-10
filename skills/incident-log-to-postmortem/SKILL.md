---
name: incident-log-to-postmortem
description: Use when summarizing incident logs, outage timelines, status updates, alerts, or team notes into a clear postmortem with impact, timeline, root-cause candidates, and follow-up actions.
---

# Incident Log To Postmortem

## Purpose

Turn scattered incident material into a readable postmortem draft without overstating the root cause.

## Inputs

- Incident timeline, alerts, logs, status updates, or chat notes.
- Impact details, affected users, duration, and remediation steps if available.
- Current uncertainty or disputed explanations.

## Workflow

1. Build a chronological timeline from earliest signal to recovery.
2. Separate confirmed facts from hypotheses.
3. Identify impact, detection, mitigation, recovery, and prevention gaps.
4. List root-cause candidates with evidence and confidence.
5. Convert prevention ideas into owner-ready follow-up actions.

## Output

Produce Markdown with:

- Incident Summary
- Impact
- Timeline
- Root-Cause Candidates
- What Worked
- What Failed
- Follow-Up Actions
- Open Questions

## Validation

- Timeline entries include timestamps or clear ordering.
- Root cause is not claimed when only candidates exist.
- Impact is scoped to evidence.
- Follow-up actions have owners or owner placeholders.
- Blame language is removed; system factors are emphasized.
