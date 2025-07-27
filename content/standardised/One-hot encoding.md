---
aliases: []
category: ML
date modified: 27-07-2025
tags: []
---
Related terms:
- Why do we need to drop one of the dummy columns? [[Dummy variable trap]]: 

==Dummy variables & One-hot encoding are fundamentally different from [[Label encoding]]==

[[Label encoding vs One-hot encoding]]

One-hot encoding is a technique used to convert categorical data into a numerical format that can be used by [[machine learning algorithms]]. It is particularly useful when dealing with categorical variables that have no ordinal relationship. 

In one-hot encoding, each category is transformed into a binary vector. If there are \( n \) unique categories, each category is represented by a vector of length \( n \) where one element is "hot" (set to 1) and the rest are "cold" (set to 0). For example, if you have a categorical variable with three categories: "red," "green," and "blue," one-hot encoding would represent them as:

- "red" -> [1, 0, 0]
- "green" -> [0, 1, 0]
- "blue" -> [0, 0, 1]

One-hot encoding is used because many machine learning [[algorithms]] cannot work directly with categorical data. By converting categories into a numerical format, one-hot encoding allows these algorithms to process the data effectively. It is commonly used in [[preprocessing]] steps for machine learning models, especially in neural networks and other algorithms that require numerical input.

Interpretation in the Model: One-Hot Encoding treats each category as a separate binary feature and does not impose any ordinal relationship between them. This means the model doesn’t assume that one category is greater or lesser than another. Each category is treated independently.
### Implementation

In [[ML_Tools]] see: [[One_hot_encoding.py]]

```python
cat_variables = ['Sex',
'ChestPainType',
'RestingECG',
'ExerciseAngina',
'ST_Slope'
]
# This will replace the columns with the one-hot encoded ones and keep the columns outside 'columns' argument as it is.
df = pd.get_dummies(data = df, prefix = cat_variables, columns = cat_variables)
```


