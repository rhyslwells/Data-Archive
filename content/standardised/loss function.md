---
aliases: []
category:
date modified: 1-08-2025
tags: [architecture, deep_learning, optimisation]
---
Loss functions are used in training machine learning models. Also known as a [[Cost Function]], error function, or objective function. Serves as a metric for [[Model Evaluation]].

Purpose: ==Measure predictive accuracy==: Measures the difference between predicted and actual values. That is they measure how well a model's predictions match the actual target values by quantifying the error between the predicted output and the true output. 

Goal: ==To be minimized==: The primary goal during model training is to minimize this loss, improving accuracy of predictions on unseen data.

Used during training to adjust [[Model Parameters]] and during evaluation to assess model performance.

### Examples

- **[[Mean Squared Error]] (MSE)**: Commonly used for [[Regression]] tasks.
- **[[Cross Entropy]]**: Often used for [[Classification]] tasks.

Resources
- [Video Explanation](https://www.youtube.com/watch?v=-qT8fJTP3Ks)
- [[Loss versus Cost function]]
