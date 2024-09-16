---
tags:
---
Type: [[Classification]] [[Unsupervised]]

## Methods

[[K-means]]
[[DBScan]]
[[Hierarchial]]
## [[How to pick the best hyperparameters]]:

[[WCSS and elbow method]]
## [[Interpretation]]

[[Standardisation]] is usefull to bring features to the same scale, as clusters look crappy if you dont [[Standardisation]].
```python
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
```


## Notes

Not to be confused with [[Clustering features]] in [[Feature Preprocessing]].