---
tags:
  - pandas
  - "#analysis"
  - code_snippet
  - drafting
title: 
importance: 
engagement: 
recency_of_interest:
---
How do you handle [[Handling Missing Data]]? The missing data can give you insights into the data collection process.
Is the missing data randomly distributed or is it specific to a given feature.


First find where na and missing are:
```python
df.isnull().sum()
df.isna().sum()
df[df.columns[df.isnull().sum() > 0].tolist()].info()
```


The missing data can give you insights into the data collection process.
Is the missing data randomly distributed or is it specific to a given feature


[[Handling Missing Data]]


How to treat missing values?;; Remove then or replace them.