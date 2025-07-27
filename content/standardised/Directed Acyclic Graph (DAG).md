---
aliases: []
category:
date modified: 27-07-2025
tags: [data_orchestration, math]
title: 
---
DAG stands for **Directed Acyclic Graph**. 

A DAG is a graph where information must travel along with a finite set of nodes connected by vertices. There is no particular start or node and also no way for data to travel through the graph in a loop that circles back to the starting point.

It's a popular way of building data pipelines in tools like [[Apache Airflow]], [[dagster]], [[Prefect]]. It clearly defines the data lineage. As well, it's made for a functional approach where you have the [idempotency](term/idempotency.md) to restart pipelines without side-effects.

![](dag.png)