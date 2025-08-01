---
aliases: [LGBM]
category:
date modified: 27-07-2025
tags: [optimisation]
---
LightGBM is a gradient boosting framework that is designed for speed and efficiency. It is particularly well-suited for handling large datasets and high-dimensional data.

- **Tree Growth**: Splits the tree leaf-wise, which can lead to faster convergence compared to level-wise growth.
- **Learning Rate**: Similar to [[Gradient Descent]], LightGBM uses a learning rate to control the contribution of each tree.
- **DART**: A variant of LightGBM known for its performance.
- **Parameter Definition**: Requires parameters to be defined in a dictionary for model configuration.

[Watch Video Explanation](https://www.youtube.com/watch?v=n_ZMQj09S6w)

### Key Parameters

- **Learning Rate**: Controls the step size at each iteration while moving toward a minimum of the loss function.
- **Number of Leaves**: Determines the complexity of the tree model.

### Advantages

- **Speed**: Renowned for its speed, often outperforming other gradient boosting implementations.
- **Memory Usage**: Optimizes memory usage, enabling efficient handling of large datasets.
- **Leaf-Wise Growth**: Grows trees leaf-wise, leading to faster convergence.
- **Parallel and GPU Learning**: Supports parallel and GPU learning for further speedup.

### Use Cases

- **Large Datasets**: Ideal for applications where speed is crucial.
- **High-Dimensional Data**: Efficient when dealing with high-dimensional data and categorical features.