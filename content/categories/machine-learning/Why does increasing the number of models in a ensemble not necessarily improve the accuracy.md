---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- modeling
---
Increasing the number of models in an ensemble ([[Model Ensemble]]) does not always lead to improved accuracy due to several limiting factors:

- **Convergence of Predictions**: Additional models may lead to similar predictions, resulting in minimal changes to the overall output.
- **Limited Data Representation**: If the dataset is noisy or incomplete, more models will only aggregate existing noise without capturing new patterns.
- **Diminishing Returns**: Each new model contributes less unique information, and performance is ultimately limited by the irreducible error in the data.
- **Increased Complexity**: More models increase computational costs and training times without necessarily improving accuracy.
- **Overfitting Risk**: Adding complex models can lead to overfitting, where the ensemble learns noise instead of underlying patterns.