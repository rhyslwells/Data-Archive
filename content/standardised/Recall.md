---
tags:
  - evaluation
---
- **Recall Score** is a metric used to evaluate the performance of a [[Classification]] model, specifically focusing on the model's ability to ==identify all relevant instances of the positive class.==
- It is defined as the proportion of true positive predictions among all actual positive instances.
- [[Classification Report]] & [[Precision or Recall]]
- The formula for recall is:
  $$\text{Recall} = \frac{TP}{TP + FN}$$
  where:
  - **TP (True Positives):** The number of correctly predicted positive instances.
  - **FN (False Negatives):** The number of actual positive instances that were incorrectly predicted as negative.

## Importance

- Recall is crucial in scenarios ==where missing a positive instance is costly==, such as in disease screening or fraud detection.
- It helps in understanding how well the model captures all the actual positive instances.

## Implementing Recall Score in Python

You can calculate the recall score in Python using the `scikit-learn` library, which provides a convenient function for this purpose.

### Example Usage

```python
from sklearn.metrics import recall_score

# Sample true labels and predicted labels
y_true = [0, 1, 1, 0, 1, 0, 1, 1]
y_pred = [0, 1, 0, 0, 1, 1, 1, 1]

# Calculate recall score
recall = recall_score(y_true, y_pred)

print("Recall Score: {:.2f}".format(recall))
```

- The `recall_score` function can handle binary and multiclass classification problems. For multiclass, you can specify the `average` parameter to determine how to calculate the recall (e.g., `average='macro'`, `average='micro'`, or `average='weighted'`).
