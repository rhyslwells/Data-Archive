Task: For each model as we tune the hyperparameters what happens to the (RMSLE) metric (scatter metric against hyperparameter).  

Using **Root Mean Squared Logarithmic Error** RMSLE to evaluate.

Practice with model and feature engineering ideas, create visualizations

- [ ] create eda for blog post
- [ ] create model training optuna for blog post



----
Questions 


[[Hyperparameter]]
[[Hyperparameter]] tuning can be done with [[Hyperparameter]]

[[Cross Validation]]
Both (sklearn)[`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) and [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html) can be very effective when used on classification problems with a severe class imbalance. They both _stratify_ the sampling by the class label; that is, they split the dataset in such a way that preserves approximately the same class distribution (i.e., the same percentage of samples of each class) in each subset/fold as in the original dataset. However, a single run of `StratifiedKFold` might result in a noisy estimate of the model's performance, as different splits of the data might result in very different results. That is where `RepeatedStratifiedKFold` comes into play.

`RepeatedStratifiedKFold` allows improving the estimated performance of a machine learning model, by simply repeating the [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) procedure multiple times (according to the `n_repeats` value), and reporting the _mean_ result across all folds from all runs. This _mean_ result is expected to be a more accurate estimate of the model's performance
