---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- business
- orchestration
---
Organizations may also consider adopting a data virtualization solution to integrate their data. 

In this type of [[Data Integration]], data from multiple sources is left in place and is ==accessed== via a virtualization layer so that it ==_appears_== as a single data store. 

This virtualization layer makes use of adapters that translate queries executed on the virtualization layer into a format that each connected source system can execute. 

The virtualization layer then combines the responses from these source systems into a single result. This data integration strategy is sometimes used when a BI tool like Tableau needs to access data from multiple data sources.

One disadvantage of data virtualization is that analytics workloads are executed on operational systems, which could interfere with their functioning. Another disadvantage is that the virtualization layer may act as a bottleneck on the performance of analytics operations.