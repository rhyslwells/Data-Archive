---
aliases: []
category: ML
date modified: 9-11-2025
tags:
  - anomaly_detection
  - model_explainability
  - statistics
  - time_series
---
## [[Anomaly Detection]] in [[Time Series]] Data

Anomaly detection in time series data involves identifying observations that **deviate significantly from expected temporal patterns**. Because time series data is ordered and may include trends and seasonality, specialized methods are often required.

### 1. Statistical Methods

* **Moving Average / Rolling Statistics**: Compute rolling mean or median and flag points that are significantly above or below expected values.
* **Seasonal Decomposition**: Break the series into trend, seasonal, and residual components. Anomalies are typically detected in the **residuals**, which represent deviations from the expected pattern. Python’s `seasonal_decompose` (STL) can be used.
* **[[Z-score]] / IQR**: Standardize residuals or raw values using Z-scores or the interquartile range to detect outliers.

### 2. Time Series Models

* **ARIMA / SARIMA**: Fit models to capture autocorrelations and trends; anomalies are detected as large residuals.
* **State Space Models / ETS**: Forecast future values and detect anomalies based on residual deviations.

### 3. Machine Learning Approaches

* **[[LSTM]] Networks**: Train sequence models to predict next values; large prediction errors indicate potential anomalies.
* **Isolation Forest / One-Class SVM**: Can be adapted for time series by encoding temporal features (e.g., lagged values).

### 4. Change Point Detection

* Detect points where the **statistical properties of the series shift** (mean, variance, correlation), which may indicate structural anomalies. Methods include Bayesian change point detection or `ruptures` library.

### 5. Visual Methods

* **Time Series Plots**: Interactive plots can help spot unusual spikes, drops, or patterns.
* **Control Charts**: Define control limits around expected values; points outside limits are flagged.
* **Residual Plots**: Plot residuals from models or decompositions to highlight anomalies.

### 6. Practical Workflow

1. **Explore the dataset**: Check time range, missing values, and initial statistics.
2. **Decompose / model**: Apply [[STL decomposition]], ARIMA, or another time series model.
3. **Detect anomalies**: Use residual-based methods (Z-score, IQR, model errors) or ML-based approaches.
4. **Visualize results**: Highlight anomalies on interactive plots to interpret patterns.
5. **Validate anomalies**: Compare against known events or domain knowledge to reduce false positives.