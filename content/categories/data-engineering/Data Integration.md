---
aliases: []
category: DE
date modified: 27-09-2025
tags:
- orchestration
- storage
---
Data integration is the process of combining data from disparate source systems into a single unified view, moving data to a [[Single Source of Truth]].

## Manual Integration
Manual integration involves analysts manually logging into source systems, analyzing and/or exporting data, and creating reports. 

### Disadvantages of Manual Integration:
- **Time-consuming**: The process requires significant time investment.
- **Security Risks**: Analysts need access to multiple operational systems.
- **Performance Issues**: Running analytics on non-optimized systems can interfere with their functioning.
- **Outdated Reports**: Data changes frequently, leading to quickly outdated reports.

## [[Data Virtualization]]

Data virtualization is a method that allows access to data without needing to replicate it, providing a unified view of data from multiple sources.

## Application Integration
Application integration links multiple applications to move data directly between them. 

### Methods of Application Integration:
- **Point-to-Point Communications**: Direct connections between applications.
- **Middleware Layer**: Using tools like an Enterprise Service Bus (ESB).
- **Application Integration Tools**: Specialized tools for integrating applications.

### Disadvantages of Application Integration:
- **Data Redundancy**: May result in multiple copies of the same data across systems.
- **Increased Costs**: Managing multiple copies can lead to higher costs.
- **Point-to-Point Traffic**: Can create excessive traffic between systems.
- **Performance Impact**: Executing analytics on operational systems may interfere with their functioning.