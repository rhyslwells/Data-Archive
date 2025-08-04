---
aliases: 
category: CS
date modified: 27-07-2025
tags:
  - system
---
> Concurrency is about *dealing with many things at once*, not necessarily *doing* them at the same time.

Concurrency refers to the ability of a system to handle multiple tasks at once, either by:
* Overlapping their execution (e.g. while one task waits for I/O, another runs), or
* Structuring code to allow interleaved progress of multiple operations.

It does not necessarily mean tasks run simultaneously (that’s parallelism), but that their progress is interleaved.

Analogy:
- Concurrent: Making dinner, and doing the dishes at the same time (yourself).
- Parallel: Making dinner (you), doing the dishes (partner).

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/SQLite/Transactions/Concurrency.ipynb