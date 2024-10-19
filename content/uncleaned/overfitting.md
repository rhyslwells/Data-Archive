---
title: Overfitting in Machine Learning  
tags: 
- ml 
- analysis 
- statistics 
- data_quality  
aliases: model overfitting, high variance models
---

>[!Summary]  
> Overfitting in machine learning occurs when a model captures not only the underlying patterns in the training data ==but also the noise==, leading to poor performance on unseen data, and is unable to generalise.
> 
>Mathematically, overfitting results in a model with low bias but high variance, meaning it adapts too closely to the training data and fails to generalize well.
>
>Key methods to address overfitting include [[regularisation]] (such as $L_1$ and $L_2$ regularization), [[Cross validation]], and simpler models.
>
>In statistical terms, it indicates a model with high complexity and too many parameters relative to the amount of training data, which results in $f(x)$ poorly representing the population distribution.

>[!Breakdown]  
> Key Components:  
> - Regularization (Lasso: $L_1$, Ridge: $L_2$) to penalize model complexity.  
> - [[Cross validation]] to ensure model generalization.  
> - Early stopping in training to avoid learning noise.  
> - Simplification of models to prevent fitting irrelevant patterns.

>[!important]  
> - Overfitting indicates high variance in the model’s performance, which can be ==identified by a significant drop in accuracy between training and test datasets.==  
> - Regularization adds penalty terms to the cost function, reducing model complexity and mitigating overfitting.

>[!attention]  
> - Overfitting is more common in models with high-dimensional datasets.  
> - Excessive model tuning (hyperparameter optimization) may inadvertently increase overfitting.

>[!Follow up questions]  
> - How does the choice of regularization type (e.g., $L_1$ vs. $L_2$) affect model generalization in overfitting scenarios?  
> - What role does the size of the training dataset play in mitigating overfitting?

>[!Related Topics]  
> - [[Cross validation]] techniques (e.g., $k$-fold, Leave-One-Out cross-validation)  
> - [[Bias and variance]]radeoff in machine learning models  