---
title: What is Schema Evolution?
tags:
  - database
---
[[Database Schema|Schema]] Evolution means adding new columns without breaking anything or even enlarging some types. 

You can even rename or reorder columns, although that might break backward compatibilities. Still, we can change one table, and the table format takes care of switching it on all distributed files. Best of all does not require rewrite of your table and underlying files.

See also:
- [[ACID Transaction]]
- [[How is schema evolution done in practice with SQL]]

