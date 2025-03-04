https://github.com/rhyslwells/ML_Tools/tree/main/Explorations\Preprocess\Factor_Analysis.py
### **1. Factor Loadings Table**

This table shows how strongly each feature (e.g., `sepal length (cm)`) is correlated with the two extracted factors (Factor 1 and Factor 2).

- **Rows**: Represent the extracted factors (`Factor 1` and `Factor 2`).
- **Columns**: Represent the original features of the Iris dataset.
- **Values**: Represent the "loading" or contribution of each feature to the factor. Higher absolute values indicate a stronger relationship between a feature and a factor.

#### Interpretation:

- **Factor 1 (Row 0)**:
    - Strongly influenced by `petal length (cm)` (loading = 1.757902) and `petal width (cm)` (loading = 0.731005).
    - Moderately influenced by `sepal length (cm)` (loading = 0.727461).
    - Weak negative contribution from `sepal width (cm)` (loading = -0.180852).
    - This factor might represent the size of petals and sepals.
      
- **Factor 2 (Row 1)**:
    - Weak contributions from all features, with slightly negative contributions from `sepal length (cm)` and `sepal width (cm)`.
    - This factor might capture a subtle relationship or orthogonal variance not well-defined by the dataset.

---

### **2. Explained Variance**

The explained variance values indicate how much of the dataset's total variance is captured by each factor.
- **Factor 1 (0.9988)**: This factor explains ~99.88% of the variance among the features.
- **Factor 2 (0.9039)**: This factor explains ~90.39% of the variance among the features.

#### Combined Variance:
The two factors together capture a large portion of the total variance in the dataset. This suggests that most of the information in the dataset can be reduced to two latent factors, simplifying its structure while retaining the core relationships.

### **Overall Interpretation**

1. **Dimensionality Reduction**: The dataset with four features can effectively be reduced to two latent factors while retaining most of its variance.
2. **Factor 1 Dominates**: Factor 1 has strong contributions from `petal length`, `petal width`, and `sepal length`. This factor likely represents size-related characteristics.
3. **Factor 2 is Subtle**: Factor 2 shows weaker relationships with the features, potentially capturing noise or orthogonal variance.

### Next Steps:

1. Would you like to visualize the factors to understand how the data clusters in the new latent space?
2. Should we explore the relationships between the factors and target classes (e.g., species in the Iris dataset)?

### Breakdown of Extensions:

1. **Visualization**:  
    After performing factor analysis, we visualize how the data clusters in the new latent space (Factor 1 vs. Factor 2). The points are colored based on the species (target classes), which helps us see if the factors capture any clustering patterns related to species.
    
    - **Plot Details**:
        - The x-axis represents **Factor 1**.
        - The y-axis represents **Factor 2**.
        - Each species is plotted in different colors to visualize possible separations.
2. **Exploring Factor-Target Relationships**:  
    We compute the **average factor values** for each species. This shows how the latent factors (Factor 1 and Factor 2) relate to the different species in the dataset.
    
    - **Interpretation**:
        - If any species tends to cluster around specific values of Factor 1 and Factor 2, it suggests that the extracted factors capture some species-specific variance.

### Next Steps:

- The plot should give a clear idea of whether the latent factors allow for a meaningful separation of species.
- The summary table of average factor values will help understand how the factors relate to the target variable.