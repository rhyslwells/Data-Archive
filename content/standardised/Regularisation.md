---
aliases: [Regularisation techniques, Regulation in ML]
category: ML
date modified: 1-08-2025
tags: [explainability, optimisation, process, visualization]
---
Regularization is a technique in machine learning that reduces the risk of overfitting by adding a penalty to the [[Loss function]] during model training. This penalty term restricts the magnitude of the model's parameters, thereby controlling the complexity of the model. It is especially useful in linear models but can also be applied to more complex models like neural networks.

==It simplifies the model.==

### Key Concepts

- **$L_1$ Regularization ([[L1 Regularisation]]):** Adds the absolute value of the coefficients to the loss function, encouraging sparsity by driving some coefficients to zero, effectively selecting a subset of features.
  
- **$L_2$ Regularization ([[Ridge]]):** Adds the square of the coefficients to the loss function, shrinking them toward zero. It encourages smaller coefficients but does not push them exactly to zero, helping reduce overfitting by penalizing large weights.

- **Elastic Net:** Combines both Lasso and Ridge regularization.

### Benefits

- **Prevents Overfitting:** Regularization adds a penalty term to the loss function to avoid overfitting.
- **Feature Sparsity:** $L_1$ encourages feature sparsity, while $L_2$ reduces coefficient magnitudes.
- **Enhanced Generalization:** Dropout enhances generalization by preventing unit co-adaptation in neural networks.

### Considerations

- **Underfitting Risk:** Over-penalizing parameters can lead to underfitting, where the model becomes too simplistic.
- **Tuning $\lambda$:** Choosing the right penalty term (i.e., $\lambda$) is crucial for balancing bias and variance.

[[When and why not to us regularisation]]
### Questions
- How does the balance between $L_1$ and $L_2$ regularization impact model performance in large feature spaces?
- What are the best practices for tuning the $\lambda$ parameter in regularization? [[Model Parameters Tuning]].

### Example

Consider a linear regression model with $L_2$ regularization (Ridge). The [[loss function]] would be:

$$ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n} \theta_j^2 $$

Here, $\lambda$ controls the strength of the regularization. Higher $\lambda$ values shrink the coefficients more.
### Related Topics

- [[Feature Selection]]: L1 regularization can zero out irrelevant features, improving model [[Interpretability]] and reducing computational costs.
- [[Model Selection]] techniques for high-dimensional data.

### Applications

Regularization is widely used in linear models but is also applied in other machine learning models, particularly those prone to overfitting:

- [[Neural network]]
- [[Regularisation of Tree based models]]

### Implementation

In [[ML_Tools]] see: [[Regularisation.py]]
