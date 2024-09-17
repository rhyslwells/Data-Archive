`pd.get_dummies(df.var1)`
 
 - Encode categorical features for numerical representation


This is in order to do [[Regression]] models. Turn all categorical results to numerical.


First  encode:

```
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
var1_cat = df_tit['var1']
var1_encoded = label_encoder.fit_transform(var1_cat)
```

Second turn to a dataframe with column titles for each category:

```
from sklearn.preprocessing import OneHotEncoder
binary_encoder = OneHotEncoder(categories='auto')
var1_1hot = binary_encoder.fit_transform(embarked_encoded.reshape(-1,1))
var1_1hot_mat = embarked_1hot.toarray()
var1_DF = pd.DataFrame(embarked_1hot_mat, columns = ['cat1', 'cat2', 'cat3'])
var1_DF.head()
```


Change all categoricals to dummies
```python
#Pclass in fact is a categorical variable, though it's type isn't object.
for col in df.columns:
    if df[col].dtype == 'object':
        dummies = pd.get_dummies(df[col], drop_first=False)
        dummies = dummies.add_prefix('{}_'.format(col))
        df.drop(col, axis=1, inplace=True)
        df = df.join(dummies)
```

What does sklearn.preprocessing import [[OneHotEncoder]] do? why use it?

```
    dataset['var1'] = dataset['var1'].map( {'A': 0, 'B': 1, 'C': 2} ).astype(int)
```

dummy variable trap theory? (one column is enough to represent a binary choice 0 or 1)