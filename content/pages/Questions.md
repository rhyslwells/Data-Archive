#question


# Drafting questions

[[What is ExcaliBrain]]

[[What is the Attention mechanism]]

In [[Linear Regression]] or polynomial ect you use [[Regularisation]]. Can you do something similar for other classifiers?
Partially answered in [[Model training]].

What does the [[Logistic Regression]] graph tell us, specifically the results?

How to use [[Sklearn Pipiline]]? Give an example with an interesting dataset.

How do you know if a [[Classifier]] has been [[overfitting]]? For example with [[Random Forests]]
A: You can use [[Cross validation]]
# Unanswered

[[What does observability mean in terms of machine learning]]

[[What is a neural nets]]

[[Is a knowledge graph the same a RAG setup]]

[[Why do we do feature importance]]

[[What is a Digital twin]]

[[How do multi-agents interact in reinforcement learning]]

[[What is Sarsa in terms of single agent reinforcement learning]]

[[Why use isolation forest (Random Forests) for outliers detection]]
# Answered (Tags to be added)

[[inferencing in Gen AI versus prediction in machine learning]]

[[How do we control a generative AI in business through the use of guardrails]]

[[How do we we access Gen AI generated content]] 

[[What common techniques are used to determine if a Gen AI is good]]

[[How do businesses use Gen AI]]

[[How to reduce the need for Gen AI responses]]

# Dataview

```dataview
TABLE 
    importance AS "Manual Importance",
    round(
        length(file.inlinks) * 2 + 
        length(file.outlinks) + 
        length(tags) + 
        min(round(file.size / 100, 2), 5)
    ) AS "Automated Importance",
    file.tags AS "Tags",
    file.mtime AS "Last Modified"
FROM "standardised"
WHERE contains(tags, "question")
SORT "Automated Importance" DESC
```
