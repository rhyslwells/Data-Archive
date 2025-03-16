Explorations\Preprocess\One_hot_encoding\One_hot_encoding.py

This script demonstrates how to preprocess categorical variables and apply linear regression for house price prediction. Key steps include:

1. **Data Loading**: It loads a dataset of house prices.
2. **Dummy Variables**: It creates dummy variables for the 'town' column using `pd.get_dummies()` and merges them with the original dataframe.
3. **Dummy Variable Trap**: It drops one dummy variable to avoid multicollinearity (dummy variable trap).
4. **Feature and Target Split**: It separates the dataset into features (X) and the target variable (price).
5. **Model Training**: A Linear Regression model is trained on the data.
6. **Predictions**: It predicts house prices based on various features and evaluates the model's accuracy.
7. **Label Encoding and One-Hot Encoding**: It applies `LabelEncoder` to convert 'town' names into numbers and uses `OneHotEncoder` to create dummy variables for categorical columns.
8. **Final Predictions**: It predicts prices using the transformed features and evaluates the model's performance.