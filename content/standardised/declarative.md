---
aliases: []
category:
date modified: 27-07-2025
tags: [orchestration, field]
title: What is declarative?
---
In a **declarative data pipeline**, the focus is on *what* needs to be achieved, not *how* it should be executed. You define the desired outcome or the data products, and the system takes care of the underlying execution details, such as the order in which tasks are performed. This is in contrast to an **imperative** pipeline, where the developer explicitly specifies the steps and the order in which they should be executed. Here's a breakdown of the key aspects:

### **Declarative Programming**:
- Focuses on *==what==* needs to be done.
- Describes the desired state or result without dictating the control flow or step-by-step process.
- In a data pipeline context, a declarative approach might involve specifying the desired data products and letting the system optimize how and when different parts of the pipeline are executed.
- Example: [[SQL]] is often considered declarative because you specify the result you want (e.g., the output of a query) without explicitly stating the steps for how the database engine should retrieve it.

### **Imperative Programming**:
- Focuses on *==how==* tasks should be done.
- Specifies the ==control flow== explicitly, dictating the exact steps to be performed and the order of operations.
- In a data pipeline, this would involve writing scripts that detail each step in the transformation and loading process in the sequence they must be executed.
- Example: A series of Python scripts that process data in a specific sequence.

### **Advantages of Declarative Pipelines**:
1. **Easier to Debug**: Since the desired state is clearly defined, it is easier to identify discrepancies between the intended outcome and the current state. This can help pinpoint issues in the pipeline.
   
2. **Automation**: Declarative systems often enable better automation since the system has the flexibility to determine the most efficient way to achieve the defined goals.

3. **Simplicity and Intent**: Declarative approaches focus on the *==intent==* of the program, making it easier for others to understand what the program is supposed to do without having to dive into implementation details. 

4. **Reactivity**: The pipeline can automatically adjust when inputs or dependencies change. For example, if certain data dependencies change, the system can rerun the necessary parts of the pipeline to maintain consistency.

### **Example in Data Engineering**:

A declarative approach to data engineering would involve **Functional Data Engineering** principles. This involves treating data as immutable and focusing on defining the desired transformations and outputs in a declarative manner. Instead of writing imperative scripts for each data transformation step, you'd define the desired outputs, and the system would optimize the execution.

### **Use Cases**:
Declarative pipelines are particularly useful in [[data lineage]], **[[Data Observability]]**, and [[Data Quality]] monitoring**. By defining *what* data products should exist and what their properties should be, it's easier to track changes and ensure the consistency and quality of data. It also makes systems more resilient to changes, as the declarative nature enables the system to adjust the execution order or method dynamically, based on current conditions.