---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- anomaly_detection
---
Anomaly detection involves identifying [[uncategorised/Outliers|Outliers]]. Detecting these anomalies is necessary for maintaining [[Data Integrity]] and improving model performance.

Outlier detection needs formalized criteria (e.g., statistical models, distance measures, density estimates) because "weird" is contextual and depends on distribution.
## Methods for Detecting Anomalies

- [ ] Explore [[PyOD]]
## Process of Detection

[[Data Preparation]]
   - [[Data Cleansing]]: Handle missing values and remove any irrelevant data points.
   - [[Normalisation]]/[[Standardisation]]: Scale the data if necessary, especially if using methods sensitive to the scale.

Normality Assumption: Data Distribution
- Many classic methods (like z-score, [[Gaussian Mixture Models]]) assume [[Gaussian Distribution|normally distributed data]]]
- If the data is not normal, other methods (e.g., Isolation Forest, One-Class SVM) may be better.
- Always inspect [[Distributions]] first (e.g., histogram, [[Q-Q Plot]].

Anomaly Detection with a model: Use a chosen method to flag anomalies
- [[Anomaly Detection with Clustering]]
- [[PCA-Based Anomaly Detection]]
- [[Anomaly Detection in Time Series]]
- [[Anomaly Detection with Statistical Methods]]

Training and Testing on Same Set (Careful!)
- In outlier detection, sometimes you train and test on the same dataset — especially in pure unsupervised settings.
- However, overfitting is a risk. It's common to:
  - Train initial model
  - Remove detected outliers
  - Re-train
  - Repeat inspection -> removal-> retraining (iterative loop you wrote about).

[[Interpretability]] & [[Data Validation]]: Why is it unusual
   - Validate the detected anomalies by comparing them against known anomalies (if available) or using domain knowledge.
   - Adjust thresholds or methods based on validation results.
   - Finding an outlier is not enough. You must ask: "Why is this point different?" Necessary for Trust & Actionability.
  - Example: Anomalous electricity usage — is it fraud, error, or legitimate increased demand?

[[Data Visualisation]]
- Visualize the results using plots (e.g., [[Scatter Plots]], box plots) to understand the distribution of data and the identified anomalies.
- [[Boxplot]]: Displays the distribution and identifies outliers using the interquartile range (IQR).
- Scatter Plot: Helps visually identify outliers.