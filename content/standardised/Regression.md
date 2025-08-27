---
aliases: [linear models, predictive regression, regressive models]
category:
date modified: 1-08-2025
tags: [regressor, statistics]
---
[[Regression]] analysis is a statistical method used to ==predict== a continuous variable based on one or more predictor variables. The most common form, [[Linear Regression]], assumes a linear relationship between the dependent variable $y$ and independent variables $x_1, x_2, \dots, x_n$. The goal is to minimize the residual sum of squares (RSS) between observed and predicted values. Other forms, such as [[Logistic Regression]], handle classification problems.
 
 Regression models can incorporate techniques like regularization ($L_1$, $L_2$) to improve performance and prevent overfitting, especially with high-dimensional data. Advanced methods like [[Polynomial Regression]] address non-linearity, while generalized linear models (GLMs) extend regression to non-normal response variables.  
 
 **Regressor**: This is a type of model used for regression tasks, where the goal is to predict continuous values. For example, a regressor might be used to predict the price of a house based on its features, or to forecast future sales figures.


 Key Components:  
 - [[Regularisation]]: Adds $L_1$ ([[L1 Regularisation]]) or $L_2$ ([[Ridge]]) penalty to prevent overfitting in high-dimensional data.  
 - Feature transformation: [[Polynomial Regression]] and logarithmic transformations adjust for non-linearity in data.  
 - Regression is a type of [[Supervised Learning]].

Important
 - [[Multicollinearity]] can inflate variances of coefficient estimates, harming model reliability.  

Attention
 - Regression assumes [[linearity]], so improper application to non-linear data can lead to biased predictions.  
 - Overfitting can occur with too many predictors, especially in small datasets. 

Follow up questions
 -  How can [[Polynomial Regression]] improve predictions in non-linear datasets?  
 -  What are the benefits of combining [[Linear Regression]] with [[Feature Engineering]] for complex datasets?  
