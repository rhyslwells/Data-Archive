---
type: term
tags:
  - preprocessing
  - "#statistics"
---
# When to use:

To check for [[Outliers]]. Need to remove then in order to do [[Data Cleansing]].

# Code


```
## Get boxplots for all features

#Price also varies depending on neighborhood.
plt.figure(figsize = (12, 6))
sb.boxplot(x='var1', y='var2', data=df, palette='hls')
sns.boxplot(x='Neighborhood', y='SalePrice',  data=data)
xt = plt.xticks(rotation=30)
```
