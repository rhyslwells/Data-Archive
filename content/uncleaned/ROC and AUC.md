---
type: term
tags:
  - evaluation
  - ml
---
# What does it do:

Used to compare different models.

Suppose we have some actual results <code>y_act = [1, 0, 1, 1, 0]</code> and let 
    <code>y_pred = [1, 1, 0, 1, 0]</code> be the results predicted with a classifier. 
    Evaluate the performance of that classifier using the ROC curve.
```python



    from sklearn.metrics import roc_curve
    from sklearn.metrics import RocCurveDisplay
    from sklearn.metrics import roc_auc_score
    y_act = [1, 0, 1, 1, 0] 
    y_pred = [1, 1, 0, 1, 0]
    # compute ROC
    fpr, tpr, threshold = roc_curve(y_act, y_pred)
    # compute the area under curve (auc)
    auc = roc_auc_score(y_act, y_pred)
    # display the ROC and AUC
    roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=auc).plot()
    # you will get auc = 0.5833

```


Explored in:
C:\Users\RhysL\Desktop\DS_Obs\1_Inbox\Work\Udemy\Part_5_Advanced_Statistical_Methods_(Machine_Learning)\logistic_regression\logistic_regression_template.py


```python
#ROC AUC

from sklearn.metrics import roc_curve, roc_auc_score
#Having trained a model ie
logreg = LogisticRegression()..

# Predict the probabilities for the positive class (class 1)
y_probs = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
# Compute ROC-AUC score
roc_auc = roc_auc_score(y_test, y_probs)

# Plot ROC curve
plt.figure(figsize=(10, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='red', linestyle='--', lw=2, label='Random Guessing')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.legend()
plt.show()
```

Why do I use:
y_probs = logreg.predict_proba(X_test)[:, 1]
and not:
y_pred = logreg.predict(X_test)

need the predicted probabilities in ROC

roc_auc = roc_auc_score(y_test, y_probs) tells us close to 1 is good.

[[threshold level]] is the threshold level refers to the probability value above which an instance is classified as the positive class (class 1), and below which it is classified as the negative class (class 0). A decision boundary,

- If you lower the threshold, you will classify more instances as positive, potentially increasing sensitivity but decreasing specificity.
- If you raise the threshold, you will classify fewer instances as positive, potentially increasing specificity but decreasing sensitivity.

In a [[ROC and AUC]] , the threshold level is varied, and the true positive rate (sensitivity) and false positive rate (1-specificity) are calculated at each threshold value.

## Questions and answers

**If you want to evaluate the performance of a classifier with a curve what do you use?**;; Use [[ROC and AUC]]. It plots [[Sensitivity]] against 1-[[Specificity]] for different threshold values. A higher area under the ROC curve (AUC) indicates better classifier performance.

What are the [[ROC and AUC]];;Curve is a graphical representation of a classifier's ([[Logistic Regression]],[[Decision Tree]],[[Support Vector Machines]]) performance across different thresholds. It shows the tradeoff between [[Sensitivity]] and [[Specificity]].

What is the [[ROC and AUC]] score;; is a metric for binary [[Classification]] problems. It represents the area under the ROC curve and ranges from 0 to 1, with a higher value indicating better performance.


How do you evaluate the performance of your machine learning models, and what metrics do you prioritize? ;; I use metrics such as accuracy, precision, recall, F1-score, and area under the ROC curve (AUC-ROC) depending on the specific task and objectives of the model.
<!--SR:!2024-04-15,4,270-->