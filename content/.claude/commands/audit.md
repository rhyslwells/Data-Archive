---
description: Run the graph health report and summarise what needs attention (read-only)
---

1. Run `python .claude/scripts/graph.py audit`.
2. Summarise the report in this order, with counts:
   - hub problems: untagged hubs, thin hubs, hubs missing from `hub_map`
   - layers: notes with a `type` or `stage` outside the knowledge.json lists, and `context` or `data` notes with no `sources`
   - linking: notes with no hub link (the largest number is usually the most useful finding)
   - dead ends and orphans
   - broken links, starting with the targets that appear in the most notes
3. For each problem, propose one concrete fix. Name the note and the link to add, tag or remove. Do not apply any fix.
4. Note which findings are likely intentional, such as archived or unpublished notes, and leave those out of the proposed fixes.
5. Finish by asking which fixes to apply.
