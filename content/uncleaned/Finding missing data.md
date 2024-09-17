---
tags:
  - pandas
  - learning
  - "#data"
  - "#analysis"
---


First find where na and missing are:
```python
df.isnull().sum()
df.isna().sum()
df[df.columns[df.isnull().sum() > 0].tolist()].info()
```

