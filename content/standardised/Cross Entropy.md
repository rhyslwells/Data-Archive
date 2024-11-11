---
tags:
  - model_architecture
  - ml_optimisation
---
Cross entropy is a [[Loss function]] used in [[Classification]] tasks, particularly for [[categorical data]]. The cross entropy loss function is particularly effective for multi-class classification problems, where the goal is to assign an input to one of several categories. 

Cross entropy works by measuring the (difference/loss) ==dissimilarity between two probability distributions==: the true distribution (actual class labels) and the predicted distribution (model's output probabilities). 

By minimizing cross entropy, the model learns to produce probability distributions that closely match the true class distributions, thereby improving its classification ==accuracy==.

1. **Probability Distributions**: In a classification task, the model outputs a probability distribution over the possible classes for each input. For example, in a three-class problem, the model might output probabilities like [0.7, 0.2, 0.1] for classes A, B, and C, respectively.

2. **True Labels**: The true class label is represented as a one-hot encoded vector. If the true class is A, the vector would be [1, 0, 0].

3. **Cross Entropy Calculation**: Cross entropy calculates the loss by comparing the predicted probabilities with the true labels. The formula for cross entropy loss $L$ for a single instance is:

   $$ L = -\sum_{i=1}^{N} y_i \log(p_i)$$

   where:
   - $N$ is the number of classes.
   - $y_i$ is the true label (1 if the class is the true class, 0 otherwise).
   - $p_i$ is the predicted probability for class $i$.

2. **Interpretation**: The cross entropy loss increases as the predicted probability diverges from the actual label. If the model assigns a high probability to the correct class, the loss is low. Conversely, if the model assigns a low probability to the correct class, the loss is high.

3. **Optimization**: During training, the model's parameters are adjusted to minimize the cross entropy loss across all training examples. This process helps the model improve its predictions over time.

## Example

Let's consider a three-class classification problem with classes A, B, and C. Suppose we have a single data point with the true class label being A. The true label in one-hot encoded form would be [1, 0, 0].

Assume the model predicts the following probabilities for this data point:

- Probability of class A: 0.7
- Probability of class B: 0.2
- Probability of class C: 0.1

The predicted probability vector is [0.7, 0.2, 0.1].

To calculate the cross entropy loss for this example, we use the formula:

$L = -\sum_{i=1}^{N} y_i \log(p_i)$

Substituting the values:

- For class A: $y_1 = 1$ and $p_1 = 0.7$
- For class B: $y_2 = 0$ and $p_2 = 0.2$
- For class C: $y_3 = 0$ and $p_3 = 0.1$

The cross entropy loss $L$ is calculated as:

$L = -(1 \cdot \log(0.7) + 0 \cdot \log(0.2) + 0 \cdot \log(0.1))$

$L = -(\log(0.7))$

$L \approx -(-0.3567) = 0.3567$

So, the cross entropy loss for this example is approximately 0.3567. This value represents the penalty for the model's predicted probabilities not perfectly matching the true class distribution. The lower the loss, the better the model's predictions align with the true labels.