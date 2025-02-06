[[Clustering]]
- Description: Outliers often form small clusters or are isolated from main clusters.

### **8. [[DBSCAN]] (Density-Based Spatial Clustering of Applications with Noise)**

- **Purpose:**  
    Finds anomalies based on density rather than explicit statistical assumptions.
- **Steps:**
    - Identify points in low-density regions as anomalies.


### **2. Local Outlier Factor (LOF)**

LOF is a density-based anomaly detection method that identifies anomalies by comparing the local density of a point with that of its neighbors.

**Steps:**

- For each point, calculate the local density based on the distance to its k-nearest neighbors.
- Compute the LOF score, which measures the degree of isolation of a point relative to its neighbors.
- Points with a LOF score significantly greater than 1 are considered anomalies.