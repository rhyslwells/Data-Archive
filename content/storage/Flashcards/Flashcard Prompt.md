You are helping me generate spaced repetition flashcards from my Obsidian vault.

For every note in the vault that contains the tag `#<<TAG>>`, do the following:

1. Read the full content of the note.
2. Based on the content, generate **spaced repetition flashcards** in the following format:
   - Use only the **Cloze deletion format** (`{{...}}`).
   - Each note should generate one or more meaningful cloze deletions.

For each note there should be a maximum of six flashcards and a minimum of at least one flashcard.

Guidelines:
- Focus on extracting atomic, useful key knowledge from each note.
- Each cloze card should be written as a **natural-language sentence**, masking only the essential word or phrase.
- Do not invent facts or extrapolate beyond the note's actual content.
- Avoid repetition and avoid prefixing each line with the note title - use a header instead.
- If no good cloze cards can be made, skip the note.

Format the output like this:
### [[Title of Note]]
- Entropy is defined as a {{measure of disorder or randomness}} in a system.
- The second law of thermodynamics states that {{entropy in an isolated system always increases}}.

Please process all notes tagged `#<<TAG>>`.
