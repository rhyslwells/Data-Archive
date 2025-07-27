---
aliases: []
category: 
date modified: 27-07-2025
tags: []
---


Python Outlier Detection library, covers many algorithms (tabular, numeric).

| PyOD - Ensembles    | Combines multiple detectors — if a point scores high across methods, it is more confidently an outlier. |
| :------------------ | :------------------------------------------------------------------------------------------------------ |

```python
# Step 1: Import libraries
from pyod.models.iforest import IForest  # Isolation Forest from PyOD
from pyod.utils.data import generate_data
from sklearn.model_selection import train_test_split

# Step 2: Generate synthetic data (normal + outliers)
X, y = generate_data(n_train=200, n_test=100, n_features=2, contamination=0.1)

# Step 3: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Initialize detector
clf = IForest(contamination=0.1)  # 'contamination' = expected proportion of outliers

# Step 5: Train model
clf.fit(X_train)

# Step 6: Predict anomalies
y_train_pred = clf.labels_    # 0 = normal, 1 = outlier
y_train_scores = clf.decision_scores_  # raw outlier scores

y_test_pred = clf.predict(X_test)      # predict on unseen test set
y_test_scores = clf.decision_function(X_test)  # outlier scores for test

# Step 7: Evaluate (basic accuracy example)
from sklearn.metrics import classification_report

print(classification_report(y_test, y_test_pred))

```