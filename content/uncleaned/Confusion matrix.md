---
title: 
tags:
  - evaluation
aliases: 
category:
---
**What matrix can you use to evaluate the performance of a classifier? How does an ideal matrix look like?**;; The [[Confusion matrix]]

# code

from sklearn.metrics import classification_report

```
confusion_matrix(y_train, y_train_pred)
array([[377, 63], [ 91, 180]], dtype=int64
```

## description

The confusion matrix you provided shows the ==performance of a classification model on the training data.== Here's a breakdown of what each element tells you:

![[Pasted image 20240120215414.png]]

- **True positives (TP):** The number of times the model correctly predicted class 0 (represented by the diagonal element in the first row). In this case, there are 377 TPs.
- **False positives (FP):** The number of times the model incorrectly predicted class 0 (represented by the element in the first row, second column). In this case, there are 63 FPs. [[Type 1 error]]
- **True negatives (TN):** The number of times the model correctly predicted class 1 (represented by the diagonal element in the second row). In this case, there are 180 TNs.
- **False negatives (FN):** The number of times the model incorrectly predicted class 1 (represented by the element in the second row, first column). In this case, there are 91 FNs. [[Type 2 error]]

From this confusion matrix, we can calculate some common metrics to evaluate the model's performance, such as accuracy, precision, recall, and F1-score.

[[Specificity]]
[[Sensitivity]]
[[Accuracy score]]
[[Precision Score]]
[[Recall Score]]
[[F1 Score]]


- **Accuracy:** The overall percentage of correct predictions. In this case, the accuracy is 78.3%.
- **Precision:** The ratio of true positives to all positive predictions (including both TPs and FPs). In this case, the precision for class 0 is 85.7% and the precision for class 1 is 66.4%.
- **Recall:** The ratio of true positives to all actual positive cases (including both TPs and FNs). In this case, the recall for class 0 is 80.6% and the recall for class 1 is 74.1%.
- **F1-score:** A harmonic average of precision and recall. In this case, the F1-score for class 0 is 83.0% and the F1-score for class 1 is 70.0%.

Overall, this confusion matrix suggests that the model is performing well on the training data, with an accuracy of 78.3%. However, there is some room for improvement, particularly in terms of the precision and recall for class 1.


![[Pasted image 20240129090924.png|500]]


- **Definition:** A table that shows the number of true positives, true negatives, false positives, and false negatives. It provides a detailed breakdown of the model's performance across different classes.
- 
- ![[Pasted image 20240116205937.png|500]]
- ![[Pasted image 20240116210541.png|500]]
- Can see what dominates.

## Questions and answers

**What is the purpose of a confusion matrix?**;; A [[Confusion matrix]] is a table that describes the performance of a [[Classification]] model.

**Why is the confusion matrix called like that?**;; It helps where the classifier is confused.

What does a confusion matrix do?;;The confusion matrix evaluates a classifier's performance, distinguishing correct and incorrect predictions.