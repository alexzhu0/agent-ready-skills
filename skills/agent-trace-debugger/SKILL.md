---
name: agent-trace-debugger
description: Use when summarizing AI-agent traces, JSONL logs, tool-call transcripts, retries, or execution histories into a failure timeline, root-cause candidates, and retry recommendations.
---

# Agent Trace Debugger

## Purpose

Make noisy agent traces readable enough to debug quickly.

Use this skill for JSONL traces, tool logs, run transcripts, orchestration logs, and retry histories.

## Inputs

- Trace file, JSONL events, pasted logs, or tool-call transcript.
- Expected task outcome if known.
- Error messages, timestamps, run IDs, and environment notes.

## Workflow

1. Build a chronological timeline of user input, agent decisions, tool calls, tool results, errors, and retries.
2. Mark the first observed failure separately from later cascading failures.
3. Classify failures: missing input, tool error, auth, network, parsing, policy, timeout, bad plan, or bad assumption.
4. Identify evidence for each root-cause candidate.
5. Recommend the smallest retry or fix that would prove or disprove the top candidate.
6. Preserve raw error strings exactly when they are useful for search.

## Output

Produce Markdown with these sections:

- Run Snapshot
- Failure Timeline
- First Failure
- Root-cause Candidates
- Retry Or Fix Plan
- Evidence To Preserve

Keep the timeline concise and omit routine success events unless they explain the failure.

## Validation

- The first failure is not confused with a later symptom.
- Every root-cause candidate has trace evidence.
- Retry steps are ordered from lowest-risk to highest-risk.
- Unknowns remain explicit.
- Raw error strings are not paraphrased away.
