---
aliases:
- SGD
category: STATISTICS
date modified: 27-09-2025
tags:
- math
- optimisation
- statistics
---
Stochastic Gradient Descent (SGD) is an optimization algorithm that updates [[Model Parameters]] using the gradient computed from a single randomly selected training example at each iteration, rather than the entire dataset, as in [[Gradient Descent]] .

#### Why do we use SGD
* It allows efficient optimization ([[Model Optimisation|Optimisation]]) when working with large datasets, as computing the gradient on the entire dataset is expensive.
* Introduces randomness, which can help escape local minima.
* Can run on a deployed system.

#### Key Characteristics
* Update Rule:
  Parameters are updated for each sample using its gradient contribution.

* Objective:
  Minimize the [[Loss function]] efficiently without processing the full dataset at every step.
#### Pros:
* Fast parameter updates.
* Handles large-scale and streaming data well.
#### Cons:
* Noisy updates can cause high [[Variance]] in the cost function.
* Requires techniques like [[Learning Rate]] scheduling or [[Momentum]] for stable convergence.