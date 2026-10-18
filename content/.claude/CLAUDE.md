# Vault briefing

Obsidian vault, published as a Quartz site. About 1,175 notes.
- `categories/`: standalone notes, one concept per note. The user's knowledge base. Do not create or edit notes here unless asked.
- `Inbox/Working/`: working notes for exploring Claude's use case. Claude's default output folder.
- `Inbox/` (other): scratch and projects. Not published, gitignored.
- `pages/`: navigation and lists
- `storage/`: unpublished reference notes and `storage/templates/`

## Read first
`.claude/Directions.md` holds one section per direction. A direction is a thread the user keeps coming back to. Each has a broad pool of related notes, and an "Active now" list that is the small subset that matters at the moment.
- Read the section for the direction a command is about before doing anything else.
- If the direction isn't clear from the request or the open note, name the most likely direction, say which one, and ask.
- Work from "Active now" and its direct links. Search the pool only when the task needs it.
- Claude may update "Active now" and add to "Log" when the focus shifts, but confirm the change with the user first.
- Claude may add a line under "Emerging" when a new theme keeps recurring. Creating a new section needs the user's approval.
- Never change Focus, In scope, Out of scope or Vocabulary without the user's approval.

## Modes
- `/explore <direction>`: generate ideas inside the stated direction. May go beyond existing notes, but not beyond the direction. All output is `status: draft`.
- `/test <note>`: stress-test one idea note against its direct links. Critical, not generative. Does not rewrite the note.

## Working in the graph
- Start from the current note and follow its direct links only.
- Pull in a hub (a portal note) only when the task needs it.
- Go no further than two hops without a stated reason.
- Do not search the whole vault unless asked.
- Skip `archived` notes unless asked.

## Note status (frontmatter `status`)
- `draft`: rough by design. Restructure freely, but never treat as settled.
- `reviewed`: standalone and trusted. Keep the wording; ask before changing it.
- `reference`: stable background that other notes can rely on.
- `archived`: historical. Excluded from traversal and `/explore`.
- A note with no `status` is treated as `draft`.
- Never set a note to `reviewed` or `reference` yourself. Generated content is `draft` until the user reviews it.

## Frontmatter
Existing notes use `tags`, `category`, `aliases` and a date field. Do not add new fields to existing notes unless asked. New notes start from `storage/templates/0-note.md`, keep its `tags` and `category`, and add:
`status`, `type` (idea | strategy | project | reference | implementation), `project` (e.g. `flexgo`), `created`, `updated`.

## Canvases and Bases
Conventions are in `.claude/Canvas Preferences.md`. Read it before creating or editing a `.canvas` or `.base` file.

## Writing
- Use only the current note and its direct links as context.
- Leave messy drafts messy unless asked to tidy them.
- Put new notes in `Inbox/Working/` unless told otherwise. Do not move notes from `Inbox/Working/` into `categories/` without asking.
- Do not delete notes.
- Ask before moving or renaming folders, editing a template in `storage/templates/`, or changing Templater and Daily Notes output. Using a template to create a note is fine.
