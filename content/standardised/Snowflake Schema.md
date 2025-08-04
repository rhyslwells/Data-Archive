---
aliases: 
category: DE
date modified: 27-07-2025
tags:
  - database
  - orchestration
---
Snowflake Schema
   - Description: A more [[Normalised Schema]] normalized form of a star schema where dimension tables are further broken down into additional tables.
   - Advantages: Reduces data redundancy and can save storage space, but may be more complex to query.
   - A variation of the [[Star Schema]], the snowflake schema normalizes dimension tables into multiple related tables. This can reduce data redundancy and improve data integrity but may complicate queries due to the additional joins required.