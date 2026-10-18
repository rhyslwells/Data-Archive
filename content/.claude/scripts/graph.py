#!/usr/bin/env python3
"""Read-only graph tools for a linked-notes knowledge base (Obsidian-style [[links]]).

Stdlib only. Reads .claude/knowledge.json for repo-specific settings. Writes nothing.

Usage, from the knowledge root:
  python .claude/scripts/graph.py audit            health report: hubs, unlinked notes, dead ends, orphans, broken links
  python .claude/scripts/graph.py path "A" "B"     shortest link path between two notes, up to connect_max_hops
  python .claude/scripts/graph.py near "A" [N]     notes within N hops of A (default: traversal.neighbourhood_hops)
  python .claude/scripts/graph.py bridges          notes that link to two or more different hubs
"""
import difflib
import json
import os
import re
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CFG_PATH = ROOT / ".claude" / "knowledge.json"
LIST_LIMIT = 40

DEFAULTS = {
    "hub_tag": "portal",
    "hub_name_hint": "Portal",
    "hub_min_links": 3,
    "exclude_dirs": [".obsidian", ".git", ".claude", ".trash"],
    "hub_map": ".claude/Vault Map.md",
    "traversal": {"neighbourhood_hops": 1, "connect_max_hops": 3},
}
LINK = re.compile(r"\[\[([^\]|#]+)")
MEDIA = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".mp3", ".mp4", ".canvas", ".base")


def load_config():
    cfg = json.loads(json.dumps(DEFAULTS))
    if CFG_PATH.exists():
        user = json.loads(CFG_PATH.read_text(encoding="utf-8"))
        for k, v in user.items():
            if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                cfg[k].update(v)
            else:
                cfg[k] = v
    return cfg


def frontmatter(text):
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def tags_of(fm):
    tags, lines = [], fm.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r"tags\s*:\s*(.*)$", line)
        if not m:
            continue
        rest = m.group(1).strip()
        if rest.startswith("["):
            tags += [t.strip().strip("'\"") for t in rest.strip("[]").split(",") if t.strip()]
        elif rest:
            tags.append(rest.strip("'\""))
        else:
            for nxt in lines[i + 1:]:
                item = re.match(r"\s*-\s+(.+)$", nxt)
                if not item:
                    break
                tags.append(item.group(1).strip().strip("'\""))
    return [t.lower() for t in tags]


def scan(cfg):
    notes, dupes = {}, []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in cfg["exclude_dirs"]]
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            path = Path(dirpath) / fn
            key = path.stem.lower()
            if key in notes:
                dupes.append(path.stem)
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            links = set()
            for raw in LINK.findall(text):
                target = raw.strip().split("/")[-1].lower()
                if target.endswith(MEDIA):
                    continue
                links.add(target[:-3] if target.endswith(".md") else target)
            links.discard(key)
            fm = frontmatter(text)
            notes[key] = {
                "name": path.stem,
                "tags": tags_of(fm),
                "links": links,
                "type": field_of(fm, "type"),
                "stage": field_of(fm, "stage"),
                "sources": sources_of(fm),
            }
    return notes, dupes


def field_of(fm, key):
    # [ \t]* not \s*: a bare "key:" must not swallow the next line as its value
    m = re.search(rf"^{key}[ \t]*:[ \t]*(.*)$", fm, re.M)
    return m.group(1).strip().strip("'\"").lower() if m else ""


def sources_of(fm):
    """Non-empty sources entries, from an inline list or a YAML block list."""
    m = re.search(r"^sources[ \t]*:[ \t]*(.*)$", fm, re.M)
    if not m:
        return []
    rest = m.group(1).strip()
    if rest.startswith("["):
        return [s for s in rest.strip("[]").split(",") if s.strip()]
    if rest:
        return [rest]
    items = []
    for ln in fm[m.end():].splitlines()[1:]:
        item = re.match(r"\s*-(.*)$", ln)
        if not item:
            break
        if item.group(1).strip():
            items.append(item.group(1).strip())
    return items


