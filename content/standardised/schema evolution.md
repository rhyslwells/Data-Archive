---
aliases: []
category:
date modified: 27-07-2025
tags: [database]
title: What is Schema Evolution?
---
[[Database Schema|Schema]] Evolution means adding new columns without breaking anything or even enlarging some types. 

You can even rename or reorder columns, although that might break backward compatibilities. Still, we can change one table, and the table format takes care of switching it on all distributed files. Best of all does not require rewrite of your table and underlying files.

### How is schema evolution done in practice

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/SQLite/Writing/Schema_Evolution.ipynb

See also:
- [[ACID Transaction]]


