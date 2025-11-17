---
aliases: []
category:
date modified: 15-11-2025
tags: [analysis, learning]
---
Algebraic notation is compact, but it follows strict rules that make it possible to know **which piece moved**, even when it doesn’t explicitly say so. Below is a clear explanation in simple steps.
## 1. Pawns have no letter

A move like
**1. d4**
means: *the pawn on the d-file moves to square d4*.
If a pawn were to capture, it would show the file it came from, for example:
**exd5** = pawn from the e-file captures something on d5.

Because pawns are the only pieces with **no letter**, the meaning is unambiguous.
## 2. Pieces use letters

K = King
Q = Queen
R = Rook
B = Bishop
N = Knight

So
**Nc3**
means: a knight moves to $c3$.
## 3. If two pieces can move to the same square, notation adds a qualifier

Example: if two knights could both move to $d2$, it might show:

* **Nbd2** (knight from the b-file goes to d2)
* **N1d2** (knight from rank 1 goes to d2)

This disambiguation is rarely needed in the opening (because piece positions are still simple), which makes the early moves readable.
## 4. Geometry determines what pieces can reach the square

You infer “which knight moved” by knowing piece movement rules and the board layout.

Example move:
**Nc3**

In the starting position:

* Knight on $g1$ cannot reach $c3$
* Knight on $b1$ *can* reach $c3$
  Therefore the knight on $b1$ moved.

The notation does not state the starting square because only one option exists.
## 5. Captures use “x”

Example:
**Bxf7+**
means: bishop captures something on $f7$ and gives check.
## 6. Checks and checkmates

`# means checkmate

Example:
**Qh5#** — queen on h5 delivers mate.

## 7. Game endings

1-0 = White wins
0-1 = Black wins
1/2-1/2 = Draw

## Example

1. d4 d5 2. c4 e6 3. Nc3 Nf6 4. Bg5 Be7 1-0

**1. d4 d5**
White plays $d4$, taking space in the centre.
Black responds with $d5$, contesting the centre symmetrically.

**2. c4 e6**
White plays $c4$, entering the *Queen’s Gambit* structure by attacking Black’s $d5$ pawn.
Black replies with $e6$, supporting the $d5$ pawn and preparing to develop the dark-squared bishop (a standard Queen’s Gambit Declined setup).

**3. Nc3 Nf6**
White develops the knight to $c3$, increasing pressure on $d5$ and preparing kingside development.
Black develops the knight to $f6$, targeting the $d5$ and $e4$ squares.

**4. Bg5 Be7**
White plays $Bg5$, pinning the knight on $f6$ to the queen.
Black responds with $Be7$ to break the pin and prepare to castle.

**1-0**
The result indicates **White won the game**.
The notation does **not** show *how* the win occurred; this is simply the final recorded result.

If you'd like, I can annotate this in the style of an Obsidian note with arrows or highlight key strategic themes (e.g., centre control, development, pins).
