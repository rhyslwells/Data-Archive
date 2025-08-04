---
aliases: []
category: 
date modified: 1-08-2025
tags: [optimisation]
---
Used in [[Feature Selection]]. Wrapper methods are powerful because they directly optimize the performance of the machine learning model by selecting the most informative subset of features. 

1. **Iterative Approach**: Unlike [[Filter method]], which assess the relevance of features based on statistical properties, wrapper methods ==directly involve the machine learning algorithm in the feature selection process.==
   
2. **Subset Selection**: Wrapper methods work by creating different subsets of features from the original dataset and training a model on each subset. These subsets can be combinations of different features or a subset of all features.

3. [[Model Evaluation]]: After training a model on each subset of features, the performance of each model is evaluated using a performance metric, such as accuracy, precision, recall, or F1-score, depending on the problem type (classification or regression).

4. **Optimization Criterion**: The goal of wrapper methods is to find the subset of features that maximizes the performance of the machine learning model. This can be achieved by selecting the subset that yields the highest performance metric on a validation set or through cross-validation.

5. **Computational Intensity**: Wrapper methods are computationally intensive because they involve training multiple models for each possible combination of features. As a result, they can be slower and require more computational resources compared to filter methods.

## **Examples of Wrapper Methods**:

   - **Forward Selection**: Starts with an empty set of features and iteratively adds one feature at a time, selecting the feature that improves model performance the most.
    
   - **Backward Elimination**: Begins with all features and iteratively removes one feature at a time, selecting the feature whose removal improves model performance the least.
     
   - **Recursive Feature Elimination (RFE)**: Iteratively removes features from the full feature set based on their importance, as determined by a specified machine learning algorithm.
     
   - **Selection Criteria**: The choice of performance metric and optimization criterion depends on the specific machine learning task and dataset characteristics. It's essential to select a metric that aligns with the goals of the project and to validate the selected subset of features on unseen data.

