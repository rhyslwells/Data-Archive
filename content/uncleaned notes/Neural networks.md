#deep_learning #focus 

Number of starting nodes depends on input parameter, similar for output.

The width and the depth of the net are called [[hyperparameter]].

Non linear functions at nodes are called [[Activation Function]]. Common activation functions:
sigmoid, TanH, RELu,softmax. But how to choose them?

Methods to get parameters (weights biases) for NN using training data to reduce the errors in predictions: 

	[[Forward propagation]] is the process of pushing inputs through the net NN. At the end of each [[epoch]], the obtained outputs are
	compared to targets to form the errors.
	
	[[Backpropagation]] of errors is an algorithm for neural networks using gradient descent. It consists of calculating
	the contribution of each parameter to the errors. We backpropagate the errorsthrough the net and update the
	parameters (weights and biases) accordingly.