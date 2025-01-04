Gini impurity is a metric used in decision trees to measure the degree or probability of misclassification in a dataset. It is associated with the leaves of a [[Decision Tree]] and helps determine the best split at each node.
## Calculation

- Mathematical Formula: Gini impurity is calculated as the probability of incorrectly classifying a randomly chosen element if it were randomly labelled according to the distribution of labels in the subset.
- Formula: 

  $$ \text{Gini Impurity} = 1 - \sum_{i=1}^{n} p_i^2 $$
  where $p_i$ is the probability of an element being classified into a particular class.

## Usage

- Decision Trees: Gini impurity is commonly used in decision trees to evaluate splits. A lower Gini impurity indicates a better split, as it means the data is more homogeneously classified.
- [[Classification]] Tasks: It is particularly useful in classification tasks where the goal is to minimize misclassification.

## Relationship to Other Metrics

- Gini impurity is one of several [[Regression Metrics]] used to evaluate the performance of decision trees, alongside others like entropy.

## Example

Suppose you have a dataset with a binary classification problem, where the target variable can be either "Yes" or "No". You have a node in your decision tree with the following distribution of classes:

- 10 samples labeled "Yes"
- 5 samples labeled "No"

### Gini Impurity Calculation

The formula for Gini impurity is:

$$ \text{Gini impurity} = 1 - \sum (p_i^2) $$

where$p_i$ is the proportion of class$i$ in the node.

#### Step-by-Step Calculation

1. **Calculate the proportion of each class**:
   - Total samples = 10 (Yes) + 5 (No) = 15
   - Proportion of "Yes" =$\frac{10}{15} = 0.67$
   - Proportion of "No" =$\frac{5}{15} = 0.33$

2. **Calculate the squared proportions**:
   - $(0.67)^2 = 0.4489$
   - $(0.33)^2 = 0.1089$

3. **Sum the squared proportions**:
   - Sum =$0.4489 + 0.1089 = 0.5578$

4. **Calculate the Gini impurity**:
   - Gini impurity =$1 - 0.5578 = 0.4422$


A Gini impurity of 0.4422 indicates the level of impurity in this node. A Gini impurity of 0 would mean the node is pure (all samples belong to one class), while a higher value indicates more impurity or mixed classes.

This calculation helps in deciding whether to split the node further or not. The goal is to choose splits that ==minimize the Gini impurity==, leading to more homogeneous branches.