---
aliases:
- null
category: LANG
date modified: 27-09-2025
tags:
- language_models
---
- [ ] Can you load a local model onto a SD card and run it on a raspberry pi?

Why small models work:
- They’re faster, cheaper, and can run on consumer hardware (laptops, even Raspberry Pi-level devices with optimisations) while giving acceptable quality for narrow, well-defined tasks. Pairing them with a vector store (e.g., Chroma, [[Weaviate]], Milvus) for [[RAG]] can dramatically boost usefulness without increasing model size.
### Use cases

#### Text Processing & Automation
* Template filling – e.g., generating structured responses, filling in report fields.
* Summarisation – condensing meeting transcripts or local documents without sending data to the cloud.
* Classification – tagging or categorising requests, tickets, or files.
* Text cleaning – grammar correction, standardising language for logs or reports.

#### Domain-Specific Models
* Fine-tune a small LLM for:
  * Industry jargon translation (e.g., maintenance logs → plain English).
  * Technical troubleshooting guides.
  * Incident classification in operations or engineering.
* Works well when paired with RAG (Retrieval-Augmented Generation) from a local knowledge base.
#### Edge & Offline Scenarios
* Field work in remote areas (e.g., utilities, scientific expeditions).
* IoT devices with natural language interfaces.
* Portable knowledge assistants for technicians, inspectors, or surveyors.
#### Educational & Training Tools
* Interactive Q\&A tutors for company onboarding.
* Scenario-based training simulations where the model plays a role.

#### Related:
- [[Small Language Models]]