[[Anki]]:
- Batch make cards: https://www.reddit.com/r/Anki/comments/gslytm/can_we_batch_create_cards_from_csv_or_any_other/

Use Anki web for flashcards
- you can build them from csv: googel sheets
- Build into https://docs.google.com/spreadsheets/d/1kRmfBEuET3cpbat5OiifAhsgrCKrdh1wTTVJEP3rp3U/edit?pli=1&gid=0#gid=0
- import as csv

### Generation:

**Prompt:**  
Convert the provided note into **Anki cloze-deletion flashcards**.

**Rules:**

- Output only the flashcard lines, one per line, in a plain text format.
- Use the syntax `{{c1::...}}` for the first cloze, `{{c2::...}}` for the second, and so on.
- If a card contains multiple clozes, number them sequentially (`c1`, `c2`, `c3`, etc.).
- Do **not** include any headers, notes, or other non-card text.