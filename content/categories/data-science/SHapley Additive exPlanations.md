---
aliases:
- SHAP
category: DS
date modified: 27-09-2025
tags:
- explainability
- modeling
---
SHAP provides a unified approach to measure [[Feature Importance]] by computing the contribution of each feature to each prediction, based on game theory.

### Key Points

- **Purpose**: SHAP provides consistent and locally accurate explanations by assigning each feature ==an importance value based== on Shapley values from cooperative game theory.

- **How it Works**: 
  - It calculates how each feature contributes to the model's output by comparing predictions with and without the feature, across various feature value combinations.

- **Use Cases**: Suitable for complex models like neural networks, random forests, or gradient boosting machines, where internal logic is difficult to understand.

- **Advantage**: 
  - Provides global explanations (model-wide feature importance) and local explanations (individual prediction reasons).

- **Scenario**: 
  - A financial institution uses a black-box XGBoost model to predict whether a loan applicant should be approved. The model takes several factors into account, such as credit score, income, employment history, and outstanding debts.
  - **SHAP Explanation**: For a specific loan rejection case, SHAP values reveal that the applicant’s high debt-to-income ratio and short employment history contributed the most to the rejection decision. These factors had the highest negative SHAP values for this prediction, providing actionable insights to both the applicant and the loan officers.

### Example Code

To compute SHAP values, you can use the SHAP library to interpret feature importance for any machine learning model:

```python
import shap

# Explain the model's predictions using SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Plot the summary plot of feature importance
shap.summary_plot(shap_values, X_test)
```