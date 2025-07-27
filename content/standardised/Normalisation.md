---
aliases: []
category: 
date modified: 27-07-2025
tags: [portal]
---
Standardizing data distributions for consistency. 

In ML:
- [[Z-Normalisation]]
- [[Standardisation]]
- [[Normalisation vs Standardisation]]
- [[Batch Normalisation]]

In [[Data Engineering]]:
- [[Normalisation of data]]
- [[Normalised Schema]]
- [[How to normalise a merged table]]

In [[NLP]]:
- [[Normalisation of Text]]


```python
# --- 15. GroupBy with Transformation (Using transform to align with original dataframe)
df['Value_transformed'] = df.groupby('Category')['Value'].transform(lambda x: x - x.mean())
# get the mean value for each category
print(df.groupby('Category')['Value'].mean())
print("\nTransformed Values with mean subtracted (transform()):")
print(df.sort_values('Category'))
```

