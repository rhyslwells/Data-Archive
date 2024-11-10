---
title: 
tags:
  - data_orchestration
  - data_orchestration
---
ELT (Extract, Load, and [Transform](Data%20Transformation.md)) is a [data integration](term/data%20integration.md) approach that extracts (E) data from a source system, and loads (L) raw data into a destination system before it transforms (T) the data. In other words, in the ELT approach, transformation (T) of the data is done _within_ the destination [Data Warehouse](Data%20Warehouse.md) after data has been loaded. 

ELT is in contrast to the more traditional [ETL](ETL.md) data integration approach, in which data is transformed before it arrives at the destination. See [ETL vs ELT](term/etl%20vs%20elt.md) for a more detailed comparison of these approaches.

The shift from the ETL paradigm to the ELT paradigm has been made possible thanks to the plummeting cost of cloud-based computation and storage, and the appearance of cloud-based data warehouses like Redshift, [[BigQuery]], or Snowflake. 

The following image demonstrates the ELT approach to [[data integration]] -- in this diagram ([[dbt]]) creates and manages the SQL that is used for transforming the data in the destination:

![](images/elt-tool.png)


