---
aliases: []
category:
date modified: 27-07-2025
tags: []
---
[[Agentic solutions]] propose an improvement over traditional Large Language Model ([[LLM]]) usage by employing networks of Small Language Models (SLMs). These systems aim to strike a balance between scalability, control, and performance, addressing specific tasks with precision while maintaining overall system adaptability.

Ideas from MLOPs talk by MaltedAI.

Agentic solutions represent a pragmatic approach to AI systems by focusing on modularity, task-specific efficiency, and the thoughtful integration of human expertise. These architectures show promise for enhancing scalability, control, and adaptability in real-world applications.
## Contrasting SLMs and LLMs

[[Small Language Models|SLM]] (Small Language Models):
    - Intent-based conversations and decision trees.
    - Controlled systems, harder to build features but easier to execute.
    - Task-specific and efficient in offline environments.

LLMs (Large Language Models):
    - Flexible and natural in handling diverse queries.
    - Suitable for general-purpose scenarios and exploratory tasks.
    - High computational and scaling costs.

### Combined Approach:

- Use [[Small Language Models|SLM]] for inference and LLMs for training.
- Shift the focus from making models larger to solving real-world problems effectively.
## Key Concepts in Agentic Solutions

1. Neural Decision Parser:
    - Acts as the "brain" of the system, determining the appropriate action given user input.
    - SLMs interpret user utterances to express code aligned with system intent.

1. Phased Policy:
    - Distinguishes between contextual and general-purpose questions.
    - Ensures deliberate task execution in stages for clarity and efficiency.

1. Knowledge Graphs and Interaction Models:
    - Complex graph structures enable intelligent conversations between models.
    - RAG setups leverage teacher-student frameworks for effective task distribution.

1. Distillation Networks of SLMs:
    - SMEs (Subject Matter Experts) guide teacher models that distill their expertise into student SLMs.
    - Enhances task scalability while controlling costs.

1. Scaling with Distillation:
    - Leverage teacher-student frameworks for high-quality, scalable data.
    - Allow teacher models to handle hard-to-scale aspects.

1. Knowledge Discovery:
    - Extract SME knowledge effectively while filtering irrelevant data.
    - Build high-quality datasets for task-specific applications.

## Applications of SLM Networks

1. Task-Specific Systems:
    - Offline processing, task search, and targeted QA.
    - Optimized embedding spaces for domain-specific applications.

1. Swarm Intelligence:
    - Decision-making through deliberation among SLMs.
    - Aggregates diverse inputs (HR, tech, CEO) for robust conclusions.

1. Business Process Models:
    
    - Search and page ranking systems.
    - Smaller, focused systems tailored to specific business needs.



## Designing Agentic Solutions

1. Role of SMEs:
    
    - Define tasks and input structures.
    - Guide model development with domain knowledge.
2. Data Preparation:
    
    - Comprehensive sampling of the problem space ensures generalization.
    - Data variability is critical for robust models.
3. Evaluation and Responsiveness:
    
    - Measure system performance to enable continuous improvement.
    - Focus on responsive, real-time processing.
4. Tool Integration:
    
    - Use LLMs with Python engines or computational tools like Wolfram for data analysis and complex interactions.



## Advantages of SLM Networks

- Precision: Models perform only what they are designed for.
- Efficiency: Smaller models are scalable and cost-effective.
- Focused Applications: Avoids the complexity of embedding spaces for entire businesses.


## Future Directions

