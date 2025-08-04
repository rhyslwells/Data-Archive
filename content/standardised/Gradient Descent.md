---
aliases: [GD]
category:
date modified: 1-08-2025
tags: [optimisation]
---
Gradient descent is an [[Optimisation function]] used to minimize errors in a model by adjusting its parameters iteratively. It works by moving in the direction of the steepest decrease of the [[Loss function]].

Uses the difference quotient.

The step size is important between derivatives (small then slow) (if large then might miss minimum).

With Stochastic method we can don't need to the entire data set again, we can just add the new information to get improvement.

Gradient descent uses the entire data set.

Used to find the min/max of [[Cost Function]].

Given any point on the cost function surfaces. Then ask, "In what direction should I go to make the biggest change downhill or up hill, i.e. gradient descent"

![[Obsidian_EPIqLAto5w.png|500]]

![[Obsidian_FEGflF5RKQ.png|500]]

How do you implement Gradient descent? You update the (direction) parameter by the small step by the [[Learning Rate]].

![[Obsidian_M4mzGSAx7d.png|500]]

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
# [[Gradient Descent]]

Gradient descent is commonly used in:
- **Deep Learning**: Frameworks like TensorFlow and PyTorch use variations of gradient descent for training.
- **Custom Implementations**: If you write logistic regression from scratch, gradient descent is a straightforward optimization method.

### **How Gradient Descent Works**

Gradient Descent, a common [[Optimisation techniques]], iteratively updates the [[Model Parameters]] by computing the gradient of the [[loss function]] with respect to the parameters. The update formula is:

$\theta = \theta - \alpha \nabla_{\theta} \text{Cost}(\theta)$

Where:
- $\theta$ are the parameters (intercept and coefficients).
- $\alpha$ is the learning rate (step size for updates).
- $\nabla_{\theta} \text{Cost}(\theta)$ is the gradient of the [[Cost Function]] with respect to the parameters $\theta$.

#### Process:

1. Calculate the gradient of the loss function.
2. Adjust the parameters in the direction of the negative gradient (to reduce loss).
3. Repeat until either:
    - The loss function converges (minimal change between updates), or
    - The maximum number of iterations is reached.

[[Gradient Descent]]

[[Cost Function]] value versus number of iterations of [[Gradient Descent]] should decrease

Can use contour plots to show [[Gradient Descent#]] moving towards minima.
![[Pasted image 20241224082847.png]]