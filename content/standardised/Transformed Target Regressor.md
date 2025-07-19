[[Scikit-Learn]]

The `TransformedTargetRegressor` is a utility class in `scikit-learn` that applies a transformation to the target values in a regression problem. This can be useful in several scenarios:

1. **Non-normal target distribution**: Many regression algorithms assume that the target variable is normally distributed. If your target variable has a skewed distribution, applying a transformation (like a [[log transformation]]) can help improve the performance of the model.
    
2. **Heteroscedasticity**: This is a situation where the variance of the error terms in a regression model is not constant. In such cases, applying a transformation to the target variable can help stabilize the variance and improve the model's performance.
    
3. **Non-linear relationships**: If the relationship between the predictors and the target variable is not linear, a transformation can help capture the non-linearity.
    

The `TransformedTargetRegressor` applies the transformation before training the model and automatically applies the inverse transformation when making predictions. This makes it easier to work with transformed target variables, as you don't have to manually apply the inverse transformation every time you want to make a prediction.