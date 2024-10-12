---
title: 
tags:
  - ml
aliases:
  - GD
---
>[!Summary]
> Gradient descent is an optimization algorithm used to minimize errors in a model by adjusting its parameters iteratively. It works by moving in the direction of the steepest decrease of the [[loss function]].
### Gradient Descent

Uses the difference quotient.

The step size is important between derivatives (small then slow) (if large then might miss minimum).

With Stochastic method we can don't need to the entire data set again, we can just add the new information to get improvement.

Gradient descent uses the entire data set.

### [[Stochastic Gradient Descent]]
Stochastic uses random entries to get derivative instead of the full dataset
Why do we use [[Stochastic Gradient Descent]]?;; To find the derivative of discrete data so we can determine a straight line with the Least Square Error (LSE).
What is [[Stochastic Gradient Descent]]?;; updates the model parameters based on the gradient of a single randomly chosen data point. 

### [[Batch gradient descent]]
What is [[Batch gradient descent]]?;; computes the gradient of the entire dataset,

### [[Mini-batch gradient descent]]
Stochastic Mini-batched descent is the fastest way (groups then does randomly).
What is [[Mini-batch gradient descent]]?;; Is a compromise of [[Batch gradient descent]] and [[Stochastic Gradient Descent]].


**What is the difference between batch gradient descent and stochastic gradient descent?**;; Batch gradient descent computes the gradient of the cost function using the entire training dataset in each iteration, while stochastic gradient descent updates the model's parameters based on the gradient of the cost function with respect to one training example at a time. Mini-batch gradient descent is a compromise, using a subset of the training data in each iteration.