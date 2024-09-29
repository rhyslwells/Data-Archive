---
tags:
  - ml
---
# Questions

What is an ensemble learning method?;;
# Flashcards

What are the most common types of problems that machine learning;; Classification, regression, clustering.

What is classification;; is to predict the category of an input item such as categorising spam emails.

What is the purpose of regression;; the goal of regression is the prediction of a numerical value such as predicting the price of houses.

What is the goal of clustering;; to group items in a way that similar items such as grouping documents by topic.

What are the typical steps of the creation of a machine learning model?;; Problem definition, data prep, model selection, training, evaluation, optimisation, deployment.
  
What is bias in machine learning?;;occurs when a model produces consistently unfair or inaccurate results. Usually caused during training because of design choice.

What does high bias mean for a machine learning model? ;; refers to a situation where a model has a strong and often simplistic bias or assumption about the underlying data, leads to underfitting.

**What is the variance of a machine learning model?**;; The variance in machine learning is the amount by which a model's predictions change when it is trained on different subsets of the training data, variance measures how much the model overfits the training data.

**What is the difference between bias and variance in machine learning?**;; Bias is the error that occurs when the model ==cannot learn the true relationship== between input and output variables. Variance is the error that arises when the model is too sensitive to the training data and ==does not generalize well to new data.==

**Explain the bias-variance trade-off in the context of model complexity.**;; The bias-variance trade-off is the relationship between model complexity and performance. High bias (underfitting) occurs when a model is too simple, leading to poor performance on both training and test data. High variance (overfitting) happens when a model is overly complex, performing well on training data but poorly on new, unseen data.

**What are some techniques that you can use to prevent overfitting in machine learning?**;;
Overfitting happens when your model works well with the training dataset but does not generalize well to new data. To prevent overfitting use ==regularization== and ==cross-validation==. 

**What is regularization?**; used to prevent overfitting in machine learning models. It involves adding a penalty term to the loss function during training, discouraging the model from assigning too much importance to specific features. For example ==Lasso== and ==Ridge== regularization. By reducing the model's complexity, regularization promotes better generalization to new, unseen data. 

**What is supervised learning?**;; Supervised learning is a process where learning algorithms are trained on labeled datasets, where each point is associated with a class or label. That is there is a y_train, then uses to get y_pred (from X_test) and compare against y_test.
<!--SR:!2024-04-08,4,270-->

What is unsupervised learning?;; process that works with unlabeled data, aiming to find patterns or structure without the guidance of labeled output.
<!--SR:!2024-04-18,14,290-->

Examples of unsupervised learning algorithms are;; clustering algorithms like K-means and hierarchical clustering, dimension reduction algorithms like PCA

**Supervised learning algorithms fall into two types called**;; Classification and regression.


---


**Give examples of supervised machine learning algorithms?**;; K-nearest neighbor, Naive Bayes, Decision Trees, Linear Regression, and Support Vector Machines.


What is reinforcement learning?;; A ML algorithm that learns through trial and error.

**What are hyperparameters?**;; parameters in machine learning models that control the learning process. They are set before training, i.e. k-value in k-nearest neighbor or the number of nodes in a [[What is a neural network|neural network]].

---


**What are ensemble methods in machine learning?**
Ensemble methods combine results from multiple ML models instead of relying on a single model. The idea is that this combination provides more accuracy. An analogy is consulting multiple doctors for a diagnosis, enhancing accuracy compared to a single doctor's opinion.

**To evaluate a generic machine learning model what metrics do you typically use?**
The choice of metrics for model evaluation depends on the problem type. Common metrics include misclassification error and accuracy. Accuracy suits balanced datasets where all classes are equally important.


How can overfitting in a decision tree be reduced, and what are the two approaches to pruning?;;Overfitting in a decision tree can be reduced using pruning. 

How do use prune a decision tree?;; Two approaches to pruning are ==Pre-pruning==, which stops tree growth based on certain criteria, and ==Post-pruning==, which allows the tree to grow and then prunes based on tree size and performance.

**What are the main techniques used to combine decision trees for a more accurate model (ensemble techniques)?**;; The main ensemble techniques for combining decision trees are ==Boosting algorithms== ==Bagging techniques==.

What are boosting algorithims?;;  these work sequentially by giving more focus to misclassified data.

What is a Bagging technique?;; these work in parallel by building models on randomized samples and combining their outputs.

**What is Random Forest, and how does it work?**;; Random Forest is an method that can perform regression, classification, dimensionality reduction, and handle missing values. It builds multiple decision trees and combines their outputs. Each tree is grown using a subset of the data and features, and the final output is determined by aggregating the predictions of individual trees.

**What is a Support Vector Machine, and what is its main idea?**;; SVM is a supervised machine learning algorithm that aims to find high-dimensional planes dividing a dataset into clusters. It does so by maximizing the margin between classes, with support vectors being the points closest to the planes.

