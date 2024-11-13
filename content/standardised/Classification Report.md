The `classification_report` function in `sklearn.metrics` is used to evaluate the performance of a classification model. It provides a summary of key metrics for each class, including precision, recall, F1-score, and support.

## Function Signature

```python
sklearn.metrics.classification_report(
    y_true, 
    y_pred, 
    , 
    labels=None, 
    target_names=None, 
    sample_weight=None, 
    digits=2, 
    output_dict=False, 
    zero_division='warn'
)
```
Parameters:
- `y_true`: Array of true labels.
- `y_pred`: Array of predicted labels.
- `labels`: (Optional) List of label indices to include in the report.
- `target_names`: (Optional) List of string names for the labels.
- `sample_weight`: (Optional) Array of weights for each sample.
- `digits`: Number of decimal places for formatting output.
- `output_dict`: If `True`, return output as a dictionary.
- `zero_division`: Sets the behavior when there is a zero division (e.g., 'warn', 0, 1).

### Metrics Explained

- [[Precision]]: The ratio of correctly predicted positive observations to the total predicted positives. It indicates the quality of the positive class predictions.
  
- [[Recall]] (Sensitivity): The ratio of correctly predicted positive observations to all actual positives. It measures the ability of a model to find all relevant cases.

- [[F1 Score]]: The weighted average of precision and recall. It is a better measure than accuracy for imbalanced classes.

- Support: The number of actual occurrences of the class in the specified dataset.

## Example Usage

Here's an example of how to use the `classification_report` with two different models:

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Assuming X and y are your features and labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

# Model 1
model_1 = RandomForestClassifier(n_estimators=2)
model_1.fit(X_train, y_train)
y_predicted_1 = model_1.predict(X_test)
print("Classification Report for Model 1:")
print(classification_report(y_test, y_predicted_1))

# Model 2
model_2 = RandomForestClassifier(n_estimators=10)
model_2.fit(X_train, y_train)
y_predicted_2 = model_2.predict(X_test)
print("\nClassification Report for Model 2:")
print(classification_report(y_test, y_predicted_2))
```
## Additional Resources

For more detailed information, you can refer to the [official documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html).


![[Pasted image 20240404163858.png|500]]


