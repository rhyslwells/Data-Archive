---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - regressor
  - optimisation
---
LBFGS stands for Limited-memory Broyden-Fletcher-Goldfarb-Shanno, which is an [[Optimisation function]]optimization algorithm used to find the minimum of a function. In the context of [[logistic regression]], LBFGS is a method for optimizing the cost function to find the optimal [[Model Parameters]] (such as the intercept and coefficients).

Here's a breakdown of the key features of LBFGS:

1. Quasi-Newton Method: LBFGS is a type of Quasi-Newton method, which approximates the inverse of the Hessian matrix (second-order derivatives of the cost function). Instead of computing the full Hessian matrix, it uses an approximation, which makes it more efficient for large datasets.
    
2. Limited Memory: The "limited-memory" part refers to the fact that LBFGS does not store the entire Hessian matrix, which is computationally expensive and memory-intensive. Instead, it keeps a limited amount of information from previous iterations, making it well-suited for large-scale problems where full memory-based methods might not be feasible.
    
3. Optimization for Smooth, Differentiable Functions: It is designed to optimize smooth, differentiable functions like the [[Cost Function]] in logistic regression.
    

In the context of logistic regression with sklearn, LBFGS is used as a solver for optimization. When you set `solver='lbfgs'`, [[Scikit-Learn]]'s logistic regression uses this algorithm to iteratively adjust the model parameters (the intercept and coefficients) to minimize the logistic loss (the cost function) while possibly incorporating regularization.

LBFGS is often preferred for its efficiency and ability to converge quickly without needing a lot of iterations, especially when the number of features is large.