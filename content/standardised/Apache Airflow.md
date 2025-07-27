---
aliases: []
category:
date modified: 27-07-2025
tags: [data_orchestration, data_orchestration, software]
title: What is Apache Airflow?
---
Schedular think CROM jobs with python.

Apache Nifi may be better.

[Airflow](https://airflow.apache.org/) is a [data orchestrator](term/data%20orchestrator.md) and the first that made task scheduling popular with [Python](term/python.md). 

Airflow programmatically author, schedule, and monitor workflows. It follows the [imperative](term/imperative.md) paradigm of schedule as *how* a DAG [[Directed Acyclic Graph (DAG)]] is run has to be defined within the Airflow jobs. Airflow calls its *Workflow as code* with the main characteristics
- **Dynamic**: Airflow pipelines are configured as Python code, allowing for dynamic pipeline generation.
- **Extensible**: The Airflow framework contains operators to connect with numerous technologies. All Airflow components are extensible to easily adjust to your environment.
- **Flexible**: Workflow parameterization is built-in leveraging the [Jinja Templating](term/jinja%20template.md) engine.
