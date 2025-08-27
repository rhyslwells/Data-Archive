---
aliases: []
category:
date modified: 1-08-2025
tags: [evaluation, modeling]
---
Crab on Python

- [ ] How would you make a simple one on [[Streamlit]]?

A recommender system, or recommendation system, is a type of information filtering system that aims to predict the preferences or interests of users by analyzing their behavior and the behavior of similar users or items. 

These systems aim to provide personalized recommendations to users.

The information is sparse therefore [[Linear Regression]], and [[Support Vector Machines|SVM]] cannot be used.

### Key Components of Recommender Systems:

1. User Data: Information about users, such as their preferences, ratings, purchase history, and interactions with items.

2. Item Data: Information about the items being recommended, which can include attributes, descriptions, and metadata.

3. Recommendation Algorithms: The methods used to generate recommendations. Common approaches include:
   - [[Collaborative Filtering]]: This technique relies on the behavior and preferences of similar users. It can be user-based (finding similar users) or item-based (finding similar items).
   - Content-Based Filtering: This approach recommends items based on the features of the items and the preferences of the user. For example, if a user likes action movies, the system will recommend other action movies based on their attributes.
   - Hybrid Methods: Combining collaborative and content-based filtering to improve recommendation accuracy and overcome limitations of each method.

1. [[Evaluation Metrics]]: Metrics used to assess the performance of the recommender system, such as precision, recall, F1 score, and mean average precision.
