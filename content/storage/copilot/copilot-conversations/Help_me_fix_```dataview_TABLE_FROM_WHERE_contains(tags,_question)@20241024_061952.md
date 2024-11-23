---
epoch: 1729747192427
modelKey: gpt-4o|openai
tags:
  - copilot/copilot-conversation
---

**user**: Help me fix:

```dataview
TABLE
FROM ""
WHERE contains(tags, "question") & (category,"CAREER")
```
[Timestamp: 2024/10/24 06:19:52]

**ai**: It looks like you're trying to create a Dataview query to display notes that have a specific tag and belong to a certain category. However, there are a couple of issues with your query syntax. Here's a corrected version:

```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "CAREER"
```

### Key Changes:
1. **Logical Operator**: Use `AND` instead of `&` for logical conjunctions in Dataview.
2. **Category Condition**: Use `=` to compare the `category` field with the string "CAREER".

This query will create a table of notes that contain the tag "question" and have the category "CAREER". Make sure that your notes have the `tags` and `category` fields properly defined for this query to work.
[Timestamp: 2024/10/24 06:19:55]