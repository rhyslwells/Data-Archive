---
tags:
  - evaluation
  - ml
category:
---
A learning curve is a diagnostic plot that shows model performance (e.g., [[accuracy]] or error) on training and validation sets as a function of training set size. It helps assess ([[Model Selection]]) whether a model suffers from underfitting, overfitting, or has converged in performance.

Core Concepts:
- A learning curve plots model scores (typically training and validation) against the number of training samples. It reveals how the model generalizes as it is trained on more data.

Typical behaviours:

- [[Overfitting]] (small data): High training score, low validation score. Model memorizes training data but generalizes poorly.
- Underfitting (high bias): Both training and validation scores are low. Model is too simple for the data.
- Convergence: As the dataset grows, training and validation scores approach each other. Once convergence is reached, adding more data does not improve performance significantly.

Key Insight:
- If both curves flatten and are close together, the model has likely reached its capacity. In this case, increasing training data further will not help—you may need a more expressive model.

Implementation Example (scikit-learn):

```python
from sklearn.model_selection import learning_curve
train_sizes, train_scores, val_scores = learning_curve(estimator, X, y, cv=5)
```

Use this to plot performance curves and analyze model behavior as training size varies.

Use Cases:
- Diagnose model complexity
- Identify data limitations
- Support decisions on collecting more data vs. changing the model
