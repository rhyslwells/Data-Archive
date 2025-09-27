---
aliases:
- null
category: DE
date modified: 27-09-2025
tags:
- transformation
---
### Joining Datasets

In [[DE_Tools]] see:
- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/Joining.ipynb

```python
# [[Merge]]
df1 = pd.DataFrame({'key': ['A', 'B'], 'value': [1, 2]})
df2 = pd.DataFrame({'key': ['A', 'B'], 'value': [3, 4]})
merged_df = pd.merge(df1, df2, on='key')

# Concat
concat_df = pd.concat([df1, df2])

# Join
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
joined_df = df1.join(df2, lsuffix='_left', rsuffix='_right')
```

Merging datasets for completeness (also see [[SQL Joins]]). 
