---
aliases: []
category:
date modified: 27-07-2025
tags: [statistics]
---
Use in understanding relationships between variables in data analysis. 

While it helps identify associations, it's important to remember that ==correlation does not imply causation.== 

Visualization tools like heatmaps and clustering can aid in identifying and interpreting these relationships effectively.

- What is Correlation?: A measure of the strength and direction of the relationship between two variables.
### Description

- Correlation measures the relationship between two variables, indicating how they change together. It ranges from -1 to 1:

  - -1: Perfect negative correlation
  - 0: No correlation
  - 1: Perfect positive correlation

### Key Points

- [[Correlation vs Causation]]: Correlation does not imply causation. While correlation highlights associations, causation establishes a direct influence.
- Significance: Correlation values < -0.5 or > +0.5 are considered significant.
- Impact of Outliers: [[standardised/Outliers]] can distort correlation results.
- Standardization: Correlation is a standardized version of [[Covariance]].

### Model Preparation

[[Feature Selection]]:
  - Identify features correlated with the target. If all are correlated, keep all.
  - For features correlated with each other, consider dropping one to avoid redundancy.
  - If two features are highly correlated with the target, both can be retained.

If two variables are strongly positively correlated, it often makes sense to drop one of them to simplify the model. This is because ==highly correlated variables can introduce redundancy==, leading to [[multicollinearity]] in regression models.

By removing one of the correlated variables, you can:

1. Reduce Complexity: Simplifying the model by reducing the number of predictors can make it easier to interpret and manage.
2. Improve Stability: Reducing multicollinearity can lead to more stable and reliable coefficient estimates.
3. Enhance Performance: In some cases, removing redundant features can improve the model's predictive performance by reducing overfitting.

However, it's important to ensure that the variable you choose to keep is the one that is more relevant or has a stronger theoretical justification for inclusion in the model. 

### Viewing Correlations

- Use [[Heatmap]] or [[Clustering]] to visualize correlations between features.

### Example Code

To find the correlation between two features:

```python
df[['var1', 'target']].groupby(['var1'], as_index=False).mean().sort_values(by='target', ascending=False)
```
