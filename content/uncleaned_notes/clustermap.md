
## Description

Can tell which ==features are the most similar== with [[Dendrograms]]

Regions of colour show [[Clustering classification]], similar to [[heatmap]]

Clustermaps performs [[Hierarchial]] clustering on both rows and columns.

![[Pasted image 20240119170302 1.png|300]]

## Resources

[Explanation](https://youtu.be/crQkHHhY7aY?t=149)

https://seaborn.pydata.org/generated/seaborn.clustermap.html
## Implementation

Input should be numerical.
Need to scale data
`sns.clustermap(df,standard_scale=0)` for rows 1 for cols
```
import seaborn as sns
sns.clustermap(x_scaled, cmap='mako')
```

