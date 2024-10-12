---
model: 
tags:
  - ml
  - learning
---
## Description

assume that the relationship between the independent variable(s) and the dependent variable is linear.

During the training phase, the algorithm adjusts the slope (m) and the intercept (b) of the line to minimize the [[loss function]].

**Evaluation**: Finally, you evaluate the performance of your model by comparing its predictions to the actual values in a separate test dataset. Common metrics for evaluating regression models include Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and [[R squared]].

The linear regression model is represented as:

$y = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n$

- \( y \) is the dependent variable (the variable we want to predict).
- \( x_1, x_2, \ldots, x_n \) are the independent variables (features or predictors).
- \( b_0, b_1, b_2, \ldots, b_n \) are the coefficients (weights) associated with each independent variable.
- \( b_0 \) is the intercept term.

Objective: Minimizing [[mean square error]] (SSE) the [[loss function]]

The goal of linear regression is to find the values of coefficients \($b_0, b_1, b_2, \ldots, b_n$ \) that minimize the sum of squared errors ([[mean square error]]), also known as the residual sum of squares (RSS) or [[mean square error]] (MSE). Mathematically, SSE is given by:

$SSE = \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$ 

where \( N \) is the number of observations, \( y_i \) is the actual value of the dependent variable for observation \( i \), and \( $\hat{y}_i$\) is the predicted value based on the linear regression model.
# Summary table: [[Model Evaluation]]

[[R squared]]

[[Adjusted R squared]] takes into account the number of variables.

[[F-statistic]] overall significance of model (lower worse).

[[Feature Selection]] Use P>|t| column to decide whether to keep variable less that 0.05

[[p-values in linear regression in sklearn]]

![[Pasted image 20240117145455 1.png|300]] ![[Pasted image 20240124135607.png|300]]

### Method: Ordinary Least Squares (OLS):

The Ordinary Least Squares method is used to minimize SSE. It achieves this by finding the values of \( $b_0, b_1, b_2, \ldots, b_n$ \) that minimize the sum of squared differences [[mean square error]] between the observed and predicted values. The formulas for \( $b_0, b_1, b_2, \ldots, b_n$ \) are derived by setting partial derivatives of SSE with respect to each coefficient to zero.

 OLS is not [[Gradient Descent]] as OLS is analytical and [[Gradient Descent|GD]] is iterative.

### Total Sum of Squares (SST), Regression Sum of Squares (SSR):

- Total Sum of Squares (SST) represents the total variability in the dependent variable \( y \).
- Regression Sum of Squares (SSR) represents the variability explained by the regression model.

The relationship between SST, SSR, and SSE is given by:

 $SST = SSR + SSE$ 

This equation reflects the decomposition of total variability into explained variability (SSR) and unexplained variability (SSE) due to errors.

### Impact of Extra Variables on Intercept:

When additional variables are introduced, it can impact the intercept (\( b_0 \)) in the linear regression model. The intercept is the value of \( y \) when all independent variables (\( x_1, x_2, \ldots, x_n \)) are zero. The presence of extra variables can affect the baseline value of the dependent variable.

**What are the most common techniques for computing the coefficients in linear regression?**;; The most common techniques for computing coefficients in linear regression are Ordinary Least Squares, which minimizes the sum of squared residuals, and Gradient Descent, which iteratively updates coefficients to minimize error.