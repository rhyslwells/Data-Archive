#ml

Overfitting is when;; the model fits the training data too well can be generalised.

[[overfitting]] is when a model memorises the training data.

## Q&A's

What is [[overfitting]];; Overfitting is when model fits training data too well (low bias, high complexity). Underfitting is the oppiste and has high bias and fails to capture underlying patterns.

What does [[overfitting]] do;; Results in the model not being good with new data (high variance).

How do you know if a model is [[overfitting]] [[overfitting]]?;; Compare performance with different test data, look for large variance.

How do you prevent [[overfitting]]?
?
- Use simpler models. 
- Use [[Regularisation]] to penalise the Lose function (Lasso and Ridge), one way to simplfy the model. 
- Use [[Cross validation]] (dividing data up for training & testing with different parts).
- Use early stopping to halt training process before its begins capturing noise.
