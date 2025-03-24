---
tags:
  - model_architecture
  - ml_optimisation
filename: Cross_Entropy
---
Cross entropy is a [[Loss function]] used in [[Classification]] tasks, particularly for [[categorical data]]. The cross entropy loss function is particularly effective for multi-class classification problems, where the goal is to assign an input to one of several categories. 

==Cross entropy measures confidence.==

Cross entropy works by measuring the (difference/loss) ==dissimilarity between two probability distributions==: the true distribution (actual class labels) and the predicted distribution (model's output probabilities). 

Fit of Predictions:
- A low cross entropy loss means the predicted probabilities are close to the true labels (e.g., assigning high probability to the correct class).
- A high loss indicates significant divergence, meaning the model's predictions are inaccurate or uncertain.

By minimizing cross entropy, the model learns to produce probability distributions that closely match the true class distributions, thereby improving its classification ==accuracy==.

1. Probability Distributions: In a classification task, the model outputs a probability distribution over the possible classes for each input. For example, in a three-class problem, the model might output probabilities like [0.7, 0.2, 0.1] for classes A, B, and C, respectively.

2. True Labels: The true class label is represented as a one-hot encoded vector. If the true class is A, the vector would be [1, 0, 0].

3. Cross Entropy Calculation calculates the loss by comparing the predicted probabilities with the true labels. The formula for cross entropy loss $L$ for a single instance is:

   $$ L = -\sum_{i=1}^{N} y_i \log(p_i)$$

   where:
   - $N$ is the number of classes.
   - $y_i$ is the true label (1 if the class is the true class, 0 otherwise).
   - $p_i$ is the predicted probability for class $i$.

2. Interpretation: The cross entropy loss increases as the predicted probability diverges from the actual label. If the model assigns a high probability to the correct class, the loss is low. Conversely, if the model assigns a low probability to the correct class, the loss is high.

3. Optimization: During training, the model's parameters are adjusted to minimize the cross entropy loss across all training examples. This process helps the model improve its predictions over time.

## Where is it used

Cross entropy is widely used in classification for several reasons:

Probabilistic Modeling:
    - It directly aligns with the goals of probabilistic classifiers, as it measures how well the predicted probability distribution matches the true distribution.
    
Focus on Confidence:
    - Encourages the model to assign higher probabilities to the correct classes, improving not just accuracy but also confidence in predictions.

Optimization Efficiency:
    - Cross entropy is smooth and convex for logistic regression-like models, enabling efficient gradient-based optimization.

Multi-Class Support:
    - Works seamlessly in multi-class scenarios where the true labels are one-hot encoded and predictions are probability distributions.

### Implementation 

In [[ML_Tools]] see: 
- [[Cross_Entropy_Single.py]]
- [[Cross_Entropy.py]]
- [[Cross_Entropy_Net.py]]



