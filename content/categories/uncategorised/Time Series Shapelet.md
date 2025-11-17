---
aliases: []
category:
date modified: 5-11-2025
tags:
  - time_series
---
Time series shapelets are ==**discriminative, short subsequences or patterns within a time series dataset that are highly predictive of a target variable, typically a class label**==. They are local features used in time series data mining, primarily for classification and clustering, offering advantages in terms of interpretability, accuracy, and efficiency compared to methods that consider only global features. 

Key Concepts

- **Discriminative Patterns**: Shapelets represent the most characteristic local patterns of a specific class. For example, a particular spike pattern in an ECG time series might be a shapelet indicative of a specific heart condition.
- **Distance Measure**: The "distance" between a shapelet and a longer time series is defined as the minimum (usually z-normalized Euclidean) distance between the shapelet and all possible subsequences of the same length within the time series. A small distance means the shapelet is present in the time series.
- **Interpretability**: A major advantage of shapelets is their interpretability. Domain experts can visually inspect the discovered shapelets to understand which specific patterns in the data drive the classification decision.
- **Feature Transformation**: Shapelets are often used to transform the original time series data into a new, typically lower-dimensional, feature space. Each time series is represented by a feature vector containing the distances to the set of discovered shapelets. This transformed data can then be used with any standard, off-the-shelf classifier (e.g., a support vector machine or random forest). 

Usage in Data Mining

The general process of using time series shapelets involves:

1. **Shapelet Candidate Extraction**: Potential shapelets (all possible subsequences of varying lengths) are identified from the training data. This is often the most computationally intensive step, leading to the development of numerous optimization algorithms to speed up the process.
2. **Candidate Evaluation**: Each candidate shapelet is evaluated for its "quality" or ability to discriminate between different classes, often using metrics like information gain or F-statistic. The best candidates are selected.
3. **Data Transformation**: The time series dataset is transformed into a tabular format using the selected shapelets' distances as features.
4. **Classification/Clustering**: A standard machine learning model is trained on the new feature space to perform the final task. 

Applications

Time series shapelets have been successfully applied in a wide range of fields where identifying specific temporal patterns is crucial, including: 

- **Human Activity Recognition**: Classifying activities like walking, running, or standing based on accelerometer data from wearable devices.
- **Healthcare**: Analyzing ECG or other sensor data to detect medical conditions or anomalies.
- **Structural Health Monitoring**: Detecting earthquake events or structural anomalies from vibration data in buildings and bridges.
- **Environmental Monitoring**: Identifying patterns in air pollution exposure time series associated with specific health outcomes.