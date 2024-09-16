Task: For each model as we tune the hyperparameters what happens to the (RMSLE) metric (scatter metric against hyperparameter).  

Using **Root Mean Squared Logarithmic Error** RMSLE to evaluate.

Practice with model and feature engineering ideas, create visualizations

- [ ] create eda for blog post
- [ ] create model training optuna for blog post



----
Questions 

Why show the [[feature importance]]? 
- help in understanding which features are most influential in making predictions.
- [[Interpretation]]
- Compare between different models [[Model Selection]], to see which features are prefered by the model - to understand the algo better. For example, decision trees might prioritize features differently than linear models or neural networks.
- Shows feature relevance over different models.
## notes:

[[outliers]]
Why use isolation forest ([[Random Forests]]) for [[outliers]] detection? 

[[How to pick the best hyperparameters]]
[[hyperparameter]] tuning can be done with [[hyperparameter optuna]]

[[Cross validation]]
Both (sklearn)[`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) and [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html) can be very effective when used on classification problems with a severe class imbalance. They both _stratify_ the sampling by the class label; that is, they split the dataset in such a way that preserves approximately the same class distribution (i.e., the same percentage of samples of each class) in each subset/fold as in the original dataset. However, a single run of `StratifiedKFold` might result in a noisy estimate of the model's performance, as different splits of the data might result in very different results. That is where `RepeatedStratifiedKFold` comes into play.

`RepeatedStratifiedKFold` allows improving the estimated performance of a machine learning model, by simply repeating the [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) procedure multiple times (according to the `n_repeats` value), and reporting the _mean_ result across all folds from all runs. This _mean_ result is expected to be a more accurate estimate of the model's performance

## Notes:



### [[TransformedTargetRegressor]]

The `TransformedTargetRegressor` is a utility class in `scikit-learn` that applies a transformation to the target values in a regression problem. This can be useful in several scenarios:

1. **Non-normal target distribution**: Many regression algorithms assume that the target variable is normally distributed. If your target variable has a skewed distribution, applying a transformation (like a log transformation) can help improve the performance of the model.
    
2. **Heteroscedasticity**: This is a situation where the variance of the error terms in a regression model is not constant. In such cases, applying a transformation to the target variable can help stabilize the variance and improve the model's performance.
    
3. **Non-linear relationships**: If the relationship between the predictors and the target variable is not linear, a transformation can help capture the non-linearity.
    

The `TransformedTargetRegressor` applies the transformation before training the model and automatically applies the inverse transformation when making predictions. This makes it easier to work with transformed target variables, as you don't have to manually apply the inverse transformation every time you want to make a prediction.