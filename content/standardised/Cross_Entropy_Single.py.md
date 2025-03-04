https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Selection/Cross_Entropy_Single.py
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

### Script Description:

1. **Cross Entropy Function**: Computes the cross entropy loss given true labels and predicted probabilities.
2. **True and Predicted Probabilities Visualization**: Bar plots display the true one-hot encoded labels and the predicted probability distribution.
3. **Cross Entropy Loss Calculation**: Prints the loss value for a sample data point.
4. **Loss Curve**: A line graph shows how the loss changes as the predicted probability for the true class increases.