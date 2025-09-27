---
tags:
  - "#flashcards"
category:
---
Pull flashcard files to phone and tablets with obsidian. Or with [[Anki]].

To do:
- Generate cards here, create txt file then upload to anki
- review cards, and delete poor ones
- share cards
- For a note in [[Data Archive]] ask to generate n cares of the for 
	- question {{c1::answer}}
## Language models

1. Small Language Models (SLMs) excel in specialized tasks due to their {{c1::computational efficiency, interpretability, and task-specific fine-tuning}}, making them highly relevant for Edge ML and edge computing, as well as for {{c2:: domain-specific}} tasks.

2. One of the advantages of SLMs is that they require less computational power and are faster in {{c1:: inference}} compared to larger language models (LLMs).

3. SLMs can be effectively fine-tuned on smaller, domain-specific datasets and can outperform general LLMs in tasks with limited {{c1:: data availability}}.

# Flashcards for [[Logistic Regression]]

1. Logistic regression models the log-odds of the probability as a linear function of the {{c1::input features}}.

2. The logistic (sigmoid) function maps any real-valued input into the range (0,1), representing the probability of belonging to the {{c1::positive class}}.

3. In logistic regression, if the probability of a data point exceeds a given threshold typically {{c1:: 0.5}},  it is classified as the positive class.


 [[Feature Engineering]]:

4. Feature engineering is the iterative process of building good features for a better model, which involves creating new features from existing ones, such as {{c1: ratios}} and {{c1: interactions}}.

5. Interaction terms are new features created by combining existing ones to capture the {{c1: interaction effects}} between them, ultimately improving model accuracy.

6. An example of feature engineering is decomposing datetime information into separate features for date and time to capture their respective {{c1: predictive powers}}.

[[DBSCAN]]

1. DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is a clustering algorithm that groups together data points based on {{c1: density}}. It is particularly useful when K-means doesn't work well, such as in datasets with {{c2:: complex shapes}} or when there are outliers.

2. One of the key features of DBSCAN is its ability to identify {{c1: outliers}} by detecting noise points that don't belong to any cluster, which are points in {{c2::low-density regions identified as anomalies}}.

---
## Data Engineering

### [[Relating Tables Together]]
- A [[Primary Key]] uniquely identifies each record in a table, {{ensuring that no two records can have the same key}}.
- A [[Foreign Key]] establishes {{a link}} between two tables, allowing for relationships to be maintained and ensuring data integrity.
- One-to-Many relationships allow {{a single record in Table A to relate to multiple records in Table B}}.
- Junction tables are used to manage {{many-to-many relationships}} by containing {{foreign keys}} from both tables it connects.

### [[Database Schema]]
- A [[Database Schema]] defines how data is organized in a database, specifying {{tables, columns, relationships, and constraints}}.
- The importance of a schema lies in its ability to ensure that data is stored {{consistently and can be queried efficiently}}. A well-defined schema helps in organizing data, making it {{manageable and meaningful}}.
### [[Data Principles]]
- Data principles ensure that data is managed, used, and maintained {{effectively and ethically}}.
- High-quality data is crucial for making {{informed decisions}} and involves ensuring {{data accuracy, completeness, and reliability}}.
- Data governance establishes {{clear policies and procedures for data management}}, ensuring compliance with regulations and data integrity.
- Data principles are essential for ensuring that data is managed, used, and maintained effectively and ethically, including aspects like {{Data Quality, Data Governance, and Data Privacy}}.

### [[Data Modeling]]
- Data modelling is the process of creating a {{visual representation}} of a system's data and the relationships between different data elements.
- The workflow of data modeling includes a {{conceptual model, logical model, and physical model}} to ensure data is logically structured and organized.

## Project Management

### [[Jobs to be done]]
- Understanding pains and gains helps you design solutions that reduce {{pains and create gains}}.

### [[Asking questions]]
- A good question is characterized by being {{purposeful, contextual, open/expansive, challenging, precise, and sequenced}}.
- Asking better questions enhances {{thinking, learning, problem-solving, and communication}}.
### [[Communication principles]]
- The main goal of effective communication is to {{enhance clarity and engagement}} in discussions.
    

### [[Change Management]]
- Change management is a structured approach to transitioning individuals, teams, and organizations from a current state to a {{desired future state}}.
- Effective change management helps {{minimize resistance, improves engagement,}} and {{increases the likelihood of successful outcomes}}.


### [[1-to-1's with a Line Manager]]
- The purpose of regular 1-to-1s is to ensure {{alignment, feedback, support, and professional growth}}.

### [[Building a data team]]
- A good data team understands and influences {{business priorities}} and is evaluated on their impact to the whole business rather than just outputs.

### [[Documentation & Meetings]]
- Documentation templates help {{standardize processes}} for meetings, ensuring clear communication and follow-up.
### [[Software Development Life Cycle]]
- The Software Development Life Cycle (SDLC) comprises several phases, including {{Planning and Analysis, Designing, Development, Testing, Deployment, and Maintenance}}. Agile methodologies focus on {{flexibility and continuous delivery}}, integrating testing throughout the development process.

