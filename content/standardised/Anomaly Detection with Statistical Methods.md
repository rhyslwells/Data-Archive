---
tags:
  - anomaly_detection
  - statistics
  - ml
---
[[Z-Normalisation|Z-Score]]

[[Gaussian Model]]

[[Isolated Forest]]

### Interquartile Range (IQR) Method 

Context:  
The IQR method is a robust and widely used statistical technique for identifying outliers, especially in [[univariate data]]. It is based on the distribution of data and is less sensitive to extreme values compared to methods reliant on mean and standard deviation.

Steps:
- Compute the IQR:
    - The IQR is the range within which the central 50% of the data lies.
    - Formula:  
        $\text{IQR} = Q3 - Q1$  
        where:
        - $Q1$: The first quartile (25th percentile)
        - $Q3$: The third quartile (75th percentile).
- Determine the bounds:
    - Define lower and upper bounds to detect potential outliers:  
        $\text{Lower Bound} = Q1 - 1.5 \cdot \text{IQR}$  
        $\text{Upper Bound} = Q3 + 1.5 \cdot \text{IQR}$
- Identify anomalies:
    - Any data point outside the lower or upper bounds is flagged as an anomaly.

Applications:
- Best suited for non-Gaussian distributions.
- Commonly used in boxplots for visualizing outliers.

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

### Dixon's Q Test

Context:  
Dixon's Q test is designed for small datasets ($n \leq 30$) and helps identify a single outlier. It is particularly effective when data has a single extreme value.

Purpose:  
To measure the relative distance of the suspected outlier from its nearest neighbor compared to the dataset's range.

Steps:

- Compute the Q statistic:  
    $Q = \frac{|x_{\text{outlier}} - x_{\text{nearest neighbor}}|}{\text{Range}}$  
    where:
    - $x_{\text{outlier}}$: The suspected outlier
    - $x_{\text{nearest neighbor}}$: Closest data point to the outlier
    - $\text{Range}$: Difference between the maximum and minimum data points.
- Compare Q to critical values:
    - Critical values are determined by the sample size and significance level $\alpha$.
    - If $Q$ exceeds the critical value, the suspected point is an outlier.

Limitations:
- Not suitable for large datasets.
- Assumes data is approximately normally distributed.

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