# notes

[[Cost Function]] value versus number of iterations of [[Gradient Descent]] should decrease

Can use contour plots to show [[Gradient Descent#]] moving towards minima.
![[Pasted image 20241224082847.png]]


## [[Feature Scaling]]

Done when one feature is at a significantly different scale.

For each data point, subtract the mean and then divide by the range (max-min).

![[Pasted image 20241224083928.png]]

# [[Feature Engineering]]

![[C1_W2_Lab07_FeatureEngLecture.png]]

# Z- normalisation /[[Normalisation vs Standardisation]]

 We do this inorder to 
 
The peak to peak range of each column is reduced from a factor of thousands to a factor of 2-3 by normalization.

Notice, above, the range of the normalized data (x-axis) is centered around zero and roughly +/- 2. Most importantly, the range is similar for each feature.

Doing this allows for [[Gradient Descent]]s [[learning rate]] is much larger.

![[Pasted image 20241224091151.png]]

![[Pasted image 20241224091157.png]]

  
  ### z-score normalization

After z-score normalization, all features will have a mean of 0 and a standard deviation of 1.

  

To implement z-score normalization, adjust your input values as shown in this formula:

$$x^{(i)}_j = \dfrac{x^{(i)}_j - \mu_j}{\sigma_j} \tag{4}$$

where $j$ selects a feature or a column in the $\mathbf{X}$ matrix. $µ_j$ is the mean of all the values for feature (j) and $\sigma_j$ is the standard deviation of feature (j).

$$

\begin{align}

\mu_j &= \frac{1}{m} \sum_{i=0}^{m-1} x^{(i)}_j \tag{5}\\

\sigma^2_j &= \frac{1}{m} \sum_{i=0}^{m-1} (x^{(i)}_j - \mu_j)^2  \tag{6}

\end{align}

$$

  

>Implementation Note: When normalizing the features, it is important

to store the values used for normalization - the mean value and the standard deviation used for the computations. After learning the parameters

from the model, we often want to predict the prices of houses we have not

seen before. Given a new x value (living room area and number of bed-

rooms), we must first normalize x using the mean and standard deviation

that we had previously computed from the training set.




  

Implementation

```python
def zscore_normalize_features(X):
    """
    computes  X, zcore normalized by column
    
    Args:
      X (ndarray (m,n))     : input data, m examples, n features
      
    Returns:
      X_norm (ndarray (m,n)): input normalized by column
      mu (ndarray (n,))     : mean of each feature
      sigma (ndarray (n,))  : standard deviation of each feature
    """
    # find the mean of each column/feature
    mu     = np.mean(X, axis=0)                 # mu will have shape (n,)
    # find the standard deviation of each column/feature
    sigma  = np.std(X, axis=0)                  # sigma will have shape (n,)
    # element-wise, subtract mu for that column from each example, divide by std for that column
    X_norm = (X - mu) / sigma      

    return (X_norm, mu, sigma)
 
#check our work
#from sklearn.preprocessing import scale
#scale(X_orig, axis=0, with_mean=True, with_std=True, copy=True)
```
![[Pasted image 20241224091007.png]]



# notes

[[Bellman Equations]]

# notes

In [[Tensorflow]] how do we build a simple neural network with say 4 layers.

# [[Logistic Regression]]

Recall that for logistic regression, the model is represented as

$$ f_{\mathbf{w},b}(x) = g(\mathbf{w}\cdot \mathbf{x} + b)$$
where function $g$ is the sigmoid function. The sigmoid function is defined as:

$$g(z) = \frac{1}{1+e^{-z}}$$
Cost function for logistic regression:

Gradient for logistic regression:

Regularized logistic regression:

Cost function for regularized logistic regression

# [[Regularisation]]

Computing the Gradient with regularization (both linear/logistic)

The gradient calculation for both linear and logistic regression are nearly identical, differing only in computation of $f_{\mathbf{w}b}$.

$$\begin{align*}

\frac{\partial J(\mathbf{w},b)}{\partial w_j}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{\mathbf{w},b}(\mathbf{x}^{(i)}) - y^{(i)})x_{j}^{(i)}  +  \frac{\lambda}{m} w_j \tag{2} \\

\frac{\partial J(\mathbf{w},b)}{\partial b}  &= \frac{1}{m} \sum\limits_{i = 0}^{m-1} (f_{\mathbf{w},b}(\mathbf{x}^{(i)}) - y^{(i)}) \tag{3}

\end{align*}$$

* m is the number of training examples in the data set      
* $f_{\mathbf{w},b}(x^{(i)})$ is the model's prediction, while $y^{(i)}$ is the target

  * For a  <span style="color:blue"> linear </span> regression model  
    $f_{\mathbf{w},b}(x) = \mathbf{w} \cdot \mathbf{x} + b$  

* For a <span style="color:blue"> logistic </span> regression model  
    $z = \mathbf{w} \cdot \mathbf{x} + b$  
    $f_{\mathbf{w},b}(x) = g(z)$  
    where $g(z)$ is the sigmoid function:  
    $g(z) = \frac{1}{1+e^{-z}}$  

The term which adds regularization is  the $\frac{\lambda}{m} w_j$.

# [[Optimisation function]]

LBFGS stands for Limited-memory Broyden-Fletcher-Goldfarb-Shanno, which is an optimization algorithm used to find the minimum of a function. In the context of logistic regression, LBFGS is a method for optimizing the cost function to find the optimal model parameters (such as the intercept and coefficients).

Here's a breakdown of the key features of LBFGS:

1. Quasi-Newton Method: LBFGS is a type of Quasi-Newton method, which approximates the inverse of the Hessian matrix (second-order derivatives of the cost function). Instead of computing the full Hessian matrix, it uses an approximation, which makes it more efficient for large datasets.
    
2. Limited Memory: The "limited-memory" part refers to the fact that LBFGS does not store the entire Hessian matrix, which is computationally expensive and memory-intensive. Instead, it keeps a limited amount of information from previous iterations, making it well-suited for large-scale problems where full memory-based methods might not be feasible.
    
3. Optimization for Smooth, Differentiable Functions: It is designed to optimize smooth, differentiable functions like the cost function in logistic regression.
    

In the context of logistic regression with sklearn, LBFGS is used as a solver for optimization. When you set `solver='lbfgs'`, sklearn's logistic regression uses this algorithm to iteratively adjust the model parameters (the intercept and coefficients) to minimize the logistic loss (the cost function) while possibly incorporating regularization.

LBFGS is often preferred for its efficiency and ability to converge quickly without needing a lot of iterations, especially when the number of features is large.

# [[Adam Optimizer]]

### 1. Momentum in Gradient Descent:

Momentum is a technique that helps accelerate gradient descent by adding a fraction of the previous update to the current update. It helps smooth out oscillations and can lead to faster convergence. Momentum is typically controlled by a hyperparameter $\beta$ (often close to 1).

#### Steps to Implement Momentum:

- Formula: vt+1=βvt+(1−β)∇θJ(θ)v_{t+1} = \beta v_t + (1 - \beta) \nabla_{\theta} J(\theta)vt+1​=βvt​+(1−β)∇θ​J(θ) θt+1=θt−αvt+1\theta_{t+1} = \theta_t - \alpha v_{t+1}θt+1​=θt​−αvt+1​ Where:
    - $v_t$ is the velocity (the accumulated gradient).
    - $\beta$ is the momentum factor (commonly set to 0.9 or 0.99).
    - $\nabla_{\theta} J(\theta)$ is the gradient of the cost function with respect to the parameters $\theta$.
    - $\alpha$ is the learning rate.

#### To explore it:

- Implement momentum in your custom gradient descent function.
- Experiment with different values of $\beta$ (e.g., 0.9, 0.99) and observe the changes in the convergence speed.
- Compare the results with standard gradient descent by plotting the cost function over iterations.

### 2. Adaptive Learning Rates (e.g., Adam Optimizer):

Adaptive learning rates adjust the learning rate for each parameter based on the estimates of the first and second moments of the gradients. Adam (short for Adaptive Moment Estimation) combines ideas from momentum and adaptive learning rates to help the optimization process.




# [[Implementing Neural network]]

[[Neural network]]


at each leaner of a neural net , we need to shape the input so the vector can go into the layer.

  [Keras Guide](https://keras.io/guides/sequential_model/)

There are weights and biases at each layer. The shape of the weights is determined by the number of units in the previous layer and the number of units in the current layer.

# Fitting weights and biases of a neural network

For a neural network model how to fit weights and biases?

Fitting weights and biases in a neural network involves optimizing these parameters so the model learns to map input features ($X$) to target outputs ($y$) effectively. This is achieved through the training process, which minimizes the error between predictions and actual values.
## 1. Initialization of Weights and Biases

Proper initialization is critical for training to converge efficiently:

### Weights:

- Use small random values (e.g., drawn from Gaussian or uniform distributions).
- Initialization techniques like He initialization (for ReLU activations) or Xavier initialization (for sigmoid/tanh activations) are commonly used.

```python
from tensorflow.keras.layers import Dense
from tensorflow.keras.initializers import HeNormal

# Example of He initialization for ReLU activation
Dense(25, activation="relu", kernel_initializer=HeNormal())
```
### Biases:

- Start with zeros (`0`) to ensure symmetry-breaking during optimization.

## 2. Forward Propagation

During forward propagation:

1. Compute activations using the current weights and biases/
2. Pass activations to subsequent layers to generate predictions.
## 3. Loss Function

The loss function quantifies the difference between predicted outputs and true labels. Common choices include:

- Binary Cross-Entropy: For binary classification.
- Categorical Cross-Entropy: For multi-class classification.
- Mean Squared Error (MSE): For regression tasks.

Example:

```python
from tensorflow.keras.losses import BinaryCrossentropy
loss_fn = BinaryCrossentropy()
```
## 4. Backward Propagation

Backpropagation computes the gradients of the loss function with respect to weights and biases using the chain rule:

1. Gradients measure how changes in weights and biases affect the loss.
2. Backpropagation adjusts the parameters to reduce the loss.

## 5. Gradient Descent Optimization

Gradients from backpropagation are used to update weights and biases iteratively:

### Basic Gradient Descent:

### Enhanced Optimizers:

- Adam, RMSprop, and SGD with momentum accelerate convergence and handle larger datasets effectively.

Example:

```python
from tensorflow.keras.optimizers import Adam
optimizer = Adam(learning_rate=0.001)
```
## 6. Batch Training

Weights and biases are updated after processing a batch of data:

1. Batch Size: Defines the number of samples processed before updating weights.
    - Small batch sizes (e.g., 32, 64) offer a balance between noisy gradients and computational efficiency.
2. Epochs: Number of full passes through the training data.

## 7. Regularization Techniques

Prevent overfitting by penalizing large weights:

### L2 Regularization (Ridge Regression):

Adds a penalty term to the loss: Lregularized=L+λ⋅∣∣W∣∣2L_{\text{regularized}} = L + \lambda \cdot ||W||^2

Example:

```python
from tensorflow.keras.regularizers import l2
Dense(25, activation="relu", kernel_regularizer=l2(0.01))
```
### Dropout:

Randomly drops units during training to improve generalization.

```python
from tensorflow.keras.layers import Dropout
Dropout(0.5)
```
## 8. Learning Rate Tuning

Learning rate impacts convergence:

- Too high: Can lead to divergence or unstable training.
- Too low: Results in slow convergence.

### Techniques:

- Learning Rate Scheduling: Reduce learning rate as training progresses.
- Adaptive Learning Rates: Optimizers like Adam dynamically adjust learning rates.

Example:

```python
from tensorflow.keras.callbacks import LearningRateScheduler

def scheduler(epoch, lr):
    return lr * 0.1 if epoch >= 10 else lr

lr_callback = LearningRateScheduler(scheduler)
```

## 9. Monitoring and Early Stopping

Track model performance on a validation set to avoid overfitting:

- Use early stopping to halt training if the validation loss stops improving.

Example:

```python
from tensorflow.keras.callbacks import EarlyStopping

callback = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model.fit(X_train, y_train, validation_data=(X_val, y_val), callbacks=[callback])
```



## Example: Complete Training Script

```python
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import LearningRateScheduler, EarlyStopping
from tensorflow.keras.regularizers import l2
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Mock data for demonstration
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=400, n_classes=2, random_state=42)
y = y.reshape(-1, 1)

# Train-validation-test split
from sklearn.model_selection import train_test_split
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Learning rate scheduler
def scheduler(epoch, lr):
    return lr * 0.1 if epoch >= 10 else lr
lr_callback = LearningRateScheduler(scheduler)

# Early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Build the model
model = Sequential([
    Dense(64, activation='relu', kernel_initializer='he_normal', kernel_regularizer=l2(0.01), input_shape=(400,)),
    Dropout(0.5),
    Dense(32, activation='relu', kernel_initializer='he_normal', kernel_regularizer=l2(0.01)),
    Dropout(0.5),
    Dense(1, activation='sigmoid', kernel_initializer='glorot_uniform')
])

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=30,
    batch_size=32,
    callbacks=[lr_callback, early_stopping]
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}")

# Predictions
y_pred = (model.predict(X_test) > 0.5).astype(int)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title("Loss over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
```
## Summary of Best Practices

1. Use appropriate weight initializations like He or Xavier.
2. Choose a suitable loss function for the task.
3. Optimize using advanced optimizers like Adam or RMSprop.
4. Experiment with batch sizes, epochs, and learning rates.
5. Apply regularization (L2, Dropout) to prevent overfitting.
6. Monitor validation metrics and use early stopping.

# Dense Layer Subroutine

A dense layer connects every neuron in the layer to every neuron in the previous layer. Each connection is associated with a weight, and every neuron has an associated bias. The dense layer performs two main steps: Linear transform and a non-linear activation.

A dense layer subroutine can be considered a function that operates on the entire layer and applies the transformation above to all inputs simultaneously.

The dense layer subroutine:
1. Implements linear transformations to combine inputs.
2. Introduces non-linearity for complex decision boundaries.
3. Enables feature extraction and mapping inputs to outputs.
4. Learns patterns and representations through optimization during training.

The purpose of a dense layer subroutine in a neural network is to perform the fundamental computations that enable learning and decision-making. 
### 1. Aggregates and Transforms Information

- A dense layer gathers information from all neurons in the previous layer and combines it linearly: $z=W⋅X+bz$
- The weights (W) determine the strength of the connections, while biases (b) shift the output.
- This transformation allows the layer to adjust inputs into forms better suited for solving the task at hand.
### 2. Adds Non-Linearity for Model Expressiveness

- After the linear transformation, a dense layer often applies a non-linear activation function like ReLU, sigmoid, or tanh: $a=activation(z)$
- This step introduces non-linearity, enabling the network to model complex relationships in data.
### 3. Learns Patterns and Features & Supports Decision Making

- Dense layers learn abstract features from data as information flows through the network:
    - Early layers capture low-level features (e.g., edges in images).
    - Later layers capture high-level features (e.g., shapes, objects, or classes)
    
- In the final layers of a network, dense layers aggregate the learned features to make predictions:
    - Classification tasks: Output probabilities for classes.
    - Regression tasks: Output continuous values.

### 5. Maps Input to Output

- Dense layers enable dimensionality changes:
    - Reduce dimensionality (e.g., compress information in hidden layers).
    - Expand dimensionality (e.g., map features to multiple classes in output layers).

### Example: Dense Layer in a Neural Network

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example dense layers in a neural network
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),  # Input: Flattened image (28x28)
    Dense(64, activation='relu'),                      # Hidden layer: 64 neurons
    Dense(10, activation='softmax')                    # Output: 10 classes
])
```
# Test loss when evaluating models

The test loss is important because it provides insight into how well a model generalizes to unseen data, which is crucial for understanding its performance in real-world applications. While test accuracy indicates how many predictions were correct, test loss measures the magnitude of errors in those predictions. 

While test accuracy is important, test loss provides complementary information that helps ensure the model is not just predicting correctly, but is also making accurate, reliable, and well-calibrated predictions. Depending on your application, you might care more about accuracy (e.g., in some classification tasks) or loss (e.g., when evaluating the confidence of predictions or calibrating probabilistic models). For most real-world problems, balancing both is crucial.

### 1. Balance between Accuracy and Error Magnitude

- Test accuracy tells you the percentage of correct predictions, but it doesn't account for the degree of correctness. For example, a model might predict class 1 with high confidence (e.g., 0.99) and still be wrong. The test loss (typically calculated as cross-entropy or mean squared error for classification tasks) would be high in this case, despite a high accuracy.
- Test loss can reveal situations where the model is confident but wrong, or the model is struggling even though it is correct in many cases. This distinction helps us understand the quality of predictions beyond simple accuracy.

### 2. Overfitting or Underfitting Detection

- If a model has high accuracy but a high test loss, it might be overfitting to the training data (memorizing patterns rather than learning the underlying structure).
- A model with low accuracy and high test loss could be underfitting, meaning it hasn't learned the data well enough.
### 3. Model Calibration

- In some applications, such as probabilistic models, a model that outputs probability values, test loss is important for understanding how well the model is calibrated. A model that’s accurate but poorly calibrated (where predicted probabilities don't match true outcomes) will have a low test accuracy but high loss.
- For example, in classification tasks, cross-entropy loss is used, and the test loss can indicate how confidently and correctly the model assigns probabilities to each class.

### 4. Hyperparameter Optimization

- When tuning hyperparameters (e.g., learning rate, batch size), you might observe that a configuration produces high test accuracy but poor test loss (or vice versa). By considering both metrics, you get a more balanced view of performance, which helps in fine-tuning the model to achieve both high accuracy and low error.

### 5. Model Comparison

- Sometimes, multiple models can achieve similar accuracy, but their losses can differ significantly. The model with the lower test loss is generally preferred as it suggests the model is not just accurate but also reliable in predicting probabilities, especially in critical applications like medical diagnoses or risk assessment.

### 6. Outlier Sensitivity

- Test loss might also help identify when a model is sensitive to outliers. A model could achieve high accuracy but perform poorly in terms of test loss if it's incorrectly classifying a few outliers but still achieving overall correctness. In contrast, a model with low test loss might be more stable in terms of making predictions, even for edge cases.


# [[Optuna]]

### In summary:
- Optuna automates the process of tuning the hyperparameters of a machine learning model. It does this by defining an objective function where different combinations of hyperparameters are tested, training the model, and evaluating its performance.
- The best set of hyperparameters is chosen based on the performance metric (test accuracy in this case) returned by the objective function.
### Benefits of Using Optuna:

1. Efficient Search: Optuna uses algorithms like TPE (Tree-structured Parzen Estimator) to search the hyperparameter space more efficiently than grid search.
2. Dynamic Search Space: Optuna can search across continuous, categorical, and discrete spaces.
3. Automatic Pruning: Optuna supports pruning of unpromising trials during training, improving computational efficiency.
4. Visualization: Optuna provides built-in tools for visualizing the optimization process, making it easier to understand the impact of hyperparameters.

Optuna is an automatic hyperparameter optimization library that helps you find the best hyperparameters for your machine learning model. Here's a simplified breakdown of what Optuna is doing in the provided code:

### 1. Creating an Optimization Study:
```python
study = optuna.create_study(direction='maximize')
```
- Optuna begins by creating a study. The study is essentially the container for tracking and managing the optimization process. 
- The `direction='maximize'` tells Optuna to maximize the output of the objective function. In this case, the objective is to maximize the model's test accuracy.

### 2. Defining the Objective Function:
```python
def objective(trial):
```
- Objective function: This is the function that Optuna will optimize. It defines the model, how it's trained, and how its performance is evaluated.
- The goal of the objective function is to return a score (test accuracy in this case), which Optuna will use to decide if the current trial is successful.

### 3. Suggesting Hyperparameters:
Inside the objective function, Optuna suggests values for the model's hyperparameters by using different `trial.suggest_*` methods:
```python
learning_rate = trial.suggest_loguniform('learning_rate', 1e-5, 1e-2)
batch_size = trial.suggest_categorical('batch_size', [32, 64, 128])
dropout = trial.suggest_uniform('dropout', 0.2, 0.5)
units_1 = trial.suggest_int('units_1', 64, 128)
```
- Hyperparameters: These are the settings for the model that you want Optuna to optimize, such as the learning rate, batch size, and dropout rate.
- `trial.suggest_*` methods: These methods tell Optuna what types of values to explore for each hyperparameter (e.g., log-uniform for learning rate, categorical for batch size, etc.).
  
### 4. Training the Model:
```python
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=config['epochs'], batch_size=config['batch_size'], callbacks=[...])
```
- Optuna uses the suggested hyperparameters to build and train a Keras model. The model is trained using the `fit()` function with the hyperparameters defined earlier.
- The goal is to evaluate the model's test accuracy to decide whether this set of hyperparameters is good.

### 5. Returning the Result:
```python
return test_accuracy
```
- After training, the model's test accuracy is returned as the result of the trial.
- Optuna uses this score to evaluate how well this set of hyperparameters performed.

### 6. Optimization:
```python
study.optimize(objective, n_trials=15)
```
- This line starts the optimization process.
- Optuna runs the `objective` function multiple times (in this case, 15 times). Each time, it tries different hyperparameter combinations.
- It uses the result (test accuracy) to decide which hyperparameters are performing best.

### 7. Best Trial:
```python
best_trial = study.best_trial
```
- After all trials, Optuna identifies the best trial, which is the trial with the highest test accuracy.
- The hyperparameters that led to this best performance are stored in `best_trial.params`.


[[K-means]]
# Anomaly Detection

Example: You have a dataset of servers unlabled We aim to detect those that do not work (anomalies).

Guassian model

To perform anomaly detection, you will first need to fit a model to the data’s distribution.

* Given a training set $\{x^{(1)}, ..., x^{(m)}\}$ you want to estimate the Gaussian distribution for each
of the features $x_i$. 

* Recall that the Gaussian distribution is given by

   $$ p(x ; \mu,\sigma ^2) = \frac{1}{\sqrt{2 \pi \sigma ^2}}\exp^{ - \frac{(x - \mu)^2}{2 \sigma ^2} }$$

   where $\mu$ is the mean and $\sigma^2$ controls the variance.
   
* For each feature $i = 1\ldots n$, you need to find parameters $\mu_i$ and $\sigma_i^2$ that fit the data in the $i$-th dimension $\{x_i^{(1)}, ..., x_i^{(m)}\}$ (the $i$-th dimension of each example).

You can estimate the parameters, ($\mu_i$, $\sigma_i^2$), of the $i$-th
feature by using the following equations. To estimate the mean, you will
use:

$$\mu_i = \frac{1}{m} \sum_{j=1}^m x_i^{(j)}$$

and for the variance you will use:
$$\sigma_i^2 = \frac{1}{m} \sum_{j=1}^m (x_i^{(j)} - \mu_i)^2$$



 Low proabaility of being togerher.
Make a 2D plot of two features. Permute feature cominbations if necessary.

What is multivariate guassian?

* The low probability examples are more likely to be the anomalies in our dataset. 
* One way to determine which examples are anomalies is to select a threshold based on a cross validation set. 
What epsilon to choose

# Reinforcement Learning

Use import gym

Action Space: What actions are available to the agent?
Observation Space: What information is available to the agent?
Reward Envioronment: What rewards can be given to the agent?

Loads the enviroemnt for examples
env = gym.make('LunarLander-v2')

Can step though the environment dynamics
next_state, reward, done, info = env.step(action)

```python
# Select an action
action = 0

