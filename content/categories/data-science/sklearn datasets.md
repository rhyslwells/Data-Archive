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
```

Sklearn Datasets are a collection of datasets used 
for testing machine learning algorithms.

with each dataset, we have keys:
- data: np array 
- target
- feature_names
- DESCR
- images
- column names: textual ordered column names
- ect
