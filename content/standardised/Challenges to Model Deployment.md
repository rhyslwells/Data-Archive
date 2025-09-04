---
aliases: []
category:
date modified: 3-09-2025
tags:
  - data_governance
  - data_pipeline
  - data_security
  - devops
  - systems
  - explainability
---
The main challenge is that a prototype focuses on *accuracy in isolation*, while production requires reliability, [[scalability]], monitoring, and integration into business systems.

Data-related issues
   * [[Data drift]]: Distribution of incoming data differs from training data.
   * [[Performance Drift|Concept drift]]: Relationship between inputs and outputs changes over time.
   * [[Data quality]]: Missing, delayed, or corrupted data in live systems.
   * Feature availability: Features used in prototyping may not exist or be delayed in production.

[[Scalability]] & performance
   * Prototype may work on a subset, but production must handle larger volumes with low [[latency]].
   * Need for real-time processing vs batch pipelines.
   * Resource constraints (CPU/GPU/memory).

Model [[Generalisation|Robustness]]
   * Prototype may overfit; needs retraining and validation under production conditions.
   * Handling edge cases and rare events.

Integration with systems
   * APIs, databases, or event-driven architectures may need redesign.
   * Version control for models and dependencies.
   * Ensuring reproducibility between dev and prod environments.

Monitoring & maintenance
   * Must track model accuracy, latency, and drift.
   * Establish alerting and retraining triggers.
   * Logging predictions for auditing and debugging.

Governance & security
   * Compliance with regulations (GDPR, HIPAA, etc.).
   * Access control for models and data.
   * Ethical considerations (bias, fairness, [[Interpretability|explainability]]).


