---
tags:
  - ml_process
  - ml_optimisation
  - evaluation
  - model_explainability
---
In tree-based models, regularization is not applied in the same way as it is in linear models (i.e., using L1 or L2 penalties). 

In tree models, [[Regularisation]] is done by controlling the growth of the trees using [[hyperparameters]] like 

- `max_depth`,
- `min_samples_split`,
- `min_samples_leaf`.

These hyperparameters restrict the growth of the tree, preventing it from becoming too complex.

For [[Model Ensembling]] methods like Random Forests and Gradient Boosting, additional regularization techniques like 

- subsampling, 
- bootstrap sampling, 
- and learning rate control

to help prevent overfitting. These techniques effectively restrict the model complexity, leading to better generalization .

Below are the common regularization techniques used in tree models such as [[Decision Trees]], [[Random Forests]].
### Regularization Techniques for Tree Models

1. Limiting Tree Depth:
    - Max Depth (`max_depth`): This parameter restricts the maximum depth of the tree. Trees that are too deep can model complex patterns, but they are prone to overfitting. By limiting the depth, you constrain the tree's ability to learn highly specific patterns in the training data.
    - Example: In scikit-learn, setting `max_depth` for a Decision Tree or Random Forest.

    ```python
    from sklearn.tree import DecisionTreeClassifier
    
    # Limit tree depth to regularize the model
    model = DecisionTreeClassifier(max_depth=5)
    model.fit(X_train, y_train)
    ```

2. Minimum Samples for Splitting:
    - Min Samples Split (`min_samples_split`): This parameter specifies the minimum number of samples required to split an internal node. Increasing this value makes the tree more conservative and prevents it from splitting when there are too few samples, thus controlling its complexity.
    - This helps avoid creating splits based on noise, which could lead to overfitting.

    ```python
    model = DecisionTreeClassifier(min_samples_split=10)
    model.fit(X_train, y_train)
    ```

3. Minimum Samples per Leaf:
    - Min Samples Leaf (`min_samples_leaf`): This parameter sets the minimum number of samples a node must have after a split to be a leaf. Higher values result in fewer splits, producing simpler trees that are less likely to overfit.
    - This also encourages broader splits that require more data, reducing the sensitivity to outliers.

    ```python
    model = DecisionTreeClassifier(min_samples_leaf=4)
    model.fit(X_train, y_train)
    ```

4. Max Number of Features:
    - Max Features (`max_features`): This controls the number of features to consider when looking for the best split. Reducing the number of features makes the model less likely to overfit, as it limits the search space for splits. For Random Forests, this also introduces randomness that can improve generalization.

    ```python
    from sklearn.ensemble import RandomForestClassifier
    
    model = RandomForestClassifier(max_features='sqrt')  # Uses sqrt of total features
    model.fit(X_train, y_train)
    ```

5. Max Leaf Nodes:
    - Max Leaf Nodes (`max_leaf_nodes`): This parameter limits the total number of leaf nodes the tree can have. Fewer leaf nodes result in simpler trees that are less likely to overfit the training data.

    ```python
    model = DecisionTreeClassifier(max_leaf_nodes=10)
    model.fit(X_train, y_train)
    ```

6. Subsampling (for Ensemble Methods like Random Forests and Gradient Boosting):
    - Bootstrap Sampling (`bootstrap`): For Random Forests, regularization is achieved through bootstrapping (random sampling with replacement) during training. This introduces variability and helps prevent overfitting.
    - Subsample (`subsample`): For Gradient Boosting, the `subsample` parameter controls the fraction of the training data used for fitting each individual tree. A value less than 1 introduces randomness and reduces the chance of overfitting, similar to how dropout works in neural networks.

    ```python
    from sklearn.ensemble import GradientBoostingClassifier
    
    model = GradientBoostingClassifier(subsample=0.8)  # Use 80% of data for each tree
    model.fit(X_train, y_train)
    ```

7. Learning Rate (for Gradient Boosting Models):

    - Learning Rate (`learning_rate`): This parameter controls how much each tree contributes to the overall model in Gradient Boosting. A lower learning rate slows down the learning process, requiring more trees but helping to avoid overfitting by making small adjustments at each step.

    ```python
    model = GradientBoostingClassifier(learning_rate=0.1)
    model.fit(X_train, y_train)
    ```

8. Pruning:
    - For Decision Trees, pruning is a post-processing regularization technique where branches that contribute little to the overall performance of the model are removed. This prevents the tree from learning noise in the data.
    - In scikit-learn, Cost Complexity Pruning (`ccp_alpha`) is used for pruning. A larger value of `ccp_alpha` leads to more aggressive pruning, simplifying the tree.

    ```python
    model = DecisionTreeClassifier(ccp_alpha=0.01)
    model.fit(X_train, y_train)
    ```

### Regularization in Different Tree Models

- Decision Trees: Prone to overfitting when not regularized, since they tend to grow large and complex trees. Regularization through pruning, limiting tree depth, and controlling minimum samples per split or leaf is critical.

- Random Forests: Regularization is mainly achieved through the use of multiple decision trees, random feature selection (`max_features`), and bootstrapping (`bootstrap`). Each tree learns a different part of the data, which reduces overfitting.

- Gradient Boosting Models (GBMs): Regularized by tuning the `learning_rate`, `subsample`, and controlling the tree depth and other tree-based hyperparameters like `min_samples_split`. The slower learning process with a smaller learning rate combined with these hyperparameters helps prevent overfitting.



