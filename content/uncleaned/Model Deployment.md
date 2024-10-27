---
tags:
  - ml
---

After building and evaluating the model, you can deploy it into production to make predictions on new data. This step involves:
     - Exporting the model (using tools like joblib or pickle in Python).
     - Deploying the model in an application, API, or automated workflow.

### Code

   ```python
   import joblib
   
   joblib.dump(model, 'linear_regression_model.pkl')
   ```


[[Sklearn Pipiline]]