class Graph:
    def __init__(self, cfg):
        self.cfg = cfg
        self.notes, self.dupes = scan(cfg)
        self.out = {k: n["links"] & self.notes.keys() for k, n in self.notes.items()}
        self.inc = {k: set() for k in self.notes}
        for k, targets in self.out.items():
            for t in targets:
                self.inc[t].add(k)
        self.broken = {}
        for k, n in self.notes.items():
            for t in n["links"] - self.notes.keys():
                self.broken.setdefault(t, set()).add(k)
        self.hubs = {k for k, n in self.notes.items() if cfg["hub_tag"] in n["tags"]}
        hint = cfg.get("hub_name_hint", "").lower()
        self.untagged_hubs = {
            k for k, n in self.notes.items()
            if hint and hint in k and k not in self.hubs
        }

    def name(self, k):
        return self.notes[k]["name"]

    def adj(self, k):
        return self.out[k] | self.inc[k]

    def resolve(self, arg):
        key = arg.strip().split("/")[-1].lower()
        if key.endswith(".md"):
            key = key[:-3]
        if key in self.notes:
            return key
        close = difflib.get_close_matches(key, self.notes.keys(), n=5, cutoff=0.6)
        names = ", ".join(self.name(c) for c in close) or "none"
        sys.exit(f"No note named '{arg}'. Close matches: {names}")

    def tag(self, k):
        return " [hub]" if k in self.hubs else ""


def show(items, g, total=None):
    total = len(items) if total is None else total
    for k in sorted(items, key=lambda x: g.name(x).lower())[:LIST_LIMIT]:
        print(f"  - {g.name(k)}{g.tag(k)}")
    if total > LIST_LIMIT:
        print(f"  ... and {total - LIST_LIMIT} more")


def cmd_audit(g):
    cfg = g.cfg
    non_hub = set(g.notes) - g.hubs
    unlinked_to_hub = {k for k in non_hub if not (g.adj(k) & g.hubs)}
    dead_ends = {k for k in g.notes if not g.out[k]}
    orphans = {k for k in g.notes if not g.inc[k]}
    total_links = sum(len(v) for v in g.out.values())

    print(f"Notes: {len(g.notes)}   resolved links: {total_links}   broken targets: {len(g.broken)}")
    if g.dupes:
        print(f"Duplicate note names (ignored, resolve ambiguously): {', '.join(g.dupes[:10])}")

    print(f"\nHubs (tag '{cfg['hub_tag']}'): {len(g.hubs)}")
    for k in sorted(g.hubs, key=lambda x: g.name(x).lower()):
        print(f"  {g.name(k)}: out={len(g.out[k])} in={len(g.inc[k])}")
    weak = {k for k in g.hubs if len(g.out[k]) < cfg["hub_min_links"]}
    if weak:
        print(f"\nHubs with fewer than {cfg['hub_min_links']} outgoing links (thin hubs):")
        show(weak, g)

    if g.untagged_hubs:
        print(f"\nNamed like a hub but not tagged '{cfg['hub_tag']}': fix the tag or rename")
        show(g.untagged_hubs, g)

    map_path = ROOT / cfg["hub_map"]
    if map_path.exists():
        listed = {m.strip().split("/")[-1].lower() for m in LINK.findall(map_path.read_text(encoding="utf-8", errors="ignore"))}
        missing = {k for k in g.hubs if k not in listed}
        if missing:
            print(f"\nHubs missing from {cfg['hub_map']}:")
            show(missing, g)

    bad_type = {k for k, n in g.notes.items() if n["type"] and n["type"] not in cfg["types"]}
    if bad_type:
        print(f"\nNotes with a type not in knowledge.json 'types': {len(bad_type)}")
        show(bad_type, g)
    bad_stage = {k for k, n in g.notes.items() if n["stage"] and n["stage"] not in cfg["stages"]}
    if bad_stage:
        print(f"\nNotes with a stage not in knowledge.json 'stages': {len(bad_stage)}")
        show(bad_stage, g)
    no_sources = {k for k, n in g.notes.items()
                  if n["type"] in cfg["sources_required_types"] and not n["sources"]}
    if no_sources:
        print(f"\nContext and data notes with no sources: {len(no_sources)}  (rule: name the source of every claim)")
        show(no_sources, g)

    print(f"\nNotes with no link to any hub: {len(unlinked_to_hub)}  (rule: each note links to at least one hub)")
    show(unlinked_to_hub, g)
    print(f"\nDead ends (no outgoing links): {len(dead_ends)}")
    show(dead_ends, g)
    print(f"\nOrphans (no incoming links): {len(orphans)}")
    show(orphans, g)
    if g.broken:
        print(f"\nBroken link targets: {len(g.broken)}")
        top = sorted(g.broken.items(), key=lambda kv: -len(kv[1]))[:15]
        for target, sources in top:
            print(f"  - [[{target}]] in {len(sources)} note(s)")


