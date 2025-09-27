---
aliases: []
category: DS
date modified: 27-09-2025
tags:
- exploration
---
[[Scikit-Learn]]
[[Datasets]]

make a dataframe by 

```python
ds = datasets.load_dataset()
df = pd.DataFrame(ds.data,columns=ds.feature_names)
df.head()
#add target column
df['target'] = ds.target
