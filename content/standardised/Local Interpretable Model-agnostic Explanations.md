---
aliases: [LIME]
category:
date modified: 27-07-2025
tags: []
---

LIME explains individual predictions ==by approximating the model locally== with an interpretable model and calculating the feature importance based on the surrogate model.

### Key Points

- **Purpose**: LIME focuses on explaining individual predictions by approximating the model locally using a simpler, interpretable model (like linear regression).
  
- **How it Works**: 
  - For a given prediction, LIME generates perturbed samples (e.g., by modifying input features).
  - It observes how the predictions change, thus inferring feature importance for that specific instance.

- **Use Cases**: Useful for understanding why a specific decision was made in complex black-box models.

- **Advantage**: 
  - LIME can work with any model type.
  - It is relatively easy to apply to tabular, text, and image data.

- **Scenario**: 
  - A healthcare provider uses a deep learning model to classify whether patients have a high or low risk of heart disease based on several health metrics, such as cholesterol levels, age, and blood pressure.
- 
  - **LIME Explanation**: LIME is used to explain why the model flagged a specific patient as high-risk. By perturbing the input data (e.g., altering cholesterol levels and re-running the prediction), LIME shows that the patient’s high cholesterol level and advanced age are the main reasons for the high-risk classification. This makes it easier for the healthcare provider to justify the decision to recommend lifestyle changes or further medical tests.

### Example Code

To use LIME for feature importance, you can use the LIME package:

```python
import lime
import lime.lime_tabular

# Create a LIME explainer
explainer = lime.lime_tabular.LimeTabularExplainer(X_train, feature_names=feature_names)

# Explain a single prediction
explanation = explainer.explain_instance(X_test[0], model.predict_proba)
explanation.show_in_notebook()
```
