---
description: Generate speculative ideas within a stated direction
argument-hint: <direction>
---

Direction: $ARGUMENTS

1. Read `.claude/Directions.md`. `$ARGUMENTS` should name one of its sections. If it names none, list the sections and stop to ask. If the idea falls under that section's "Out of scope", stop and ask.
2. If a note is open, start from it and follow its direct links. Pull in a hub only if the task needs it. Do not search the whole vault.
3. Propose 5 ideas unless the user asks for a different number. Each must stay within the direction. They may go beyond the existing notes.
4. Write each idea as a new note in `Inbox/Working/`, starting from `storage/templates/0-note.md`, with:
   - frontmatter: keep the template's `tags` and `category`, and add `status: draft`, `type: idea`, `created` (today), `updated` (today)
   - a first line stating the idea is speculative
   - `[[links]]` to the existing notes it draws on
5. Do not edit existing notes.
6. Finish with a list of the created files, each with a one-line summary.
