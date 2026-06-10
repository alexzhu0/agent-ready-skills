# Example: bug-report-to-repro

Use this with `skills/bug-report-to-repro/SKILL.md`.

## Before

```text
The import button fails for CSV files over 20MB. User sees "Upload complete" but the file never appears. Browser: Chrome. Account: admin test tenant. It worked last week.
```

## After

```markdown
## Reproduction Brief
- Symptom: CSV import appears complete but file does not appear.
- Scope: Chrome, admin test tenant, files over 20MB.
- Regression clue: worked last week.

## Repro Steps
1. Sign in as admin in the test tenant.
2. Upload a CSV file larger than 20MB.
3. Observe the "Upload complete" message.
4. Check whether the file appears in the import list.

## Expected Vs Actual
- Expected: uploaded CSV appears in the import list.
- Actual: upload completion is shown, but the file is missing.

## Missing Data
- Exact file size and sample CSV shape.
- Network/API response after upload.
- Server-side import job status.
```
