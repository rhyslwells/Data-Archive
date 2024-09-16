#ml 
How to use pipelines in sklearn? #question 

```python
# Naivebayesfor email prediction
from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])
clf.fit(X_train, y_train)
clf.score(X_test,y_test)
clf.predict(user_input)
```
