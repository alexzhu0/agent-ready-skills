---
name: meeting-to-action-brief
description: Use when turning meeting notes, transcripts, chat summaries, or call fragments into a concise action brief with decisions, owners, deadlines, blockers, evidence, and follow-up prompts.
---

# Meeting To Action Brief

## Purpose

Convert raw meeting material into a practical action brief that people and agents can execute.

Use this skill for standups, project reviews, customer calls, planning meetings, incident reviews, and async chat summaries.

## Inputs

- Meeting notes, transcript fragments, chat messages, or pasted summaries.
- Meeting date, participants, team, project, and audience if known.
- Any known action format or priority scheme.

## Workflow

1. Separate facts from interpretation. Preserve exact names, dates, systems, and commitments.
2. Extract decisions, action items, owners, deadlines, blockers, dependencies, risks, and open questions.
3. Mark missing owners or deadlines as unresolved instead of inventing them.
4. Group actions by owner or workstream when that makes execution easier.
5. Convert vague follow-ups into concrete prompts a human or agent can ask next.
6. Highlight conflicts, ambiguous commitments, and decisions that need confirmation.

## Output

Produce Markdown with these sections:

- Meeting Snapshot
- Decisions
- Action Items
- Blockers And Risks
- Open Questions
- Follow-up Prompts
- Evidence Notes

Use tables for action items and blockers. Keep the brief short enough to paste into a tracker.

## Validation

- Each action has an owner or is explicitly marked `Owner TBD`.
- Each deadline has a concrete date or is marked `Deadline TBD`.
- Decisions are separated from suggestions.
- No private or sensitive content is amplified beyond the provided notes.
- The final brief lets a reader know what changed and what happens next.
