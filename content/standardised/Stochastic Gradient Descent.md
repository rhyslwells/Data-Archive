---
aliases:
  - SGD
category: STATISTICS
date modified: 1-08-2025
tags:
  - math
  - statistics
  - optimisation
---
Stochastic Gradient Descent (SGD) is an optimization algorithm that updates [[model parameters]] using the gradient computed from a single randomly selected training example at each iteration, rather than the entire dataset, as in [[Gradient Descent]] .

#### Why do we use SGD
* It allows efficient optimization ([[Model Optimisation|Optimisation]]) when working with large datasets, as computing the gradient on the entire dataset is expensive.
* Introduces randomness, which can help escape local minima.

#### Key Characteristics
* Update Rule:
  Parameters are updated for each sample using its gradient contribution.

* Objective:
  Minimize the [[loss function]] efficiently without processing the full dataset at every step.
#### Pros:
* Fast parameter updates.
* Handles large-scale and streaming data well.
#### Cons:
* Noisy updates can cause high [[variance]] in the cost function.
* Requires techniques like [[learning rate]] scheduling or [[momentum]] for stable convergence.