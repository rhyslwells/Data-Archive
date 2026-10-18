# Canvas Preferences

How the user likes Obsidian canvases built. Read before creating or editing any `.canvas` file.

## Location
- Canvases go in `outputs.canvases` from `.claude/knowledge.json`.
- Bases go in `outputs.bases` from `.claude/knowledge.json`.

## Nodes
- Use text nodes containing only a `[[link]]`, not file nodes. File nodes show the note body, which is too much.
- Keep each canvas under 20 nodes. Group frames and the centre node count.
- Only link to notes that exist. Check each link against the knowledge folders before writing.
- Spread nodes out so nothing overlaps. Leave clear gaps between branches.

## Themes
- One theme per canvas. Be creative about what the canvas focuses on.
- Several canvases are welcome if they each have a clear theme.

## Layouts
- Topic maps: centre on a root note (a hub-map or index note), with hub notes (tagged `hub_tag`) as branches and a few notes under each branch.
- Flow canvases: use labelled groups as stages, laid out left to right, with arrows between stages.

## Example files
- `Inbox/Working/canvases/Example - Topic Map.canvas`: the centred topic map.
- `Inbox/Working/canvases/Example - Model Evaluation Flow.canvas`: the staged flow.
