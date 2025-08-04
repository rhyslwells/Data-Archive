---
aliases: []
category:
date modified: 1-08-2025
tags: [cleaning, preprocessing, regressor]
---
Categorical variables need to be converted into numerical representations to be used in models, particularly in [[Regression]] analysis. This process is essential for transforming categorical results into a format that algorithms can interpret.
### [[Label Encoding]]

This method assigns a unique integer to each category in the variable.

```python
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
var1_cat = df['var1']  # Replace df with your DataFrame
var1_encoded = label_encoder.fit_transform(var1_cat)
```
For example, if `df[col]` contains the categories `['apple', 'banana', 'orange']`, the `LabelEncoder` would transform them into `[0, 1, 2]`.

However, keep in mind that this encoding can imply an order or hierarchy in the data, which might not be intended. In some cases, you might want to use `OneHotEncoder` instead, which creates a binary vector for each category.{}

Given a term in the df you can transform it without needing to look up its value.
```python
company="google"
company_n = LabelEncoder().transform([company])
```
### One-Hot Encoding

This technique creates a binary column for each category, allowing the model to treat each category as a separate feature.

```python
from sklearn.preprocessing import OneHotEncoder

binary_encoder = OneHotEncoder(categories='auto')
var1_1hot = binary_encoder.fit_transform(var1_encoded.reshape(-1, 1))
var1_1hot_mat = var1_1hot.toarray()
var1_DF = pd.DataFrame(var1_1hot_mat, columns=['cat1', 'cat2', 'cat3'])  # Adjust column names as needed
var1_DF.head()
```

Understanding OneHotEncoder:

The `OneHotEncoder` from `sklearn.preprocessing` is used to convert categorical integer values into a format that can be provided to machine learning algorithms to do a better job in prediction. It creates a binary column for each category and returns a sparse matrix or dense array.

When using one-hot encoding, it's important to avoid the [[dummy variable trap]], which occurs when one category can be perfectly predicted from the others. To prevent this, you can drop one of the dummy variables, as one column is sufficient to represent a binary choice (0 or 1).

### Converting All Categorical Variables to Dummies

To convert all categorical variables in a DataFrame to dummy variables, you can use the following loop:

```python
for col in df.columns:
    if df[col].dtype == 'object':
        dummies = pd.get_dummies(df[col], drop_first=False)
        dummies = dummies.add_prefix(f'{col}_')
        df.drop(col, axis=1, inplace=True)
        df = df.join(dummies)
```

### Alternative Encoding Method
Another way to encode categorical variables is by mapping them directly to integers:

```python
dataset['var1'] = dataset['var1'].map({'A': 0, 'B': 1, 'C': 2}).astype(int)
```
### Related Topics
- **[[Regression]]**: Understanding how regression models utilize encoded variables.
- **[[Feature Engineering]]**: Techniques to enhance model performance through better feature representation.