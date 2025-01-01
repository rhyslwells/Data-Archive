# Optimising a [[Logistic Regression]] Model

In `sklearn`, the logistic regression model uses an optimization algorithm to find the best parameters (intercept and coefficients) that minimize a loss function, typically the logistic loss (cross-entropy loss). Here's an overview of how it works:

Optimization process: `sklearn` optimizes the logistic regression parameters using iterative solvers (like LBFGS, newton-cg, or liblinear) that minimize the logistic loss function.`sklearn` is using one of these optimization algorithms (likely `lbfgs` or `liblinear` by default) to minimize the logistic loss function. 

### Objective Function (Loss Function)

The objective of logistic regression is to minimize the logistic [[loss function]] (also called cross-entropy loss) given by:

$\text{Cost}(\theta) = -\frac{1}{m} \sum_{i=1}^m \left( y^{(i)} \log(h_{\theta}(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_{\theta}(x^{(i)})) \right)$

Where:
- $h_{\theta}(x) = \frac{1}{1 + \exp(-\theta^T x)}$ is the sigmoid function that predicts probabilities.
- $y^{(i)}$ is the actual label for the $i$-th sample (either 0 or 1).
- $m$ is the number of samples.
- $\theta$ is the vector of parameters (intercept and coefficients).
  
The goal is to minimize this [[cost function]] by finding the optimal $\theta$ values (intercept and coefficients).

### Optimization Algorithm (Solvers)

[[sklearn]] provides different [[Optimisation function]] to find the optimal [[Model Parameters]] for logistic regression. These solvers use optimization techniques like Gradient Descent or more advanced methods like Newton’s Method or Limited-memory Broyden–Fletcher–Goldfarb–Shanno (LBFGS). Here are the main solvers used in `sklearn`:

- 'liblinear': This solver uses coordinate descent or regularized Newton's method and is a good choice for smaller datasets. It supports both L1 (lasso) and L2 ([[ridge]]) regularization.
  
- 'lbfgs': This is a quasi-Newton method (Limited-memory BFGS), which approximates the Newton's method and is more efficient for larger datasets. It’s an iterative solver that converges faster and requires fewer iterations than simple gradient descent.
  
- 'newton-cg': This solver is based on Newton’s method, which computes the second-order derivative (Hessian matrix) and updates parameters using the inverse of this matrix. It works well for logistic regression with large datasets and is efficient when the number of features is large.
  
- 'saga': An efficient solver that can handle L1 regularization (for sparse solutions) and large datasets. It’s a variant of Stochastic Gradient Descent (SGD) and supports L1, L2, and ElasticNet regularization.

- 'sgd': This is a solver for stochastic [[gradient descent]], which updates parameters iteratively using only a single data point (or a small batch) at a time. It can be slower but is useful for very large datasets.

### 5. Convergence Criteria

`sklearn`’s logistic regression solvers have specific criteria for when to stop the optimization process:
- Convergence tolerance (`tol`): This is the threshold for when the optimization stops. When the improvement in the cost function between iterations becomes smaller than `tol`, the process stops.
- Maximum iterations (`max_iter`): The maximum number of iterations allowed before the solver stops. If convergence is not achieved within the allowed iterations, the algorithm will stop, and a warning will be issued.


