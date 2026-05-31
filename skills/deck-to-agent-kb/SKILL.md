---
name: deck-to-agent-kb
description: Use when converting slide decks, PPT notes, exported screenshots, or mixed enterprise presentation material into an agent-queryable knowledge base with evidence, risks, actions, and answer boundaries.
---

# Deck To Agent KB

## Purpose

Turn a messy deck into a knowledge base that another agent can search, cite, and use safely.

Use this skill when the source is a slide deck, slide screenshots, speaker notes, or a pasted page-by-page summary.

## Inputs

- Deck file, slide screenshots, extracted text, speaker notes, or page-by-page notes.
- Any known audience, product, project, date, and source path.
- The user's target format if provided.

## Workflow

1. Inventory available evidence: deck file, screenshots, text extraction, notes, filenames, dates, and missing pages.
2. Build a page-by-page analysis. For every page, capture title, observed facts, visual evidence, decisions, risks, and open questions.
3. Do not trust text extraction alone when screenshots or diagrams carry meaning. If visuals are unavailable, mark visual facts as unverified.
4. Merge repeated facts into a compact knowledge base organized by topic, product, system, workflow, and stakeholder.
5. Create a keyword and entity index for names, systems, dates, metrics, tools, risks, and decisions.
6. Create a risk and action index with evidence, owner if known, priority, and next step.
7. Define answer boundaries so downstream agents know what they may claim, what they must hedge, and what requires human confirmation.

## Output

Produce Markdown with these sections:

- Source Snapshot
- Page Analysis
- Agent Knowledge Base
- Keyword And Entity Index
- Risk And Action Index
- Recommended Answer Boundaries
- Unverified Or Missing Evidence

Keep claims tied to slide/page evidence. Prefer concise tables for risks, actions, and entities.

## Validation

- Every important claim points to a page, screenshot, note, or explicit user-provided source.
- Screenshot-heavy pages are marked as visually inspected or not visually available.
- The risk/action index contains only evidence-backed items.
- Answer boundaries are specific enough to prevent overclaiming.
- The final Markdown can stand alone without the original deck.
