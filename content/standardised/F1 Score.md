---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - evaluation
---
### Definition
- The F1 Score is the harmonic mean of precision and recall. It provides a balanced view of both metrics and is particularly useful when:
  - There is an uneven class distribution.
  - Both precision and recall are important.

The formula for the F1 Score is:

$$F1 = 2 \times \frac{{\text{Precision} \times \text{Recall}}}{{\text{Precision} + \text{Recall}}} $$

Where:
- [[Precision]] is calculated as $\frac{{\text{True Positives}}}{{\text{True Positives} + \text{False Positives}}}$.
- [[Recall]] is calculated as $\frac{{\text{True Positives}}}{{\text{True Positives} + \text{False Negatives}}}$.

The F1 Score is the harmonic mean of precision and recall, which ensures that the score is high only when both precision and recall are high.

### Components
- Precision: The ratio of true positive predictions to the total predicted positives. It measures the accuracy of positive predictions.
- Recall: The ratio of true positive predictions to the total actual positives. It measures the ability to find all positive instances.

### Importance
- The F1 Score is suitable for imbalanced datasets where considering both false positives and false negatives is crucial.
- It ranges from 0 to 1, where a higher score indicates better overall classifier performance.

### Use
- The F1 Score, also known as the F-measure, combines precision and recall using the harmonic mean. This makes it a useful metric for evaluating models where a balance between precision and recall is desired.

### Understanding the F1 Score

The F1 Score is a metric used to evaluate the performance of a classification model, especially in scenarios where the classes are imbalanced. It helps in understanding how well the model is performing in terms of both precision (how many selected items are relevant) and recall (how many relevant items are selected).

- Why [[Harmonic Mean]]?: The harmonic mean is used instead of the arithmetic mean because it punishes extreme values more. This means that if either precision or recall is very low, the F1 Score will also be low, reflecting the poor performance in one of the areas.

- When to Use: Use the F1 Score when you need a single metric that considers both false positives and false negatives, especially in cases where the cost of false positives and false negatives is similar.

By focusing on both precision and recall, the F1 Score provides a more comprehensive measure of a model's accuracy, particularly in situations where one class is much more frequent than the other.