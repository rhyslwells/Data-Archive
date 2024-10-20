---
tags:
  - ml
  - deep_learning
  - model
---

A Loss functions guides model training by providing a measure of prediction accuracy. The ultimate aim is to ==minimize the loss==, ensuring the model makes accurate predictions on unseen data.
### Terminology

- **Loss Function**: Also referred to as a ==cost function, error function, or objective function==. It is a component in training machine learning models.

- **[[Reward Function]]**: Mentioned as the opposite of a cost function, typically used in reinforcement learning to indicate the desirability of an outcome.

### Description

- **Purpose**: A loss function quantifies how well a model's predictions align with the actual target values. It serves as a guide for the optimization process during model training.

- **Minimization**: The ==primary goal is to minimize the loss function==, which indicates that the model's predictions are becoming more accurate.

- **[[Overfitting]]**: The note hints at the relationship between loss functions and overfitting. A model that fits the training data too well (low training loss) might not generalize to new data, leading to overfitting.

### Examples

- **Types of Problems**: The note suggests that different types of problems (e.g., regression, classification) use different loss functions. For instance, cross entropy is commonly used for classification tasks.

### Evaluation

- **Disparity Measurement**: The loss function measures the difference between predicted and actual values, providing a metric for model evaluation.

- **Training and Evaluation**: Loss functions are used both during training (to adjust model parameters) and evaluation (to assess model performance).


#### Resources
[LINK](https://www.youtube.com/watch?v=-qT8fJTP3Ks)
