---
tags: 
  - statistics
  - data_analysis
aliases:
category: STATISTICS
phase: Model Selection
topic: Covariance Calculation
filename:
---

In statistics, covariance is a measure of the degree to which two random variables change together. It indicates the direction of the linear relationship between the variables. Specifically, covariance can be defined as follows:

- **Positive Covariance**: If the covariance is positive, it means that as one variable increases, the other variable tends to also increase. Conversely, if one variable decreases, the other variable tends to decrease as well.
  
- **Negative Covariance**: If the covariance is negative, it indicates that as one variable increases, the other variable tends to decrease, and vice versa.

- **Zero Covariance**: A covariance close to zero suggests that there is no linear relationship between the two variables.

The formula for calculating the covariance between two random variables $X$ and $Y$ is given by:

$$
\text{Cov}(X, Y) = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \bar{X})(Y_i - \bar{Y})
$$

where:
- $X_i$ and $Y_i$ are the individual sample points,
- $\bar{X}$ and $\bar{Y}$ are the means of $X$ and $Y$ respectively,
- $n$ is the number of data points.

Covariance is used in:
- in the calculation of [[correlation]] coefficients 
- and in multivariate statistics, such as in [[Gaussian Mixture Models]] where it helps describe the shape and orientation of the data distribution.