---
aliases: []
category: DEVOPS
date modified: 27-03-2026
tags:
  - dashboards
  - r
  - visualisation
---
**Shiny** is an R framework for building **interactive web applications and [[dashboards]]** directly from [[R]], without requiring JavaScript or frontend development.
## Core idea

Shiny allows you to:

* define a **UI (user interface)**
* define a **server function (logic and computation)**
* connect them through **reactivity**

Reactivity means outputs automatically update when inputs change.

## What it enables

* Interactive dashboards (filters, sliders, selectors)
* Data exploration tools
* Real-time model outputs
* Internal tools for analysts or stakeholders
* Lightweight web apps for sharing analysis

## Typical components

* **Inputs** → user controls (dropdowns, sliders, date ranges)
* **Outputs** → plots, tables, text
* **Reactive expressions** → computations that update automatically



## Relation to tidyverse

* **tidyverse** → [[data preparation]] and transformation
* **Shiny** → presentation and interaction layer

They are often used together:

* [[tidyverse]] prepares and aggregates the data
* Shiny exposes it through an interactive interface
## Conceptual view

Shiny acts as a **wrapper around analytical workflows**, turning static R analysis into **interactive systems**.
## Comparison to Python ecosystem

R Shiny is similar to:

* **Dash ([[Plotly]])**
* **[[Streamlit]]**

## When to use Shiny

* You need to **share analysis interactively** without building a full web app
* Stakeholders need **self-service exploration**
* You want a fast path from **analysis → dashboard**

## Free hosting options

### 1. Local (development)

* Runs on your machine
* Access via browser (`localhost`)
* Not shareable externally
### 2. shinyapps.io (free tier)

* Managed hosting platform by Posit
* Deploy directly from RStudio
* No infrastructure required

**Characteristics:**

* Public URL for sharing
* Limited compute and usage hours
* Apps may sleep when inactive
## Conceptual summary

Shiny provides a **lightweight path from R analysis to interactive dashboards**, and the free tier (shinyapps.io) allows simple [[Model Deployment|deployment]] and sharing via a public URL without managing infrastructure.