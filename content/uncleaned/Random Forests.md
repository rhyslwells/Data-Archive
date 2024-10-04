---
tags:
  - ml
  - classifer
  - learning
---

# Statquest notes:

[link](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)  part 1

What is an issue with [[Random Forests]];; susceptible to overfitting, especially when dealing with noisy or high-dimensional data. Proper tuning of hyperparameters like the number of trees and maximum depth is crucial to mitigate this.

[[Decision Tree]] are not the best - need to make flexible for new data. THey work well with the data set they are defined on.

How to proceed with random forest: (build tree's randomly) i.e solve the issue with decision trees. Processis called [[Bagging]]
1) randomly select a dataset (bootstrap)
2) randomly select two (or multiple) features for each branch and proceed like in decision tree.

variety makes trees better.

To make a prediction , run data through trees in forest, and get prediction, conclude with majority prediciton.

How to know if random forest is good ?

Use data that was not in boot strap data set - measure the accuracy based on these classiifcations.

Refine the random forest by qweaking the [[hyperparameter]] of number of features used per step.

---
missing data

make initial guess for missing data and refine. Use [[Imputation]]. Remember where missing data was.


[link part 2](https://www.youtube.com/watch?v=sQ870aTKqiM)

[[Proximity matrix]] [[Finding missing data]]

![[Pasted image 20240411095614.png|500]]


# Description:
A random forest is an [[Ensemble model]] of [[Decision Tree]]s. Take many decision trees decisions to get better result.

![[Pasted image 20240128194716.png|500]]
![[Pasted image 20240118145117.png|500]]
# Applications

Apply the random forest regressor a dataset. Then evaluate the model performance with the R-squared metric [[R squared]]

```python
import numpy as np
    import pandas as pd
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import r2_score

    np.random.seed(1234)
    # load dataset
    ds = fetch_california_housing()
    df = pd.DataFrame(ds['data'], columns = ds['feature_names'])
    df['target'] = ds['target']
    # dependent variables
    X = df.drop('target', axis=1)
    # independent variable
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = RandomForestRegressor( n_estimators=100 )
    model.fit(X_train, y_train)
    model.score(X_test, y_test)
    y_pred = model.predict(X_test)
    r2_score(y_test, y_pred)
    # you should get 0.8049
```

Train the RandomForestClassifier on a dataset and evaluate it with [[Cross validation]].

```python
    import numpy as np
    import pandas as pd
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    np.random.seed(12)
    ds = load_iris()
    df = pd.DataFrame(ds.data, columns=ds.feature_names)
    df['target'] = pd.Series(ds.target)
    X = df.drop('target', axis=1)
    y = df['target']
    model = RandomForestClassifier()
    cross_val_score(model, X, y)
    # As result you should get array([0.96666667, 0.96666667, 0.93333333, 0.96666667, 1.])
```
## Questions and answers:

What is the difference between RandomForestClassifier and RandomForestRegressor?;; One predicts a categorical and the other a continuous outcome.

What is the Random Forest method;; an ensemble learning method based on constructing multiple decision trees during training and combining their predictions through averaging. Random Forests are flexibility, robustness, and ability to handle high-dimensional data, as well as their resistance to overfitting.

What is an issue with [[Random Forests]];; susceptible to overfitting, especially when dealing with noisy or high-dimensional data. Proper tuning of hyperparameters like the number of trees and maximum depth is crucial to mitigate this.

What is Regression?;; aimed to estimate conious variables, linear, multi linear, used in prediction.

How do you evaluate the performance of your machine learning models, and what metrics do you prioritize? ;; I use metrics such as accuracy, precision, recall, F1-score, and area under the ROC curve (AUC-ROC) depending on the specific task and objectives of the model.
<!--SR:!2024-04-15,4,270-->
### Business and situational questions

Tell about a recent project of yours;; Collaborating in the image matching kaggle competition. Obviously S2DS project too.
<!--SR:!2024-04-15,4,270-->

What are some areas in this business you are interested in?;;
Technical consulting, [[Energy]] projects. Any area with the room to problem solve, to apply the scientific method to business problems. Areas where data can be turned into decisions. Building technical systems too for operations (feasibility projects).

How do you approach prioritizing tasks in a data science project?;; Current project objectives, complexity, dependencies, and client impact.
<!--SR:!2024-04-15,4,270-->

How do you handle conflicts or disagreements within a data science team?;; I promote open communication, facilitate discussions, and seek win-win solutions to resolve conflicts constructively.

How do you stay updated with the latest developments and trends in data science?;; I would like to attend events, talk to peers, stay connect to colleagues online. Watch updates on youtube.

---

How do you ensure the quality and reliability of data used in your data science projects? ;; I implement data validation and cleaning procedures, conduct exploratory data analysis, and would collaborate with domain experts  and engineers to verify data accuracy and relevance.
<!--SR:!2024-04-15,4,277-->

Can you describe a time when you had to make a decision under tight deadlines in a data science project? ;; In S2DS the client wanted further features to be added, so we said no nicely.
<!--SR:!2024-04-15,4,270-->


What strategies do you employ to ensure alignment between data science initiatives and business objectives? ;; I collaborate closely with stakeholders to understand business goals, prioritize projects based on their strategic importance, and regularly communicate progress and results to ensure alignment and maximize impact.

How do you stay organized and manage deadlines in your data science projects? ;; I utilize project management tools, break down tasks into manageable components, set realistic timelines, and regularly reassess priorities to ensure timely delivery.
<!--SR:!2024-04-15,4,277-->


Can you discuss a challenging problem you encountered in a data science project and how you resolved it? ;; In alice in wonderland people issue,, I analyzed the root cause, consulted domain experts or literature, experimented with alternative approaches, and iteratively refined solutions until achieving satisfactory results.
### Team work questions

What do you think is the most important thing in a team?;; Buy in, communication, also initiative.

What do you think is a no-go in a team?;; Lack of accountability/blaming people, just own your mistakes and learn from them its more productive
### General questions

What are some areas of the DS field you are interested in?;; NLP (the techniques machines use to understand complex concepts), time series analysis (very real, forecasting).

Why are you interested in data science?;; Problem solving aspect, with tools that are technically interesting. Work with technical minded people. I enjoy the scientific viewpoint.

How would you interact with the data science community?;; Participate in Datafest, Kaggle projects, and engage with colleagues.
<!--SR:!2024-04-15,4,277-->

### Example experiences of some data science techniques.

Talk about a project you used with included a ML technique
?
==In linkedin postings project I used ML to make predictions based on feature space.==
==Clustering. Used random forests to make predictions.==
In Alice in wonderland - used NLP to derive some quantifiers and make plots (character appearance ect). She/him issue.



## Interview to ask

Ask does that answer your question.
### To show commercial awareness

[link](https://www.datascienceweekly.org/articles/how-to-show-awareness-of-the-wider-commercial-impact-of-data-science)
1. What problems does this company face?
2. What are you doing to currently to solve these issues (pro/cons).
3. What is success/ what is enough.
### My questions

What does success look like in this role.

What will be expected in the first 6 months.
### After admin

Follow up thank you emails, with random questions.


When you sample a dataset, how do you do the [[data selection]]?
A: By randomly sampling, by time period (use a feature)..

How do you handle [[Finding missing data]]? The missing data can give you insights into the data collection process.
Is the missing data randomly distributed or is it specific to a given feature.