# Run a single time step of the environment's dynamics with the given action.
next_state, reward, done, info = env.step(action)

with np.printoptions(formatter={'float': '{:.3f}'.format}):
    print("Initial State:", initial_state)
    print("Action:", action)
    print("Next State:", next_state)
    print("Reward Received:", reward)
    print("Episode Terminated:", done)
    print("Info:", info)
```

# Deep Q-Learning

Target Network?- when does this occur/when is it needed.
The target can be changed per iteration. Use soft update to change the target slowly.

Experience Relay?
What issue does this aim to resolve, give an example where this causes an issue.
When an agent interacts with the environment, the states, actions, and rewards the agent experiences are sequential by nature. 
If the agent tries to learn from these consecutive experiences it can run into problems due to the strong correlations between them. 
To avoid this, we employ a technique known as Experience Replay to generate uncorrelated experiences for training our agent. 
Experience replay consists of storing the agent's experiences (i.e the states, actions, and rewards the agent receives) in 
a memory buffer and then sampling a random mini-batch of experiences from the buffer to do the learning. The
 experience tuples $(S_t, A_t, R_t, S_{t+1})$ will be added to the memory buffer at each time step as the agent interacts with 
 the environment. By using experience replay we avoid problematic correlations, oscillations and instabilities. In addition, 
 experience replay also allows the agent to potentially use the same experience in multiple weight updates, which increases data 
 efficiency.

# Neurons

each neural network needs to be instantiated.

neuron can mini a linear regression. 

Can apply a activation function to the output of the neuron, i.e in logisitc regression. - which is linear regression with a sigmoid activation.

Examples: logistic and linear regression neurons.

Neural model types:
- Sequential

You can get out the layers of a neural net model, and the weights at that layer. You can set the weights at a given layer.

Fitting weights to a neural net model, works better if the data is normalized.

In keras you can:
- adapt, to learn the mean and varience of a dataset.

Normalisation example of a neural network.
Use sample dataset, with output
```python
print(f"Temperature Max, Min pre normalization: {np.max(X[:,0]):0.2f}, {np.min(X[:,0]):0.2f}")
print(f"Duration    Max, Min pre normalization: {np.max(X[:,1]):0.2f}, {np.min(X[:,1]):0.2f}")
norm_l = tf.keras.layers.Normalization(axis=-1)
norm_l.adapt(X)  # learns mean, variance
Xn = norm_l(X)
print(f"Temperature Max, Min post normalization: {np.max(Xn[:,0]):0.2f}, {np.min(Xn[:,0]):0.2f}")
print(f"Duration    Max, Min post normalization: {np.max(Xn[:,1]):0.2f}, {np.min(Xn[:,1]):0.2f}")
```

At the compile stage of a keras model
in a keras model there is keras.losses.BinaryCrossentropy amd keras.optimizers.Adam. What are these?

Why do we have a number of epochs N? 
The data gets applied to the model N times.
N=10
```
Epoch 1/10
6250/6250 [==============================] - 6s 910us/step - loss: 0.1782
```
The first line, `Epoch 1/10`, describes which epoch the model is currently running. For efficiency, the training data set is broken into 'batches'. The default size of a batch in Tensorflow is 32. There are 200000 examples in our expanded data set or 6250 batches. The notation on the 2nd line `6250/6250 [====` is describing which batch has been executed.

Can use neural networks for multi-class prediction.
The final proabilities with be over the number of classes.

In tensorflow the input dimension of the the first later is based on the size of the input. However it is possible to include an input layer that specifies the input dimension of the first layer.

### 4.5 Softmax placement at end?
Numerical stability is improved if the softmax is grouped with the loss function rather than the output layer during training. This has implications when *building* the model and *using* the model.  
Building:  
* The final Dense layer should use a 'linear' activation. This is effectively no activation. 
* The `model.compile` statement will indicate this by including `from_logits=True`.
`loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True) `  
* This does not impact the form of the target. In the case of SparseCategorialCrossentropy, the target is the expected digit, 0-9 (MNIST example).

Using the model:
* The outputs are not probabilities. If output probabilities are desired, apply a softmax function.

Why use from_logits=True?

```python
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
)

