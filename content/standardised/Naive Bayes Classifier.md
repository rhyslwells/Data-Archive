---
aliases: []
category: ML
date modified: 23-08-2025
projects:
tags:
  - analysis
  - classifer
  - ml
  - NLP
  - probability
---
A probabilistic classifier based on Bayes’ theorem, assuming that features are conditionally independent given the class. This assumption is why it’s called “naive.”

Bayes’ theorem:

$$
P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
$$

where:

* $P(A|B)$ = Posterior probability
* $P(B|A)$ = Likelihood
* $P(A)$ = Prior probability
* $P(B)$ = Evidence

When to use:
* Text classification (spam detection, sentiment analysis).
* ==Problems with many independent features.==
### Why Naive Bayes?

Assumes features are independent, which is rarely true, but works surprisingly well in practice.

* Simple, fast, and works well for high-dimensional data (e.g., [[Text Classification]]).
* Treats data as a ==bag of features== (order doesn’t matter).
* Handles categorical and numeric data (with assumptions):
	- Categorical: Works directly or via encoding.
	- Numeric: Assumes normal distribution (Gaussian NB).

Advantages:
* Scales well to large datasets.
* Requires small amount of training data.
* Effective for text and document classification.

Smoothing Issue:
- To avoid zero probabilities (when a feature value was not seen in training), we add a small value $\alpha$ (Laplace smoothing).

### Types of Naive Bayes

* BernoulliNB: For binary features (e.g., word presence/absence).
* MultinomialNB: For count-based features (e.g., word counts in text).
* GaussianNB: For continuous features (assumes Gaussian distribution).

### Example

```python
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB(alpha=1.0)  # Laplace smoothing
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

