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

>[!Summary]  
> Backpropagation is an essential algorithm in the training of neural networks and iteratively correcting its mistakes. It involves a process of calculating the gradient of the loss function $L(\theta)$ concerning each weight in the network, allowing the system to update its weights via [[Gradient Descent]]. 
> 
> This process helps minimize the difference between predicted outputs and actual target values. Mathematically, the chain rule of calculus is employed to propagate errors backward through the network.
> 
Each layer in the network computes a partial derivative that is used to adjust the weights. This iterative approach continues until a convergence criterion is met, typically when the change in loss falls below a threshold.
>
>The backpropagation algorithm is critical in [[Supervised Learning]], where labeled data is used to train models to recognize patterns.

>[!Breakdown]  
> Key Components:  
> - **Algorithm**: Gradient Descent  
> - **Mathematical Foundation**: Chain Rule for derivatives  
> - **Metrics**: Loss function (e.g., Mean Squared Error, Cross-Entropy)

>[!important]  
> - Gradient descent uses $\nabla L(\theta) = \frac{\partial L}{\partial \theta}$ to iteratively minimize the loss.  
> - Backpropagation optimizes deep learning models by adjusting weights based on error gradients.

>[!attention]  
> - The method is computationally expensive for deep networks due to the need to compute gradients for each layer.  
> - Vanishing/exploding gradients in deep layers can prevent proper weight updates.

>[!Example]  
> A feed-forward neural network trained on image classification data uses backpropagation to minimize cross-entropy loss. The gradient of the loss is calculated layer by layer, adjusting weights through an optimization algorithm like Adam.

>[!Follow up questions]  
> - How does backpropagation compare with other optimization algorithms such as Newton’s method or evolutionary strategies?  
> - What role does [[Regularisation]] play in addressing overfitting when using backpropagation in deep neural networks?

>[!Related Topics]  
> - Gradient Descent Optimizers ([[Adam Optimizer]], RMSprop)  
> - [[vanishing and exploding gradients problem]]


# Backpropgation

Backpropgation is used to calc the gradient of the loss function with respect to the model parameters, when there are a lot of parameters - i.e in a neural network.
Simple example of backpropgation

Simple example of computation graph
Computation graph - calcing derivatives?
Use sympy to calculate derivatives for the loss function.

> The steps in backprop   
>Now that you have worked through several nodes, we can write down the basic method:\
> working right to left, for each node:
>- calculate the local derivative(s) of the node
>- using the chain rule, combine with the derivative of the cost with respect to the node to the right.   

The 'local derivative(s)' are the derivative(s) of the output of the current node with respect to all inputs or parameters.

Example of using sympy to calculate derivatives for the loss function. Use `diff`, `subs`
```python
from sympy import symbols, diff
```

## [[Sympy]]