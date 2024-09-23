---
tags:
  - ml
  - classifer
---
## Description

types are [[Supervised]] and [[Unsupervised]]

why classifiers?  **enabling automated decision-making and predictive analytics**.

How do I choose a classifier algorithm?

**In this article, you will learn some tips and factors to consider when choosing the best classification algorithm for your data.**

1. 1 Data characteristics. ...
2. 2 Problem complexity. ...
3. 3 Model performance. ...
4. 4 Model [[interpretability]]. ...
5. 5 Model scalability. ...
6. 6 Model flexibility. ...
# Description


what is a classifier?

Models can take in pandas datas frames of numpy arrays.

 Classifiers are trained using labelled data ([[Supervised]]) to identify patterns that distinguish the classes. The classifer given unlabelled data makes predictions on the labels the data can have.

Examples: 

[[Neural networks]]
[[Regression]]
[[Naive Bayes]]
[[Decision Tree]]
[[SVM]]
## Flashcards

What is a [[Classifier]]?;; It is an algorithm that categorizes data into one or more of a set of “classes.

**What is a [[Decision Tree]]?**;;A decision tree is a model that maps features to target values by making decisions at each internal node. It is constructed by recursively splitting the data based on the most informative feature.

Explain support vector machines [[SVM]] and their use in classification ;;SVM is an algorithm that finds a hyperplane to separate data into classes. It is effective in high-dimensional spaces and is widely used in image classification and text categorization.

**How does the [[K-means]] algorithm work?**;; It is an algorithm that partitions a dataset into K clusters. It assigns each data point to the cluster whose mean has the closest Euclidean distance to the data point. The means are then updated, and the process repeats until convergence. Another is [[DBScan]] (stronger).
	
**Describe the [[K-nearest neighbours]] algorithm and its applications.**;; It is an Algo which assigns a new data point to the majority class of its k nearest neighbours. Used in [[Recommender systems]]