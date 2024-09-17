#ml


## Description

Logistic Regression uses a logistic function (also called a sigmoid function) to model the probability that a given input belongs to a particular category. This function squishes any input into a range between 0 and 1.

Once the model is trained, it creates a ==decision boundary== that separates the two classes. In 2D space, this boundary is a line, but in higher dimensions, it's a hyperplane. The logistic function gives the probability that a point belongs to one class, and if that probability is above a certain threshold (usually 0.5), we classify it as belonging to that class.

Logistic Regression determines the point at which the logistic function (sigmoid) transitions from predicting one class to predicting the other. This decision boundary is akin to the concept of a hyperplane in Support Vector Machines ([[SVM]]),
# Notes

- **Binary Classification Task**: ie Yes or No of target.
- Given a parameter want low values to be assigned to 0 and high values to 1.
- Can use more than one independent variable input.
- Logistic regression does not have standard residuals as seen in [[Linear Regression]]
# Good for:

If the decision boundary between the two classes in your feature space is approximately linear, logistic regression can perform well.

# Example

Using logistic regression in Breast Cancer dataset can be a suitable choice for binary classification tasks, such as predicting whether a tumor is malignant or benign. Or in the titanic dataset wrt survival 0 or 1.

# Code set up of model


```python
import statsmodels.api as sm
y = data['Admitted'] #target
x1 = data[['SAT','Gender']] #input

x = sm.add_constant(x1)
reg_log = sm.Logit(y,x)
results_log = reg_log.fit()
# Get the regression summary
results_log.summary()
```

# Summary table

[Explanation of summary](https://youtu.be/JwUj5M8QY4U?t=658)

The dependent variable is 'duration'. The model used is a Logit regression (logistic in common lingo), while the method 
- Maximum Likelihood Estimation (MLE). It has clearly converged after classifying 518 observations.
- The Pseudo R-squared is 0.21 which is within the 'acceptable region'.
- The duration variable is significant and its coefficient is 0.0051.
- The constant is also significant and equals: -1.70 (p value close to 0)
-  High p value, suggests to remove from model, drop one by one, ie [[Feature Selection]].

![[Pasted image 20240124095043.png|500]]
# What is the odds of an input variable?

The ==odds== are of the form (different from probability):

$P(winning)/P(not winning)= p(win)/(1-p(win))$

Log odds are the Log of the odds (makes wining /not winning symmetrical).

[Explanation of log odds](https://www.youtube.com/watch?v=ARfXDSkQf1Y)

[Explanation of log odd function](https://www.youtube.com/watch?v=fJ53tIDbvTM)

$$ln(\frac{p}{1-p})=b_0 + b_1 x$$
# What does the graph tell us?
#question 
Specifically a graph such as,

![[Pasted image 20240124095916.png]]

## [[Model Evaluation]] in [[Scikit-learn]]

Need model in sklearn to use [[Confusion matrix]] or Classification report, where [[Accuracy score]] is general evaluator.


