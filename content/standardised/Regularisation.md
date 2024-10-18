---
title: Regularization in Machine Learning  
tags: 
- ml  
- ml_process  
- data_visualization  
- statistics  
aliases: [Regulation in ML, Regularisation techniques]  
category: Machine Learning  
---

>[!Summary]  
>
>Regularization is the process of adding a tuning parameter to a model to ==induce smoothness in order to prevent overfitting.== It helps in controlling the complexity of the model and reduces the chance of fitting noise in the training data.
>
>Regularization is a  technique in machine learning that reduces the risk of overfitting by adding a penalty to the [[loss function]] during model training. This penalty term restricts the magnitude of the model's parameters, thereby controlling the complexity of the model. 
>
>Common forms of regularization include $L_1$ regularization ([[Lasso]]) and $L_2$ regularization ([[Ridge]]). 
>
>Lasso results in sparse models by setting ==less important feature weights to zero==, while Ridge ==shrinks all feature coefficients==, reducing their impact without eliminating any features. 
>
>[[Dropout]] is another regularization technique specifically used in neural networks, randomly dropping units during training to encourage robust feature learning.

>[!Breakdown]  
> Key Components:  
> - $L_1$ regularization (Lasso): Adds the absolute value of the coefficients to the loss function, encouraging sparsity.  
> - $L_2$ regularization (Ridge): Adds the square of the coefficients to the loss function, shrinking them toward zero.  
> - Dropout: A neural network regularization method that drops units at random during training to prevent over-reliance on specific neurons.

>[!important]  
> - Regularization adds a penalty term to the loss function to avoid overfitting.  
> - $L_1$ encourages feature sparsity, while $L_2$ reduces coefficient magnitudes.  
> - Dropout enhances generalization by preventing unit co-adaptation in neural networks.

>[!attention]  
> - Over-penalizing parameters can lead to underfitting, where the model becomes too simplistic.  
> - Choosing the right penalty term (i.e., $\lambda$) is crucial for balancing bias and variance.

>[!Example]  
Consider a linear regression model with $L_2$ regularization (Ridge). The cost function would be:  
$$ J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_{\theta}(x^{(i)}) - y^{(i)})^2 + \lambda \sum_{j=1}^{n} \theta_j^2 $$  
Here, $\lambda$ controls the strength of the regularization. Higher $\lambda$ values shrink the coefficients more.

>[!Follow up questions]  
> - How does the balance between $L_1$ and $L_2$ regularization impact model performance in large feature spaces?  
> - What are the best practices for tuning the $\lambda$ parameter in regularization?

>[!Related Topics]  
> - [[Feature Selection]] methods in machine learning  
> - [[Model Selection]] techniques for high-dimensional data  



