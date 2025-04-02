---
title: What is data transformation?
tags:
  - data_cleaning
  - data_transformation
---
Data transformation is the process of converting data from one format to another. 

Data transformation may involve:  
- [[Data Cleansing]]: Removing inconsistencies and errors.
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Cleaning
- Structuring: Organizing raw data.
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/multi_index.ipynb
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/reshaping.ipynb
- Aggregation: Summarizing data for analysis ([[Pandas Pivot Table]]).  
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/group_by.ipynb
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/pivot_table.ipynb
- Selection:
	- [[Data Selection]]
- Joining: Merging datasets for completeness (also see [[SQL Joins]]). 
	- https://github.com/rhyslwells/DE_Tools/blob/main/Explorations/Transformation/Joining.ipynb

Others:
- Normalizing: Standardizing data distributions for consistency.  See [[Normalisation]]
- Sorting: Arranging data in a logical order.  
- Enriching: Adding external or missing information. 
- Validating: Ensuring data integrity and accuracy.  

Key Aspects  
- Normalization & Scaling: Adjusting numerical values to a consistent range. See: [[Normalisation of data]]
- Data Type Conversion: Changing data types (e.g., converting strings to integers).  
- Schema Normalization: Ensuring a consistent data structure for efficiency.  
- File Format Conversion: Transforming data between formats (e.g., `.xls` to `.csv`).  

Related:
- [[Data Transformation with Pandas]]  
- [[Data transformation in Data Engineering]]
- [[Data transformation in Machine Learning]]
- [[Benefits of Data Transformation]]

