---
tags:
  - metric
---



```python
# Evaluation
accuracy = accuracy_score(pred, y_test)
print("Prediction accuracy: {}%".format(accuracy * 100.0))
```

- **Dwefinition:** The proportion of correct predictions out of all predictions made.
- That is, the percentage of correct predictions.
- Can have issues with imbalanced data sets. more of one thing than another.
- $$TN + TP/ All=accurary$$