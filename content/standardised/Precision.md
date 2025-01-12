---
tags:
  - evaluation
aliases: 
category:
---
**Precision Score** is a metric used to evaluate the [[Accuracy]] of a [[Classification]] model, specifically focusing on the positive class.

==How many retrieved items are relevant?==

This metric indicates the accuracy of positive predictions. The formula for precision is:

$$\text{Precision} = \frac{TP}{TP + FP}$$

where:
- **TP (True Positives):** The number of correctly predicted positive instances.
- **FP (False Positives):** The number of instances incorrectly predicted as positive.

Importance:
- Precision is crucial in scenarios where the **cost of false positives is high**, such as in spam detection or medical diagnosis. It helps in understanding how many of the predicted positive instances are actually positive.

![[Pasted image 20241222091831.png]]

## Related Concepts

- [[Classification Report]] & [[Precision or Recall]]