**What is the technique called kerneling that is used by Support Vector Machine?**;; SVM uses a kerneling to map the dataset into a higher dimension, making it easier to identify clusters that may not be apparent in lower dimensions.
<!--SR:!2024-04-08,4,270-->

**What is a Support Vector Machine particularly advantages and disadvantages?**;; SVM is good at classifying high-dimensional data with many features and disadvantages such as poor performance with large datasets due to computational costs and the need to carefully choose the kernel.

**What is the difference between batch gradient descent and stochastic gradient descent?**;; Batch gradient descent computes the gradient of the cost function using the entire training dataset in each iteration, while stochastic gradient descent updates the model's parameters based on the gradient of the cost function with respect to one training example at a time. Mini-batch gradient descent is a compromise, using a subset of the training data in each iteration.

**Why is the confusion matrix called like that?**;; It helps where the classifier is confused.

What does a confusion matrix do?;;The confusion matrix evaluates a classifier's performance, distinguishing correct and incorrect predictions.

**What is the meaning and use of the F-measure (also called F1-score)?**;; The F-measure, or F1-score, combines precision and recall using the harmonic mean. It ranges from 0 to 1, indicating a balance between precision and recall. A high F-measure suggests a good overall classifier performance.

**What is the Bayes theorem?**;; The formula is P(A|B) = P(B|A) * P(A) / P(B).

**What are the main advantages of Naive Bayes, and when is it commonly used?**;; simplicity, quick implementation, and scalability, used in text classification.
<!--SR:!2024-04-07,3,250-->

**When using Naive Bayes with numerical variables, what condition is assumed on the data?;; Naive Bayes assumes that numerical variables follow a normal distribution.

**How does Naive Bayes perform with categorical variables?** makes no assumptions about the data distribution.


**What are the most common techniques for computing the coefficients in linear regression?**;; The most common techniques for computing coefficients in linear regression are Ordinary Least Squares, which minimizes the sum of squared residuals, and Gradient Descent, which iteratively updates coefficients to minimize error.

**What is logistic regression, and what does it predict?**;; Used to binary predict an outcome.

**Can you explain a real use case for logistic regression?**;; used to predict the probability that a customer will buy a product, making it valuable for marketing and sales predictions.

**How can you turn logistic regression into a classifier?**;; Logistic regression can be turned into a classifier by using a threshold. If the predicted probability is above the threshold, it is classified as one class; otherwise, it is classified as the other class.

**What metrics can be used to evaluate regression models?**;; Metrics for evaluating regression models include \(R^2\) (coefficient of determination), Mean Absolute Error (MAE), and Mean Squared Error (MSE).


**What is the K-nearest neighbor (KNN) algorithm, and for what is it used?**;; Used to find the K closest data points to a given point based on a chosen metric. Used for both classification and regression tasks, where classification involves assigning to the most common class among the K neighbors, and regression involves predicting the average value among the K neighbors.

**What is a decision tree?** ;;An algorithm that generates a flowchart from a dataset, representing a tree-like structure. It can also be seen as a series of if-else conditions where a feature is evaluated at each node.


**How are decision trees built?**;; Built in a decision tree is a recursive process. At each step, the algorithm searches for the best feature to split the dataset while minimizing ==entropy==.  The process continues until the tree is sufficiently homogenous or another stopping criterion is met.

What is Entropy in regards to Decision trees?;; Entropy describes dataset variety.

**What are the main advantages of decision trees?**;; output simplicity, minimal data preparation requirements, and human readability, making them suitable for transparent decision-making.

**What are some disadvantages of decision trees?**;;overfitting, instability to small changes in input data, and the potential for complex structures with datasets having many features.

**What is Naive Bayes, and why is it called "naive"?**;; Algo which uses Bayes theorem, used for classification problems. It is "naive" because it assumes that predictor variables are independent, which may not be the case in reality. The algorithm calculates the probability of an item belonging to each possible class and chooses the class with the highest probability as the output.

**What is cross-validation?**;; plitting the dataset into subsets multiple times used to
assesses performance and generalization. It helps detect overfitting, provides reliable performance estimates.








** How are precision and recall in binary classification, related?**;; They are related through a trade-off: increasing one may decrease the other. 



**What matrix can you use to evaluate the performance of a classifier? How does an ideal matrix look like?**;; The [[Confusion matrix]]

**Can you mention some of the most common metrics used to evaluate binary classifiers and some [[Categorical metrics]]?**;;[[Sensitivity]],[[Specificity]],[[Recall score]],[[Precision score]],[[Accuracy score]],[[F1 Score]].


F1-score, a combination of what?;; precision and recall, is suitable for imbalanced datasets when considering both false positives and false negatives is important.



















