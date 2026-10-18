---
description: Build a data-understanding note from a dataset, document or note
argument-hint: <source path or note name>
---

Source: $ARGUMENTS

1. Read `.claude/knowledge.json`. Identify the source: a file path, or a note name to resolve with `graph.py near`. If it is ambiguous, ask.
2. Profile the source, without copying its content:
   - **Dataset (csv, parquet, xlsx, etc.)**: read the schema and at most the first 20 rows, then compute summary facts with code where that is practical: row count, column types, null rates, distinct counts for key-like columns, date range. Do not quote rows or values from individual records.
   - **Document or meeting note**: read it and extract the definitions, owners, refresh rules, and any stated problems with the data it describes.
   - **Existing note**: read it and its direct links only.
3. Write a `data` note in `working_dir`, from `templates_dir/data-source.md`:
   - frontmatter: `type: data`, `status: draft`, `created` and `updated` (today), `sources` listing the source path or name, the date it was read, and who supplied it if known
   - each template section filled from the profile. Mark anything you could not establish as `unknown`, not as a guess
   - `[[links]]` to a hub and to any `context` note the data serves
4. Do not edit any existing note. If the source contradicts a `data` note already in the vault, name that note and the difference, and leave the reconciliation to the user.
5. Finish with the file path, the facts you established, and a list of what is still unknown.
