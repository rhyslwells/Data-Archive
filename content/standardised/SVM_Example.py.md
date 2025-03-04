https://github.com/rhyslwells/ML_Tools/tree/main\Explorations\Build\Classifiers\SVM\SVM_Example.py

## **Overview**

- **Objective**: To classify Iris flowers using SVM and explore various hyperparameters like kernel type, regularization (C), and gamma.
- **Dataset**: The Iris dataset contains information about sepal and petal dimensions for three flower species.
- To explore the effect of **soft boundaries** in SVMs, you can adjust the regularization parameter CCC. A smaller CCC allows a **softer boundary** (more margin violations), prioritizing generalization. A larger CCC enforces a **harder boundary** with fewer margin violations, but may lead to overfitting. Here's an extended version of the script to include this exploration:

### **Steps in the Script**

#### 1. **Data Loading and Preparation**

- The Iris dataset is loaded using `sklearn.datasets.load_iris`.
- A DataFrame is created with:
    - Features: Sepal and petal dimensions.
    - Target: Numerical representation of flower species.
    - Flower name: Categorical species name derived from the target.

#### 2. **Data Visualization**

- The data is visualized to explore relationships between features:
    - **Sepal Length vs. Sepal Width** for two species (Setosa vs. Versicolor).
    - **Petal Length vs. Petal Width** for the same species.
- Scatter plots are used to identify separable patterns.

#### 3. **Model Training**

- The data is split into training and testing sets (80%-20%).
- An **SVM classifier** (`sklearn.svm.SVC`) is trained on the training set.
- The model's performance is evaluated using the `.score()` method.

#### 4. **Hyperparameter Tuning**

- **Regularization (C)**:
    - Adjusting `C` controls the trade-off between achieving a large margin and minimizing classification errors.
    - Lower values of `C` allow a larger margin but can tolerate misclassified points.
    - Higher values of `C` prioritize correct classification over a larger margin.
- **Gamma**:
    - Controls the influence of individual data points. A high value means data points closer to the hyperplane have more influence.
- **Kernel**:
    - Different kernels (e.g., `linear`, `rbf`) are tested to find the best mapping of data into higher dimensions for better separation.

#### 5. **Prediction and Accuracy**

- The model is used to predict flower species for new samples.
- The accuracy of the model is reported for each combination of hyperparameters.