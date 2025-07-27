---
aliases: []
category:
date modified: 27-07-2025
tags: [deep_learning, ml, optimisation]
title: 
---
The vanishing gradient problem arises when gradients of the loss with respect to early layer weights approach zero, hindering learning in those layers. This typically occurs due to activation functions like sigmoid or tanh and deep architectures.

## Description

The vanishing gradient problem occurs when gradients become extremely small in early layers during [[backpropagation]]. This leads to:

- Slow convergence
- Poor learning of long-term dependencies
## Causes

- Activation functions: Sigmoid and tanh functions saturate for large inputs, resulting in gradients near zero. These small gradients, when propagated backward, diminish layer by layer.
- Deep architectures: As depth increases, gradient signals can diminish before reaching early layers.
- Ineffective optimization: Poor initialization or unsuitable learning rates can worsen the problem.
## Symptoms

- Loss remains constant over epochs.
- Weight values do not change significantly during training.

These symptoms can be diagnosed using:

- Loss monitoring tools in frameworks like [[Keras]]
- Plots of weight values across epochs
## Mathematical Background

The vanishing gradient problem is linked to the product of Jacobian matrices across layers. When the Jacobian matrices have eigenvalues with magnitudes less than 1, the gradient norm can shrink exponentially with the number of layers due to the chain rule.
## Related
- [[Batch Normalisation]]
- [[Xaiver]]
- [[Relu]] or [[initialization methods]]
- [[Recurrent Neural Networks|RNN]]
