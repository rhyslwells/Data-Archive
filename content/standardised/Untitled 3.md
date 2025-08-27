---
tags: 
category: 
---
#### 1. Generative Models

* Definition: Models the *joint probability distribution* $P(X, Y)$ of the input features $X$ and the label $Y$.
* Goal: Learn how data is generated so that you can:

  * Generate new samples
  * Compute likelihood of data
  * Predict $P(Y|X)$ using Bayes' rule
* Examples:
  * Naïve Bayes
  * Hidden Markov Models
  * Gaussian Mixture Models
  * Generative Adversarial Networks (GANs)

* Key Characteristics:
  * Can generate synthetic data
  * Requires modeling $P(X)$ as well
  * Typically more assumptions about data distribution



#### 2. Discriminative Models

* Definition: Models the *conditional probability distribution* $P(Y|X)$ directly or learns a decision boundary between classes.
* Goal: Focus on classification accuracy rather than modeling data generation.
* Examples:

  * Logistic Regression
  * Support Vector Machines (SVM)
  * Decision Trees, Random Forest
  * Most Neural Networks
* Key Characteristics:

  * Cannot generate new samples (does not model $P(X)$)
  * Usually simpler and more accurate for prediction tasks
  * Requires less data than generative models for the same accuracy
#### Why does this matter?

* Generative models are useful when you need synthetic data, unsupervised learning, or semi-supervised settings.
* Discriminative models dominate in supervised learning because they usually give better predictive performance for classification tasks.
