---
aliases: []
category: ML
date modified: 27-09-2025
tags: []
---
Variance measures how much a model’s predictions change when trained on different subsets of the training data. It reflects the model’s sensitivity to the specific data used for training.

#### High Variance

* The model is too sensitive to the training data.
* Captures noise as well as signal; poor generalization.
* Symptom: Good performance on training data, poor performance on test data (overfitting).
#### Bias–Variance Context

* Variance = Error due to instability in the model (changes drastically with small variations in training data).
* High flexibility; higher variance.
* Low variance models = more stable but less flexible.

#### Intuition

If you slightly change the training data and the predictions change a lot; high variance.
If predictions remain almost the same; low variance.

#### Key Point

Variance is about model sensitivity and stability:

$$
\text{High Variance} \implies \text{Overfitting}, \quad \text{Low Variance} \implies \text{More stable but risk of underfitting}.
$$
Related:
- [[Bias in ML]]
- [[Bias-Variance Trade Off]]