# Example: deck-to-agent-kb

Use this with `skills/deck-to-agent-kb/SKILL.md`.

## Before

```text
Source: Demo deck notes from an internal agent pilot.

Slide 1: "Agent Knowledge Base Pilot"
- Goal: make internal demo and UAT material answerable by an agent.

Slide 2: Current problem
- Product notes, UAT screenshots, model comparisons, and roadmap comments are mixed together.
- Teams ask the same questions repeatedly.

Slide 3: UAT screenshot notes
- Permission prompt blocked one automation path.
- Mobile screenshots were hard to read.
- User asked for "answer boundaries" so the agent does not overclaim.

Slide 4: Model comparison
- Large model gives better summaries.
- Small model is faster and cheaper.
- Need to preserve uncertainty and page evidence.

Slide 5: Desired output
- Page analysis.
- Keyword index.
- Risk and action index.
- Recommended agent answer boundaries.
```

## After

```markdown
# Agent Knowledge Base

## Source Snapshot

| Field | Value |
| --- | --- |
| Source | Demo deck notes from an internal agent pilot |
| Evidence type | Slide notes, UAT screenshot notes, model comparison notes |
| Verification status | Text notes available; original screenshots not visually inspected |

## Page Analysis

| Page | Key facts | Risks | Open questions |
| --- | --- | --- | --- |
| Slide 1 | Pilot goal is to make demo and UAT material answerable by an agent. | None stated. | Who owns the pilot? |
| Slide 2 | Source material mixes product notes, UAT screenshots, model comparisons, and roadmap comments. | Repeated questions suggest missing retrieval structure. | Which topics are highest volume? |
| Slide 3 | Permission prompt blocked automation; mobile screenshots were hard to read; answer boundaries requested. | Automation may fail without approval handling; visual evidence is not fully verified. | What approval path is acceptable? |
| Slide 4 | Large model improves summaries; small model is faster and cheaper. | Quality/cost tradeoff is unresolved. | What latency and budget limits apply? |
| Slide 5 | Desired output includes page analysis, keyword index, risk/action index, and answer boundaries. | None stated. | What final storage format is required? |

## Key Facts

- The pilot turns mixed internal deck material into an agent-queryable knowledge base.
- The source material combines product notes, UAT screenshots, model comparison notes, and roadmap comments.
- UAT found a permission-prompt blocker and mobile readability issue.
- Model choice has a quality, latency, and cost tradeoff.

## Risk And Action Index

| Risk | Evidence | Action |
| --- | --- | --- |
| Permission prompts block automation | Slide 3 | Define approval handling and fallback path before claiming automation readiness. |
| Visual evidence may be incomplete | Slide 3 notes only | Visually inspect original screenshots before finalizing screenshot-specific claims. |
| Model choice is unresolved | Slide 4 | Record target latency, budget, and quality threshold. |

## Keyword And Entity Index

- Agent Knowledge Base Pilot
- UAT screenshots
- permission prompt
- answer boundaries
- model comparison
- latency
- cost

## Recommended Answer Boundaries

- The agent may summarize facts explicitly present in the slide notes.
- The agent must label screenshot-specific findings as note-derived until screenshots are visually inspected.
- The agent must not claim production readiness, final model choice, or resolved approval handling without additional evidence.
```
