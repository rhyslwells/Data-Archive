---
aliases: 
category: 
date modified: 1-08-2025
tags:
  - deep_learning
  - ml
---
For a neural network model, fitting weights and biases involves optimizing these [[Model Parameters]] so the model learns to map input features ($X$) to target outputs ($y$) effectively. This is achieved through the training process, which minimizes the error between predictions and actual values.

Best Practices
- Use appropriate weight initializations like He or Xavier.
- Choose a suitable [[loss function]] for the task.
- Optimize using advanced optimizers like Adam or RMSprop.
- Experiment with batch sizes, epochs, and learning rates.
- Apply regularization (L2, [[Dropout]]) to prevent overfitting.
- Monitor validation metrics and use early stopping.

In [[ML_Tools]] see: Neural_Net_Weights_Biases.py

## Initialization of Weights and Biases

Initializing all weights randomly. The weights are assigned randomly by initializing them very close to 0. It gives better accuracy to the model since every neuron performs different computations.

Proper initialization is critical for training to converge efficiently. Poor initialization can lead to slow convergence or getting stuck in local minima. By starting with well-chosen initial values, the network can learn more effectively and avoid issues like vanishing or exploding gradients.

Weights:
- Use small random values (e.g., drawn from Gaussian or uniform [[distributions]]) to break symmetry and ensure that neurons learn different features.
- Initialization techniques like He initialization (for [[ReLU]] activations) or Xavier initialization (for sigmoid/tanh activations) are commonly used because they help maintain the scale of gradients across layers, promoting stable and faster convergence.

```python
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import HeNormal

# Example of He initialization for ReLU activation
Dense(25, activation="relu", kernel_initializer=HeNormal())
```
Biases:
- Start with zeros (`0`) to ensure symmetry-breaking during optimization. This allows the network to learn offsets for the activations without introducing bias in the initial learning phase.

## [[Forward Propagation]]

During forward propagation, the network computes activations using the current weights and biases, and passes these activations to subsequent layers to generate predictions. This step is crucial as it determines how well the network can map inputs to outputs based on its current parameters.

## Loss Function

The loss function quantifies the difference between predicted outputs and true labels. It serves as the objective function that the network aims to minimize during training. Choosing the right loss function is essential as it directly impacts the learning process and the network's ability to generalize.

- Binary Cross-Entropy: For [[Binary Classification]].
- Categorical Cross-Entropy: For multi-class classification.
- [[Mean Squared Error]] (MSE): For regression tasks.

Example:
```python
from tensorflow.keras.losses import BinaryCrossentropy
loss_fn = BinaryCrossentropy()
```
## [[Backpropagation]]

Backpropagation computes the gradients of the loss function with respect to weights and biases using the chain rule. This process is fundamental for learning, as it provides the necessary information to update the parameters in a way that reduces the loss.

## [[Gradient Descent]] Optimization

Gradients from backpropagation are used to update weights and biases iteratively. Optimization algorithms like Adam, RMSprop, and [[Stochastic Gradient Descent|SGD]] with momentum are crucial as they determine the efficiency and speed of convergence, especially in large datasets and complex models.

Example:
```python
from tensorflow.keras.optimizers import Adam
optimizer = Adam(learning_rate=0.001)
```

## Batch Training

Weights and biases are updated after processing a batch of data. Batch training helps in stabilizing the learning process and can lead to faster convergence compared to updating after each sample. The choice of batch size and number of epochs affects the trade-off between computational efficiency and the quality of the learned model.

## [[Regularisation]] Techniques

Prevent overfitting by penalizing large weights. Regularization is essential for improving the generalization of the model, ensuring it performs well on unseen data.

[[Ridge]]
[[Dropout]]
## Learning Rate Tuning

Learning rate impacts convergence. It is a [[hyperparameter]] that determines the step size during optimization. A poorly chosen learning rate can lead to divergence or slow convergence.

Techniques:
- [[Learning Rate]] Scheduling: Reduce learning rate as training progresses to fine-tune the learning process.
- Adaptive Learning Rates: Optimizers [[Optimisation techniques]]