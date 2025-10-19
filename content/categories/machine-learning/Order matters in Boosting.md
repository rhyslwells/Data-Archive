---
aliases: []
category:
date modified: 19-10-2025
tags: [ml, ml_process]
---
Order matters in Boosting


**Summary:**
Boosting is inherently sequential, and each step depends on the errors of the previous step. Therefore, **the order of training matters** and affects the final model performance.

### **Why order matters**

1. **Sequential learning:**

   * Boosting algorithms (like **AdaBoost**, **Gradient Boosting**) build models **sequentially**.
   * Each model is trained to **correct the mistakes** of the previous models.

2. **Error weighting:**

   * Observations that were mispredicted by earlier models get **higher weight** in subsequent models.
   * The order determines which mistakes are focused on first and influences the final combined model.

3. **Cumulative effect:**

   * Since predictions are combined sequentially, the **early models have more influence** on later corrections.
   * The order of learning affects convergence, bias, and variance.
### **Contrast with Bagging**

* In **bagging** (like Random Forests), models are trained **independently**, so the order **does not matter**.
* Boosting relies on **dependency between models**, so changing the sequence can change the outcome.