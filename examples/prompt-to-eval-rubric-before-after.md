# Example: prompt-to-eval-rubric

Use this with `skills/prompt-to-eval-rubric/SKILL.md`.

## Before

```text
Prompt: Summarize customer support tickets and identify urgent issues. Be concise and do not miss important blockers.
```

## After

```markdown
## Eval Rubric

| Criterion | Good behavior | Failure mode |
| --- | --- | --- |
| Urgency detection | Flags outages, account lockouts, payment failures, and data loss | Treats urgent issues as normal feedback |
| Evidence use | Cites ticket text or clear paraphrases | Invents details not present in the ticket |
| Concision | Produces a compact summary with actions | Produces broad commentary without decisions |

## Test Cases

1. Billing outage ticket should be labeled urgent.
2. Feature request without blocker should not be labeled urgent.
3. Ambiguous complaint should list missing evidence instead of guessing.

## Assertions

- Output includes severity.
- Output includes evidence.
- Output includes next action or missing information.
```
