---
aliases: []
category: DS
date modified: 27-09-2025
tags: []
---
Purpose
* Collect, explore, and understand the data.
* Ensure [[Data Quality]] before moving to [[Data Preparation]].
* Gain insights relevant to the problem and identify potential hidden patterns.
* Part of the [[Data Mining - CRISP]] process; crucial for guiding later modeling steps.


Key Activities
* Describe the data: Document sources, formats, variables,[[Data Dictionary]], and basic structure.
* Explore the data: Summarize distributions, check for [[storage/utils/file_getter/selected_files/Outliers|anomalies]], and visualize relationships.
* Verify quality: Assess missing values, duplicates, inconsistencies, and measurement errors.
* Refine scope: Decide what data is relevant, discard unnecessary variables.

Exploration Guidelines

* Identify the target variable (if supervised).
* Group features to make exploration manageable.
* Use methods such as [[Decision Tree]] analysis for investigating relationships and [[Feature Selection]].

Outcome
* A clear understanding of what data is available, its limitations, and its suitability for the problem.
* A foundation for [[Data Preparation]] and subsequent modeling.

Data Understanding: How to describe the data: First pass, efficiently: get initial questions
- Where is data from
- Structuring on data, weird values, groupings
- Bring up questions to 
- What do the type of values in a categorical mean, look at the sources 
- What is the context for this dataset: the story
- Create a Discards sheet with comments on why you have these rows in here.
- Create a table of a few examples of those that could create an error.
- Duplicate keys?


