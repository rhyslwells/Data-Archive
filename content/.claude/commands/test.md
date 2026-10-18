---
description: Stress-test one idea note against its direct neighbourhood
argument-hint: <note name>
---

Note: $ARGUMENTS

1. Read `.claude/Directions.md` and find the section the note belongs to, for context. If the note fits no section, say so. Then read the note itself.
2. Check the note against its direct links only:
   - conflicts with existing notes
   - dependencies it assumes but does not state
   - evidence that supports it
   - evidence that undercuts it
   Cite each point as `[[note]]`.
3. Be critical, not generative. Do not rewrite the idea and do not add new ideas.
4. If the note's status is `reviewed` or `reference`, critique only. Do not suggest wording changes.
5. Report in chat only. Do not edit the note. Offer to append a "## Stress test" section if the user asks.
6. End with what would need to be true for the idea to hold, and any links you did not check because they were beyond two hops.
