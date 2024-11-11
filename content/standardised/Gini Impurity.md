Gini impurity is a metric used in decision trees to measure the degree or probability of misclassification in a dataset. It is associated with the leaves of a [[Decision Tree]] and helps determine the best split at each node.

## Calculation

- Mathematical Formula: Gini impurity is calculated as the probability of incorrectly classifying a randomly chosen element if it were randomly labeled according to the distribution of labels in the subset.
- Formula: 

  $$ \text{Gini Impurity} = 1 - \sum_{i=1}^{n} p_i^2 $$
  where $p_i$ is the probability of an element being classified into a particular class.

## Usage

- Decision Trees: Gini impurity is commonly used in decision trees to evaluate splits. A lower Gini impurity indicates a better split, as it means the data is more homogeneously classified.
- [[Classification]] Tasks: It is particularly useful in classification tasks where the goal is to minimize misclassification.

## Relationship to Other Metrics

- Gini impurity is one of several [[Regression metrics]] used to evaluate the performance of decision trees, alongside others like entropy.

