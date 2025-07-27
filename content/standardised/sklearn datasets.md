---
aliases: []
category: 
date modified: 27-07-2025
tags: []
---
[[Scikit-Learn]]

make a dataframe by 

```python
ds = datasets.load_dataset()
df = pd.DataFrame(ds.data,columns=ds.feature_names)
df.head()
#add target column
df['target'] = ds.target
