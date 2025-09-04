---
aliases: []
category:
date modified: 1-08-2025
tags: ["#evaluation"]
type: 
---
Cross-validation is a statistical technique used in machine learning to ==assess how well a model will generalize== to an independent dataset. It is a crucial step in the model-building process because it helps ensure that the model is not [[overfitting]] or underfitting the training data.

- Cross-validation is a technique used in machine learning and statistics to evaluate the performance ([[Model Optimisation]]) of a predictive model.
- It provides a robust evaluation by splitting the training data into smaller chunks and training the model multiple times.
- K-Fold Cross-Validation: Involves dividing the dataset into (k) equal-sized subsets (called "folds") and using each fold as a validation set once, while the remaining (k-1) folds are used for training.
- The model's performance is averaged across all (k) folds to provide a more robust estimate of its generalization performance.
### Common Variations

- K-Fold Cross-Validation: The most common method, where the data is split into (k) folds and the model is trained (k) times, each time using a different fold as the validation set.
- Stratified K-Fold: Ensures each fold has a similar proportion of class labels, important for imbalanced datasets.
- Repeated K-Fold: Repeats the process multiple times with different random splits for more robust results.
- Leave-One-Out Cross-Validation (LOOCV): Each data point is used once as a test set while the rest serve as the training set.

### How Cross-Validation Fits into Building a Machine Learning Model

1. [[Model Evaluation]]: Used to evaluate the performance of different models or algorithms to choose the best one.
2. [[Hyperparameter]] Tuning: Provides a reliable performance metric for each set of hyperparameters.
3. [[Model Validation]]: Ensures consistent performance across different subsets of data.
4. [[Bias in ML]] tradeoff: Helps in understanding the tradeoff between bias and variance, guiding the choice of model complexity.

Advantages:
- Reduced Bias: Offers a more reliable performance estimate compared to using a single validation set.
- Efficient Data Use: All data is used for both training and validation.
- Prevents Overfitting: By evaluating on multiple folds, it can detect if the model is overfitting to the training data.
### Choosing (k)

- Common values: 5 or 10
- Higher (k) leads to more accurate estimates but increases computation time.
- Consider dataset size and complexity when choosing (k).

### Code Implementation

In [[ML_Tools]] see:
- [[KFold_Cross_Validation.py]]

### Cross-Validation Strategy in [[Time Series]]

All notebooks use cross-validation based on `TimeSeriesSplit` to ensure proper evaluation of performance with no [[Data Leakage]]. This method ensures that training and test data are split while maintaining the chronological order of the data.

### Related

[[Learning Curve]]

[[Cross Validation]]
Both (sklearn)[`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) and [`RepeatedStratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedStratifiedKFold.html) can be very effective when used on classification problems with a severe class imbalance. They both _stratify_ the sampling by the class label; that is, they split the dataset in such a way that preserves approximately the same class distribution (i.e., the same percentage of samples of each class) in each subset/fold as in the original dataset. However, a single run of `StratifiedKFold` might result in a noisy estimate of the model's performance, as different splits of the data might result in very different results. That is where `RepeatedStratifiedKFold` comes into play.

`RepeatedStratifiedKFold` allows improving the estimated performance of a machine learning model, by simply repeating the [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) procedure multiple times (according to the `n_repeats` value), and reporting the _mean_ result across all folds from all runs. This _mean_ result is expected to be a more accurate estimate of the model's performance