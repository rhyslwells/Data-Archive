---
aliases: []
category:
date modified: 1-08-2025
tags: [architecture]
---
Resources:
[LINK](https://www.youtube.com/watch?v=LsK-xG1cLYA)
# Overview:

Ada Boosting short for ==Adaptive Boosting==, is a specific type of [[Boosting]] algorithm that focuses on improving the accuracy of predictions by ==combining multiple weak learners== into a strong learner. It is particularly known for its ==simplicity== and effectiveness in classification tasks.

### How AdaBoost Works:

1. **Base Learners**: In AdaBoost, the base learners are typically low-depth trees, also known as ==stumps==. These are simple models that perform slightly better than random guessing.

2. **Sequential Training**: AdaBoost trains these stumps sequentially. Each stump is trained to correct the errors made by the previous stumps. This sequential approach ensures that each new model focuses on the data points that were misclassified by earlier models.

3. **Weighting**: After each stump is trained, ==AdaBoost assigns a weight to it based on its accuracy==. More accurate stumps receive higher weights, giving them more influence in the final prediction.

4. **Error Focus**: The algorithm ==increases the weights of the misclassified data points==, making them more prominent in the training of the next stump. This ensures that subsequent models pay more attention to the difficult-to-classify instances.

5. **Final Prediction**: The final prediction is a weighted sum of the predictions from all the stumps. The stumps with higher accuracy have more say in the final classification.

# Further Understanding

### Creating a Forest with AdaBoost:

To create a forest using AdaBoost, you start with a [[Decision Tree]] or [[Random Forests]] approach, but instead of using full-sized trees, you use stumps. 

These stumps are trained sequentially, with each one focusing on the errors of the previous stumps. 

The final prediction is a weighted sum of the predictions from all the stumps, where more accurate stumps have more influence on the final outcome.

### Key Differences from [[Random Forests]]:

- **Tree Depth**: In [[Random Forests]], full-sized trees are used, and each tree gets an equal say in the final prediction. In contrast, AdaBoost uses low-depth trees (stumps) and assigns different weights to each stump based on its accuracy.

- **Order and Sequence**: In AdaBoost, the order of the stumps is important because errors are passed on in sequence. In [[Random Forests]], trees are built independently and simultaneously.

### Advantages of AdaBoost:

- **Increased Accuracy**: By focusing on the errors of previous models, AdaBoost can significantly improve the accuracy of predictions.
- **Simplicity**: AdaBoost is relatively simple to implement and understand compared to other ensemble methods.
- **Flexibility**: It can be applied to various types of base models and is not limited to a specific algorithm.

### Challenges of AdaBoost:

- **Sensitivity to Noisy Data**: AdaBoost can be sensitive to noisy data and outliers, as it focuses heavily on correcting errors.
- **Complexity**: While simpler than some other boosting methods, AdaBoost can still be computationally intensive due to its sequential nature.