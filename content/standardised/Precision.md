---
tags:
  - evaluation
aliases: 
category:
---
- **Precision Score** is a metric used to evaluate the [[Accuracy]] of a [[Classification]] model, specifically focusing on the positive class.
- It is defined as the proportion of true positive predictions among all positive predictions made by the model.
- [[Classification Report]] & [[Precision or Recall]]
- The formula for precision is:
  $$\text{Precision} = \frac{TP}{TP + FP}$$
  where:
  - **TP (True Positives):** The number of correctly predicted positive instances.
  - **FP (False Positives):** The number of instances incorrectly predicted as positive.

Importance:

- Precision is crucial in scenarios where the ==cost of false positives is high==, such as in spam detection or medical diagnosis.
- It helps in understanding how many of the predicted positive instances are actually positive.

## Implementing Precision Score in Python

You can calculate the precision score in Python using the `scikit-learn` library, which provides a convenient function for this purpose.

### Example Usage

```python
from sklearn.metrics import precision_score

# Sample true labels and predicted labels
y_true = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 1, 1, 1]

# Calculate precision score
precision = precision_score(y_true, y_pred)

print("Precision Score: {:.2f}".format(precision))
```

- The `precision_score` function can handle binary and multiclass classification problems. For multiclass, you can specify the `average` parameter to determine how to calculate the precision (e.g., `average='macro'`, `average='micro'`, or `average='weighted'`).
