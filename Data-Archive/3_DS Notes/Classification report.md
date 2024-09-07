## Example 

```python
# model 1
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=3)
model_1 = RandomForestClassifier(n_estimators=2)
model_1.fit(X_train, y_train)
y_predicted_1 = model_1.predict(X_test)
print("Classification Report for Model 1:")
print(classification_report(y_test, y_predicted_1))

# Model 2
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=3)
model_2 = RandomForestClassifier(n_estimators=10)
model_2.fit(X_train, y_train)
y_predicted_2 = model_2.predict(X_test)
print("\nClassification Report for Model 2:")
print(classification_report(y_test, y_predicted_2))
```

![[Pasted image 20240404163858.png|500]]



[link](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)





1. **Support**: Support is the number of actual occurrences of the class in the specified dataset.