---
tags:
  - data_quality
  - data_cleaning
  - data_exploration
aliases:
  - Class Imbalance
category:
---
Handling imbalanced datasets is a common challenge in machine learning, particularly in classification tasks where one class significantly outnumbers the other(s). 

In [[Classification]] tasks, an imbalanced dataset can lead to a model that ==performs well on the majority class but poorly on the minority class==. This is because the model may learn to predict the majority class more often due to its prevalence. 

For [[Regression]] tasks, handling outliers or data skewness might be necessary.

### Techniques

1. **Resampling**:
   - **Oversampling**: Increase the number of instances in the minority class by duplicating existing samples or generating new ones.
   - **Undersampling**: Reduce the number of instances in the majority class by randomly removing samples.

2. **Synthetic Data Generation**:
   - **SMOTE (Synthetic Minority Over-sampling Technique)**: Generate synthetic samples for the minority class by interpolating between existing samples.

3. **Weighted Loss Functions**:
   - Assign higher weights to the minority class during training to penalize misclassification more heavily.

4. [[Model Evaluation]]
   - Use metrics like precision, recall, F1-score, and AUC-ROC instead of accuracy to better evaluate model performance on imbalanced data.

### Example: Handling Imbalanced Data with SMOTE

Consider a scenario where you have an imbalanced dataset of resumes, with a majority of male resumes and a minority of female resumes. You want to build a model to predict gender based on resume features.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample dataset
data = {
    'feature1': [1, 2, 3, 4, 5, 6, 7,8 , 9, 10],
    'feature2': [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    'gender': ['male', 'male', 'male', 'male', 'male', 'female', 'female', 'female', 'female', 'female']
}

df = pd.DataFrame(data)

# Split data into features and target
X = df[['feature1', 'feature2']]
y = df['gender']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to balance the dataset
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Train a classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_resampled, y_resampled)

# Predict and evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
```
**SMOTE**: This technique generates synthetic samples for the minority class (female resumes) by creating new instances that are interpolations of existing ones.

Handling imbalanced datasets is crucial for building robust models that perform well across all classes. Techniques like SMOTE, resampling, and using appropriate evaluation metrics can significantly improve model performance on minority classes.

Handling class imbalances in machine learning is crucial for building models that perform well across all classes, especially when one class is significantly underrepresented. Here are several strategies to address class imbalance:

### 1. Data-Level Approaches

- **Resampling Techniques:**
  - **Oversampling:** Increase the number of instances in the minority class by duplicating existing samples or generating new ones using techniques like SMOTE (Synthetic Minority Over-sampling Technique).
  - **Undersampling:** Reduce the number of instances in the majority class by randomly removing samples. This can help balance the dataset but may lead to loss of important information.

- **Data Augmentation:** Apply transformations to existing data to create new samples, which is particularly useful in image data. Techniques include rotation, flipping, scaling, and cropping.

### 2. Algorithm-Level Approaches

- **Cost-Sensitive Learning:** Modify the learning algorithm to give more importance to the minority class. This can be done by assigning higher misclassification costs to the minority class during training.

- **Ensemble Methods:**
  - **[[Bagging]] and Boosting:** Use ensemble techniques like [[Random Forests]] or AdaBoost, which can be adapted to handle class imbalance by adjusting the sample weights or using balanced bootstrap samples.

### 3. Hybrid Approaches

- **Combine Resampling with Ensemble Methods:** Use resampling techniques in conjunction with ensemble methods to improve model performance. For example, apply SMOTE followed by training a Random Forest.

### 4. Evaluation Metrics

- **Use Appropriate Metrics:** Instead of accuracy, use metrics that are more informative for [[imbalanced datasets]], such as precision, recall, F1-score, and the area under the ROC curve (AUC-ROC).

### 5. Advanced Techniques

- **[[Anomaly Detection]] Models:** Treat the minority class as anomalies and use [[anomaly detection]] techniques to identify them.

- **[[Transfer Learning]]:** Use pre-trained models that have learned features from a balanced dataset, which can be fine-tuned on the imbalanced dataset.

