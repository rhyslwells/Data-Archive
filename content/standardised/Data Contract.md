---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
### [[Data Contract]]

pattern to handle schema changes

Pattern to apply to organisation using tools they have.

Tooling:
- [[dbt]]

Data contracts help prevent preventable data issues while increasing collaboration and reducing costs.

A data contract is an agreed interface between
the generators of data and its consumers. It sets
the expectations around that data, defines how
it should be governed, and facilitates the
explicit generation of quality data that meets
the business requirements.

Interfaces:
- [[API]] for data.

A document to codify what has been agreed.

Q: How does the Data Contract allow for contextual rules? Example the same schema can support multiple products in our org but the DQ rules can be different for different Products
A: Data contracts are particular business. Could use ==inheritance== of rules in data contracts - basic template. To get standardisation across products.

[[Data Contract]]
By establishing a [[data contract]] and building interfaces based on it, organizations can improve data quality. Implementing structured agreements and automated change management processes can help business users, who may not be data experts, produce higher-quality data ([[Data Quality]]).

### Images

![[Pasted image 20250312163351.png]]