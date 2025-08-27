---
aliases:
category:
date modified: 27-07-2025
tags:
  - math
  - ml
  - optimisation
---
Mini-Batch Gradient Descent is an optimization algorithm that serves as a compromise between Batch Gradient Descent and Stochastic Gradient Descent (SGD). Instead of using the entire dataset or a single data point, it updates model parameters using small, random subsets (mini-batches) of the training data.

Pros:
- Faster than batch gradient descent.
- More stable than [[Stochastic Gradient Descent]]
- Leverages hardware acceleration (GPUs).