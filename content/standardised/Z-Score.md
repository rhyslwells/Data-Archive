---
aliases: []
category: 
date modified: 27-07-2025
tags: [statistics]
---
Z-scores standardize a value relative to a distribution by measuring how many standard deviations it is from the mean. This is useful for [[standardised/Outliers|Outliers]] and [[Normalisation]].

Definition:  
The Z-score of a value $x$ is given by:
    $$Z = \frac{x - \bar{x}}{s}$$
    
where $\bar{x}$ is the sample mean and $s$ is the sample standard deviation.
    
Interpretation:
- $Z = 0$: The value equals the mean.
- $|Z| > 2$: Indicates a possible outlier (if normality is assumed).
- Z-scores allow comparisons across different distributions.
	
Assumptions:
- Data is approximately normally distributed.
- Useful primarily when comparing existing values to a distribution.

Use Cases:
- Standardizing data for machine learning algorithms.
- Detecting anomalies.
- Ranking or scoring values.

Related terms:
- [[Z-Test]]
- [[Z-Normalisation]]
- [[Z-Score]]

### **2. Modified Z-Score**

- **Formula:**  
    $M = \frac{0.6745 \cdot (X - \text{median})}{\text{MAD}}$
    - $MAD$: Median Absolute Deviation
- **Procedure:**
    - Use this method for datasets with extreme outliers.
    - Points with $M > 3.5$ are typically anomalies.