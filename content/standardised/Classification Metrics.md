---
tags:
  - code_snippet
  - evaluation
---
## Description

[[Confusion Matrix]]
[[Accuracy]]
[[Precision]]
[[Recall]]
[[Precision or Recall]]
[[F1 Score]]
[[Sensitivity]]
[[Specificity]]

Resources:
[Link to good website describing these](https://txt.cohere.com/classification-eval-metrics/)
## Code snippet

```python
## om sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
```



