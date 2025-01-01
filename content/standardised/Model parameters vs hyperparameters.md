Model parameters and hyperparameters serve different roles:

[[Model Parameters]]
   - These are the internal variables of the model that are learned from the training data. They define the model's structure and are adjusted during the training process to minimize the [[Loss function]].
   - Examples include:
	   - the weights and biases in a neural network,
	   - the coefficients in a linear regression model,
	   - or the support vectors in a support vector machine.
   - Model parameters are directly influenced by the data and are optimized through algorithms like [[gradient descent]].

[[Hyperparameter]]
   - These are external configurations set before the training process begins. They are not learned from the data but are used for controlling the learning process and the model's architecture.
   - Examples include the:
	   - [[learning rate]], 
	   - the number of hidden layers in a [[Neural network]],
	   - the number of trees in a random forest,
	   - or the regularization parameter in a regression model.
   - Hyperparameters are typically tuned through methods like grid search or random search to find the best configuration that results in optimal model performance.