# Example: prompt-to-eval-rubric

Use this with `skills/prompt-to-eval-rubric/SKILL.md`.

## What This Shows

A loose prompt becomes a repeatable eval rubric with scoring criteria, representative cases, assertions, and known gaps.

## Before

```text
System prompt draft:

"You summarize customer support tickets for the product team.
Be concise. Identify urgent issues and important blockers.
Do not miss anything important. Include next steps when needed."

Known complaints from PM:
- The model sometimes marks feature requests as urgent.
- It missed a data-loss report because the customer used vague language.
- Summaries are too long for the weekly triage doc.
- It occasionally invents a next step that support did not promise.
```

## After

````markdown
## Eval Goal

Check whether the ticket summarizer separates urgent operational risk from normal feedback, preserves evidence, stays concise, and avoids invented commitments.

## Eval Rubric

Score each output from 0 to 2 per criterion.

| Criterion | 2 - Pass | 1 - Partial | 0 - Fail |
| --- | --- | --- |
| Urgency detection | Flags outages, account lockouts, payment failures, security risk, or data loss | Flags risk but severity is vague | Treats urgent issues as normal feedback or marks low-risk feature requests urgent |
| Evidence use | Grounds every severity and next step in ticket text | Uses evidence for the main claim but leaves one unsupported detail | Invents facts, owners, dates, or commitments |
| Concision | Produces a compact summary suitable for a triage doc | Slightly verbose but still scannable | Produces broad commentary or repeats the whole ticket |
| Next step quality | Gives a concrete next action or says what is missing | Next action is useful but underspecified | Invents a promise or routes to the wrong owner |
| Uncertainty handling | Marks vague input as unclear and asks for missing facts | Notes uncertainty but still overstates confidence | Hides uncertainty or guesses |

## Test Cases

### Case 1: Real Urgent Issue

Input:

```text
We upgraded last night and now 400 invoices disappeared from the export screen.
Finance cannot close month-end. Please call us today.
```

Expected behavior:
- Severity is urgent.
- Summary names possible data loss or missing records.
- Next step routes to engineering/support escalation.
- Output does not claim invoices were deleted unless evidence proves deletion.

### Case 2: Non-Urgent Feature Request

Input:

```text
Can you add dark mode to the admin dashboard? It would be nice for our night shift team.
No production issue, just a request.
```

Expected behavior:
- Severity is not urgent.
- Summary labels it as a feature request.
- Next step is product backlog or no immediate action.

### Case 3: Vague Complaint With Risk Words

Input:

```text
The system did something weird and our numbers look wrong.
I am worried we will send the wrong report tomorrow.
```

Expected behavior:
- Severity is needs triage, not automatically confirmed urgent.
- Output asks for affected report, expected numbers, actual numbers, and account/date range.
- Output does not invent a root cause.

## Assertions

- Output includes `severity`.
- Output includes a one-sentence summary under 40 words.
- Output includes quoted or paraphrased evidence from the ticket.
- Output includes next action or missing information.
- Output does not invent commitments, owners, dates, or root causes.

## Failure Modes

- False positive urgency for ordinary feature requests.
- False negative urgency for data loss, billing blockage, access lockout, or production outage.
- Unsupported next steps such as "engineering will fix today."
- Long summaries that are not usable in a weekly triage doc.

## Missing Requirements

- No explicit severity scale was provided. This rubric assumes `urgent`, `needs triage`, and `normal`.
- No owner taxonomy was provided. Routing should stay generic unless the product team supplies owner rules.
````
