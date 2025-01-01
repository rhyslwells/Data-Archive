---
tags:
  - deleted
  - model_architecture
---
 Deploy the model into a production environment where it can be used


After building and evaluating the model, you can deploy it into production to make predictions on new data. This step involves:
     - Exporting the model (using tools like joblib or pickle in Python).
     - Deploying the model in an application, API, or automated workflow.

### Code

   ```python
   import joblib
   
   joblib.dump(model, 'linear_regression_model.pkl')
   ```


[[Sklearn Pipiline]]


- **What is the issue with [[Outliers]] in [[Model Deployment]]?**
  - Outliers can sway the generality of the model, skewing predictions and increasing the standard deviation.