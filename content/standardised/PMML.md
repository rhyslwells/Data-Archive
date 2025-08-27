---
tags: 
category: 
---
PMML is an XML-based standard developed by the Data Mining Group (DMG) that allows applications to describe and share predictive models across different platforms and tools.
#### Purpose
* Provides a common representation for predictive analytics models.
* Enables model portability: train a model in one tool and deploy it in another without custom code.
#### What It Contains
* Model structure: Type (e.g., Decision Tree, Regression, Neural Network).
* Data dictionary: Input and output fields, data types.
* Transforms: Preprocessing steps (normalization, binning, etc.).
* Model parameters: Coefficients, splits, weights.
#### Why Important
* Facilitates interoperability in heterogeneous environments.
* Reduces the need for re-implementation.
* Commonly used in banking, insurance, and enterprise systems for deploying models.
#### Example Use
* Train a logistic regression model in R or Python → export as PMML → load into a Java-based scoring engine.
