---
aliases: []
category:
date modified: 27-07-2025
tags: [deep_learning, ml_optimisation, model_architecture]
---
Loss functions are used in training machine learning models. Also known as a [[cost function]], error function, or objective function. Serves as a metric for [[model evaluation]].

Purpose: ==Measure predictive accuracy==: Measures the difference between predicted and actual values. That is they measure how well a model's predictions match the actual target values by quantifying the error between the predicted output and the true output. 

Goal: ==To be minimized==: The primary goal during model training is to minimize this loss, improving accuracy of predictions on unseen data.

Used during training to adjust [[model parameters]] and during evaluation to assess model performance.

### Examples

- **[[Mean Squared Error]] (MSE)**: Commonly used for [[regression]] tasks.
- **[[Cross Entropy]]**: Often used for [[classification]] tasks.

Resources
- [Video Explanation](https://www.youtube.com/watch?v=-qT8fJTP3Ks)
- [[Loss versus Cost function]]
