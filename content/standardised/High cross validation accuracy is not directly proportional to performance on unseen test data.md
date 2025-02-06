Reasons a Model with High [[Cross Validation]] Accuracy May Perform Poorly on Unseen Test Data

[[Data Leakage]]: 
  - Information from test folds leaks into training, inflating CV accuracy.
  - Solution: Apply [[preprocessing]] independently within each CV fold.

Overfitting: 
  - Model captures noise in training data, leading to high CV but low test accuracy.
  - Solution: Use simpler models, regularization, and evaluate test performance during [[hyperparameter tuning]].

Insufficient Cross-Validation Folds: 
  - Too few folds lead to high variance in performance estimates.
  - Solution: Use more folds (e.g., 5- or 10-fold CV) for reliable estimates.

Over-Optimized Hyperparameters: 
  - Excessive tuning results in models that fail to generalize.
  - Solution: Reserve a separate validation set for tuning and use nested cross-validation.

Small Dataset Size: 
  - Small datasets may lead to unreliable accuracy estimates.
  - Solution: Use bootstrapping or collect more data if possible.

Inappropriate Performance Metric: 
  - CV accuracy may not align with the true objective (e.g., [[imbalanced datasets]]).
  - Solution: Choose appropriate [[Evaluation Metrics]]  based on the problem context.

### Practical Recommendations
- Evaluate the model on a completely independent test set after cross-validation.
- Check for [[Distributions|distribution]] differences between training and test data.
- Avoid data leakage by ensuring strict separation of preprocessing in CV folds.
