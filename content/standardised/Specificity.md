---
tags:
  - evaluation
aliases: 
category:
---
- **Specificity**, also known as the true negative rate, measures the proportion of actual negatives that are correctly identified by the model. It indicates how well the model is at identifying negative instances.

## Formula

$$\text{Specificity} = \frac{TN}{TN + FP}$$

where:
- **TN (True Negatives):** The number of correctly predicted negative instances.
- **FP (False Positives):** The number of instances incorrectly predicted as positive.

## Importance

- Specificity is crucial in scenarios where it is important to correctly identify negative instances, such as in medical testing where a false positive could lead to unnecessary treatment.

## Related Concepts

- [[Confusion Matrix]]
- [[Sensitivity]]