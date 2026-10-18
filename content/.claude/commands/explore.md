---
description: Generate speculative ideas within a stated direction
argument-hint: <direction>
---

Direction: $ARGUMENTS

1. Read `.claude/knowledge.json` and `.claude/Directions.md`. `$ARGUMENTS` should name one section of Directions. If it names none, list the sections and stop to ask. If the idea falls under that section's "Out of scope", stop and ask.
2. Find the material to build from:
   - If a note is open, start from it with `python .claude/scripts/graph.py near "<note>"`.
   - Otherwise start from the section's "Active now" notes, and use `python .claude/scripts/graph.py bridges` to find notes that link two or more hubs. Those are the best seeds for cross-cluster ideas.
   - Read only the notes the graph output names. Do not search the whole vault.
3. Propose 5 ideas unless the user asks for a different number. Each must stay within the direction. They may go beyond existing notes. Where an idea rests on a connection between clusters, say which path it comes from, as `graph.py path` reports it.
   Give each idea a different lens, so the five are not variations on one theme. Lenses:
   - **Analogy**: a solution from another industry, applied to this business problem.
   - **Inversion**: the opposite of the business question. What if the cost is the thing to optimise, not the output?
   - **Constraint removal**: assume the obvious data source does not exist. What can be done with what remains?
   - **Surprise**: the question a data scientist would find unexpected, and why the business has not asked it.
   If a lens does not fit the direction, say so and use another.
4. Write each idea as a new note in `working_dir`, using `templates_dir/idea.md`, with:
   - frontmatter: keep the template's `tags` and `category`, and set `status: draft`, `type: idea`, `stage: proposed`, `created` (today), `updated` (today)
   - the hypothesis, assumptions with how each would be falsified, success measure, data needed, and scores filled in
   - a first line stating the idea is speculative
   - `[[links]]` to the existing notes it draws on, including at least one hub, and to the `context` and `data` notes it rests on
5. Do not edit existing notes.
6. Finish with the created files, each with a one-line summary.
