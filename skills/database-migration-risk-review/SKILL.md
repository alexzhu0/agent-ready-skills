---
name: database-migration-risk-review
description: Use when reviewing schema migrations, SQL changes, data backfills, index changes, or rollout plans for data loss risk, locking, rollback gaps, validation checks, and production safety.
---

# Database Migration Risk Review

## Purpose

Find practical risks in database migrations before they reach production.

## Inputs

- Migration files, SQL snippets, schema diff, backfill plan, or rollout notes.
- Database type, table size, traffic patterns, and deployment process if available.
- Rollback expectations and validation commands.

## Workflow

1. Classify the migration type: schema, data, index, backfill, constraint, or cleanup.
2. Identify locking, data loss, long-running query, and compatibility risks.
3. Check forward and backward compatibility with application code.
4. Recommend validation queries and rollout sequencing.
5. State rollback limits honestly.

## Output

Produce Markdown with:

- Migration Snapshot
- Risk Map
- Compatibility Review
- Validation Checks
- Rollout Plan
- Rollback Notes
- Open Questions

## Validation

- Data loss risks are explicit.
- Locking and runtime impact are considered.
- Rollback is not promised when impossible.
- Validation checks are concrete.
- Unknown table size or traffic is flagged as a risk.
