---
tags:
  - ml_optimisation
---

Split data into training and testing sets.

Train the model on the training set.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(inputs,target,test_size=0.3)
```

### 4. Train-Test Split
   - Objective: Split your data into training and testing sets. The model will be trained on the training data and evaluated on the test data.
   - Typical Split: 70-80% training data, 20-30% testing data.
   - Term: #evaluation

   ```python
   from sklearn.model_selection import train_test_split
   
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)