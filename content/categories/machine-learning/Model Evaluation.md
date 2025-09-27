---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- evaluation
- modeling
type: process
---
Assess the model's performance using various metrics to ensure it meets the desired accuracy and reliability.

Appropriate evaluation metrics are used based on the problem type (classification vs. regression), to assess how well the model predicts.

==The aim is to improve accuracy but also to generalize and avoid biases== and [[Overfitting]].

- **Performance Assessment**: Models are evaluated on a testing set using metrics relevant to the problem type.
- **Generalization and Bias**: Evaluation includes assessing how well the model generalizes to new data and identifying any biases.

For categorical classifiers: [[Evaluation Metrics]]: Use metrics such as accuracy, precision, recall, F1-score, and confusion matrix to evaluate performance.

For regression tasks: [[Regression Metrics]]: Metrics like [[Mean Absolute Error]] (MAE), Mean Squared Error (MSE), [[Root Mean Squared Error]] (RMSE), and R-squared (R²) are used.

[[Cross Validation]] is a technique used to assess the performance of a model by splitting the data into multiple subsets for training and testing to assesses performance and generalization. It helps detect [[Overfitting]], provides reliable performance estimates.

[[Feature Importance]]: After training, analyze which features have the most significant impact on the model's predictions.

Related:
- [[Test Loss When Evaluating Models]]