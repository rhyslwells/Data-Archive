---
title: What is Data Integration?
tags:
  - data_storage
  - data_integration
---
Data integration is the process of ==combining data from disparate source systems into a single unified view.== Moving data to a [[Single source of truth]]

## Manual integration 

Before implementing a systematic approach to data integration, organizations may initially make use of manual integration when trying to make sense of data that is spread across multiple systems. 

This involves analysts manually logging into source systems, analyzing and/or exporting data on these systems, and creating reports based on their findings. 

Manual integration as a data integration strategy has several disadvantages. In addition to being time-consuming, analysts require access to multiple operational systems which creates security risks. 

Furthermore, analysts may run expensive analytics operations on systems that are not optimized for such workloads, which may interfere with the functioning of these systems. Finally, data in the source systems may frequently change which means that manually generated reports will quickly become outdated. 

## [[Data virtualization]]

Organizations may also consider adopting a data virtualization solution to integrate their data. 

In this type of data integration, data from multiple sources is left in place and is ==accessed== via a virtualization layer so that it ==_appears_== as a single data store. 

This virtualization layer makes use of adapters that translate queries executed on the virtualization layer into a format that each connected source system can execute. 

The virtualization layer then combines the responses from these source systems into a single result. This data integration strategy is sometimes used when a BI tool like Tableau needs to access data from multiple data sources.

One disadvantage of data virtualization is that analytics workloads are executed on operational systems, which could interfere with their functioning. Another disadvantage is that the virtualization layer may act as a bottleneck on the performance of analytics operations.  

## Application integration

Another alternative data integration solution is to directly link multiple applications to each other and move data directly between them. This is known as application integration, and linking can be done via point-to-point communications, via a middleware layer such as an enterprise service bus (ESB), or through an application integration tool. 

Application integration may result in many copies of the same data across multiple source systems, which may increase cost, and may cause a large amount of point-to-point traffic between various systems. Furthermore, as with the previous data integration types, executing analytics workloads directly on operational systems could interfere with their functioning.




