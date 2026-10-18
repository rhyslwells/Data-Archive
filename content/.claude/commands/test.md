---
description: Stress-test one idea note against its direct neighbourhood
argument-hint: <note name>
---

Note: $ARGUMENTS

1. Read `.claude/Directions.md` and find the section the note belongs to, for context. If it fits no section, say so. Then read the note itself.
2. Get its neighbourhood with `python .claude/scripts/graph.py near "<note>"` (one hop). Read the direct links. Read a hub only if it is needed to judge a point.
3. Check the note against those direct links only:
   - conflicts with existing notes
   - dependencies it assumes but does not state
   - evidence that supports it
   - evidence that undercuts it
   - **Assumptions**: take each row of its Assumptions table and say whether the linked notes support it, contradict it, or are silent. Name the check that would settle it.
   - **Data feasibility**: check the `data` notes it links to. Is the grain right, are the key fields defined, are the known issues a blocker? If the data it needs has no `data` note, say so. That is a finding.
   - **Business fit**: check the `context` notes it links to. Does the idea respect the constraints and measures written there? If it has no `sources`, say so.
   Cite each point as `[[note]]`.
4. Be critical, not generative. Do not rewrite the idea and do not add new ideas.
5. If the note's status is `reviewed` or `reference`, critique only. Do not suggest wording changes.
6. Report in chat only. Do not edit the note. Offer to append a "## Stress test" section if the user asks.
7. End with what would need to be true for the idea to hold, and any links you did not check because they were beyond one hop.
