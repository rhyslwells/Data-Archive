---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - statistics
---
[[Covariance]] provides a basic measure of how two variables move together, correlation offers a more [[interpretability]] and standardized way to understand their relationship.

Definition:
   - Covariance measures the degree to which two variables change together. It can take any value, which makes it difficult to interpret the strength of the relationship.
   - Correlation, on the other hand, is a standardized measure of the relationship between two variables, ranging from -1 to 1. This standardization allows for easier interpretation of the strength and direction of the relationship.

Formula:
   - Correlation is derived from covariance. The formula for the correlation coefficient $r$between two variables $X$ and $Y$ is:
   $$
   r = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
   $$
   where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$, respectively. This formula shows that correlation is essentially the covariance normalized by the product of the standard deviations of the two variables.

Interpretation:
   - While covariance can indicate the direction of the relationship (positive or negative), it does not provide information about the strength of that relationship. 
   - Correlation, being bounded between -1 and 1, allows for a clearer understanding of how strongly the two variables are related.
