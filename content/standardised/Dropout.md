---
tags:
  - deep_learning
  - ml_optimisation
aliases: 
category: 
phase: 
topic: 
filename:
---
**Dropout** is a [[Regularisation]] technique used in [[Neural network]] training to prevent [[overfitting]]. It works by randomly dropping units (neurons) during training, which helps the network to not rely too heavily on any single neuron.

Purpose
- The main goal of dropout is to improve the generalization of the model by reducing over-reliance on specific neurons. This encourages the network to learn more robust features that are useful in different contexts.

How It Works
- During each training iteration, a subset of neurons is randomly selected and ignored (dropped out). This means their contribution to the activation of downstream neurons is temporarily removed on the forward pass, and any weight updates are not applied to the neuron on the backward pass.

Implementation
```python
from tensorflow.keras.layers import Dropout
# Add a dropout layer with a dropout rate of 0.5
# The dropout rate (e.g., 0.5) specifies the fraction of neurons to drop during training. A rate of 0.5 means that half of the neurons will be dropped at each iteration.
Dropout(0.5)
```