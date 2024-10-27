Example: Amazon's imbalanced dataset of mostly male resumes.

Handling Imbalanced Data (If Relevant)

- Objective: If the target variable has imbalanced classes (for classification tasks), the model might not perform well on the minority class. For regression, handling outliers or data skewness could be important.

- Techniques:

- Resampling: Oversample the minority class or undersample the majority class.

- Synthetic Data Generation: Use techniques like [[SMOTE]] (Synthetic Minority Over-sampling Technique).

- Weighted Loss Functions: Assign higher weights to the minority class.

- Term: #data_preprocessing #ml_optimisation


python

Copy code

`from imblearn.over_sampling import SMOTE smote = SMOTE() X_resampled, y_resampled = smote.fit_resample(X_train, y_train)`