---
tags:
  - ml
---


Split data into training and testing sets.
Train the model on the training set.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
```

adjusting the model [[hyperparameter]] to minimize the difference between predicted and actual class labels.





