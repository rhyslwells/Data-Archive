---
aliases: []
category: ML
date modified: 2-11-2025
tags:
  - ml
---
### **Robustness and Testing**

**Why it matters:**
Model performance can vary due to randomness in initialization, sampling, or feature selection. Testing robustness involves checking whether results remain stable across different random seeds or random states.

**Scikit-learn resources:**

* [Glossary: random_state](https://scikit-learn.org/dev/glossary.html#term-random_state)
* [Common Pitfalls: Randomness](https://scikit-learn.org/dev/common_pitfalls.html#randomness)

**Definition:**

* `random_state` controls the source of randomness.
* An *integer* seed (e.g. 0, 42) ensures full reproducibility — the same pseudo-random sequence is used every time.
* A `RandomState` instance generates new random numbers each time, providing variability between model fits or folds.
* Integer values must be within $[0, 2^{32} - 1]$.

**Example:**

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
import numpy as np

X, y = make_classification(random_state=0)

rf_int = RandomForestClassifier(random_state=123)
rf_rng = RandomForestClassifier(random_state=np.random.RandomState(0))

cross_val_score(rf_int, X, y)
# same RNG across folds → identical randomness

cross_val_score(rf_rng, X, y)
# new RNG per fold → variable randomness
```

**Explanation:**

* With an **integer seed**, each fold in [[Cross Validation]] reuses the same RNG. This means the random subset of features or samples in each fold is identical, possibly overestimating model stability.
* With a **RandomState instance**, each fold starts from a fresh RNG, leading to more realistic variability in performance.

**Recommendation:**
For robustness testing, evaluate model sensitivity across several distinct seeds or by passing a `RandomState` instance. This helps ensure that observed performance is not dependent on one random configuration.

**Diagnostic approach:**
Plot accuracy (or another metric) against the number of estimators and different seeds to identify:

* The minimum ensemble size required for stable accuracy.
* A performance plateau where adding estimators no longer improves results.