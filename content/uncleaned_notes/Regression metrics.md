Motivating question: How do you evaluate a regression classifier?

Regression Metrics

1. Mean Absolute Error (MAE). Lower better.

```python
from sklearn.metrics import mean_absolute_error
# Assuming y_true and y_pred are your true and predicted values respectively
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)
```

2. Mean Squared Error (MSE). Lower better. MSE is more sensitive to outliers

```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)
```

3. Root Mean Squared Error (RMSE)

```python
import numpy as np
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print("Root Mean Squared Error:", rmse)
```

4. R-squared (R2)I [[R squared]]. t ranges from 0 to 1, where 1 indicates perfect predictions. Higher R2 values signify better model fit to the data

```python
from sklearn.metrics import r2_score
r2 = r2_score(y_true, y_pred)
print("R-squared:", r2)
```

5. Median Absolute Error

```python
from sklearn.metrics import median_absolute_error
median_abs_err = median_absolute_error(y_true, y_pred)
print("Median Absolute Error:", median_abs_err)
```

6. Explained Variance Score

```python
from sklearn.metrics import explained_variance_score
explained_var = explained_variance_score(y_true, y_pred)
print("Explained Variance Score:", explained_var)
```