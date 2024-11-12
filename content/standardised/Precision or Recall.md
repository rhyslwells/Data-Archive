---
tags:
  - evaluation
aliases: 
category:
---
- [[Precision]] and [[Recall]] are two fundamental metrics used to evaluate the performance of a [[Classification]] model, particularly in binary classification tasks.
- They are related through a trade-off: improving one often comes at the expense of the other.

## Key Differences

- Precision focuses on the quality of positive predictions, defined as the proportion of true positive predictions among ==all== positive predictions made by the model.
    $$\text{Precision} = \frac{TP}{TP + FP}$$
- Recall focuses on the ability to identify all relevant positive instances, defined as the proportion of true positive predictions among all ==actual== positive instances.
    $$\text{Recall} = \frac{TP}{TP + FN}$$

![[Pasted image 20240116211130.png|500]]
## Trade-off

- It is challenging to optimize both precision and recall simultaneously. Improving precision by reducing false positives may lead to an increase in false negatives, thereby reducing recall, and vice versa.
- The choice between prioritizing precision or recall is task-dependent.

## Task Dependency Example

- In a spam classification task, it might be more important to avoid moving important emails to the spam folder (high precision) than to occasionally allow spam emails into the inbox (lower recall). Thus, precision is prioritized over recall in this context.

## Related Concepts
- [[Classification Report]]

