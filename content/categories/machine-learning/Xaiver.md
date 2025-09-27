---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- deep_learning
- optimisation
---
Xavier initialization (also known as Glorot initialization) is a weight initialization technique designed to improve the training of deep neural networks. It maintains stable variance of activations and gradients across layers, helping prevent both the vanishing and exploding gradient problems. Proposed by Xavier Glorot and Yoshua Bengio in their 2010 paper _"Understanding the difficulty of training deep feedforward neural networks."_
## Purpose

To ensure that the variance of the activations and gradients remains consistent across layers during both forward and backward propagation.

This helps with [[vanishing and exploding gradients problem]].
## Role in Training Stability

[[Xavier]] initialization helps stabilize training by setting the initial weights to values that are neither too small nor too large. This supports:

- Better gradient flow
- Faster and more stable convergence
- Improved learning in deeper networks
    

### Related Notes
- [[initialization methods]]