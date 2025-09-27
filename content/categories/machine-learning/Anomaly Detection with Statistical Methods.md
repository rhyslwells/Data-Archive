---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- anomaly_detection
- ml
- statistics
---
Basic:
- [[Z-Normalisation|Z-Score]]
- [[Interquartile Range (IQR) Detection]]
- [[Percentile Detection]]

Advanced:
- [[Gaussian Model]]
- [[Isolated Forest]]
- [[Kernel Density Estimation]] (KDE): Estimate the probability density, flag low-density regions as anomalies.

Refernences:
- Outlier detection Manning
# Others
### Histogram-Based Outlier Detection (HBOS)

Context:  

HBOS is a [[non-parametric]] method that detects anomalies by analyzing the distribution of individual features independently. It relies on histograms, which estimate feature density.

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