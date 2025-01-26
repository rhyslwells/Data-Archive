---
tags: 
  - ml_process
  - data_visualization
aliases:
category: DATA_ANALYSIS
phase: Preprocessing
topic: Dimensionality Reduction Techniques
filename: dimensionality_reduction_techniques.py
---
Dimensionality reduction is a step in the [[Preprocessing]] phase of machine learning that helps simplify models, enhance interpretability, and improve computational efficiency.

Its a technique used to reduce the number of input variables (features) in a dataset while retaining as much information as possible. This process is essential for several reasons:

1. **Improves Model Performance**: Reducing the number of features can help improve the performance of machine learning models by minimizing overfitting and reducing noise.

2. **Enhances Visualization**: It allows for easier [[Data Visualisation]] of high-dimensional data by projecting it into lower dimensions (e.g., 2D or 3D).

3. **Reduces Computational Cost**: Fewer features mean less computational power and time required for training models.

### Common Techniques
- **Principal Component Analysis ([[Principal Component Analysis]])**: A statistical method that transforms the data into a new coordinate system, where the greatest variance by any projection lies on the first coordinate ==(principal component/orthogonal components )==, the second greatest variance on the second coordinate, and so on.

- **t-Distributed Stochastic Neighbor Embedding ([[t-SNE]])**: A technique particularly well-suited for visualizing high-dimensional data by reducing it to two or three dimensions while preserving the local structure of the data. t-SNE is a non-linear technique used for visualization and dimensionality reduction by preserving pairwise similarities between data points, making it suitable for exploring high-dimensional data.

- [[Linear Discriminant Analysis]] method used for both classification and dimensionality reduction, which finds a linear combination of features that best separates two or more classes.

### [[Explain the curse of dimensionality]]
