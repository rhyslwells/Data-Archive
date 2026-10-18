---
description: Explain how two notes relate through the link graph (read-only)
argument-hint: <note A> <note B>
---

Notes: $ARGUMENTS

1. Run `python .claude/scripts/graph.py path "<A>" "<B>"`, using the two names from the arguments. Use the quoted form if a name has spaces.
2. If there is a path, read only the notes on it, plus the hubs it passes through. Explain the connection in a few sentences. Quote the path as the script printed it.
3. If there is no path within `traversal.connect_max_hops`, say so. Do not widen the search. Offer to run `graph.py near` on each note so the user can see how far apart their neighbourhoods are.
4. If either note is a hub with no path, say that too. A hub with no path usually points to a missing link.
5. Do not edit any note. If the connection suggests a missing link, name the two notes and say why, but leave the change to the user.
