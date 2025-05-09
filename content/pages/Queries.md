This note contains dataview queries and they will not display. I will insert those of interest above the queries.
## Papers that I am currently reading
```dataview
TABLE
FROM ""
WHERE contains(category, "paper")
LIMIT 8
```
## [[Data Science]]

[[What is the role of gradient-based optimization in training deep learning models.]]
```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "DS"
```
## [[Machine Learning Operations]]
```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "MLOPS"
```
## [[Language Models]]
```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "LANG"
```
## [[Software Development Portal]]
```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "DEVOPS"
```
## [[Career Interest]]
```dataview
TABLE
FROM ""
WHERE contains(tags, "question") AND category = "CAREER"
```

## All Questions

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
