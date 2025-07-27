---
aliases: []
category: 
date modified: 27-07-2025
tags: [evaluation]
---
**AUC (Area Under the Curve)** is a metric for binary classification problems, representing the area under the [[ROC (Receiver Operating Characteristic)]]

#### Key Concepts
Represents the area under the ROC curve.

AUC values range from 0 to 1, where 1 indicates perfect classification and 0.5 suggests no discriminative power (equivalent to random guessing).

#### Roc and Auc Score

The `roc_auc_score` is a function from the `sklearn.metrics` module in Python that computes the Area Under the Receiver Operating Characteristic Curve (ROC AUC) from prediction scores. It is a widely used metric for evaluating the performance of binary classification models.

Key Points about `roc_auc_score`:

- **Purpose**: It quantifies the overall ability of the model to discriminate between the positive and negative classes across all possible classification thresholds.
- **Range**: The score ranges from 0 to 1, where:
    - 1 indicates perfect discrimination (the model perfectly distinguishes between the positive and negative classes).
    - 0.5 suggests no discriminative power (equivalent to random guessing).
    - Values below 0.5 indicate a model that performs worse than random guessing.
- **Input**: The function takes the true binary labels and the predicted probabilities (or decision function scores) as inputs.
- **Output**: It returns a single scalar value representing the AUC.

#### Example Code

```python
from sklearn.metrics import roc_auc_score

# Actual and predicted values
y_act = [1, 0, 1, 1, 0]
y_pred = [1, 1, 0, 1, 0]

# Compute AUC
auc = roc_auc_score(y_act, y_pred)
print(f'AUC: {auc}')
```