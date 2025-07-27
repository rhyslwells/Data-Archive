---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
# Logistic regression in sklearn & Gradient Descent

sklearn's Logistic Regression implementation does not use [[Gradient Descent]] by default. Instead, it uses more sophisticated optimization techniques depending on the solver specified. These solvers are more efficient and robust for finding the optimal parameters for logistic regression. Here's a summary:

### [[Optimisation function]]: Solvers in sklearn's Logistic Regression**

1. **`lbfgs` (default in many cases)**:
    - Stands for Limited-memory Broyden–Fletcher–Goldfarb–Shanno.
    - It's a quasi-Newton method, which approximates the second derivatives (Hessian matrix) to find the minimum of the cost function efficiently.
      
2. **`liblinear`**:
    - Uses the coordinate descent method for optimization.
    - Ideal for small datasets or when `penalty='l1'` is used.
      
3. **`sag` (Stochastic Average Gradient)**:
    - An iterative solver similar to stochastic gradient descent (SGD) but averages gradients over all samples.
    - Efficient for large datasets.
      
4. **`saga`**:
    - An improved version of `sag`, supporting both `l1` and `l2` penalties.
    - Suitable for sparse and large datasets.
      
5. **`newton-cg`**:
    - Uses the Newton method with conjugate gradients.
    - Efficient for datasets with many features.