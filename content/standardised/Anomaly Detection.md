Anomaly detection involves identifying [[standardised/Outliers|Outliers]]. Detecting these anomalies is crucial for maintaining [[data integrity]] and improving model performance.
## Methods for Detecting Anomalies

In [[ML_Tools]] see: [[Pycaret_Anomaly.ipynb]]
## Process of Detection

Data Preparation
   - [[Data Cleansing]]: Handle missing values and remove any irrelevant data points.
   - [[Normalisation]]/[[Standardisation]]: Scale the data if necessary, especially if using methods sensitive to the scale.

Anomaly Detection with a model: Use a chosen method to flag anomalies
- [[Anomaly Detection with Clustering]]
- [[PCA-Based Anomaly Detection]]
- [[Anomaly Detection in Time Series]]
- [[Anomaly Detection with Statistical Methods]]

Validation
   - Validate the detected anomalies by comparing them against known anomalies (if available) or using domain knowledge.
   - Adjust thresholds or methods based on validation results.

Visualization

- Visualize the results using plots (e.g., scatter plots, box plots) to understand the distribution of data and the identified anomalies.
- [[Boxplot]]: Displays the distribution and identifies outliers using the interquartile range (IQR).
- Scatter Plot: Helps visually identify outliers.