## Business

### [[Operational Resilience for Growth and Adaptability]]
- Operational resilience involves preparation, foundational planning, and adaptability to {{future disruptions}} such as economic, regulatory, and climate changes. Resilience creates a {{competitive advantage}} by allowing businesses to seize emerging opportunities while others falter. Key practices for operational resilience include {{continuity and recovery planning}} embedded in daily operations. Trust-building is essential; people must understand and value the {{role they play}} in resilience efforts.

### [[Digital Transformation]]
- Digital transformation aims to provide {{innovation to business processes}} and save time, do more, and save money.
- To digitally transform your department, you'll need to approach the process in a {{structured and strategic way}}.
- Digital transformation should not only address today’s inefficiencies but also prepare digital assets and infrastructure for {{future automation, analytics, and growth}}.
### [[Business observability]]
- Business observability refers to the ability to gain insights into the internal state and performance of a business through {{continuous monitoring and analysis of data}}.
- Key components of business observability include {{data collection}}, {{monitoring, analysis, and feedback loops}}. Effective business observability helps organizations {{detect issues early}} and optimize operations.
## ML

### [[NLP]]
- In NLP the [[Bag of words]] model represents text data by counting the {{occurrence of each word}} in a document. TF-IDF stands for {{Term Frequency-Inverse Document Frequency}} and improves on Bag of Words by considering the importance of a word in a document relative to its frequency across multiple documents.
- One-hot encoding converts categorical data into a {{binary vector representation}}.

### [[nltk]]
- NLTK (Natural Language Toolkit) is a Python library for working with {{human language data}}. It provides tools for text processing, linguistic analysis, and building natural language processing ([[NLP]]) models. Key features of NLTK include {{tokenization}}, {{stopwords removal}}, and {{Part of Speech Tagging}}.

### [[Named Entity Recognition]]
- Named Entity Recognition (NER) is a subtask of NLP that involves identifying and classifying key entities in text into {{predefined categories}} such as names, organizations, and locations.

### [[Prompt Engineering]]
- Prompt engineering is a technique in NLP that involves designing and optimizing {{input prompts}} to get the most relevant and accurate responses from large language models (LLMs). Techniques like {{prompt retrievers}} enhance the ability to retrieve and generate contextually appropriate prompts. Quality prompts can reduce {{ambiguity}} and guide model outputs.

### [[BERT]]
- BERT (Bidirectional Encoder Representations from Transformers) is a state-of-the-art NLP model developed by {{Google}}. It utilizes a {{bidirectional approach}} to capture the context of a word based on both its left and right surroundings in a sentence. BERT is pre-trained on a large corpus using {{Masked Language Modeling}} and {{Next Sentence Prediction}}.

### [[Transformer]]
- A transformer is a deep learning model architecture designed to process {{sequential data}} like natural language. The core innovation of transformers is the {{self-attention mechanism}}, which allows the model to weigh the importance of different words in a sentence relative to each other. Transformers can process entire sequences in {{parallel}}, making them more efficient than {{RNNs}}.

### [[Attention mechanism]]
- The attention mechanism allows a model to focus on {{different parts of an input sequence}} when making predictions. In its simplest form, attention assigns {{weights}} to each input token based on its relevance to the current output token being generated.

### [[Backpropagation]]
- Backpropagation is an algorithm for training neural networks by iteratively correcting {{prediction errors}}. It calculates the gradient of the loss function with respect to each model parameter, enabling updates via {{Gradient Descent}}. The chain rule from calculus is employed to propagate {{errors backward}} through the network.
### [[Vector Embedding]]
- Vector embedding is a technique used to represent data in a {{continuous vector space}}. In the embedding space, similar items are positioned {{close to each other}}. Popular methods for generating vector embeddings include {{Word2Vec}}, GloVe, and FastText.

### [Feature Extraction.md](obsidian://open?vault=content&file=standardised%2FFeature%20Extraction.md)

- Feature extraction is the process of transforming raw data into a {{structured set of informative features}} that are most relevant to a machine learning task. A core strategy in feature extraction is {{Dimensionality Reduction}}, which compresses data while preserving its most important variance.
### [[Machine Learning Algorithms]]
- Machine learning algorithms are used to {{automate tasks, extract insights, and make informed decisions}}. Choosing the right algorithm involves understanding the {{task, characteristics of the data, and strengths and limitations of different algorithms}}.
- Common classification algorithms include {{Logistic Regression, Support Vector Machines, and Decision Trees}}. Common regression algorithms include {{Linear Regression and Support Vector Regression}}.


### [[Model Optimisation]]
- Model optimization aims to enhance a model's performance by fine-tuning its {{parameters and hyperparameters}}. The goal of model optimization is to improve the model's {{accuracy, efficiency, and ability to generalize}} to new data. Techniques like {{grid search}} can be used for hyperparameter tuning.

- Evaluating a models using appropriate metrics is crucial for {{detecting overfitting and providing reliable performance estimates}}. A technique to assess the model's performance by splitting the data into multiple subsets for training and testing is called {{Cross Validation}}. Metrics for classification include {{accuracy, precision, recall, F1-score}}, and for regression include {{Mean Absolute Error (MAE), Mean Squared Error (MSE)}}.

