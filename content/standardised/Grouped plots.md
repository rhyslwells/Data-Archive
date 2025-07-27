---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Related:
- [[Data Visualisation]]
- pairplots

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tips = sns.load_dataset("tips")

# Facet Grid Example
g = sns.FacetGrid(tips, col="sex", row="time")
g.map_dataframe(sns.histplot, x="total_bill", bins=20)

plt.show()
```

![[Pasted image 20250402212849.png]]