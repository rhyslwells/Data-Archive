---
tags: 
aliases: 
category:
---
Weak learners are simple models that perform slightly better than random guessing. They are often used as the building blocks in [[Model Ensemble]] methods to create a strong predictive model.

## Characteristics

- **Simplicity:** Weak learners are typically simple models, such as [[Decision Tree]] stumps, which split the data based on a single feature.
- **Performance:** Individually, they may not perform well, but when combined, they can produce a powerful ensemble model.

## Role in Model Ensembling

Weak learners are a crucial component of [[Model Ensemble]] techniques, such as boosting and bagging, where multiple weak learners are combined to improve overall model performance.

## Learning Rate

- The [[Learning Rate]] is a [[Hyperparameter]]that controls the contribution of each weak learner to the final ensemble model.
- A smaller learning rate means that each weak learner has a smaller impact, often requiring more learners to achieve good performance.
