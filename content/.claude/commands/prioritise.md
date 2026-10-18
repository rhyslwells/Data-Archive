---
description: Score and rank the ideas in one direction on impact, feasibility, data availability and novelty
argument-hint: <direction>
---

Direction: $ARGUMENTS

1. Read `.claude/knowledge.json` and the section of `.claude/Directions.md` named by the argument. If it names none, list the sections and stop to ask.
2. Find the idea notes for that direction: those in its "Active now" list, plus any `idea` note linked from them. Use `python .claude/scripts/graph.py near "<note>"` to find them. Read only idea notes, and the `data` and `context` notes they link to.
3. For each idea, read its scores (impact, feasibility, data availability, novelty). If a score is missing, estimate it and say you did so. Use the reasoning in the idea note, not a fresh opinion.
4. Rank the ideas by impact times feasibility, with data availability as a multiplier: an idea with no usable data scores low however good it sounds. Show the ranking as a table with the four scores and one line of reasoning per idea.
5. Do not write any scores to notes unless the user asks. If they do, update only the score lines.
6. For each idea at `proposed`, say whether it is ready for `tested`, and which assumption most needs testing first. Do not change any `stage` yourself.
7. Be clear that scores are judgement, not measurement. Name the one or two scores most worth checking with the user.