def cmd_path(g, a, b):
    start, goal = g.resolve(a), g.resolve(b)
    maxh = g.cfg["traversal"]["connect_max_hops"]
    prev = {start: None}
    q = deque([(start, 0)])
    while q:
        node, depth = q.popleft()
        if node == goal:
            break
        if depth == maxh:
            continue
        for nxt in sorted(g.adj(node)):
            if nxt not in prev:
                prev[nxt] = node
                q.append((nxt, depth + 1))
    if goal not in prev:
        print(f"No path between '{g.name(start)}' and '{g.name(goal)}' within {maxh} hops.")
        return
    chain, node = [], goal
    while node is not None:
        chain.append(node)
        node = prev[node]
    chain.reverse()
    print(f"{len(chain) - 1} hop(s):")
    for i, k in enumerate(chain):
        print(f"  {'-> ' if i else '   '}{g.name(k)}{g.tag(k)}")
    via_hubs = [g.name(k) for k in chain[1:-1] if k in g.hubs]
    print(f"Hubs on path: {', '.join(via_hubs) if via_hubs else 'none'}")


def cmd_near(g, a, hops):
    start = g.resolve(a)
    seen = {start: 0}
    frontier = [start]
    for depth in range(1, hops + 1):
        nxt = []
        for node in frontier:
            for m in sorted(g.adj(node)):
                if m not in seen:
                    seen[m] = depth
                    nxt.append(m)
        frontier = nxt
    print(f"'{g.name(start)}'{g.tag(start)}: {len(seen) - 1} note(s) within {hops} hop(s)")
    for depth in range(1, hops + 1):
        layer = [k for k, d in seen.items() if d == depth]
        print(f"hop {depth} ({len(layer)}):")
        show(layer, g)


def cmd_bridges(g):
    rows = []
    for k in g.notes:
        if k in g.hubs:
            continue
        hubs = sorted(h for h in g.adj(k) if h in g.hubs)
        if len(hubs) >= 2:
            rows.append((k, hubs))
    rows.sort(key=lambda r: (-len(r[1]), g.name(r[0]).lower()))
    print(f"Bridge notes (link to 2+ hubs): {len(rows)}")
    for k, hubs in rows[:LIST_LIMIT]:
        print(f"  - {g.name(k)}: {', '.join(g.name(h) for h in hubs)}")
    if len(rows) > LIST_LIMIT:
        print(f"  ... and {len(rows) - LIST_LIMIT} more")


def main(argv):
    if len(argv) < 2 or argv[1] not in {"audit", "path", "near", "bridges"}:
        print(__doc__)
        return 1
    g = Graph(load_config())
    cmd = argv[1]
    if cmd == "audit":
        cmd_audit(g)
    elif cmd == "path" and len(argv) == 4:
        cmd_path(g, argv[2], argv[3])
    elif cmd == "near" and len(argv) in (3, 4):
        hops = int(argv[3]) if len(argv) == 4 else g.cfg["traversal"]["neighbourhood_hops"]
        cmd_near(g, argv[2], hops)
    elif cmd == "bridges":
        cmd_bridges(g)
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
