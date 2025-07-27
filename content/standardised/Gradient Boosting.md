---
aliases: []
category:
date modified: 27-07-2025
tags: [ml_optimisation]
---
Gradient Boosting is a technique used for building predictive models [[Model Building]], particularly in tasks like regression and classification. It combines the concepts of [[Boosting]] and [[Gradient Descent]] to create strong models by sequentially combining multiple [[Weak Learners]] ([[Decision Tree]]. 

Key Idea: Instead of fitting a single strong model, Gradient Boosting builds multiple weak learners sequentially. Each new model focuses on ==correcting the mistakes made by the previous ones== by fitting to the residuals (differences between observed and predicted values).

Gradient Boosting builds an ensemble of [[Weak Learners]] (usually [[Decision Tree]]) sequentially. Each new model focuses on the errors of the previous ones, aiming to minimize the residual errors.

Final Prediction: The final prediction is made by aggregating the predictions of all the weak models, usually through a weighted sum.

High Performance: Known for its high performance and efficiency in terms of speed and memory usage.

[Watch Video Explanation](https://www.youtube.com/watch?v=3CC4N4z3GJc)

[[Model Ensemble]]
### Key Components

- [[Weak Learners]]: Typically decision trees used in the ensemble.
- [[Loss Function]]: Measures how well the model fits the data.
- [[Learning Rate]]: Controls the contribution of each weak learner to the final model.

### Examples

- [[LightGBM]]
- [[XGBoost]]
- [[CatBoost]]
### Benefits

- Predictive Accuracy: Often outperforms other [[Machine Learning Algorithms]].
- Feature Handling: Effectively manages [[heterogeneous features]] and automatically selects relevant ones.
- [[Overfitting]]: Less prone to overfitting compared to other complex models.