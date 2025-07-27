---
aliases: [Data Activation, Operational Analytics]
category:
date modified: 27-07-2025
tags: [data_transformation]
title: What is Reverse ETL?
---
Reverse [[ETL]] is the flip side of the [ETL](ETL.md)/[ELT](term/elt.md). **With Reverse ETL, the data warehouse becomes the source rather than the destination**. Data is taken from the warehouse, transformed to match the destination's data formatting requirements, and loaded into an application – for example, a CRM like Salesforce – to enable action.

In a way, the Reverse ETL concept is not new to data engineers, who have been enabling data movement warehouses to business applications for a long time. 

As [Maxime Beauchemin](term/maxime%20beauchemin.md) mentions in [his article](https://preset.io/blog/reshaping-data-engineering/), Reverse ETL “appears to be a modern new means of addressing a subset of what was formerly known as  [Master Data Management (MDM)](master%20data%20management.md).”

Read more about in [Reverse ETL Explained](https://airbyte.com/blog/reverse-etl#so-what-is-a-reverse-etl).