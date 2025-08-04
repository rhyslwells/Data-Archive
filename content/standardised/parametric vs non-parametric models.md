---
aliases: []
category:
date modified: 1-08-2025
tags: [statistics]
---

### Parametric Models [[parametric]]

Definition: Models that summarize data with a ==set of parameters of fixed size, regardless of the number of data points.==

Characteristics:
  - Assumes a specific form for the function mapping inputs to outputs (e.g., linear regression assumes a linear relationship).
  - Requires estimation of a finite number of parameters.
  - Generally faster to train and predict due to their simplicity.
  - Risk of underfitting if the model assumptions do not align well with the data.

  Examples: 
  - Linear [[Regression]], [[logistic regression]], neural networks (with a fixed architecture).

### Non-parametric Models [[non-parametric]] Models

Definition: Models that do ==not assume a fixed form for the function== mapping inputs to outputs and can grow in complexity with more data.

Characteristics:
  - Do not make strong assumptions about the underlying data distribution.
  - Can adapt to the data's complexity, potentially capturing more intricate patterns.
  - Generally require more data to make accurate predictions.
  - Risk of overfitting, especially with small datasets, as they can model noise in the data.

Examples: 
- K-nearest neighbors, decision trees, [[support vector machines]] (with certain kernels).

### Key Differences

- Flexibility: Non-parametric models are more flexible and can model complex relationships, while parametric models are simpler and rely on assumptions about the data.
- Data Requirements: Non-parametric models typically require more data to achieve good performance compared to parametric models.
- Computation: Parametric models are usually computationally less intensive than non-parametric models.
