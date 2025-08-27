---
aliases: []
category:
date modified: 24-08-2025
tags: []
---
Batch Gradient Descent computes the gradient of the [[cost function]] ==using the entire training dataset== at each iteration before updating the [[model parameters]].

#### Key Characteristics
* Update Rule:
  Parameters are updated once per [[epoch]], after processing the entire dataset.
* Objective:
  Achieve accurate and stable updates, as the gradient is computed over all training examples.
#### Pros:
* Produces a stable convergence path.
* Provides an accurate estimate of the gradient.

#### Cons:
* Computationally expensive for large datasets.
* Requires the entire dataset to fit in memory, which may not be feasible for big data.
* Slower to start learning compared to [[Stochastic Gradient Descent|SGD]] or Mini-Batch methods.