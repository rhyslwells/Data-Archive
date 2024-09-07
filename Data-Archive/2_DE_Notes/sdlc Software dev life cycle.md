---
tags:
  - business
---


# Software Development Life Cycle (SDLC)

## Introduction

A structured approach like the Software Development Life Cycle (SDLC) ensures ==systematic progression through various stages of development==. SDLC remains relevant today by outlining the essential stages a product must undergo to achieve success.

## SDLC Stages

The SDLC comprises several phases, each critical to the overall development process:

1. **Planning and Analysis**
    - **Purpose**: Collect business and user requirements, perform cost and time estimation, and conduct scoping activities.
    - **Activities**: Define what the final product must do and how it should work. This phase may include a separate requirements analysis stage.

2. **Designing**
    - **Purpose**: Prepare the product's architecture and design.
    - **Activities**: A software architect sets the high-level structure of the future system, selecting technology and drafting user experience and visual design.

3. **Development**
    - **Purpose**: Transform the design into actual code.
    - **Activities**: Programmers write code according to the design specifications, revealing some aspects of the final product to stakeholders.

4. **Testing**
    - **Purpose**: Ensure the quality and functionality of the product.
    - **Activities**: Testers and QA professionals review the code and usability, identifying bugs and errors for correction before deployment.

5. **Deployment**
    - **Purpose**: Release the product to users.
    - **Activities**: Launch the product, making it available for use. Often combined with the maintenance phase.

6. **Maintenance**
    - **Purpose**: Provide ongoing support and updates.
    - **Activities**: Gather user feedback, fix issues, and add new features as needed.

Additionally, some projects include a **Prototyping** stage between planning and designing to validate ideas with minimal effort and cost.

## SDLC Methodologies

### Waterfall (old)

The Waterfall model, strictly follows the SDLC stages sequentially. ==Each phase must be completed before the next begins, making it straightforward and easy to manage==. However, its lack of flexibility and late testing phase often lead to delays and budget overruns when changes are needed. Out of favour. Opposite of flexible, needs roll backs.

- detail documentation

### [[Agile]] (current)

- Produce only essential documentation. Collaborative effort. 
- Focuses on features users will like.

In response to the rigid Waterfall model, Agile emerged in the early 2000s with a ==focus on flexibility and continuous delivery.== Agile methodologies like Scrum, Lean, and Extreme Programming (XP) integrate testing throughout the development process and welcome changes even in late stages.

See agile manifesto : Working software over documentation

- **Scrum**: Breaks development into short cycles called ==sprints==, each lasting 1-4 weeks. At the end of each sprint==, a functional product increment is presented to stakeholders,== allowing for quick adaptation based on feedback.
- **Lean**: Aims to ==eliminate waste== through a build-measure-learn feedback loop, continuously refining the product. Steps: build, measure, learn.
- **Extreme Programming (XP)**: Emphasizes technical excellence with practices such as test-driven development, code refactoring, and pair programming.
- Kanban: management method for efficiency. 

### DevOps

Emerging from Agile principles, ==DevOps emphasizes collaboration between development and operations teams.== This approach uses continuous integration and continuous delivery ([[CI-CD]]) to ensure frequent code changes and quick feedback loops. DevOps practices enable rapid and reliable updates, with high levels of automation and efficiency.

- Makes sure existing process are optimised and streamlined.
