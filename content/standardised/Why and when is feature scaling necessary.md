---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
[[Feature Scaling]] is useful for models that use distances like [[Support Vector Machines|SVM]] and [[K-means]]
### When Scaling Is Unnecessary

1. **Tree-based Algorithms:**
    - Algorithms like [[Decision Tree]], [[Random Forests]], and Gradient Boosted Trees are invariant to feature scaling because they split data based on thresholds, not distances.
    - Example: Splits are determined by feature values, not their magnitude.
      
2. **Data with Uniform Scales:**
    - If all features have the same range or are already normalized (e.g., percentages), scaling may not be required.
      
