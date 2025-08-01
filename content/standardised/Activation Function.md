---
aliases: []
category:
date modified: 27-07-2025
tags: [deep_learning]
---
Activation functions play a role in [[Neural network]] by introducing non-linearity, allowing models to learn from complex patterns and relationships in the data.

[[How do we choose the right Activation Function]]
### Key Uses of Activation Functions:

1. Non-linearity: Without activation functions, neural networks would behave as linear models, unable to capture complex, non-linear patterns in the data
2. [[Data transformation]]: Activation functions modify input signals from one layer to another, helping the model focus on important information while ignoring irrelevant data,
3. [[Backpropagation]]: They enable gradient-based optimization by making the network differentiable, essential for efficient learning.

### Purpose of Typical Activation Functions

Linear: Outputs a continuous value, suitable for regression.

ReLU (Rectified Linear Unit): 
  - Purpose: ReLU is used to introduce non-linearity by turning neurons "on" or "off." It outputs the input directly if it is positive; otherwise, it outputs zero. This helps in efficiently training deep networks by mitigating the vanishing gradient problem.
  - Function:$f(x) = \max(0, x)$

Sigmoid:
  - Purpose: Sigmoid is used primarily in [[Binary Classification]] tasks. It squashes input values to a range between 0 and 1, making it suitable for representing probabilities.
  - Function:$f(x) = \frac{1}{1 + e^{-x}}$

 Tanh:
  - Purpose: Tanh is similar to the sigmoid function but outputs values in the range of -1 to 1. This zero-centered output can be beneficial for optimization in certain scenarios.
  - Function:$f(x) = \tanh(x)$

Softmax:
  - Purpose: Softmax is used in multi-class classification tasks. It converts a vector of raw scores (logits) into a probability distribution, where each value is between 0 and 1, and the sum of all values is 1. This allows the outputs to be interpreted as probabilities, with larger inputs corresponding to larger output probabilities.
  - Application: In both softmax regression and neural networks with softmax outputs, a vector$\mathbf{z}$is generated by a linear function and then passed through the softmax function to produce a probability distribution. This enables the selection of one output as the predicted category.

The softmax function converts a vector of raw scores (logits) into a probability distribution. The formula for the softmax function for a vector $\mathbf{z} = [z_1, z_2, \ldots, z_N]$is given by:

$$\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{N} e^{z_j}}$$

This ensures that the output values are between 0 and 1 and that they sum to 1, making them [[interpretability|interpretable]] as probabilities.




