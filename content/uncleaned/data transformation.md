---
title: What is data transformation?
tags:
  - data_processing
---

Data transformation is the process of converting data from one format into a different format. Reasons for doing this could be to optimize the data for a different use case than it was originally intended for, or to meet the requirements for storing data in a different system. Data transformation may involve steps such as cleansing, normalizing, [structuring](term/structured%20data.md), validation, sorting, joining, or [enriching](term/data%20enrichment.md) data. 


- Data Transformation: Normalizing or scaling numerical values, encoding categorical variables, and converting data types.

[[Encoding Categorical Variables]]

## How is data transformation done
Data is often transformed as part of an [ETL (Extract, Transform, Load)](ETL.md) or [ELT (Extract, Load, Transform)](term/elt.md) approach to [data integration](term/data%20integration.md). 

See [ETL vs. ELT](term/etl%20vs%20elt.md) for a comparison of these two approaches.  

Additionally, a hybrid approach has recently emerged which is known as [EtLT (Extract, “tweak”, Load, Transform)](term/etlt.md). This combines aspects of both ETL and ELT. 
## Benefits of data transformation
When used correctly, data transformation can provide the following benefits:

- Improved query-time efficiency and speed. 
- Conversion of data into a format that is required by a target system.
- Enrichment of data with additional information that allows insights to be more easily extracted.
- Improved data quality by validating and fixing data, and removal of duplicates. 
## Examples of data transformation
Below are some examples of how data may be transformed to achieve some of the benefits mentioned above.

### Improved efficiency and speed
One kind of transformation could be the extraction of structured data from data that is stored in a string. Imagine data that looks as follows: 

```
input_string: "Bob is 29"
```

In order to efficiently process this data in the future, it may preferable to transform this data into additional/new fields, and store it as:

```
name: "Bob"
age: 29
```

Storing the data in this manner makes it much more efficient to analyze with operations such as:

```sql
SELECT * FROM X where Age=29
```



### Data Wrangling 
Transform raw data into a format that best describes the problem to the model. This includes formatting and normalization.

**Formatting**
- Convert data into the required format, e.g., from .xls to .csv.

 [[Database Normalization]]
- Ensure consistent data representation and scale features appropriately.
  - Example: Normalize monetary values and quantities to a common scale using methods like min-max normalization.


Data must be transformed into a format that is most suitable for the machine learning model. This includes several steps such as ==labeling, cleansing, and feature engineering.==

**Labelling**
- **[[Supervised Learning]]**: This involves annotating the dataset with the correct answers (labels) to teach the model. For example, labeling images of apples to distinguish them from other fruits.
- **Manual and Automated Labeling**: Manual labeling by humans or leveraging existing labeled data. Tools like Google’s reCAPTCHA help in building labeled datasets.



Transform raw data into a format that best describes the problem to the model. This includes formatting and normalization.

Formatting
- Convert data into the required format, e.g., from .xls to .csv.

 [[Database Normalization]]
- Ensure consistent data representation and scale features appropriately.
  - Example: Normalize monetary values and quantities to a common scale using methods like min-max normalization.