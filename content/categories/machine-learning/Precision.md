---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- evaluation
---
**Precision Score** is a metric used to evaluate the [[Accuracy]] of a [[Classification]] model, specifically focusing on the positive class.

==How many retrieved items are relevant?==

This metric indicates the accuracy of positive predictions. The formula for precision is:

$$\text{Precision} = \frac{TP}{TP + FP}$$

where:
- **TP (True Positives):** The number of correctly predicted positive instances.
- **FP (False Positives):** The number of instances incorrectly predicted as positive.

Importance:
- Precision is helpful in scenarios where the **cost of false positives is high**, such as in spam detection. It helps in understanding how many of the predicted positive instances are actually positive.

![[Pasted image 20241222091831.png]]

## Related Concepts

- [[Classification Report]] & [[Precision or Recall]]




