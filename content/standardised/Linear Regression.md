---
model: 
tags:
  - ml
  - linear
  - model
---
# Description

Linear regression assumes [[linearity]] between the input features and the target variable. Assumes that the relationship between the independent variable(s) and the dependent variable is linear.

During the training phase, the algorithm adjusts the slope (m) and the intercept (b) of the line to minimize the [[loss function]].

The linear regression model is represented as:

$y = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n$

- $y$ is the dependent variable (the variable we want to predict).
- $x_1, x_2, \ldots, x_n$ are the independent variables (features or predictors).
- $b_0, b_1, b_2, \ldots, b_n$ are the coefficients (weights) associated with each independent variable.
- $b_0$ is the intercept term.

You ==evaluate== the performance of your model by comparing its predictions to the actual values in a separate test dataset. Common metrics for evaluating regression models  are:

-  Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
-  [[R squared]].

The goal of linear regression is to find the values of coefficients $$b_0, b_1, b_2, \ldots, b_n$$ that ==minimize the sum of squared errors (SSE),== also known as the residual sum of squares (RSS) or (MSE - mean square error).

Mathematically, SSE is a [[loss function]] given by:

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
### [[Ordinary Least Squares]]

The Ordinary Least Squares method is used to minimize SSE. It achieves this by finding the values of  that minimize the sum of squared differences between the observed and predicted values. The formulas for  are derived by setting partial derivatives of SSE with respect to each coefficient to zero.

OLS is an analytical method
### [[Gradient Descent]]

It ==iteratively== updates coefficients to minimize error.

Gradient descent is an optimization algorithm used to minimize the cost function in linear regression by iteratively adjusting the model parameters (coefficients). Here's how it works with linear regression:

1. **Initialize Parameters**: Start with initial guesses for the coefficients (weights), typically set to zero or small random values.
2. **Compute Predictions**: Use the current coefficients to make predictions for the dependent variable $\hat{y}$ using the linear regression model: $\hat{y} = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n$
3. **Calculate the Cost Function**:Compute the loss function, SSE.
4. **Compute the Gradient**: Calculate the gradient of SSE function with respect to each coefficient. The gradient is a vector of partial derivatives indicating the direction and rate of change of the cost function:
     $$\frac{\partial J}{\partial b_j} = -\frac{2}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i) x_{ij}$$
   Here, $x_{ij}$ is the value of the $j$-th feature for the $i$-th observation.
5. **Update the Coefficients**: Adjust the coefficients in the opposite direction of the gradient to reduce the cost function. This is done using a [[learning rate]]$\alpha$, which controls the size of the steps taken: $b_j = b_j - \alpha \frac{\partial J}{\partial b_j}$

6. **Iterate** & Converge Repeat steps 2 to 5 until the cost function converges to a minimum or a predefined number of iterations is reached. The algorithm converges when the changes in the cost function or the coefficients become very small, indicating that the minimum has been reached.


# [[Model Evaluation]]

- [[R squared]]
- [[Adjusted R squared]] takes into account the number of variables.
- [[F-statistic]] overall significance of model (lower worse).
- [[Feature Selection]] Use P>|t| column to decide whether to keep variable less that 0.05
- [[p-values in linear regression in sklearn]]

![[Pasted image 20240117145455 1.png|500]] ![[Pasted image 20240124135607.png|500]]
### Impact of Extra Variables on Intercept:

When additional variables are introduced, it can impact the intercept ($b_0$) in the linear regression model. The intercept is the value of $y$ when all independent variables ($x_1, x_2, \ldots, x_n$) are zero. The presence of extra variables can affect the baseline value of the dependent variable.
