---
tags:
  - ml
---
## Description

- **Gradient Boosting**: All three frameworks utilize gradient boosting techniques to build strong predictive models by combining multiple weak learners sequentially.

[LINK](https://www.youtube.com/watch?v=3CC4N4z3GJc)

- Used for building predictive models, especially for tasks like regression and classification.
- Gradient boosting combines the concepts of [[Boosting]] and [[Gradient Descent]]. Instead of fitting a single strong model, it builds multiple [[weak learners]] sequentially, where each new model focuses on the mistakes made by the previous ones.
- The key idea is to fit a new model to the residuals (the differences between the observed and predicted values) of the previous model. This way, each new model learns ==to correct the errors of the ensemble.==
- The final prediction is made by aggregating the predictions of all the weak models, usually through a weighted sum.
- **High Performance**: Each framework is known for its high performance and efficiency in terms of speed and memory usage.
## **Key Components:**
   - [[weak learners]]
   - [[loss function]] 
   - [[learning rate]] 
## Examples

[[LightGBM]] (LGBM), [[XGBoost]] (XGM), and [[CatBoost]] (CAT) are three popular [[Gradient boosting]] frameworks widely used in machine learning competitions and real-world applications. 

## **Benefits:**
   - Gradient boosting often outperforms other [[machine learning algorithms]] in terms of predictive accuracy.
   - It handles [[heterogeneous features]] well and automatically selects relevant features.
   - It is less prone to [[Overfitting]] compared to other complex models.

## **Implementation:**
   - Popular libraries for gradient boosting include [[XGBoost]], LightGBM, and CatBoost.
## Q&A's

**Describe the working principles of [[Gradient boosting]].**;; Gradient boosting builds an ensemble of [[weak learners]] (usually [[Decision Tree]]) sequentially, with each new model focusing on the errors of the previous ones. It aims to minimize the residual errors.

## [[Gradient boosting]] for [[Regression]]

## [[Gradient boosting]] for [[Classification]]