---
aliases: []
category:
date modified: 12-08-2025
tags:
  - documentation
---
Purpose

* Transform raw data into a clean, integrated, and analysable form suitable for modeling and deployment.
* Ensure that the dataset is free from missing or irrelevant values, aligned with business objectives, and structured for the unit of analysis (e.g., per person, per transaction).
* Bridge the gap between [[Data Understanding]] and modeling.

End Goals

* No unaddressed missing data.
* All fields useful, relevant, and reliable.
* Dataset in the correct form for deployment.
* Comprehensive representation of the business problem, not limited to chosen KPIs or incentives.

Key Considerations

* Unit of analysis: For transactional data, aggregate variables so one row represents the entity being analyzed.
* Stakeholder input: Collaborate with SMEs and business teams to ensure alignment with problem objectives.
* Metrics & incentives: Verify that chosen features address business problems, not only organizational KPIs.

Core Tasks

1. Data Integration: Combine data from multiple sources, addressing missingness and inconsistencies.
2. Data Selection: Decide which variables and records to include or exclude.
3. Data Quality Verification: Reassess missing data, duplicates, and anomalies.
4. Feature Engineering: Construct new variables and transformations from existing data.
5. Feature Selection: Identify the most relevant features for modeling.

Process Characteristics

* Iterative: Data understanding and data preparation overlap, feeding back into each other.
* Checklist-driven: Preparation should follow a plan built during [[Data Understanding]].

Formal Documentation

* Documentation is essential for reproducibility, progress tracking, and deployment readiness.
* Reports generated in this phase form part of the CRISP-DM cycle and provide long-term value.

Reports to Produce

* Initial Data Collection Report: Data sources, acquisition methods, extraction details, problems encountered.
* Data Description Report: Field definitions, metadata, and integration implications.
* Data Exploration Report: Document patterns, anomalies, and SME discussions.
* Data Quality Report: Missing data treatment, imputation methods, and feature construction records.

Outcome

* A finalized dataset ready for modeling, supported by clear documentation of sources, transformations, and decisions.
* Traceability of how features, imputations, and integrations were performed.
