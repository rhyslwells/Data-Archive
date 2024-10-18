---
tags:
  - statistics
  - evaluation
---
Use same dataset, and dependant variables

**- Adjusted R² penalizes for the number of predictors, giving a more reliable assessment of fit.**

**- It's always less than or equal to [[R squared]], and values closer to 1 indicate a better fit.**

**- Use adjusted R² to compare models with different numbers of predictors and avoid [[Overfitting]].**

Use [[Adjusted R squared]] and [[R squared]]  if big difference then we are penalised for extra varaibles. If there is a big difference we can drop the extra variable.

When evaluating a [[Linear Regression]] what does the [[Adjusted R squared]] do?;; it is used to evaluate the model.
<!--SR:!2024-04-23,12,270-->

# Formula for Adjusted R^2

$R^2_{adj.} = 1 - (1-R^2)*\frac{n-1}{n-p-1}$