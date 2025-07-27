---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
`pd.Grouper` is a utility in pandas used with `.groupby()` to flexibly group data by a specific column, often useful for time-based grouping, multi-index grouping, or applying custom frequency aggregation.

See:
- [[Groupby]]
- [[Multi-level index]]

### Why Use `pd.Grouper`?
- Allows more readable and declarative code when working with time-indexed data.
- Supports multi-index groupings without restructuring your data.
- Enables resampling-like grouping without setting the index.
### Syntax
```python
pd.Grouper(key=None, level=None, freq=None, axis=0, sort=False)
```
### Parameters
- `key`: The column name to group by.
- `level`: For MultiIndex, the level to group by.
- `freq`: Used to group time-series data (e.g., `'D'` for daily, `'M'` for monthly).
- `axis`: Default is 0 (rows).
- `sort`: Whether to sort the result.




