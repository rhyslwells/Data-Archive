https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Preprocess/PCA/PCA_Analysis.ipynb

This script performs Principal Component Analysis (PCA) on the Iris dataset to reduce its dimensionality while preserving key variance. 

See also [[Principal Component Analysis|PCA]]

Summary:

1. Load and Preprocess Data
    - Loads the Iris dataset and extracts features and target labels.
    - Scales the data to standardize feature ranges.

2. Apply PCA (3 Components)
    - Fits PCA to the scaled data and transforms it into three principal components.
    - Stores the transformed data in a DataFrame with species labels.
    
3. Analyze PCA Loadings & Variance
    - Computes and stores PCA loadings (weights of original features in principal components).
    - Computes explained variance and cumulative variance to assess PCA effectiveness.

4. Visualizations
    - Explained variance: Bar plot of individual and cumulative variance contributions.
    - PCA Scores: 3D scatter plots of transformed data, colored by species.
    - PCA Loadings: 3D scatter plot showing feature contributions to principal components.
    - Heatmap: Displays PCA component weights for feature importance analysis.

5. Additional Full PCA Analysis
    - Computes and prints explained variance for all components.
    - Uses Seaborn to generate a heatmap of PCA component contributions.