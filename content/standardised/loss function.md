---
aliases: []
category:
date modified: 1-08-2025
tags:
  - optimisation
---
A loss function is a key component in training machine learning models. It is closely related to the [[Cost Function]], error function, and [[objective function]], and serves as an important metric for [[Model Evaluation]].

#### Purpose
* Measure predictive accuracy:
  Quantifies the difference between predicted and actual values.
  In other words, it measures how well a model’s predictions match the true targets by assigning an error value to each prediction.
- Goal: To be minimized:
  During training, the primary objective is to minimize the loss function so that predictions become more accurate, even on unseen data.

#### Usage
* Training: Guides updates to [[Model Parameters]] during optimization (e.g., using [[Gradient Descent]]).
* Evaluation: Assesses how well the trained model performs on validation or test data.

#### Examples
* [[Mean Squared Error]] (MSE): Common in [[Regression]] tasks.
* [[Cross Entropy]] (Log Loss): Common in [[Classification]] tasks.

#### Related Notes
* [[Loss versus Cost function]]
* [[Model Optimisation]]
