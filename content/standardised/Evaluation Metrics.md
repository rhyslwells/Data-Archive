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

## Evaluation metrics in practice

Having many evaluation metrics is hard to understand and optimise. Best to combine into one.

Use a single number i.e. accuracy or [[F1 Score]] . 

This speeds up development of ml projects.

In order to use metrics to evaluate a model we can:
- Can combine multiple metrics a formula, i.e. weighted average.
- If there is a metrics we are happy that the model passes a given level then we can have it "==Satisfying==". So the for the given metric it just needs to pass a given level.
- For metrics we are interested in we have it "==Optimising==", the one we want to be the best.
- Setup: Pick N-1 satisfying and 1 optimising.

![[Pasted image 20241217073706.png|500]]




