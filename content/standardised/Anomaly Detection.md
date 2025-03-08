Anomaly detection involves identifying unusual or unexpected data points that deviate from the norm. Detecting these anomalies is crucial for maintaining data integrity and improving model performance.

## Methods for Detecting Anomalies

1. **[[Anomaly Detection with Clustering]]**
2. [[PCA-Based Anomaly Detection]]
   - For implementation, see: [[ML_Tools]] - [[PCA_Based_Anomaly_Detection.py]]
3. **[[Anomaly Detection in Time Series]]**
4. **[[Anomaly Detection with Statistical Methods]]**

## Process of Detection

### 1. **Data Preparation**
   - **Clean the Data:**  
     Handle missing values and remove any irrelevant data points.
   - **Normalize/Standardize:**  
     Scale the data if necessary, especially if using methods sensitive to the scale.

### 2. **Model Fitting**
   - Fit a statistical model to the data, such as a Gaussian distribution if applicable.
   - Estimate parameters like mean ($\mu$) and variance ($\sigma^2$) for the model.

### 3. **Anomaly Detection**
   - Use a chosen method to flag anomalies based on the calculated statistics.

### 4. **Validation**
   - Validate the detected anomalies by comparing them against known anomalies (if available) or using domain knowledge.
   - Adjust thresholds or methods based on validation results.

### 5. **Visualization**
   - Visualize the results using plots (e.g., scatter plots, box plots) to understand the distribution of data and the identified anomalies.
- **[[Boxplot]]:** Displays the distribution and identifies outliers using the interquartile range (IQR).
- **Scatter Plot:** Helps visually identify outliers.

### 6. **Iterate and Refine**
   - Based on the results, refine your approach by trying different statistical methods or adjusting parameters.