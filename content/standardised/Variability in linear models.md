---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
Variability in linear models

Mathematically, SSE is a [[Loss function]] given by:

$$SSE = \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

where $N$ is the number of observations, $y_i$ is the actual value of the dependent variable for observation $i$, and $\hat{y}_i$ is the predicted value based on the linear regression model.

The formula for the Regression Sum of Squares (SSR) in the context of linear regression is:

$$SSR = \sum_{i=1}^{N} (\hat{y}_i - \bar{y})^2 $$

Where:
- $\hat{y}_i$ is the predicted value of the dependent variable for observation $i$ based on the linear regression model.
- $\bar{y}$ is the mean of the observed values of the dependent variable.
- $N$ is the total number of observations.

SSR measures the amount of variability in the dependent variable that is explained by the independent variables in the model. It ==reflects how well the regression model captures the relationship between the independent and dependent variables.==

Total Sum of Squares (SST) represents the total variability in the dependent variable $y$. The relationship between SST, SSR, and SSE is given by:

 $SST = SSR + SSE$ 

This equation reflects the decomposition of total variability into explained variability (SSR) and unexplained variability (SSE) due to errors.