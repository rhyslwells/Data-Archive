---
aliases: []
category:
date modified: 27-07-2025
model: 
tags: [regressor]
---
Linear regression assumes [[linearity]] between the input features and the target variable. Assumes that the relationship between the independent variable(s) and the dependent variable is linear.

During the training phase, the algorithm adjusts the slope (m) and the intercept (b) of the line to minimize the [[Loss function]].

The linear regression model is represented as:

$$y = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n$$

- $y$ is the dependent variable (the variable we want to predict).
- $x_1, x_2, \ldots, x_n$ are the independent variables (features or predictors).
- $b_0, b_1, b_2, \ldots, b_n$ are the coefficients (weights) associated with each independent variable.
- $b_0$ is the intercept term.

The goal of linear regression is to find the values of coefficients $$b_0, b_1, b_2, \ldots, b_n$$ that ==minimize the sum of squared errors (SSE),== also known as the residual sum of squares (RSS) or (MSE - mean square error).

You ==evaluate== the performance of your model by comparing its predictions to the actual values in a separate test dataset. Common metrics for evaluating regression models are:
-  Mean Squared Error (MSE)
-  Root Mean Squared Error (RMSE)
-  [[R squared]].

Related terms:
- [[Ordinary Least Squares]]
- [[Gradient descent in linear regression]]
- [[Variability in linear models]]
- [[Why standardise features]]

### Impact of Extra Variables on Intercept of linear regression

When additional variables are introduced, it can impact the intercept ($b_0$) in the linear regression model. The intercept is the value of $y$ when all independent variables ($x_1, x_2, \ldots, x_n$) are zero. The presence of extra variables can affect the baseline value of the dependent variable.

### [[Model Evaluation]]

- [[R squared]]
- [[Adjusted R squared]] takes into account the number of variables.
- [[f-regression]]