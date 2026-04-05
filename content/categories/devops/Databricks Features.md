---
aliases: []
category: DEVOPS
date modified: 27-03-2026
tags: []
---
#### Features inside of [[Databricks]]

SQL Warehouse - to config your workspace setup
- Can setup connection to powerbi ect
- Can set up permissions

Catalogs:
- manage control, schemas 
- ER diagrams: from catalog explorer, go to schema : view relationships
- data lineage: at a table: lineage: where the table comes from i.e volume goes to bronze goes to a silver table. Shows relationship of source to target. 
- Permissions in catalog: Catalogs, schemas, volumes, tables, views
- AI-generated - documentation using catalog explorer, for a table

Volumes:
- govenernace over non tabular data sets
- volumes only for path based data not tables
- volumens attached to schema in a catalog

streaming tables:
- continuuoislt ingest data, as get updated.

Materialized views:
- good for silver and gold layers

Query History:
- See efficiency of queries

Genie spaces:
- User pov:
	- creating AI/BI dashboard:
		- filters, 
		- parameters: like filters in sql query
	- publishing dsashboards
	- can ask about data indashboard using genie
- dedicated genie space
	- GENIE tab
		- connect tables, 
		- have a history of questions
		- can get query output fron questions
		- evaluating genie, through benchmarks: to make space more accurate.
			- add a question and ground through
			- descriptions in tables help genie with context

