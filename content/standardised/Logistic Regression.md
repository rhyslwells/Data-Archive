---
title: 
tags:
  - classifier
  - regressor
aliases: 
category:
---
Logistic [[Regression]] is a machine learning algorithm used for [[Binary Classification]]tasks, where the goal is to predict one of two possible outcomes (e.g., "Yes" or "No").

==Logistic regression models the log-odds of the probability as a linear function of the input features.==

It models the probability of an input belonging to a particular class using a logistic (sigmoid) function.

The model establishes a decision boundary (threshold) in the feature space and leverages the concept of odds and log-odds to make predictions.

Logistic regression is best suited for cases where the decision boundary is approximately linear in the feature space.

Although logistic regression naturally outputs odds, these can be transformed into probabilities using the sigmoid function.

### Related Notes:

- [[Logistic Regression Statsmodel Summary table]]
- [[Logistic Regression does not predict probabilities]]
- [[Interpreting logistic regression model parameters]]
- [[Model Evaluation]]

In [[ML_Tools]], see:
- [[Regression_Logistic_Metrics.ipynb]]
## Key Concepts of Logistic Regression

### Logistic Function (Sigmoid Function)

Logistic regression models the probability that an input belongs to a particular class using the logistic (sigmoid) function}. This function maps any real-valued input into the range (0,1), representing the probability of belonging to the positive class (usually class 1).

The sigmoid function is defined as:  
$$ \sigma(z) = \frac{1}{1 + e^{-z}} $$  
where  
$$ z = \mathbf{w} \cdot \mathbf{x} + b $$  
Thus, the logistic regression model is given by:  
$$ P(y=1 \mid \mathbf{x}) = g(\mathbf{w} \cdot \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w} \cdot \mathbf{x} + b)}} $$  
Where the Natural Log Appears: (Transforming from continuous to 0-1). Logistic regression is based on the ==log-odds== (logit) transformation, which expresses probability in terms of odds:

$$ \text{Odds} = \frac{P(y=1 \mid \mathbf{x})}{1 - P(y=1 \mid \mathbf{x})} $$

Taking the natural logarithm of both sides gives the logit function}:

$$ \log \left(\frac{P(y=1 \mid \mathbf{x})}{1 - P(y=1 \mid \mathbf{x})} \right) = \mathbf{w} \cdot \mathbf{x} + b $$

This equation shows that ==logistic regression models the log-odds of the probability as a linear function of the input features.==

Additionally, the log loss function} (used to optimize logistic regression) is defined as:

$$ \mathcal{L} = - \frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log P(y_i) + (1 - y_i) \log (1 - P(y_i)) \right] $$

where $y_i$ is the actual class label (0 or 1) and $P(y_i)$ is the predicted probability. The logarithm ensures that incorrect confident predictions are penalized more heavily.
### Decision Boundary

- Similar to [[Support Vector Machines]], logistic regression defines a decision boundary that separates the two classes.
- In a 2D feature space, this boundary is a straight line, while in higher dimensions, it forms a hyperplane.
- The logistic function determines the probability of a data point belonging to a specific class. If this probability exceeds a given ==threshold== (typically 0.5), the model assigns the point to the positive class; otherwise, it is classified as negative.
### [[Binary Classification]]

- Logistic regression is primarily used for binary classification tasks, where the target variable has only two possible values (e.g., "0" and "1").
- It can handle multiple independent variables (features) and assigns probabilities to the target classes based on the feature values.
- Examples include:
    - Predicting whether a tumor is malignant or benign (Breast Cancer dataset).
    - Determining whether a passenger survived the Titanic disaster (Titanic dataset).

### No Residuals

- Unlike [[Linear Regression]], logistic regression does not compute standard residuals.
- Instead, [[Model Evaluation]] is performed by comparing predicted probabilities with actual class labels using metrics such as accuracy, precision, recall, and the [[Confusion Matrix]].

### Maximum likelihood estimation

How to get [[Model Parameters]]
### Extending Logistic Regression

Logistic regression can be extended to handle non-linear decision boundaries through:

- Polynomial features to capture more complex relationships.
- Regularization techniques to improve generalization.

### Also see:
- Cost function for logistic regression
- Gradient computation in logistic regression
- Regularized logistic regression
- Cost function for regularized logistic regression

### Resources

[Explaining logistic regression](https://www.youtube.com/watch?v=Iju8l2qgaJU)
