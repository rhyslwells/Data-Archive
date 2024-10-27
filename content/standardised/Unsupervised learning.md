---
title: 
tags:
  - "#clustering"
  - drafting
  - paradigm
aliases:
  - unsupervised
category:
---
In summary, **unsupervised learning** is about discovering hidden patterns in data without predefined labels, making it valuable for exploratory data analysis, [[clustering]], and [[Isolated Forests]].

**Unsupervised learning** is a type of machine learning where the algorithm is ==trained on data without explicit labels or predefined outputs.== The goal of unsupervised learning is to find hidden patterns, relationships, or structures in the data. Unlike **supervised learning**, where the model learns from labeled input-output pairs, unsupervised learning only uses input data, and the algorithm attempts to uncover insights from the data by itself.
### Key Concepts of Unsupervised Learning:
1. **No Labeled Data**: There is no ground truth or correct output associated with the input data.
2. **Data Patterns**: The algorithm identifies inherent structures, ==clusters==, or associations within the dataset.
3. **Objective**: The primary objective is to explore the data and organize it in a way that makes the ==underlying patterns== more apparent.

### Common Types of Unsupervised Learning:

 **[[Clustering]]**
 
   - The algorithm groups similar data points together based on their features.
   - Example: Customer segmentation in marketing. A clustering algorithm can divide customers into different groups based on purchasing behavior, demographics, or browsing history.
   - Popular Algorithms: 
     - [[K-means]] Divides the data into $k$ clusters, where each data point belongs to the nearest cluster.
     - **Hierachal [[Clustering]]**: Builds a tree of clusters by progressively merging or splitting groups based on similarity.
     - **[[DBScan]] (Density-Based Spatial Clustering of Applications with Noise)**: Forms clusters based on data density, allowing it to find arbitrarily shaped clusters.
     - [[Support Vector Machines]]
     - [[K-nearest neighbours]]

**Example**: Clustering customers into distinct groups based on their purchasing patterns in an e-commerce business.

**[[Dimensionality Reduction]]**:
   - Reduces the number of input variables (features) while preserving as much information as possible. This is helpful when dealing with high-dimensional data, where visualization and analysis become challenging.
   - Popular Algorithms: 
     - **Principal Component Analysis ([[Principal Component Analysis]])**: Transforms the data into a set of ==orthogonal components== that explain the maximum variance.
   **Example**: PCA used to reduce the dimensions of a dataset containing hundreds of features, such as a dataset of pixel values from images.

3. [[Isolated Forests]]
   - Identifies [[Outliers]] or unusual data points that don’t conform to the expected pattern in the dataset.
   - Example: Detecting fraudulent credit card transactions by identifying transactions that deviate significantly from typical spending patterns.
   - Works by randomly partitioning the data and identifying anomalies as points that can be isolated quickly.


