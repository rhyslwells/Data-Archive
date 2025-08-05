---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - optimisation
  - ml
---
Gradient descent in [[linear regression]]

Related terms:
- [[Gradient Descent]]

It ==iteratively== updates coefficients to minimize error.

Gradient descent is an optimization algorithm used to minimize the cost function in linear regression by iteratively adjusting the model parameters (coefficients). Here's how it works with linear regression:

1. Initialize Parameters: Start with initial guesses for the coefficients (weights), typically set to zero or small random values.
2. Compute Predictions: Use the current coefficients to make predictions for the dependent variable $\hat{y}$ using the linear regression model: $\hat{y} = b_0 + b_1x_1 + b_2x_2 + \ldots + b_nx_n$
3. Calculate the Cost Function:Compute the loss function, SSE.
4. Compute the Gradient: Calculate the gradient of SSE function with respect to each coefficient. The gradient is a vector of partial derivatives indicating the direction and rate of change of the cost function:
     $$\frac{\partial J}{\partial b_j} = -\frac{2}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i) x_{ij}$$
   Here, $x_{ij}$ is the value of the $j$-th feature for the $i$-th observation.
5. Update the Coefficients: Adjust the coefficients in the opposite direction of the gradient to reduce the cost function. This is done using a [[Learning Rate]]$\alpha$, which controls the size of the steps taken: $b_j = b_j - \alpha \frac{\partial J}{\partial b_j}$

6. Iterate & Converge Repeat steps 2 to 5 until the cost function converges to a minimum or a predefined number of iterations is reached. The algorithm converges when the changes in the cost function or the coefficients become very small, indicating that the minimum has been reached.