### [[Machine Learning Operations]]
- MLOps emphasizes the importance of {{monitoring and maintaining models}} over time.
- Continuous monitoring of model performance is crucial in MLOps, as it helps identify when a model needs {{retraining}} due to changes in data patterns, and data drift.

### [Supervised Learning.md](obsidian://open?vault=content&file=standardised%2FSupervised%20Learning.md)

- Supervised learning is a type of machine learning where an algorithm learns from {{labeled data}} to make predictions or decisions.

### [Classification.md](obsidian://open?vault=content&file=standardised%2FClassification.md)

- Classification is a type of supervised learning in machine learning, where the algorithm learns from {{labeled data}} to predict which {{category or class a new, unlabeled data point belongs to.}} The goal is to assign the correct label to input data based on patterns learned from the training set. {{Decision Trees}} is a type of classification algorithm.
### [Overfitting.md](obsidian://open?vault=content&file=standardised%2FOverfitting.md)

- Overfitting in machine learning occurs when a model captures {{not only the underlying patterns in the training data but also the noise}}, leading to poor performance on unseen data. Overfitting indicates high variance in the model’s performance, which can be identified by a significant {{drop in accuracy}} between {{training and test datasets}}.

### [Bagging.md](obsidian://open?vault=content&file=standardised%2FBagging.md)

- Bagging, short for Bootstrap Aggregating, is an {{ensemble technique}} designed to improve the stability and accuracy of machine learning algorithms. It works by {{training multiple instances of the same learning algorithm on different subsets of the training data and then combining their predictions}}. A well-known example of a bagging technique is {{the Random Forest}} algorithm.

### [Gradient Boosting.md](obsidian://open?vault=content&file=standardised%2FGradient%20Boosting.md)

- Gradient Boosting is a technique used for building predictive models, particularly in tasks like regression and classification. It combines the concepts of boosting and gradient descent to create strong models by {{sequentially combining multiple weak learners.}} Each new model focuses on {{correcting the mistakes made by the previous ones}} by fitting to the residuals.

### [Cross Validation.md](obsidian://open?vault=content&file=standardised%2FCross%20Validation.md)

- Cross-validation is a statistical technique used in machine learning to assess how well a model will {{generalize to an independent dataset.}}
- Cross-validation involves dividing the dataset into equal-sized subsets (folds) and using each fold as a {{validation}} set once, while the remaining  folds are used for {{training}}.
- With cross validation the model's performance is averaged across all  folds to provide a more robust {{estimate of its generalization performance.}}


## Statistics

### [[Statistics]]

- In hypothesis testing, the {{null hypothesis}} ($H_0$) states that there is no effect or difference.
- A small p-value (typically {{< 0.05}}) suggests that we should reject the null hypothesis. A small p-value indicates that the observed effect is {{statistically significant}}.
- The Central Limit Theorem states that the distribution of the sum of a large number of independent random variables approaches a {{normal distribution}}.
- Statistics is the science of collecting, analyzing, interpreting, presenting, and organizing data to understand the world, which is made of {{probabilities}}.

### [[Hypothesis testing]]
- In hypothesis testing, the {{null hypothesis}} ($H_0$) is tested against the alternative hypothesis ($H_1$). Accepting the null hypothesis means there is {{insufficient evidence}} to support the alternative hypothesis.
- The T-test is an example of a statistical test used to compare the {{means of two groups}}.

### [[Covariance]]
- Covariance measures the degree to which two random variables {{change together}}. A positive covariance indicates that as one variable increases, the other variable tends to {{also increase}}.

### [[Standard deviation]]
- Standard deviation quantifies the amount of {{variation or dispersion}} in a set of data values.
- A small standard deviation indicates that data points are {{close to the mean}}.

### [[Covariance Structures]]
- A covariance structure describes how variability and relationships between {{variables}} are modeled in a dataset.
- The covariance matrix shows the variance of each variable along the {{diagonal}} and the covariances between variables off the diagonal.
- Covariance structures are crucial for multivariate statistical methods like {{principal component analysis}} and regression.

### [[Statistics]]
- Statistics is the science of collecting, analyzing, interpreting, presenting, and organizing data to understand the world, which is made of {{probabilities}}.

### [[Distributions]]
- Discrete distributions have probabilities concentrated on specific values, while {{continuous distributions}} have probabilities spread over a continuous range.

### [[Statistical Tests]]
- Statistical tests are methods used to determine if there is a {{significant difference}} between groups or if a relationship exists between variables.

### [[Statistical Assumptions]]
- The assumption of normality posits that the data follows a {{normal distribution}}, which is crucial for many statistical tests.

### [[Hypothesis testing]]
- In hypothesis testing, the null hypothesis ($H_0$) states that there is {{no effect or no difference}}.

### [[Regression]]
- Linear regression assumes a {{linear relationship}} between the dependent variable and independent variables, aiming to {{minimize the residual sum of squares}}.




























