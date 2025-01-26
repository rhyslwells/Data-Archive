### **Key Differences Between [[k-Means]] and GMM**

#### Cluster Shape

- **k-Means**: Assumes clusters are spherical and equidistant from their centroids.
- **GMM**: Models clusters as Gaussian distributions, allowing for **different shapes** (e.g., ellipses) by incorporating mean and covariance matrices. GMM can model clusters of varying **shapes and sizes** by adjusting the [[Covariance Structures]] (e.g., full, diagonal, spherical).

#### Probability-Based Assignments

- **k-Means**: Assigns each point deterministically to the nearest cluster centroid.
- **GMM**: Provides a **probability [[Distributions|distribution]]** for cluster membership, making it a soft clustering method.
- GMM handles overlapping clusters effectively by assigning **probabilities** to data points for each cluster, instead of enforcing hard boundaries like k-means.

#### Flexibility

- **k-Means**: Performs well when clusters are **spherical** and well-separated.
- **GMM**: Handles **overlapping clusters** and clusters with **different shapes**, leveraging its covariance modeling capability.