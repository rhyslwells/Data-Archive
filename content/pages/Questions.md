
| Top Questions                                                        | Interest | Recency of Interest |
| -------------------------------------------------------------------- | -------- | ------------------- |
| [[Neural network]]                                         | 42       | September 28, 2024  |
| [[What does observability mean in terms of machine learning]]        | 22       | September 28, 2024  |
| [[Why do we do feature importance]]<br>                              | 14       | September 26, 2024  |
| [[What common techniques are used to determine if a Gen AI is good]] | 13       | September 26, 2024  |
|                                                                      |          |                     |

### Unanswered

| Question                                                                                                                                     | Interest |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [[Transformer]]                                                                                               | 10       |
| [[Why use isolation forest (Random Forests) for outliers detection]]                                                                         | 6        |
| [[What is Sarsa in terms of single agent reinforcement learning]]                                                                            | 6        |
| [[Backpropagation]]                                                                                                            | 5        |
| [[How do multi-agents interact in reinforcement learning]]                                                                                   | 4        |
| [[Why do we do feature importance]]                                                                                                          | 2        |
| [[Backpropagation]]                                                                                                            | 2        |
| [[For other classifiers is there a similar process like regularisation in linear regression]]                                                | 0        |
| [[How can machine learning models be made more interpretable to non-technical stakeholders]]                                                 |          |
| [[How can we ensure that models generalize well to new, unseen data, especially in dynamic environments]]                                    |          |
| [[What techniques can help models remain robust to noisy data]]                                                                              |          |
| [[How can data science tools and models be better integrated into decision-making processes in businesses]]                                  |          |
| [[Why is LSTM worse then using transformers]]                                                                                                |          |
| [[How do transformer models represent and manipulate mathematical structures to solve problems accurately?]]                                 |          |
| Current challenges within the energy sector, related to reinforcement learning and that can be progressed with recent technological advances |          |
| Current challenges withing the telecommunications sector, related to reinforcement learning                                                  |          |
|                                                                                                                                              |          |
| What techniques from information theory can be used to measure and optimize the amount of information conveyed by an AI model                |          |
| What current methods are being used to improve interpretability on AI models                                                                 |          |
| How do AI system provide formal mathematical models/frameworks to questions                                                                  |          |
|                                                                                                                                              |          |

### Dataview

I have tagged new questions in generating notes, they will appear at the bottom of this.

```dataview
TABLE
    round(length(file.inlinks) * 2 +
          length(file.outlinks) +
          length(tags) + 
          min(round(file.size / 100, 2), 5)) AS "Interest Score",
    recency_of_interest AS "Recency of Interest"
    // filter(file.tags, (tag) => !contains(tag, "question")) AS "Tags"
FROM ""
WHERE contains(tags, "question")
SORT round(length(file.inlinks) * 2 +
          length(file.outlinks) +
          length(tags) + 
          min(round(file.size / 100, 2), 5)) DESC
```

# Drafting questions

What does the [[Logistic Regression]] graph tell us, specifically the results?

How to use [[Sklearn Pipiline]]? Give an example with an interesting dataset.

How do you know if a [[Classification]] has been [[Overfitting]]? For example with [[Random Forests]]
A: You can use [[Cross validation]]