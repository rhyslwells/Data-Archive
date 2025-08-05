---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - explainability
---
[[PCA Explained Variance Ratio]]
- The variance explained by each principal component is printed using `pca.explained_variance_ratio_`.
- The sum of the explained variances is calculated and printed, which should ideally equal 1 (indicating that all variance in the data is accounted for by the principal components).

The **explained variance** refers to how much of the total variance in the original dataset is captured or explained by each principal component (PC) in Principal Component Analysis (PCA).

### In the context of PCA:
    
2. **Explained Variance**: After performing PCA, each principal component corresponds to a certain amount of variance in the original data. The **explained variance** of a principal component is the proportion of the total variance in the original dataset that is captured by that component.
    
3. **Explained Variance Ratio**: This is the proportion of the total variance explained by each principal component. It is calculated as:
    
    Explained Variance Ratio of PCi=Variance explained by PCiTotal variance of the dataset\text{Explained Variance Ratio of PC}_i = \frac{\text{Variance explained by PC}_i}{\text{Total variance of the dataset}}
    
    It tells us how much of the total variance in the data is accounted for by each component. For example, if the first principal component explains 70% of the total variance, then the explained variance ratio for that component would be 0.70.
    
4. **Cumulative Explained Variance**: If we sum up the explained variance ratios of the first few principal components, we can assess how many components are needed to explain a significant portion of the total variance. For example, if the first two components explain 90% of the variance, it means that we can reduce the dataset's dimensionality by keeping just those two components without losing much information.
    

### Example:

In PCA applied to the Iris dataset:

```python
pca.explained_variance_ratio_
```

This might return something like:

```
[0.924, 0.053, 0.018, 0.005]
```

This means:

- The first principal component explains 92.4% of the total variance.
- The second principal component explains 5.3% of the variance.
- The third and fourth components explain very little (1.8% and 0.5%, respectively).

Summing these ratios gives the total variance explained by the first few components. In this case, the first two components explain over 97% of the variance in the dataset, meaning the remaining components contribute very little additional information.

### Why it matters:

- **Dimensionality Reduction**: PCA is used to reduce the number of dimensions (features) in the dataset. The goal is to retain as much variance as possible while reducing the number of dimensions. By selecting the components with the highest explained variance, we can reduce the dataset's complexity without sacrificing much information.
    
- **Data [[interpretability]]**: The explained variance helps us understand how important each component is in representing the dataset. If the first few components explain most of the variance, we can focus on them for analysis and modeling.
    