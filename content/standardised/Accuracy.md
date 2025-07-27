---
aliases: []
category:
date modified: 27-07-2025
tags: [evaluation]
---
## Definition

- Accuracy Score is the proportion of correct predictions out of all predictions made. In other words, it is the percentage of correct predictions.
- Accuracy can have issues with [[Imbalanced Datasets]]where there is more of one class than another.

## Formula

- The formula for accuracy is:
  $$\text{Accuracy} = \frac{TN + TP}{\text{Total}}$$
In the context of [[Classification]] problems, particularly binary classification, TN and TP are components of the confusion matrix:

- TP (True Positive): The number of instances that are correctly predicted as the positive class. For example, if the model predicts a positive outcome and it is indeed positive, it counts as a true positive.
- TN (True Negative): The number of instances that are correctly predicted as the negative class. For example, if the model predicts a negative outcome and it is indeed negative, it counts as a true negative.

The [[Confusion Matrix]] also includes:

- FP (False Positive): The number of instances that are incorrectly predicted as the positive class. This is also known as a "Type I error."
- FN (False Negative): The number of instances that are incorrectly predicted as the negative class. This is also known as a "Type II error."

These metrics are used to evaluate the performance of a classification model, providing insights into not just accuracy but also precision, recall, and other performance measures.
## Exploring Accuracy in Python

To explore accuracy in Python, you can use libraries such as `scikit-learn`, which provides the `accuracy_score` function. This function compares the predicted labels with the true labels and calculates the accuracy.

### Example Usage

```python
from sklearn.metrics import accuracy_score
# Assuming pred and y_test are defined
accuracy = accuracy_score(y_test, pred)
print("Prediction accuracy: {:.2f}%".format(accuracy  100.0))
```

- Make sure to replace `pred` and `y_test` with your actual prediction and test data variables.