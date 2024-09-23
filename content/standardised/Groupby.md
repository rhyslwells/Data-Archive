---
type: grouping
tags:
  - pandas
---

See [[Groupby vs crosstab]] too
# What it is used for:

```python
	df.groubpy("var1").describe()
```


# How to use:

```
# Grouping by 'var1' 
var1_groups = df.groupby(df['var1']]) 
# Accessing the group for 'element' 
element_var1=var1_groups.get_group(element)
```
