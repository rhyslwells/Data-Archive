---
tags:
  - ml
---
## Description

[[Cross validation]]
## Terms

[Link to good website describing these](https://txt.cohere.com/classification-eval-metrics/)
[[Confusion matrix]]

[[Accuracy score]]
[[Precision score]]
[[Recall score]]
[[Precision or Recall]]
[[F1 Score]]
## Implementation

```python
## om sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
```

**Can you mention some of the most common metrics used to evaluate binary classifiers and some [[Categorical metrics]]?**;;[[Sensitivity]],[[Specificity]],[[Recall score]],[[Precision score]],[[Accuracy score]],[[F1 Score]].

** How are precision and recall in binary classification, related?**;; They are related through a trade-off: increasing one may decrease the other. 

**What matrix can you use to evaluate the performance of a classifier? How does an ideal matrix look like?**;; The [[Confusion matrix]]