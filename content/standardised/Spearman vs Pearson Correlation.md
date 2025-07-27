---
aliases: []
category: STATISTICS
date modified: 27-07-2025
tags: [analysis, statistics]
---
Spearman [[correlation]] is a rank-based measure of association, whereas Pearson correlation quantifies the strength of a linear relationship between two continuous variables.
### Key Differences

1. Data Type and Distribution
   * Pearson assumes:
     * Continuous variables
     * Linear relationships
     * Normally distributed variables (or large enough samples for CLT)

   * Spearman can be applied to:
     * Discrete, ordinal, or continuous variables
     * Non-normal [[distributions]]
     * Nonlinear but monotonic relationships

1. Sensitivity to [[storage/utils/file_getter/selected_files/Outliers|Outliers]]
   * Pearson is sensitive to outliers, as it directly uses raw values.
   * Spearman works on ranks, making it more robust to extreme values or skewed distributions.

1. Functional Form of Relationship
   * Pearson measures linear correlation (i.e., whether $y$ changes linearly with $x$).
   * Spearman measures monotonic correlation (i.e., whether $y$ tends to increase or decrease as $x$ increases, regardless of the exact form).
### Summary

> Spearman correlation is better suited for ordinal, skewed, or discrete data, especially when the relationship is monotonic but non-linear, or when outliers are present. Pearson is preferable when the relationship is expected to be linear and homoscedastic between two continuous variables.

### Example: Visualising the Difference

We create a synthetic dataset with:

* A non-linear but monotonic relationship between $x$ and $y$
* Some outliers to test robustness

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

np.random.seed(0)

# Simulate x (discrete low-cardinality variable)
x = np.random.choice([0, 1, 2, 3, 4], size=100, p=[0.2, 0.3, 0.3, 0.15, 0.05])

# Simulate y: nonlinear monotonic trend with noise
y = x2 + np.random.normal(0, 2, size=100)

# Inject outliers
y[::15] += np.random.randint(10, 20, size=7)

# Correlations
pearson_corr, _ = pearsonr(x, y)
spearman_corr, _ = spearmanr(x, y)

# Plot
plt.figure(figsize=(6, 4))
plt.scatter(x, y, alpha=0.7)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Non-linear Relationship with Outliers")
plt.grid(True)
plt.tight_layout()
plt.show()

print(f"Pearson correlation: {pearson_corr:.3f}")
print(f"Spearman correlation: {spearman_corr:.3f}")
```

### Interpretation of Results

Typical output (may vary):

```
Pearson correlation: 0.68
Spearman correlation: 0.83
```

* Pearson is reduced due to:
  * Nonlinearity (e.g., quadratic growth)
  * Outliers inflating variance

* Spearman remains strong:
  * Preserves rank order
  * Diminishes influence of outliers
### Conclusion

This example highlights that Spearman correlation is more robust and flexible in many real-world settings where:

* Variables are discrete, ranked, or not normally distributed
* The relationship is monotonic but not linear
* Outliers may distort direct measurements of association

For rigorous statistical analysis, it’s important to examine data characteristics and the underlying [[Statistical Assumptions]] before selecting a correlation metric.