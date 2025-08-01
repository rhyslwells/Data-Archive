---
tags:
  - "#flashcards"
category:
---
## database

### [[Relating Tables Together]]
- A [[Primary Key]] uniquely identifies each record in a table, {{ensuring that no two records can have the same key}}.
- A [[Foreign Key]] establishes {{a link}} between two tables, allowing for relationships to be maintained and ensuring data integrity.
- One-to-One relationships mean that {{each record in Table A relates to one record in Table B}} and vice versa.
- One-to-Many relationships allow {{a single record in Table A to relate to multiple records in Table B}}.
- Junction tables are used to manage {{many-to-many relationships}} by containing {{foreign keys}} from both tables it connects.

### [[Database Schema]]
- A [[Database Schema]] defines how data is organized in a database, specifying {{tables, columns, relationships, and constraints}}.
- The importance of a schema lies in its ability to ensure that data is stored {{consistently and can be queried efficiently}}.
- Schema on Write enforces structure when data is written, while Schema on Read applies structure when data is accessed.
- A well-defined schema helps in organizing data, making it {{manageable and meaningful}}.

### [[Data Storage]]
- Structured data is formatted into a {{well-defined schema}}, allowing it to be easily understood and queried by machines.
- Examples of structured fields include {{age, name, phone number, credit card numbers, or address}}.
- Unstructured data does not conform to a data model and is difficult to analyze, such as the contents of an {{email or social media data}}.
### [[Data Principles]]
- Data principles ensure that data is managed, used, and maintained {{effectively and ethically}}.
- High-quality data is crucial for making {{informed decisions}} and involves ensuring {{data accuracy, completeness, and reliability}}.
- Data governance establishes {{clear policies and procedures for data management}}, ensuring compliance with regulations and data integrity.

### [[Data Modelling]]
- Data modelling is the process of creating a {{visual representation}} of a system's data and the relationships between different data elements.
- The workflow of data modeling includes a {{conceptual model, logical model, and physical model}} to ensure data is logically structured and organized.

## ML

### [Feature Extraction.md](obsidian://open?vault=content&file=standardised%2FFeature%20Extraction.md)

- Feature extraction is the process of transforming raw data into a {{structured set of informative features}} that are most relevant to a machine learning task.
- A core strategy in feature extraction is {{Dimensionality Reduction}}, which compresses data while preserving its most important variance.
- The purpose of feature extraction is to extract {{key attributes}} from raw data to enable learning algorithms to detect patterns and make accurate predictions.
- Informative features help reduce complexity by generating a {{smaller, more meaningful set of features}}.
- Feature extraction enhances both model performance and efficiency by simplifying input data and focusing on its most {{meaningful attributes}}.

### [[Machine Learning Algorithms]]
- Machine learning algorithms are used to {{automate tasks, extract insights, and make more informed decisions}}.
- Common classification algorithms include {{Logistic Regression, Support Vector Machines, and Decision Trees}}.
- Common regression algorithms include {{Linear Regression and Support Vector Regression}}.
- Choosing the right algorithm involves understanding the {{task, characteristics of the data, and strengths and limitations of different algorithms}}.

### [[Model Optimisation]]
- Model optimization aims to enhance a model's performance by fine-tuning its {{parameters and hyperparameters}}.
- The goal of model optimization is to improve the model's {{accuracy, efficiency, and ability to generalize}} to new data.
- Techniques like {{grid search, random search, or Bayesian optimization}} can be used for hyperparameter tuning.
- Evaluating the model using appropriate metrics is crucial for {{detecting overfitting and providing reliable performance estimates}}.
- A technique to assess the model's performance by splitting the data into multiple subsets for training and testing is called {{Cross Validation}}.
- Metrics for classification include {{accuracy, precision, recall, F1-score}}, and for regression include {{Mean Absolute Error (MAE), Mean Squared Error (MSE)}}.

