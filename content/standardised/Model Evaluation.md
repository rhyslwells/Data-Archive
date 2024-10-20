---
type: process
tags:
  - evaluation
  - ml
---
# Overview

Appropriate evaluation metrics are used based on the problem type (classification vs. regression).

==The aim is to improve accuracy but also to generalize and avoid biases== and [[Overfitting]].

- **Performance Assessment**: Models are evaluated on a testing set using metrics relevant to the problem type.
- **Generalization and Bias**: Evaluation includes assessing how well the model generalizes to new data and identifying any biases.

For categorical classifiers: [[Categorical metrics]]:  Use metrics such as accuracy, precision, recall, F1-score, and confusion matrix to evaluate performance.

For regression tasks: [[Regression metrics]]: Metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared (R²) are used.

[[Cross validation]] is a technique used to assess the performance of a model by splitting the data into multiple subsets for training and testing to
assesses performance and generalization. It helps detect [[Overfitting]], provides reliable performance estimates.
# Next step: [[Model Optimisation]]

