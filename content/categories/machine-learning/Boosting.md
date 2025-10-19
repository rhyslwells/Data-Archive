---
aliases: []
category: ML
date modified: 27-09-2025
tags:
  - architecture
  - explainability
---
Boosting is a type of [[Model Ensemble]] in machine learning that focuses on improving the accuracy of predictions by building a ==sequence of models==. Each subsequent model focuses on correcting the errors made by the previous ones.

It combines [[Weak Learners]] (models that are slightly better than random guessing) to create a strong learner. 

### Key Concepts of Boosting:

1. Sequential Learning: Boosting involves training models sequentially. Each new model is trained to correct the errors made by the previous models. This means that the models are not independent of each other; instead, ==each model is built on the mistakes of the previous ones.==

2. Focus on Misclassified Data: As models are trained in sequence, more emphasis is placed on the data points that were misclassified by earlier models. This helps the ensemble model to gradually improve its performance by focusing on the difficult-to-classify instances.

3. [[Weak Learners]]: Boosting combines multiple weak learners, which are models that perform slightly better than random guessing. By combining these weak learners, boosting creates a strong learner that has improved accuracy.

4. Examples of Boosting Algorithms: Some well-known boosting algorithms include [[Ada boosting]], [[Gradient Boosting]], and [[XGBoost]]. Each of these algorithms has its own approach to boosting, but they all share the core principle of sequentially improving model performance.

### Advantages of Boosting:

- Increased Accuracy: By focusing on the errors of previous models, boosting can significantly improve the accuracy of predictions.
- Flexibility: Boosting can be applied to various types of base models and is not limited to a specific algorithm.
- Robustness: Boosting can handle complex datasets and is effective in reducing bias and variance.

### Challenges of Boosting:

- Complexity: Boosting models can be more complex and computationally intensive than single models.
- [[Interpretability]]: The final model may be harder to interpret compared to simpler models like decision trees.

## Related
- [[Order matters in Boosting]]

### [[Boosting]]

* **How it works:**
  * Train models **sequentially**, each correcting errors of the previous one.
  * Combine predictions using **weighted sums**.

* **Example:** AdaBoost, Gradient Boosting, XGBoost.

* **Focus:** Reduce **bias** by turning weak learners into a strong model.

* **Pros:**
  * Can achieve very high accuracy.
  * Strong at capturing patterns in complex datasets.

* **Cons:**
  * Sensitive to noisy data and outliers.
  * Risk of overfitting if not tuned carefully.