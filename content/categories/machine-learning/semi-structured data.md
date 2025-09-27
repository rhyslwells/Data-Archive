---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- modeling
- storage
---
Semi-structured data is data that lacks a rigid structure and that does not conform directly to a data model, but that has tags, metadata, or elements that describe the data. 

Examples of semi-structured data are JSON or [[XML]] files. 

==Semi-structured data often contains enough information that it can be relatively easily converted into == [[structured data]]. 

[[Json]] data embedded inside of a string, is an example of semi-structured data. The string contains all the information required to understand the structure of the data, but is still for the moment just a string -- it hasn't been structured yet.

|          | **data**                        |
| -------- | ------------------------------- |
| Record 1 | \"{'id': 1, 'name': 'Mary X'}\" |
| Record 2 | \"{'id': 2, 'name': 'John D'}\" |


It is often relatively straightforward to convert semi-structured data into structured data. Converting semi-structured data into structured data is often done during the [Data Transformation](Data%20Transformation.md) stage in an [ETL](ETL.md) or [ELT](term/elt.md) process.  



