---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - transformation
  - python
---
Pivot Table: Summarize Data
```python
df = pd.DataFrame({'A': ['foo', 'foo', 'bar'], 'B': ['one', 'two', 'one'], 'C': [1, 2, 3]})
pivot_table = df.pivot_table(values='C', index='A', columns='B', aggfunc='sum')
```

Relevant links:
- https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/pivot_table.ipynb