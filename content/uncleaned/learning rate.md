---
tags:
  - ml
---


This controls the contribution of each [[weak learners]] to the final ensemble. A lower learning rate makes the ==model more robust but requires more iterations==.

## Description

The learning rate is a [[hyperparameter]] that determines the ==step size at which the model parameters are updated during training.== :
## **Parameter Updates:**
   - During the training of a machine learning model, such as [[What is a neural network]] or gradient-based algorithms like [[Gradient Descent]], the model's parameters (weights and biases) are adjusted iteratively to minimize the [[loss function]].
   - A high learning rate means larger steps, which can lead to faster convergence but may overshoot the minimum.
   - A low learning rate means smaller steps, which can ensure stability and accuracy but may result in slow convergence or getting stuck in local minima.
## **Impact:**
   - Learning rate greatly influences the training process and the performance of the model.
   - It affects how quickly the model learns and how accurately it converges to the best solution.
   - Choosing an appropriate learning rate is crucial for achieving optimal performance and avoiding issues like slow convergence, oscillations, or divergence.
## **Tuning:**
   - The learning rate is a [[hyperparameter]] that needs to be tuned during the model training process.
   - Typically, it's adjusted along with other hyperparameters through techniques like [[How to pick the best hyperparameters]] .
   - Value depends on factors like the dataset, the complexity of the model, and the optimization algorithm used.
