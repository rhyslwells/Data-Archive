
# Question How to include [[p values]] in sklearn for a [[Linear Regression]]? 

import scipy.stats as stat.

You can modify the class of LinearRegression() from sklearn to include them

C:\Users\RhysL\Desktop\DS_Obs\1_Inbox\Work\Udemy\Part_5_Advanced_Statistical_Methods_(Machine_Learning)\multiple_linear_regression\sklearn - How to properly include p-values.ipynb

# What is f_regression and why can it compute p values?

from sklearn.feature_selection 
import f_regression
p_values = f_regression(x,y)[1]
p_values

[link](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_regression.html)

We will look into: f_regression
f_regression finds the F-statistics for the *simple* regressions created with each of the independent variables
In our case, this would mean running a simple linear regression on GPA where SAT is the independent variable
and a simple linear regression on GPA where Rand 1,2,3 is the indepdent variable
The limitation of this approach is that it doe==s not take into account the mutual effect of the two features==

f_regression(x,y)

There are two output arrays
The first one contains the F-statistics for each of the regressions
The second one contains the p-values of these F-statistics

outputs:
(array([56.04804786, 0.17558437]), array([7.19951844e-11, 6.76291372e-01]))