---
tags:
  - "#data"
  - "#analysis"
---


# Flashcards

What are the two main types of data?;; numeric &  categorical.


How to find outliers in a dataset?;; Use scatter plot, boxplot, IQR



What are the main techniques of feature engineering?;;The main techniques of feature engineering are selection (picking subset), learning (picking the best), extraction and combination(combining).

What are the main purposes of feature selection?;;Reducing the number of features increases understandability, reducing the training times, reducing dimensionality, removing noise.
<!--SR:!2024-04-14,3,250-->



  
What is a heatmap? When is it used?;; A <b>heatmap</b> is a two-dimensional grid that is used for visualizing numerical data organized in a table-like format. Used for Correlation and confusion matrix analysis.  

What is a violin plot? When is it particularly useful?;; As a visual it is an extension of a boxplot showing the data distribution. Useful when comparing distributions, skewness.

What are some difference between a bar chart and a histogram?;; A bar chart shows the frequency of each value of a categorical variable. An <b>histogram</b> is used to represent the distribution of a <u>continuous</u> variable.

PCA is affected by scale what is a crucial first step?;;, a crucial first step is standardization or scaling of the data. 

What is PCA? When do you use it?;; It consists in projecting data in a higher dimensional space into a lower dimensional space by maximizing the variance of each dimension.


What are some steps involved in the preprocessing of a text?;; make text lower case ,remove punctuation, tokenize the text (split up the words in a sentence),remove stop words as they convey grammar rather than meaning, word stemming (reduce words to their stems).

Examples of algorithms not affected by feature scaling are;; Naive Bayes, tree-based algorithms, and Linear Discriminant Analysis.

When is it reasonably possible to drop items with missing values?;;It is reasonably possible to drop items with missing values when the items to remove are few compared to the size of the training set.

What is A/B testing?;;A/B testing is a method of performance testing two versions of a product like an app.
<!--SR:!2024-04-21,10,274-->

What are some common algorithms of dimensionality reduction?;; PCA is a linear technique that reduces the dimensionality of data by transforming it into a new coordinate system based on the principal components, which are orthogonal and capture the most variance in the data.     t-Distributed Stochastic Neighbor Embedding (t-SNE): t-SNE is a non-linear technique used for visualization and dimensionality reduction by preserving pairwise similarities between data points, making it suitable for exploring high-dimensional data.

What is dimensionality reduction?;; decrease the number of features in a dataset while retaining as much relevant information as possible and simplify the dataset.

How can you use correlation for [[Feature Selection]]?;; Use the correlation of each feature with the target. Keep features with a significant correlation, i.e., a correlation value < -0.5 or > +0.5. Use pairwise correlation between features. If two features are highly correlated, one can be dropped since they provide the same information.

What is correlation?;;**Correlation** is a measure of the strength and direction of the relationship between two variables. 

How to treat missing values?;; Remove then or replace them.

What is **Causation**?;; is the relationship between two variables where one variable causes the other variable to change. 

What is the difference between correlation and causation?;; Just because two variables are correlated does not mean that there is a causal relationship between them. 


What range of values can have [[Correlation]]? What values are significant?;;Correlation is a statistical value that quantifies the dependency between two variables. The correlation value ranges from -1 to +1. The -1 (+1) value represents a perfectly negative (positive) correlation. The closer the value to 0 is, the weaker the linear correlation is. As a rule of thumb, values < -0.5 or > +0.5 are considered to have a significant relationship.

How can you use variance for [[Feature Selection]]?;;Features with low variance can be dropped since (almost) constant features do not provide any information.



What are the main techniques of [[Feature Selection]]?;; [[Filter method]], [[wrapper methods]] and [[embedded methods]]


[[Filter method]] in feature selection are?;; Statistical techniques are used to evaluate the relationship between individual features and the target features. 

[[wrapper methods]] in feature selection are?;; adding/removing features so you can evaluate their effect on the model based on a certain scoring.

 [[embedded methods]] in feature selection are?;;  The features are selected during the model training, and more important features are assigned a higher rank. Examples of such models are decision trees and lasso regression models.






















    
    
