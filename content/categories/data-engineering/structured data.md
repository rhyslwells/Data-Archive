---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- modeling
- storage
---
Structured data refers to data that has been formatted into a well-defined schema ([[Database Schema]]). An example would be data that is stored with precisely defined columns in a relational [[Database]] or excel spreadsheet. Examples of ==structured fields could be age, name, phone number, credit card numbers or address.== Storing data in a structured format allows it to be easily understood and queried by machines and with tools such as SQL.

## Example of structure data

Below is an example of structured data as it would appear in a database:

| | **age**| **name**| **phone**| 
|---------|-----|------|-----|
|Record 1| 29 | Bob | 123-456 |
|Record 2| 30 | Sue | 789-123 | 

It may seem that all data is structured, but this is not always the case -- data can be unstructured, or semi-structured. The differences are best understood by example, and are discussed in the following sections. 

## Structured data vs. unstructured data

Structured data can be contrasted with [unstructured data](unstructured%20data.md), which does not conform to a data model and has no easily identifiable structure. Unstructured data cannot be easily used by programs, and is difficult to analyze. Examples of unstructured data could be the contents of an email, contents of a word document, data from social media, photos, videos, survey results, etc.   

An simple example of unstructured data is a string that contains interesting information inside of it, but that has not been formatted into a well defined schema. An example is given below:

|               |  **UnstructuredString**|
|---------| -----------|
|Record 1| "Bob is 29" |
|Record 2| "Mary just turned 30"|

## Structuring of unstructured data

Converting unstructured data into structured data can be done during the [Data Transformation](Data%20Transformation.md) stage in an [ETL](ETL.md) or [ELT](term/elt.md) process.  

For example, in order to efficiently make use of the unstructured data given in the previous example, it may desirable to transform it into structured data such as the following:

|               |  **name** | **age** |
|---------| -----------|---- |
|Record 1| "Bob" | 29 |
|Record 2| "Mary"| 30 |

Storing the data in a structured manner makes it much more efficient to query the data. For example, after structuring the data it is possible to easily and efficiently execute the following query on the structured data:
  
``` SQL
SELECT * FROM X where Age=29
```

A query such as this would be expensive and/or more difficult to execute on unstructured data.

## Structured data vs. semi-structured data

Structured data can also be contrasted with [semi-structured data](term/semi-structured%20data.md), which lacks a rigid structure and does not conform directly to a data model. However, semi-structured data has tags and elements that describe the data. 

Examples of semi-structured data are [[Json]] or [[XML]] files. Semi-structured data often contains enough information that it can be relatively easily converted into structured data. 

==[structured data](term/structured%20data.md) refers to data that has been formatted into a well-defined schema==. An example would be data that is stored with precisely defined columns in a [[Relational Database]] or excel spreadsheet. Examples of structured fields could be age, name, phone number, credit card numbers or address.