history = model.fit(
    X,y,
    epochs=40
)
```

 #### Tensorflow historiy Loss  (cost)
We track the progress of gradient descent by monitoring the cost. Ideally, the cost will decrease as the number of iterations of the algorithm increases. Tensorflow refers to the cost as `loss`. Above, you saw the loss displayed each epoch as `model.fit` was executing. The [.fit](https://www.tensorflow.org/api_docs/python/tf/keras/Model) method returns a variety of metrics including the loss. This is captured in the `history` variable above.
What else does historiy capture?



## SparseCategorialCrossentropy or CategoricalCrossEntropy
Tensorflow has two potential formats for target values and the selection of the loss defines which is expected.
- SparseCategorialCrossentropy: expects the target to be an integer corresponding to the index. For example, if there are 10 potential target values, y would be between 0 and 9. 
- CategoricalCrossEntropy: Expects the target value of an example to be one-hot encoded where the value at the target index is 1 while the other N-1 entries are zero. An example with 10 potential target values, where the target is 2 would be [0,0,1,0,0,0,0,0,0,0].

# Backpropgation

Backpropgation is used to calc the gradient of the loss function with respect to the model parameters, when there are a lot of parameters - i.e in a neural network.
Simple example of backpropgation

Simple example of computation graph
Computation graph - calcing derivatives?
Use sympy to calculate derivatives for the loss function.

> The steps in backprop   
>Now that you have worked through several nodes, we can write down the basic method:\
> working right to left, for each node:
>- calculate the local derivative(s) of the node
>- using the chain rule, combine with the derivative of the cost with respect to the node to the right.   

The 'local derivative(s)' are the derivative(s) of the output of the current node with respect to all inputs or parameters.

Example of using sympy to calculate derivatives for the loss function. Use `diff`, `subs`
```python
from sympy import symbols, diff
```

# Training the model to get paramaters.

The test set error shows this model will not work well on new data. If you use the test error to guide improvements in the model, then the model will perform well on the test data... but the test data was meant to represent *new* data.
You need yet another set of data to test new data performance.

The proposal made during lecture is to separate data into three groups. The distribution of training, cross-validation and test sets shown in the below table is a typical distribution, but can be varied depending on the amount of data available.

| data             | % of total | Description |
|------------------|:----------:|:---------|
| training         | 60         | Data used to tune model parameters $w$ and $b$ in training or fitting |
| cross-validation | 20         | Data used to tune other model parameters like degree of polynomial, regularization or the architecture of a neural network.|
| test             | 20         | Data used to test the model after tuning to gauge performance on new data |

```python
# Generate  data
X,y, x_ideal,y_ideal = gen_data(40, 5, 0.7)
print("X.shape", X.shape, "y.shape", y.shape)

#split the data using sklearn routine 
X_train, X_, y_train, y_ = train_test_split(X,y,test_size=0.40, random_state=1)
X_cv, X_test, y_cv, y_test = train_test_split(X_,y_,test_size=0.50, random_state=1)
print("X_train.shape", X_train.shape, "y_train.shape", y_train.shape)
print("X_cv.shape", X_cv.shape, "y_cv.shape", y_cv.shape)
print("X_test.shape", X_test.shape, "y_test.shape", y_test.shape)
```

To find optimial model paramaters, graph the paramater against error of the model. Such as the degree of the polynomial. 
use `train_test_split` to split the data into training and cross-validation sets.

![alt text](image.png)

- On the left plot, the solid lines represent the predictions from these models. A polynomial model with degree 1 produces a straight line that intersects very few data points, while the maximum degree hews very closely to every data point. 
- on the right:
    - the error on the trained data (blue) decreases as the model complexity increases as expected
    - the error of the cross-validation data decreases initially as the model starts to conform to the data, but then increases as the model starts to over-fit on the training data (fails to *generalize*).     

[[Regularisation]]
