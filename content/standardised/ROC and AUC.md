---
type: term
tags:
  - evaluation
---
ROC (Receiver Operating Characteristic) and AUC (Area Under the Curve) are essential tools for evaluating the performance of binary classifiers. They provide insights into the trade-offs between sensitivity (true positive rate) and specificity (1 - false positive rate) across various threshold levels.

The ROC curve is a graphical representation of a classifier's performance across different thresholds, showing the trade-off between sensitivity and specificity. The AUC score is a metric for binary classification problems, representing the area under the ROC curve.

#### Key Concepts

ROC Curve: 
  - A graphical plot that illustrates the diagnostic ability of a binary classifier system as its discrimination ==threshold== is varied.
  - It plots the true positive rate (TPR) against the false positive rate (FPR) at different threshold settings.

AUC:
  - Represents the area under the ROC curve.
  - AUC values range from 0 to 1, where 1 indicates perfect classification and 0.5 suggests no discriminative power (equivalent to random guessing).

#### Why Use Predicted Probabilities?

In ROC analysis, predicted probabilities (`y_probs`) are used instead of predicted classes (`y_pred`) because the ROC curve evaluates the model's performance across different threshold levels. Probabilities allow you to adjust the threshold to see how it affects sensitivity and specificity.

#### Threshold Level

The threshold level is the probability value above which an instance is classified as the positive class. Adjusting the threshold affects [[Sensitivity]] and [[Specificity]]:
  - Lower Threshold: Increases sensitivity but may decrease specificity.
  - Higher Threshold: Increases specificity but may decrease sensitivity.

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

### Code Implementation

#### Example Code

```python
from sklearn.metrics import roc_curve, roc_auc_score, RocCurveDisplay
import matplotlib.pyplot as plt

# Actual and predicted values
y_act = [1, 0, 1, 1, 0]
y_pred = [1, 1, 0, 1, 0]

# Compute ROC curve
fpr, tpr, thresholds = roc_curve(y_act, y_pred)

# Compute AUC
auc = roc_auc_score(y_act, y_pred)

# Display ROC curve and AUC
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=auc).plot()
plt.show()
```

#### [[Logistic Regression]] Example

```python
from sklearn.linear_model import LogisticRegression

# Train a logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Predict probabilities for the positive class
y_probs = logreg.predict_proba(X_test)[:, 1]

# Compute ROC curve and AUC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = roc_auc_score(y_test, y_probs)

# Plot ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='red', linestyle='--', lw=2, label='Random Guessing')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.legend()
plt.show()
```