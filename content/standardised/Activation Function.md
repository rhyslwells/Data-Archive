---
tags:
  - deep_learning
---
Used in [[Neural network]] for non-linearity

Activation functions play a crucial role in neural networks by introducing **non-linearity**, allowing models to learn from complex patterns and relationships in the data.
### Key Uses of Activation Functions:

1. **Non-linearity**: Without activation functions, neural networks would behave as linear models, unable to capture complex, non-linear patterns in the data
2. **Data transformation**: Activation functions modify input signals from one layer to another, helping the model focus on important information while ignoring irrelevant data,
3. **[[Backpropagation]]**: They enable gradient-based optimization by making the network differentiable, essential for efficient learning.
### Common Activation Functions:
- **Sigmoid**: Used for binary classification, outputting values between 0 and 1.
- **ReLU (Rectified Linear Unit)**: Popular in deep networks, it outputs the input if positive and zero otherwise, improving training efficiency.
- **Tanh**: Similar to sigmoid but ranges from -1 to 1, helping in zero-centered output.
- **Softmax**: Used in multi-class classification to produce probabilities that sum to 1.

- **ReLU (Rectified Linear Unit)**: $f(x) = \max(0, x)$
- **Sigmoid**: $f(x) = \frac{1}{1 + e^{-x}}$
- **Tanh**: $f(x) = \tanh(x)$
