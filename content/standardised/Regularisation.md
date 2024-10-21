---
title: Regularization in Machine Learning
tags:
  - ml
  - ml_process
  - data_visualization
  - statistics
  - optimisation
  - model_explainability
aliases:
  - Regulation in ML
  - Regularisation techniques
category: Machine Learning
---

>[!Summary]  
>
>Regularization is the process of adding a tuning parameter to a model to ==induce smoothness in order to prevent overfitting.== It helps in controlling the complexity of the model and reduces the chance of fitting noise in the training data.
>
>Regularization is a  technique in machine learning that reduces the risk of overfitting by adding a penalty to the [[Loss function]] during model training. This penalty term restricts the magnitude of the model's parameters, thereby controlling the complexity of the model. 
>
>Common forms of regularization include $L_1$ regularization ([[Lasso]]) and $L_2$ regularization ([[Ridge]]). 
>
>Used to improve model performance by preventing overfitting. It is especially useful in linear models but can also be applied to more complex models like neural networks. 
>
>Lasso results in sparse models by setting ==less important feature weights to zero==, while Ridge ==shrinks all feature coefficients==, reducing their impact without eliminating any features. 
>
>[[Dropout]] is another regularization technique specifically used in neural networks, randomly dropping units during training to encourage robust feature learning.

>[!Breakdown]  
> Key Components:  
> - $L_1$ regularization ([[Lasso]]): Adds the absolute value of the coefficients to the loss function, encouraging sparsity.  
> - $L_2$ regularization ([[Ridge]]): Adds the square of the coefficients to the loss function, shrinking them toward zero.  
> - [[Elastic Net]] : Combines bothe lasso and ridge.
> - Dropout: A neural network regularization method that drops units at random during training to prevent over-reliance on specific neurons.

>[!important]  
> - Regularization adds a penalty term to the loss function to avoid overfitting.  
> - $L_1$ encourages feature sparsity, while $L_2$ reduces coefficient magnitudes.  
> - Dropout enhances generalization by preventing unit co-adaptation in neural networks.

>[!attention]  
> - Over-penalizing parameters can lead to underfitting, where the model becomes too simplistic.  
> - Choosing the right penalty term (i.e., $\lambda$) is crucial for balancing bias and variance.

>[!Example]  
Consider a linear regression model with $L_2$ regularization (Ridge). The [[loss function]] would be:  
$$ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n} \theta_j^2 $$  
Here, $\lambda$ controls the strength of the regularization. Higher $\lambda$ values shrink the coefficients more.

>[!Follow up questions]  
> - How does the balance between $L_1$ and $L_2$ regularization impact model performance in large feature spaces?  
> - What are the best practices for tuning the $\lambda$ parameter in regularization?

>[!Related Topics]  
> - [[Feature Selection]]: L1 regularization, in particular, can zero out irrelevant features, improving model [[interpretability]] and reducing computational costs.
> - [[Model Selection]] techniques for high-dimensional data  

# Models that Use Regularization

Regularization is widely used in linear models but is also applied in other machine learning models, particularly those prone to overfitting:

1. Linear Models:
    - Linear regression, logistic regression, and support vector machines (SVM) can use L1 (Lasso) and L2 (Ridge) regularization to avoid overfitting by controlling the size of the model coefficients.
   
2. [[Neural network]]
    - Neural networks are highly flexible and can overfit when trained on complex datasets. L2 regularization (also called weight decay) is commonly used to penalize large weights.
    - [[Dropout]] is another form of regularization for neural networks, where randomly selected neurons are ignored (dropped out) during training to reduce overfitting.

3. [[Regularisation of Tree based models]]
    - Tree models, such as Random Forests and Gradient Boosting, can also be regularized, although they don’t use L1 or L2 regularization directly. Instead, they are regularized through hyperparameters like max depth, min samples split, and learning rate to control the complexity of the trees.



