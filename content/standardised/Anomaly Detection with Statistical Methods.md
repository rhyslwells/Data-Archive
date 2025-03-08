---
tags:
  - anomaly_detection
  - statistics
  - ml
---
Basic:
- [[Z-Normalisation|Z-Score]]
- [[Interquartile Range (IQR) Detection]]
- [[Percentile Detection]]

Advanced:
- [[Gaussian Model]]
- [[Isolated Forest]]

### Grubbs' Test

Context:  
Grubbs' test is a hypothesis test designed to detect a single outlier in a normally distributed dataset. It tests the largest deviation from the mean relative to the standard deviation. This test is iterative and removes one outlier at a time.

Purpose:  
To determine whether the most extreme data point (either smallest or largest) is a statistical outlier.

Steps:
- Compute the test statistic:  
    $G = \frac{\max(|X - \mu|)}{\sigma}$  
    where:
    - $X$: Data points
    - $\mu$: Mean of the dataset
    - $\sigma$: Standard deviation of the dataset.
- Compare $G$ to a critical value:
    - The critical value depends on the sample size $n$ and significance level $\alpha$ (e.g., 0.05).
    - If $G$ exceeds the critical value, the data point is considered an outlier.

Limitations:
- Assumes data follows a normal distribution.
- Inefficient for detecting multiple outliers simultaneously.

### Histogram-Based Outlier Detection (HBOS)

Context:  

HBOS is a non-parametric method that detects anomalies by analyzing the distribution of individual features independently. It relies on histograms, which estimate feature density.

Purpose:  
To identify outliers as data points falling in bins with low frequencies or densities.

Steps:
- Create histograms for each feature:
    - Divide each feature's range into bins.
    - Count the frequency of data points in each bin.
- Calculate scores for each data point:
    - Outliers are points in bins with significantly lower densities compared to others.

Advantages:
- Does not assume a specific data distribution.
- Scales well to large datasets.

Limitations:
- Assumes feature independence (not ideal for [[multivariate data]]).
- Sensitive to bin size selection.

### One-Class SVM

One-Class Support Vector Machine is a variation of the SVM algorithm used for anomaly detection. It learns a decision boundary around the normal data points.

Steps:
- Train the model on the normal data points.
- The model attempts to find a hyperplane that separates the normal data from the origin.
- Points that fall outside this boundary are classified as anomalies.