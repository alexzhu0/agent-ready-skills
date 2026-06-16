# Example: bug-report-to-repro

Use this with `skills/bug-report-to-repro/SKILL.md`.

## What This Shows

A vague support complaint becomes an issue-ready reproduction brief with facts, assumptions, missing evidence, and the fastest next checks.

## Before

```text
Support ticket:
"Import is broken again. The customer says the upload finished, but the file is nowhere.
This is blocking the monthly billing run."

Slack follow-up:
- CSV file is around 23MB.
- User is an admin in the Acme sandbox tenant.
- Browser is Chrome 126 on macOS.
- It worked last Tuesday before the import queue change.
- No screenshot yet.

Log snippet from support:
2026-06-15T09:42:11Z POST /imports csv status=202 duration=831ms
2026-06-15T09:42:13Z job.import.created tenant=acme-sandbox size=24111792
2026-06-15T09:42:18Z job.import.completed rows=0 warnings=0
```

## After

```markdown
## Reproduction Brief
- Symptom: CSV import reports completion, but the uploaded file does not appear in the import list or downstream billing workflow.
- Impact: blocks monthly billing run for Acme sandbox tenant.
- Affected area: CSV import flow and import queue processing.
- Scope: Chrome 126 on macOS, admin user, CSV around 23MB.
- Regression clue: support says the flow worked last Tuesday before the import queue change.
- Confidence: medium. The ticket has environment and logs, but no screenshot or UI recording.

## Environment

| Field | Value | Evidence |
| --- | --- | --- |
| Tenant | Acme sandbox | Slack follow-up |
| Role | Admin | Slack follow-up |
| Browser | Chrome 126 | Slack follow-up |
| OS | macOS | Slack follow-up |
| File type | CSV | Ticket and log path |
| File size | 24,111,792 bytes / about 23MB | `job.import.created` log |

## Repro Steps
1. Sign in as admin in the test tenant.
2. Open the CSV import page.
3. Upload a valid CSV file between 20MB and 25MB.
4. Wait for the UI to show upload completion.
5. Refresh the import list.
6. Check whether the file appears and whether the billing workflow can select it.

## Expected Vs Actual
- Expected: import appears in the import list with a nonzero row count, or the UI shows a clear validation/import failure.
- Actual: logs show `job.import.completed rows=0 warnings=0`, while the customer reports the file is missing after completion.

## Evidence

| Claim | Evidence | Notes |
| --- | --- | --- |
| Upload request accepted | `POST /imports csv status=202` | API accepted the import request. |
| File is larger than 20MB | `size=24111792` | Matches support note. |
| Job completed with zero rows | `job.import.completed rows=0 warnings=0` | Suspicious completion state. |
| Regression after queue change | "worked last Tuesday before the import queue change" | Needs release/change reference. |

## Missing Data
- Sample CSV shape or sanitized fixture.
- Screenshot or screen recording showing the completion message and missing list entry.
- Import job ID and correlation ID across API, queue, and UI list query.
- Release or commit that changed the import queue.
- Whether the issue reproduces below 20MB or only above 20MB.

## Triage Notes
- Priority: high if this blocks billing for a paying customer.
- First check: compare UI import list query with the completed job record for the same tenant.
- Likely failure class: accepted job reaches an invalid completed state instead of creating a visible import record.
- Fastest diagnostic question: does a 19MB CSV with the same schema appear correctly?
```
