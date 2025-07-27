---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
## Clustermap

Related to:
[[Preprocessing|Preprocess]]

- Purpose: Identify which features are most similar using [[Dendrograms]].
- Visualization: Regions of color show clustering, similar to a heatmap.
- Functionality: Performs clustering on both rows and columns.

Requirements: Input should be numerical; data needs to be scaled.
  ```python
  import seaborn as sns
  sns.clustermap(x_scaled, cmap='mako', standard_scale=0)  # 0 for rows, 1 for columns
  ```
## Resources
- [Video Explanation](https://youtu.be/crQkHHhY7aY?t=149)
- [Seaborn Clustermap Documentation](https://seaborn.pydata.org/generated/seaborn.clustermap.html)