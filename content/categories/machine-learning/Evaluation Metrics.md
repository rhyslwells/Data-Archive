---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- code_snippet
- evaluation
---
## Description

[[Confusion Matrix]]
[[Accuracy]]
[[Precision]]
[[Recall]]
[[Precision or Recall]]
[[F1 Score]]
[[Recall]]
[[Specificity]]


![[Pasted image 20241222091831.png]]

## Resources:
[Link to good website describing these](https://txt.cohere.com/classification-eval-metrics/)
## Types of predictions

Types of predictions in evaluating models. Also see [[Why Type 1 and Type 2 matter]]

**True Positive (TP)**:
- This occurs when the model correctly predicts the positive class. For example, if the model predicts that an email is spam and it actually is spam, that's a true positive.

**False Positive (FP)**:
- Also known as a =="Type I error,"== this occurs when the model incorrectly predicts the positive class. For example, if the model predicts that an email is spam but it is not, that's a false positive.

**True Negative (TN)**:
- This occurs when the model correctly predicts the negative class. For example, if the model predicts that an email is not spam and it actually is not spam, that's a true negative.

**False Negative (FN)**:
- Also known as a =="Type II error,"== this occurs when the model incorrectly predicts the negative class. For example, if the model predicts that an email is not spam but it actually is spam, that's a false negative.

## Evaluation metrics in practice

Having many evaluation metrics is hard to understand and optimise. Sometimes it is best to combine into one.

Use a single number i.e. accuracy or [[F1 Score]] . 

This speeds up development of ml projects.

In order to use metrics to evaluate a model we can:
- Can combine multiple metrics a formula, i.e. weighted average.
- If there is a metrics we are happy that the model passes a given level then we can have it "==Satisfying==". So the for the given metric it just needs to pass a given level.
- For metrics we are interested in we have it "==Optimising==", the one we want to be the best.
- Setup: Pick N-1 satisfying and 1 optimising.

![[Pasted image 20241217073706.png]]





