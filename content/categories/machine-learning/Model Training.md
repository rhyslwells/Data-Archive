---
aliases: []
category: ML
date modified: 24-02-2026
tags:
  - ml
  - ml_process
  - optimisation
  - training
---
Model training is the numerical [[Model Optimisation]] procedure that adjusts a model’s parameters ([[Model Parameters]]) so that its predictions approximate a target function with respect to observed data.

More formally:

Given:

* A dataset $\mathcal{D} = {(x_i, y_i)}_{i=1}^n$
* A parametric model $f(x; \theta)$
* A loss function $\mathcal{L}(y, \hat{y})$

Training solves (explicitly or approximately):

$$
\theta^* = \arg\min_{\theta} \frac{1}{n} \sum_{i=1}^{n} \mathcal{L}(y_i, f(x_i; \theta))
$$

The outcome is an estimate $\theta^*$ that minimises empirical risk.

---

## What Actually Changes During Training

Training modifies **model parameters**:

* Linear regression: weights $w$ and bias $b$
* Neural networks: weight matrices and bias vectors
* Tree-based models: split thresholds and structure
* SVM: support vectors and margin parameters

The structure of the model is fixed beforehand. Training does not change the model class, only its parameter values.

---

## Core Components

### 1. Forward Pass

Compute predictions:
$$
\hat{y}_i = f(x_i; \theta)
$$

### 2. Loss Computation

Measure discrepancy between prediction and target:

* Regression: $\mathcal{L} = (y - \hat{y})^2$
* Classification: cross-entropy
* Others: hinge loss, MAE, etc.

### 3. Optimisation Step

Update parameters using an optimisation algorithm:

$$
\theta \leftarrow \theta - \eta \nabla_\theta \mathcal{L}
$$

Where:

* $\eta$ = learning rate
* $\nabla_\theta \mathcal{L}$ = gradient of loss

This is typically stochastic gradient descent (SGD) or a variant (Adam, RMSProp).

---

## What Training Achieves

Training attempts to:

* Learn the mapping $x \mapsto y$
* Reduce empirical error
* Capture statistical structure in the data
* Generalise to unseen data

The final model encodes patterns from the training data into parameter values.

---

## Conceptual View

Training is:

* An optimisation problem (minimise loss)
* A statistical estimation problem (estimate parameters)
* A numerical procedure (iterative updates)
* A representation learning process (in deep learning)

---

## Important Distinctions

Training is not:

* Evaluation (that happens on [[Validation]]/test sets)
* Feature engineering (done before training)
* Hyperparameter tuning (outer loop optimisation)
* Inference (using the trained model for prediction)

---

## Example

Linear regression:

Model:
$$
\hat{y} = w x + b
$$

Loss:
$$
\mathcal{L} = (y - \hat{y})^2
$$

Training computes optimal $w^*, b^*$ that minimise squared error across the dataset.

After training, prediction is just:

$$
\hat{y}*{new} = w^* x*{new} + b^*
$$
