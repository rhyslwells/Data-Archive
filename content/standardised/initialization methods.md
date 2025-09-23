---
aliases: []
category:
date modified: 27-07-2025
tags: [deep_learning, optimisation]
---
A weight initialization method sets the initial values of a [[neural network]]’s weights *before* training begins. This choice significantly affects how well and how fast the network learns.

## Why Initialization Matters

During training, weights are updated via [[gradient descent]]. If weights start too small or too large, gradients can:

* Vanish (approach zero), halting learning in earlier layers.
* Explode (grow very large), causing unstable updates.

Proper initialization ensures that:

* The input signal maintains a consistent scale as it propagates forward.
* The gradient signal maintains a consistent scale as it propagates backward.
## Main Goals of Initialization

1. Prevent vanishing/exploding gradients.
2. Maintain similar variance of activations and gradients across layers.
3. Speed up convergence.

## Common Initialization Methods

* Xavier (Glorot): Scales weights based on the number of input and output units to maintain variance.
* He: Optimized for [[Relu]] activations, focuses on variance preservation from the input side.
* Uniform / Normal: Basic methods that are prone to instability in deep networks.

## Related Notes

* [[Xaiver]]
* [[initialization methods]]
* [[vanishing and exploding gradients problem]]

