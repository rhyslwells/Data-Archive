---
tags:
  - statistics
---
## Notes:

Corrolation: 
which features are corrolated with the target - if all - keep all.
which features are corrolated with each other: 
    - if two features are highly corrolated, we can drop one of them
    - if two features are highly corrolated with the target, we can keep both

## Description

- Correlation measures the relationship between two variables, indicating how they change together.ranging from -1 to 1. 
- With [[outliers]] able to distort results.
- It doesn't indicate the strength of the relationship or account for other influencing factors. 
- It's a standardized version of [[covariance]].

## Correlation vs Causation

- ==The measure of Correlation, it doesn't imply that changes in one variable cause changes in the other.==== 
- Causation, on the other hand, suggests a direct cause-and-effect relationship between variables.
- Establishing causation requires experimentation to demonstrate that changes in one variable directly lead to changes in another.
- In essence, correlation highlights associations, while causation establishes a direct influence.
## [[Model preparation]] : What features are in [[Correlation]]?

To find the [[Correlation]] between two features we can use:
```python
df[['var1', 'target']].groupby(['var1'], as_index=False).mean().sort_values(by='target', ascending=False)
```

One would want to:
	Correlate numerical features
	Correlate categorical features
## Viewing

Correlations between features can be viewed through [[heatmap]] or [[clustermap]].