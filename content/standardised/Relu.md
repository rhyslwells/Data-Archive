---
aliases: 
category: DS
date modified: 27-07-2025
tags:
  - deep_learning
---
How does the ReLU [[activation function]] help overcome the vanishing gradient problem?

The rectified linear unit (ReLU) activation function helps overcome the vanishing gradient problem by avoiding ==gradient saturation==. ReLU replaces negative values with zero, ensuring that the gradients flowing backward remain non-zero and do not vanish. This promotes better gradient flow and enables effective learning in deep neural networks.
[[vanishing and exploding gradients problem]]