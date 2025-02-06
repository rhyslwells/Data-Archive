[[Z-Normalisation|Z-Score]]
- **Formula:**  
    $Z = \frac{(X - \mu)}{\sigma}$
    - $X$: Data point
    - $\mu$: Mean of the dataset
    - $\sigma$: Standard deviation of the dataset
- **Procedure:**
    - Set a threshold (commonly $|Z| > 3$). Points exceeding the threshold are anomalies.

### **2. Modified Z-Score**

- **Formula:**  
    $M = \frac{0.6745 \cdot (X - \text{median})}{\text{MAD}}$
    - $MAD$: Median Absolute Deviation
- **Procedure:**
    - Use this method for datasets with extreme outliers.
    - Points with $M > 3.5$ are typically anomalies.