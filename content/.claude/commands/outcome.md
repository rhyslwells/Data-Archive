---
description: Record what happened after an idea was built or tested
argument-hint: <idea note name>
---

Idea: $ARGUMENTS

1. Read `.claude/knowledge.json`, then the idea note and its direct links.
2. Ask for the evidence if it is not already given: what was built, the measured result, and the period it covers. Do not invent a result. If the user has no measurement yet, stop and say which measurement is missing.
3. Write a `build` note in `working_dir`, from `templates_dir/build.md`:
   - frontmatter: `type: build`, `status: draft`, `stage` as the user states it (default `building`), `idea: [[idea note]]`, `created` and `updated` (today)
   - the sections filled from the evidence. Compare the result with the idea note's success measure and say whether the hypothesis held, partly held, or failed
   - `[[links]]` to the idea note, the `data` notes used, and a hub
4. Do not edit the idea note or any other existing note.
5. Propose two follow-ups, and apply neither without approval:
   - the `stage` change for the idea note, with the reason
   - one line for the Log in `Directions.md`, dated today, naming the outcome
6. Finish with the new file path and the proposed changes.
