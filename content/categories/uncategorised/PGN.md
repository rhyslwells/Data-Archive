---
aliases: []
category: 
date modified: 14-11-2025
tags: [analysis, data]
---
A PGN file is a plain-text format used to record chess games. PGN stands for *Portable Game Notation*. It captures both the **metadata** of a game and the **move sequence**, making it a standard for storing, sharing, and analysing chess data.

**Structure**
A PGN file contains two main parts:

1. **Tag Pairs** (metadata)
   Written inside square brackets.
   Examples:

   * `[Event "World Championship"]`
   * `[White "Carlsen"]`
   * `[Black "Nepo"]`
   * `[Result "1-0"]`

2. **Movetext** (game record)
   A sequence of moves in [[algebraic chess notation]].
   Example:
   `1. e4 e5 2. Nf3 Nc6 3. Bb5 a6`

**Key Features**

* Human-readable and easy to parse.
* Supports annotations, comments, and variations.
* Widely used in chess engines, databases, and analytical workflows.

**Example**

```
[Event "Casual Game"]
[White "Player1"]
[Black "Player2"]
[Result "1-0"]

1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 1-0
```