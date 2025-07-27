---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Preprocess/Outliers/outliers_IQR.py

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