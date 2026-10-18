# Knowledge base briefing

This repo is a linked-notes knowledge base (Obsidian-style `[[links]]`, optionally published). Repo-specific settings live in `.claude/knowledge.json`. Read it first and use its keys (`read_only_dirs`, `working_dir`, `hub_tag`, `template`, ...) rather than folder names written in these instructions.

## Read first
- `.claude/Directions.md` holds one section per direction, a thread the user keeps returning to. Read the section for the request's direction before anything else.
- If the direction isn't clear, name the most likely one, say which, and ask.
- Work from "Active now" and its direct links. Search the pool only when the task needs it.
- You may update "Active now" and add to "Log" when the focus shifts, but confirm with the user first.
- You may add a line under "Emerging" when a theme keeps recurring. Creating a section needs approval.
- Never change Focus, In scope, Out of scope or Vocabulary without approval.

## Graph: how notes link and how to move through them

These rules are decided. Change them only with the user.

### Linking
- Every non-hub note links to at least one hub, and may link to several. Hubs are notes whose tags include `hub_tag`.
- Tags are optional on ordinary notes. Hubs must carry `hub_tag`.
- A note should also link to the 2–3 closest existing notes it draws on. More than that needs a reason.
- A note with no outgoing links is a dead end. Give it a hub link or at least one neighbour.
- Hubs link to their children and to related hubs. A hub with fewer than `hub_min_links` outgoing links is thin.
- Only link to notes that exist. Check the file is there first.

### Traversal
1. **Neighbourhood (default).** The current note and its direct links, which include any hubs it links to. Get it with `python .claude/scripts/graph.py near "<note>"`. Use `near "<note>" 2` to reach a hub's children, which is the usual way into a cluster.
2. **Connecting two notes.** `python .claude/scripts/graph.py path "<A>" "<B>"` returns the shortest link path up to `traversal.connect_max_hops` (3). Read only the notes on that path and state the path in your answer.
3. **Cross-cluster seeds.** `python .claude/scripts/graph.py bridges` lists notes linking to two or more hubs. These are where ideas across clusters tend to sit, so they are good starting points for `/explore`.
4. **Bounds.** Never read the whole vault. The script answers graph questions without opening notes, so read only the notes the answer names. If `path` finds nothing within 3 hops, say so and ask before going further. Going past 3 hops needs a stated reason.

Why these limits: they keep the cost bounded, hubs give a two-hop reach into their cluster, and three hops is enough to find a connection across clusters.

### Health
- Run `python .claude/scripts/graph.py audit` before changing a hub or the hub map. It reports untagged hubs, thin hubs, notes without a hub link, dead ends, orphans and broken links.
- Propose fixes from the audit. Don't apply them in bulk unless asked.

## Modes
- `/explore <direction>`: generate ideas inside the direction. May go beyond existing notes. Output is `status: draft`.
- `/test <note>`: stress-test one idea note against its direct links. Critical, not generative. Doesn't rewrite the note.
- `/connect <A> <B>`: find and explain how two notes relate through the graph. Read-only.
- `/audit`: run the health report and summarise it. Read-only.
- `/ground <source>`: build a data-understanding note from a dataset, document or note. Output is a `data` note.
- `/prioritise <direction>`: score the ideas in a direction on impact, feasibility, data availability and novelty. Writes scores to the idea notes only, when asked.
- `/outcome <idea>`: record what happened after an idea was built. Output is a `build` note, and a proposed Log line for `Directions.md`.

## Layers and lifecycle
Each note has one `type` from `types` in `knowledge.json`:
- `context`: what the business does, its processes, KPIs, stakeholders, constraints. Template: `templates/context.md`.
- `data`: a data source, its grain, owner, definitions, known issues and joins. Template: `templates/data-source.md`.
- `idea`: a speculative idea, with hypothesis, assumptions, success measure and scores. Template: `templates/idea.md`.
- `build`: what was built or tested, and what happened. Template: `templates/build.md`.
- Other types (`strategy`, `project`, `reference`, `implementation`) are unchanged.

`status` says how far a note can be trusted. `stage` says where an idea is in the pipeline: `proposed`, `tested`, `approved`, `building`, `live`, `retired`, or `rejected`. Only `idea` and `build` notes carry a `stage`. Moving a stage forward needs the user's say-so.

## Sources
- Every `context` and `data` note lists its origin under `sources`: a person, a document, a dataset or a profiling run, each with a date.
- Claims in an `idea` note that come from business knowledge should link to the `context` or `data` note they rest on, so the chain back to evidence is in the graph.
- Sources may be meeting notes, documents or data extracts. Record the origin, not the content.

## Data handling
- Never paste client or personal data, or credentials, into notes. Summarise rather than copy rows.
- Client-specific notes belong in `unpublished_dirs`. Do not write them into any folder that is published.
- If a request needs confidential material, ask what can be summarised before writing anything down.

## Note status (frontmatter `status`)
- `draft`: rough by design. Restructure freely, but never treat as settled.
- `reviewed`: standalone and trusted. Keep the wording; ask before changing it.
- `reference`: stable background other notes can rely on.
- `archived`: historical. Excluded from traversal and `/explore`.
- No `status` means `draft`.
- Never set `reviewed` or `reference` yourself. Generated content stays `draft` until the user reviews it.
- Values come from `statuses` in `knowledge.json`.

## Frontmatter
- Existing notes: don't add fields unless asked.
- New notes start from `template` and keep its `tags` and `category`. Add the fields in `required_frontmatter_new_notes`. `type` must be one of `types`.
- New `context`, `data`, `idea` and `build` notes start from the matching file in `templates_dir`, not from `template`.

## Writing
- Use only the current note and its direct links as context.
- Leave messy drafts messy unless asked to tidy them.
- Put new notes in `working_dir` unless told otherwise. Don't move notes out of `working_dir` into `read_only_dirs` without asking.
- Don't delete notes.
- Ask before moving or renaming folders, editing the template, or changing Templater or Daily Notes output. Creating a note from the template is fine.
- Canvases and bases: read `.claude/Canvas Preferences.md` first.

## Scripts
- `.claude/scripts/graph.py` is read-only, stdlib-only Python. It reads `knowledge.json`, so it works in any knowledge repo that uses `[[links]]`.
