# Anomaly Detection

Identify unusual or unexpected data points that deviate from the norm.

There are several ways to detect [[Outliers]]

Use visual methods like boxplots, statistical methods like Z-scores, or clustering techniques.

## Visual Methods

- [[Boxplot]]: Displays the distribution and identifies outliers using the interquartile range (IQR).
- Scatter Plot: Helps visually identify outliers.

## [[Clustering]]

- Description: Outliers often form small clusters or are isolated from main clusters.

## PCA-Based Anomaly Detection

In [[ML_Tools]] see: PCA_Based_Anomaly_Detection.py

## [[Time Series]] Methods

See [[Time Series]].

## Statistical Methods

 [[Z-Score]]: Identifies outliers by measuring how many standard deviations a data point is from the mean.
### Gaussian method

![[Pasted image 20241230202826.png|500]]# [[Anomaly Detection]]

Example: You have a dataset of servers unlabled We aim to detect those that do not work (anomalies).

### Guassian model

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