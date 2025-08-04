---
aliases: []
category: ML
date modified: 1-08-2025
tags: [modeling, optimisation]
---
Adam (Adaptive Moment Estimation) is an advanced optimization algorithm that combines the benefits of both [[Momentum]] and adaptive learning rates. It is widely used due to its efficiency and effectiveness in training [[deep learning]] models.

Adam is particularly effective for large datasets and complex models, as it provides robust convergence and requires minimal tuning compared to other optimization algorithms. Its ability to ==dynamically adjust learning rates== makes it a popular choice in the deep learning community.
#### Key Features of Adam:

**Adaptive Learning Rates:** Adam adjusts the [[Learning Rate]] for each parameter individually, based on the first and second moments of the gradients. This allows for more precise updates and better convergence.

**Momentum and RMSProp Combination:** Adam incorporates the concept of momentum by using moving averages of the gradients (first moment) and the squared gradients ==(second moment)==, similar to RMSProp.

**Parameter Update Rule:** The update rule involves computing biased estimates of the first and second moments, which are then corrected to provide unbiased estimates. These are used to update the parameters.

**[[Hyperparameter]]:**
  - **Learning Rate (\($\alpha$\)):** Typically set to 0.001, but can be tuned for specific tasks.
  - **Beta1 and Beta2:** Control the decay rates for the moving averages of the first and second moments. Common values are 0.9 and 0.999, respectively.
  - **Epsilon (\($\epsilon$\)):** A small constant added for numerical stability, usually set to \(1 \times 10^{-8}\).

**Implementation Challenges:**
  - **Parameter Tuning:** Careful tuning of learning rate, beta1, and beta2 is essential for optimal performance.
  - **Numerical Stability:** Adjusting epsilon can help prevent division by zero and other numerical issues.  
## Related concepts
- [[Gradient Descent]]
- [[Why does the Adam Optimizer converge]]
- 