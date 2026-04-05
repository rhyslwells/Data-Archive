---
aliases: []
category:
date modified: 27-03-2026
tags: [evaluation, ml, ml_process, term]
---
In machine learning, **validation** refers to the process of evaluating a model on data that was **not used during training**, in order to guide model development.

More precisely:

* You split your data into at least two parts:
  * **Training set**: used to fit the [[model parameters]]
  * **Validation set**: used to assess model performance during development

The validation set is used to:

1. **Tune hyperparameters**
   For example, choosing:
   * [[regularisation]] strength $\lambda$
   * tree depth in a random forest
   * learning rate in gradient methods ([[Learning Rate]])

   You train multiple models with different settings and select the one with the best validation performance.

2. **Select models**: Compare different model classes (e.g., linear regression vs. gradient boosting) using the same validation set.

3. **Detect overfitting**: If training performance improves but validation performance degrades, the model is fitting noise rather than signal.
### Formal view

Let:

* $D = {(x_i, y_i)}_{i=1}^n$ be the dataset
* Split into $D_{\text{train}}$ and $D_{\text{val}}$
* and $l$ be the loss fucntion
* $l(f_\theta(x),y)$=error between prediction and truth

Train a model:

$$f_\theta \leftarrow \text{fit}(D_{\text{train}})
$$

Evaluate on validation:

$$
\text{ValError} = \frac{1}{|D_{\text{val}}|} \sum_{(x,y)\in D_{\text{val}}} \ell(f_\theta(x), y)
$$

This approximates how well the model generalises to unseen data.

### Distinction from test data

* **Validation set**: used repeatedly during development
* **Test set**: used once at the end for an unbiased estimate

Repeated use of validation data introduces bias [[Bias in ML]], which is why a separate test set is needed.

### Common extensions

1. [[Cross Validation]]
   Instead of a single split, partition data into $k$ folds and rotate the validation set:
$$  \text{CV error} = \frac{1}{k} \sum_{j=1}^k \text{error}_j$$

2. **Time series validation**
   Use ordered splits (e.g., train on past, validate on future) rather than random splits.

### Simple example

* Train a model on 80% of the data
* Evaluate accuracy on the remaining 20%
* Adjust hyperparameters and repeat until performance stabilises

Future questions:

* [ ] how validation interacts with **[[model selection]] bias**

Related:
- [[Train-Dev-Test Sets]]