### [[Machine Learning Operations]]
- MLOps emphasizes the importance of {{monitoring and maintaining models}} over time.
- Continuous monitoring of model performance is crucial in MLOps, as it helps identify when a model needs {{retraining}} due to changes in data patterns.

### [Supervised Learning.md](obsidian://open?vault=content&file=standardised%2FSupervised%20Learning.md)

- Supervised learning is a type of machine learning where an algorithm learns from {{**labeled data**}} to make predictions or decisions.

### [Classification.md](obsidian://open?vault=content&file=standardised%2FClassification.md)

- Classification is a type of supervised learning in machine learning, where the algorithm learns from {{labeled data}} to predict which {{category or class a new, unlabeled data point belongs to.}}
- The goal is to assign the correct label to input data based on patterns learned from the training set.
- Common classifiers include {{[Naive Bayes.md](obsidian://open?vault=content&file=standardised%2FNaive%20Bayes.md), [Decision Trees](app://obsidian.md/Decision%20Trees), and [Support Vector Machines.md](obsidian://open?vault=content&file=standardised%2FSupport%20Vector%20Machines.md).}}

### [Overfitting.md](obsidian://open?vault=content&file=standardised%2FOverfitting.md)

- Overfitting in machine learning occurs when a model captures {{not only the underlying patterns in the training data but also the noise}}, leading to poor performance on unseen data.
- Overfitting indicates high variance in the model’s performance, which can be identified by a significant {{drop in accuracy}} between {{training and test datasets}}.

### [Bagging.md](obsidian://open?vault=content&file=standardised%2FBagging.md)

- Bagging, short for Bootstrap Aggregating, is an {{ensemble technique}} designed to improve the stability and accuracy of machine learning algorithms. It works by training multiple instances of the same learning algorithm on different subsets of the training data and then combining their predictions.
- A well-known example of a bagging technique is {{the [[Random Forests.md]]}} algorithm.

### [Gradient Boosting.md](obsidian://open?vault=content&file=standardised%2FGradient%20Boosting.md)

- Gradient Boosting is a technique used for building predictive models, particularly in tasks like regression and classification. It combines the concepts of boosting and gradient descent to create strong models by {{sequentially combining multiple weak learners.}} Each new model focuses on {{correcting the mistakes made by the previous ones}} by fitting to the residuals.

### [Cross Validation.md](obsidian://open?vault=content&file=standardised%2FCross%20Validation.md)

- Cross-validation is a statistical technique used in machine learning to assess how well a model will {{generalize to an independent dataset.}}
- Cross-validation involves dividing the dataset into equal-sized subsets (folds) and using each fold as a {{validation}} set once, while the remaining  folds are used for {{training}}.
- With cross validation the model's performance is averaged across all  folds to provide a more robust {{estimate of its generalization performance.}}
## communication

### [[Communication Techniques]]

- The purpose of a Context Bridge in communication is to {{align everyone by setting the context before diving into details}}.
    
- A Change Bridge emphasizes shifts in a discussion using phrases like {{"Here's the before, and here's the after..." or "We’re shifting from X to Y..."}}.
<!--SR:!2025-07-30,1,230-->
    
- An Insight Bridge shares deeper insights or unique perspectives, creating {{"aha" moments}}.
<!--SR:!2025-07-30,1,230-->
    
- An Analysis Bridge anchors the discussion in {{evidence}}, keeping it grounded.
<!--SR:!2025-07-30,1,230-->
    
- A Summary Bridge helps ensure that key messages stay clear, especially in {{long discussions}}.
    
- An Action Bridge concludes with {{actionable steps}}, defining the next moves.
<!--SR:!2025-07-30,1,230-->
    

### [[Communication principles]]

- The main goal of effective communication is to {{enhance clarity and engagement}} in discussions.
    

### [[Asking questions]]

- A good question is characterized by being {{purposeful, contextual, open/expansive, challenging, precise, and sequenced}}.
<!--SR:!2025-07-30,1,230-->
    

### [[1-to-1's with a Line Manager]]

- The purpose of regular 1-to-1s is to ensure {{alignment, feedback, support, and professional growth}}.
### [[Change Management]]

- The first step in the change management process is {{Planning}}, which involves identifying the need for change and developing a strategy to implement it.
## statistics

### [[Distributions]]
- A **Uniform Distribution** has all outcomes that are {{equally likely}}.
- The **Bernoulli Distribution** represents two possible outcomes, such as {{heads or tails}} in a coin flip.
- The **Binomial Distribution** counts the number of successes in a sequence of {{Bernoulli trials}}.
- The **Poisson Distribution** models the frequency of events in a {{fixed interval}}.
- The **Gaussian Distribution** is characterized by a {{bell-shaped curve}} and is symmetric with thin tails.
- The **T Distribution** is similar to the normal distribution but has {{fatter tails}}, making it useful with limited data.

### [[Statistics]]
- The purpose of statistics is to {{understand the world}} through the modeling of probabilities.
- In hypothesis testing, the {{null hypothesis}} ($H_0$) states that there is no effect or difference.
- A small p-value (typically {{< 0.05}}) suggests that we should reject the null hypothesis.
- The Central Limit Theorem states that the distribution of the sum of a large number of independent random variables approaches a {{normal distribution}}.
- Statistics is the science of collecting, analyzing, interpreting, presenting, and organizing data to understand the world, which is made of {{probabilities}}.

### [[Hypothesis testing]]
- In hypothesis testing, the {{null hypothesis}} ($H_0$) is tested against the alternative hypothesis ($H_1$).
- A small p-value indicates that the observed effect is {{statistically significant}}.
- Accepting the null hypothesis means there is {{insufficient evidence}} to support the alternative hypothesis.
- The T-test is an example of a statistical test used to compare the {{means of two groups}}.

### [[Covariance]]
- Covariance measures the degree to which two random variables {{change together}}.
- A positive covariance indicates that as one variable increases, the other variable tends to {{also increase}}.

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

## business

### [[Operational Resilience for Growth and Adaptability]]
- Operational resilience involves preparation, foundational planning, and adaptability to {{future disruptions}} such as economic, regulatory, and climate changes.
- Resilience creates a {{competitive advantage}} by allowing businesses to seize emerging opportunities while others falter.
- Key practices for operational resilience include {{continuity and recovery planning}} embedded in daily operations.
- Trust-building is essential; people must understand and value the {{role they play}} in resilience efforts.

### [[Business observability]]
- Business observability refers to the ability to gain insights into the internal state and performance of a business through {{continuous monitoring and analysis}} of data.
- Key components of business observability include {{data collection}}, monitoring, analysis, and feedback loops.
- Effective business observability helps organizations {{detect issues early}} and optimize operations.

### [[Data AI Education at Work]]
- Integrating data and AI education into organizational strategies is essential for maintaining {{competitiveness}} and fostering a culture of continuous learning.
- Organizations should provide clear guidance on how to {{access training courses}} and encourage peer-to-peer learning.
- The risks of not upskilling include losing {{competitive edges}} and potential staff retention issues.

### [[Change Management]]
- Change management is a structured approach to transitioning individuals and organizations from a current state to a {{desired future state}}.
- Effective change management helps minimize {{resistance}} and improves engagement among employees.
- The process typically includes planning, communication, training, and {{monitoring and evaluation}}.

### [[Jobs to be done]]
- The Jobs to Be Done (JTBD) framework asks, "What job is the customer {{hiring a product or service to do}}?"
- Understanding pains and gains helps design solutions that reduce {{pains}} and create desired outcomes for customers.

### [[business intelligence]]
- Business intelligence (BI) leverages software and services to transform data into {{actionable insights}} that inform business decisions.
- A key goal of BI is to provide a {{single source of truth}} for data, ensuring consistency and accuracy across the organization.

### [[1-to-1's with a Line Manager]]
- The purpose of regular 1-to-1s is to ensure {{alignment, feedback, support, and professional growth}}.

### [[Business observability]]
- Business observability refers to the ability to gain insights into the internal state and performance of a business through {{continuous monitoring and analysis of data}}.

### [[Building a data team]]
- A good data team understands and influences {{business priorities}} and is evaluated on their impact to the whole business rather than just outputs.

### [[Data AI Education at Work]]
- Integrating data and AI education into organizational strategies is essential for maintaining {{competitiveness and fostering a culture of continuous learning}}.

### [[Digital Transformation]]
- Digital transformation should not only address today’s inefficiencies but also prepare digital assets and infrastructure for {{future automation, analytics, and growth}}.

### [[Communication Techniques]]
- The purpose of a Context Bridge in communication is to {{align everyone by setting the context before diving into details}}.

### [[Asking questions]]
- A good question is characterized by being {{purposeful, contextual, open/expansive, challenging, precise, and sequenced}}.

### [[Prevention Is Better Than The Cure]]
- Preventing data quality issues is the most effective strategy, involving {{identifying and addressing potential problems at the source}}.

### [[Data AI Education at Work]]
- Integrating data and AI education into organizational strategies is essential for maintaining {{competitiveness and fostering a culture of continuous learning}}.

### [[Jobs to be done]]
- The JTBD framework asks: *“What job is the customer {{hiring a product or service to do}}?”*
- Understanding pains and gains helps you design solutions that reduce {{pains and create gains}}.

### [[Asking questions]]
- A good question is characterized by being {{purposeful, contextual, open/expansive, challenging, precise, and sequenced}}.
- Asking better questions enhances {{thinking, learning, problem-solving, and communication}}.

### [[Change Management]]
- Change management is a structured approach to transitioning individuals, teams, and organizations from a current state to a {{desired future state}}.
- Effective change management helps minimize {{resistance, improves engagement, and increases the likelihood of successful outcomes}}.

### [[Digital Transformation]]
- Digital transformation aims to provide {{innovation to business processes}} and save time, do more, and save money.
- To digitally transform your department, you'll need to approach the process in a {{structured and strategic way}}.

### [[Documentation & Meetings]]
- Effective meetings include types such as {{Project & Technical Meetings, Data & Analytics Meetings, and Cross-functional / Stakeholder Meetings}}.
- Documentation templates help {{standardize processes}} for meetings, ensuring clear communication and follow-up.

### [[Performance Dimensions]]
- Efficiency & Performance includes aspects like {{Cost-efficiency, Speed, and Performance}}.
- Flexibility & Scalability ensure that the system can handle increasing volumes of data without {{performance degradation}}.

### [[Gartner Hype Cycle]]
- The Gartner Hype Cycle represents the typical progression of new technologies through five key phases: {{Innovation Trigger, Peak of Inflated Expectations, Trough of Disillusionment, Slope of Enlightenment, and Plateau of Productivity}}.

### [[Data Principles]]
- Data principles are essential for ensuring that data is managed, used, and maintained effectively and ethically, including aspects like {{Data Quality, Data Governance, and Data Privacy}}.
- High-quality data is crucial for making {{informed decisions}}.

### [[Software Development Life Cycle]]
- The SDLC comprises several phases, including {{Planning and Analysis, Designing, Development, Testing, Deployment, and Maintenance}}. Agile methodologies focus on {{flexibility and continuous delivery}}, integrating testing throughout the development process.

### [[Excel]]
- Excel supports advanced data modeling and integration through features like {{Power Pivot, Data Connections, and VLOOKUP}}. It provides tools for analysis and forecasting, including {{PivotTables and What-If Analysis}}.

### [[Implementing Gen AI]]
- The integration of generative AI within businesses is driven by its potential to transform operations and enhance {{productivity}}.
- Simplicity is crucial in AI implementation to ensure easier adoption and minimize {{resistance}}.

### [[Data Modelling]]
- Data modelling is the process of creating a visual representation of a system's data and the {{relationships between different data elements}}.
- It includes stages like {{Conceptual Model, Logical Model, and Physical Model}}.

## NLP

### [[NLP]]
- Natural Language Processing (NLP) involves the interaction between computers and humans using {{natural language}}.
- Key concepts in NLP include [[Feature Preprocessing]], which involves {{normalization of text}} and [[Part of Speech Tagging]].
- The [[Bag of Words]] model represents text data by counting the {{occurrence of each word}} in a document.
- [[TF-IDF]] stands for {{Term Frequency-Inverse Document Frequency}} and improves on Bag of Words by considering the importance of a word in a document relative to its frequency across multiple documents.
- [[One-hot encoding]] converts categorical data into a {{binary vector representation}}.

### [[nltk]]
- NLTK (Natural Language Toolkit) is a Python library for working with {{human language data}}. It provides tools for text processing, linguistic analysis, and building natural language processing ([[NLP]]) models.
- Key features of NLTK include {{tokenization}}, stopwords removal, and [[Part of Speech Tagging]].

### [[Named Entity Recognition]]
- Named Entity Recognition (NER) is a subtask of NLP that involves identifying and classifying key entities in text into {{predefined categories}} such as names, organizations, and locations.
- NER can be framed as a {{sequence labeling problem}} where the goal is to assign a label to each token in a sentence.
- The choice of model significantly impacts the {{accuracy of entity recognition}}.

### [[Prompt Engineering]]
- Prompt engineering is a technique in NLP that involves designing and optimizing {{input prompts}} to get the most relevant and accurate responses from large language models (LLMs).
- Techniques like {{prompt retrievers}} enhance the ability to retrieve and generate contextually appropriate prompts.
- Quality prompts can reduce {{ambiguity}} and guide model outputs.

### [[BERT]]
- BERT (Bidirectional Encoder Representations from Transformers) is a state-of-the-art NLP model developed by {{Google}}. It utilizes a {{bidirectional approach}} to capture the context of a word based on both its left and right surroundings in a sentence.
- BERT is pre-trained on a large corpus using {{Masked Language Modeling}} and {{Next Sentence Prediction}}.

### [[Transformer]]
- A transformer is a deep learning model architecture designed to process {{sequential data}} like natural language.
- The core innovation of transformers is the {{self-attention mechanism}}, which allows the model to weigh the importance of different words in a sentence relative to each other.
- Transformers can process entire sequences in {{parallel}}, making them more efficient than {{RNNs}}.

### [[Attention mechanism]]
- The attention mechanism allows a model to focus on {{different parts of an input sequence}} when making predictions. In its simplest form, attention assigns {{weights}} to each input token based on its relevance to the current output token being generated.
- The formula for calculating attention is given by: $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$, where $Q$, $K$, and $V$ are {{matrices of query, key, and value vectors}}.

### [[Energy]]
- Techniques like {{Differential Equations}} are used to model dynamic systems in energy generation and consumption.
- Predictive maintenance can be implemented using data from {{smart sensors}} in energy infrastructure.

### [[Data Principles]]
- Data principles ensure that data is managed, used, and maintained {{effectively and ethically}}.
- High-quality data is crucial for making {{informed decisions}}.
- Data privacy involves protecting personal and sensitive information by adhering to {{privacy laws}} and regulations.

### [[Backpropagation]]
- Backpropagation is an algorithm for training neural networks by iteratively correcting {{prediction errors}}.
- It calculates the gradient of the loss function with respect to each model parameter, enabling updates via {{Gradient Descent}}.
- The chain rule from calculus is employed to propagate {{errors backward}} through the network.

### [[Data Modelling]]
- Data modelling is the process of creating a {{visual representation}} of a system's data and the relationships between different data elements.
- The workflow of data modeling includes a {{conceptual model}}, a logical model, and a physical model.
- Types of modeling include relational, object-oriented, and {{hierarchical}}.

### [[Vector Embedding]]
- Vector embedding is a technique used to represent data in a {{continuous vector space}}.
- In the embedding space, similar items are positioned {{close to each other}}.
- Popular methods for generating vector embeddings include {{Word2Vec}}, GloVe, and FastText.