---
tags:
  - data_quality
  - data_cleaning
  - data_exploration
aliases:
  - Class Imbalance
category:
---
Handling imbalanced datasets to ensure robustness of models is a common challenge in machine learning, particularly in classification tasks where one class significantly outnumbers the other(s). 

In [[Classification]] tasks, an imbalanced dataset can lead to a model that ==performs well on the majority class but poorly on the minority class==. This is because the model may learn to predict the majority class more often due to its prevalence. 

For [[Regression]] tasks, handling outliers or data skewness might be necessary.
### Examples

Consider a scenario where you have an imbalanced dataset of resumes, with a majority of male resumes and a minority of female resumes. You want to build a model to predict gender based on resume features.

[[Imbalanced_Datasets_SMOTE.py]]

## Techniques

Resampling
   - Oversampling: Increase the number of instances in the minority class by duplicating existing samples or generating new ones.
   - Undersampling: Reduce the number of instances in the majority class by randomly removing samples.

[[SMOTE (Synthetic Minority Over-sampling Technique)]]

5. Weighted Loss Functions:
   - Assign higher weights to the minority class during training to penalize misclassification more heavily.

6. [[Model Evaluation]]
   - Use metrics like precision, recall, F1-score, and AUC-ROC instead of accuracy to better evaluate model performance on imbalanced data.
## Strategies to address imbalances
### 1. Data-Level Approaches

- Resampling Techniques:
  - Oversampling: Increase the number of instances in the minority class by duplicating existing samples or generating new ones using techniques like SMOTE (Synthetic Minority Over-sampling Technique).
  - Undersampling: Reduce the number of instances in the majority class by randomly removing samples. This can help balance the dataset but may lead to loss of important information.

- Data Augmentation: Apply transformations to existing data to create new samples, which is particularly useful in image data. Techniques include rotation, flipping, scaling, and cropping.

### 2. Algorithm-Level Approaches

- [[Cost-Sensitive Analysis]] / Cost-Sensitive Learning: Modify the learning algorithm to give more importance to the minority class. This can be done by assigning higher misclassification costs to the minority class during training.

- Ensemble Methods:
  - [[Bagging]] and Boosting: Use ensemble techniques like [[Random Forests]] or AdaBoost, which can be adapted to handle class imbalance by adjusting the sample weights or using balanced bootstrap samples.

### 3. Hybrid Approaches

- Combine Resampling with Ensemble Methods: Use resampling techniques in conjunction with ensemble methods to improve model performance. For example, apply [[SMOTE (Synthetic Minority Over-sampling Technique)|SMOTE]] followed by training a Random Forest.

### 4. Evaluation Metrics

- Use Appropriate Metrics: Instead of accuracy, use metrics that are more informative for [[imbalanced datasets]], such as precision, recall, F1-score, and the area under the ROC curve (AUC-ROC).

### 5. Advanced Techniques

- [[Anomaly Detection]] Models: Treat the minority class as anomalies and use [[anomaly detection]] techniques to identify them.

- [[Transfer Learning]]: Use pre-trained models that have learned features from a balanced dataset, which can be fine-tuned on the imbalanced dataset.

