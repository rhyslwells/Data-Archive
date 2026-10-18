---
name: Roadmap
description: Improvements to the .claude setup for knowledge work, with rationale and open questions. Items 1-9 are implemented; open questions remain.
status: draft
type: strategy
created: 2026-10-18
updated: 2026-10-18
tags: [claude]
---

# Roadmap

Proposed changes to the `.claude` setup, in priority order.

## Implementation status
- 1 Layers: done. `types` now includes `context`, `data`, `idea`, `build`. Templates are in `templates/`.
- 2 Lifecycle: done. `stage` values are in `knowledge.json`, and the audit checks them.
- 3 Provenance: done. `sources` is required on `context` and `data` notes, and the audit reports gaps.
- 4 Data understanding: done. `templates/data-source.md`, `/ground`, and a data check in `/test`.
- 5 Testable ideas: done. `templates/idea.md`, and `/test` and `/prioritise` work through the assumptions.
- 6 Outcomes: done. `templates/build.md` and `/outcome`. Log lines are proposed, not written.
- 7 Data handling: done. Rules in `CLAUDE.md`.
- 8 Lenses: done. Four lenses in `/explore`.
- 9 Commands: done. `/ground`, `/prioritise`, `/outcome`.
- Memory: the user profile is saved to memory.

Decisions made while implementing, to confirm:
- `sources` accepts any origin (meeting, document or extract). The open question below was not answered, so `/ground` handles all three.
- The existing note types `process`, `term`, `grouping` and `language` were added to `types`, because the vault already uses them.
- Existing notes were not given the new fields. They apply to new notes only.
- `/prioritise` ranks by impact times feasibility, with data availability as a multiplier. That weighting is a judgement, and can be changed in the command file.

Items below are the original proposals, kept for the reasoning.

## 1. Separate the layers of knowledge
Every note is currently either a concept or an idea. Make four layers explicit with `type` in frontmatter:
- **Context**: what the business does, its processes, KPIs, stakeholders and constraints. Source: interviews, documents, meetings.
- **Data**: what data exists, what it means and how reliable it is.
- **Ideas**: speculative, `status: draft`.
- **Build**: what was tested, decided, implemented, and what happened.

`/explore` draws from Context and Data and writes to Ideas. A hub per business or client gives a clean entry point.

**Why:** the graph currently mixes what is known with what is speculative, so it is hard to tell which links are evidence and which are guesses.

## 2. Add a lifecycle, separate from trust
`status` records how far a note can be trusted, not where an idea is in the pipeline. Add a `stage` field: `proposed → tested → approved → building → live → retired`, with `rejected` as a side exit. `status` stays as it is.

**Why:** an idea can be `draft` and still be live, or `reviewed` and abandoned.

## 3. Require provenance
Every business-derived claim names its source: stakeholder, document, dataset and date. Add a `sources` field to Context and Data notes.

**Why:** without provenance you cannot trace an idea back to its evidence, and business context goes stale quickly.

## 4. Data understanding as first-class notes
One note per data source: grain, owner, refresh frequency, date range, known issues, definitions and join keys. Add a data-feasibility check to `/test`.

**Why:** most idea feasibility depends on these facts, and they are easy to get wrong.

## 5. Make ideas testable
Each idea has a hypothesis, assumptions (each with how it would be falsified), a success measure, the data needed, and rough impact and effort scores. `/test` attacks the assumptions one at a time. `/explore` ranks candidates rather than only listing them.

**Why:** a plain list of ideas cannot be prioritised or disproved.

## 6. Close the loop after implementation
Record outcomes: what was built, what was measured, and whether the result matched the hypothesis. Outcomes flow back into the Log in `Directions.md` and into the links.

**Why:** a tested idea that failed is still a finding, and outcomes show which clusters produce results.

## 7. Data-handling rules
- Never paste client data, personal data or credentials into notes.
- Keep client-specific notes in `unpublished_dirs`, not anything Quartz publishes.
- Summarise sensitive data rather than copying rows.

**Why:** business knowledge is often confidential, and these notes may be published.

## 8. Divergent-thinking lenses in `/explore`
Rotate through fixed lenses: an analogy from another industry, the inverse of the business question, a constraint that removes the obvious data source, and the question a data scientist would find surprising.

**Why:** these push past obvious ideas, which matters more for innovation work than plain brainstorming.

## 9. Further commands
- `/ground <dataset or note>`: builds a data-understanding note from a source.
- `/prioritise <direction>`: scores ideas on impact, feasibility and data availability.
- `/outcome <idea>`: records what happened after an idea was built.

## Also worth doing
- Save the user's role and focus (data scientist, business-derived ideas, innovation, data understanding) to memory, so sessions start with the same context.

## Open questions
- Where does business knowledge arrive from: meeting notes, documents, or data extracts? This decides what `sources` points to and what `/ground` reads.

## Suggested order
Items 1, 2 and 7 first, since they affect everything else. Items 3–6 depend on the answer to the open question. Item 9 comes last.
