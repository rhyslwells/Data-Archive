## Description

Adds a ==penalty==.

[LINK](https://www.youtube.com/watch?v=Q81RR3yKn30)

Given a [[Linear Regression]] example with a line fitted using using [[least squares]] ([[Ordinary Least Squares]]).

If we have a [[Overfitting]] line, we can correct it by making fitted line slightly bad to make the model better.

**L2 Regularization (Ridge)**: L2 regularization adds a penalty term proportional to the square of the weights to the loss function. This encourages smaller weights overall and tends to distribute the weight values more evenly across all features.

lambda - 0 to infinity (is the scaler which is the penalty.) 

How to find the best $\lambda$? Try a bunch and use [[Cross validation]] and pick the one with the lowest [[variance]]

Also works for discrete data

Can be applied to [[Logistic Regression]].

- Adds a penalty term proportional to the ==square of the model's coefficients.==
- Encourages smaller coefficient values overall.
- Does not drive coefficients to exactly zero, but rather reduces their magnitude.
- Useful for reducing the impact of multicollinearity (high correlation between features) by shrinking the coefficients of correlated features.
- Tends to ==retain all features==, but with reduced magnitudes.