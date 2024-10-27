---
title: 
tags:
  - ml
  - classifer
aliases: 
category:
---
# Summary

**Logistic Regression** is a machine learning algorithm used for **binary [[Classification]] tasks**, where the goal is to predict one of two possible outcomes (e.g., "Yes" or "No").  

It works by modeling the ==probability of an input belonging to a particular class== using a **logistic function**.  

It creates a ==**decision boundary (threshold)**== in the feature space and uses the concept of ==**odds** and **log-odds**== to make predictions.

It's suitable for cases where the decision boundary and feature space is approximately ==linear==.

Logistic regression naturally outputs probabilities, but it can be converted into a **classifier** by setting a threshold. The most common threshold is 0.5, meaning that if the model predicts a probability greater than 0.5, the input is classified as the positive class (1), otherwise as the negative class (0).

### Key Concepts of Logistic Regression:

1. **Logistic Function (Sigmoid Function)**:

   - Logistic regression models the probability that a given input belongs to a particular class using a logistic (sigmoid) function, which transforms any input into a value between 0 and 1. This output represents the **probability** of the input belonging to the positive class (usually class "1").

   - The sigmoid function is defined as:

   $$ \sigma(z) = \frac{1}{1 + e^{-z}} $$

   where $z$ is the weighted sum of the input features.

2. **Decision Boundary**:

   This concept is similar to the decision boundary in [[Support Vector Machines]], where a hyperplane is used to separate classes.
   
   - Once the model is trained, it creates a **decision boundary** that separates the two classes. In 2D space, this boundary is a straight line, while in higher dimensions, it becomes a **hyperplane**.

   - Logistic regression uses the logistic function to determine the probability that a data point belongs to a certain class. If the probability is above a certain threshold (typically 0.5), the model predicts that the point belongs to the positive class; otherwise, it predicts the negative class.

3. **Binary Classification**:

   - Logistic regression is primarily used for **binary classification tasks**, where the target variable has only two possible values (e.g., "0" and "1"). It can handle multiple independent variables (features), and based on the feature values, it assigns probabilities to the target classes.

   - Examples of binary classification tasks include predicting whether a tumor is malignant or benign (Breast Cancer dataset), or whether a passenger survived the Titanic disaster (Titanic dataset).

5. **No Residuals**:

   - Unlike [[Linear Regression]], logistic regression does not have standard residuals. Instead, the model evaluates performance by comparing predicted probabilities with actual class labels using metrics like accuracy, precision, recall, and the [[Confusion matrix]].

### Odds and Log-Odds:

[[What is the difference between odds and probability]]

In logistic regression, the model predicts the ==**odds** of an event happening rather than directly predicting probabilities.== The **odds** are defined as:

$$ \text{Odds} = \frac{P(\text{success})}{P(\text{failure})} = \frac{p}{1-p} $$

  where $p$ is the probability of success. The **log-odds** (or **logit function**) is the natural logarithm of the odds:
  $$ \text{Log-Odds} = \ln\left(\frac{p}{1-p}\right) = b_0 + b_1 x $$
  This transformation makes the relationship between the independent variables and the dependent variable linear, allowing logistic regression to estimate the parameters $b_0$ and $b_1$.

Resources:
- [Explanation of log odds](https://www.youtube.com/watch?v=ARfXDSkQf1Y)
- [Explanation of log odd function](https://www.youtube.com/watch?v=fJ53tIDbvTM)

# Further Understanding
### Use Cases:

Logistic regression is widely used in real-world applications, especially in binary classification problems like:
  - Predicting whether a customer will buy a product (marketing predictions).
  - Medical diagnoses (e.g., predicting the likelihood of a patient developing a condition).
  - Financial analysis (e.g., predicting loan defaults).
### Examples

Consider predicting whether a student will be admitted based on their **SAT score** and **gender**. The logistic regression model estimates the probability of admission (0 or 1).

A simple code example using the **statsmodels** library in Python:

```python
import statsmodels.api as sm

y = data['Admitted']  # Target variable
x1 = data[['SAT', 'Gender']]  # Input features

x = sm.add_constant(x1)  # Add intercept
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()

# Get the regression summary
results_log.summary()
```

The summary will show the coefficients of the model, including the intercept, p-values, and overall fit statistics like the **Pseudo R-squared**, which gives an indication of model quality (typically between 0 and 1).

Another example is using logistic regression in Breast Cancer dataset can be a suitable choice for binary classification tasks, such as predicting whether a tumor is malignant or benign. Or in the titanic dataset wrt survival 0 or 1.
### [[Model Evaluation]]

In machine learning, after training the logistic regression model, we evaluate its performance using metrics such as the **[[Confusion matrix]]** or the **Classification report**, which provide insight into the model's **accuracy**, **precision**, **recall**, and **[[F1 score]]**.

In [[Scikit-learn]], logistic regression can be implemented as follows:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Confusion matrix
print(confusion_matrix(y_test, y_pred))

# Classification report
print(classification_report(y_test, y_pred))
```

The [[confusion matrix]] and [[classification report]] help evaluate how well the model distinguishes between the two classes.

### Statsmodel Summary table

Statsmodel has this summary table unlike [[Scikit-learn]]

[Explanation of summary](https://youtu.be/JwUj5M8QY4U?t=658)

The dependent variable is 'duration'. The model used is a Logit regression (logistic in common lingo), while the method 
- Maximum Likelihood Estimation ([[MLE]]). It has clearly converged after classifying 518 observations.
- The Pseudo R-squared is 0.21 which is within the 'acceptable region'.
- The duration variable is significant and its coefficient is 0.0051.
- The constant is also significant and equals: -1.70 (p value close to 0)
- High p value, suggests to remove from model, drop one by one, ie [[Feature Selection]].

Specifically a graph such as,
![[Pasted image 20240124095916.png]]

