---
title: Backpropagation in Neural Networks
tags:
  - deep_learning
  - ml_optimisation
  - statistics
aliases:
  - Backprop
  - BP
  - backward propagation
category: Machine Learning
---
Backpropagation is an algorithm for training neural networks by iteratively correcting prediction errors. It calculates the gradient of the [[loss function]] $L(\theta)$ with respect to each model parameter $\theta$, enabling updates via [[Gradient Descent]] to minimize the loss.

Mathematically, backpropagation employs the chain rule from calculus to propagate errors backward through the network. Each layer computes a partial derivative, which is used to adjust its weights. This iterative process continues until a convergence criterion is met, typically when the loss change falls below a threshold.

Backpropagation is especially critical in [[Supervised Learning]], where models learn from labeled data to recognize patterns.
## Important Notes
- Gradient descent minimizes the loss by updating parameters in the direction of the negative gradient:  
  $\nabla L(\theta) = \frac{\partial L}{\partial \theta}$.  
- Backpropagation adjusts weights based on computed error gradients, enabling effective deep model optimization.
- Computational Cost: Backpropagation can be expensive for deep networks, requiring computation of gradients across all layers.  
- Vanishing/Exploding Gradients: In deep networks, gradients can become too small or too large, hindering effective training.
## Example Application

A [[Feed Forward Neural Network]] trained for image classification uses backpropagation to minimize cross-entropy loss. The gradient of the loss is calculated layer-by-layer and weights are updated using an optimizer like Adam.
## Backpropagation Step-by-Step (Manual Calculation)

When dealing with many parameters, like in neural networks, it can be helpful to think in terms of ==computation graphs.==

Basic backpropagation procedure through a computation graph:
1. Work right to left: starting from the output layer back towards the input.
2. For each node:
   - Calculate the local derivative(s) (i.e., the derivative of the node’s output with respect to its input).
   - Combine this with the derivative of the loss with respect to the node using the chain rule.

Definition:  
The "local derivative(s)" are the derivatives of the current node’s output with respect to each of its inputs or parameters.
## Computation Graph Example (using [[Sympy]])
To manually calculate gradients through a computation graph, symbolic differentiation can be used.

```python
from sympy import symbols, diff

# Define symbols
x, w, b = symbols('x w b')
y = symbols('y')  # true label

# Define a simple model: prediction = wx + b
prediction = w*x + b

# Define a loss function: squared error
loss = (prediction - y)2

# Compute gradients
grad_w = diff(loss, w)
grad_b = diff(loss, b)

print(grad_w)
print(grad_b)
```
This symbolic approach helps verify gradient calculations during small-scale experiments.
## Follow-Up Questions
- How does backpropagation compare to optimization methods like Newton’s Method or evolutionary strategies?  
- What role does [[Regularisation]] play in addressing [[overfitting]] when training deep networks with backpropagation?
## Related Topics
- [[Gradient Descent Optimizers]] (e.g., [[Adam Optimizer]], RMSprop)  
- [[vanishing and exploding gradients problem]]  
