---
tags:
  - pandas
  - "#analysis"
  - code_snippet
---
How do you handle [[Finding missing data]]? The missing data can give you insights into the data collection process.
Is the missing data randomly distributed or is it specific to a given feature.


First find where na and missing are:
```python
df.isnull().sum()
df.isna().sum()
df[df.columns[df.isnull().sum() > 0].tolist()].info()
```

