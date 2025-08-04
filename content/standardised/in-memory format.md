---
aliases: []
category: 
date modified: 1-08-2025
tags: [storage, system]
---
The term "in-memory format" refers to the way data is stored and managed directly in a ==computer's RAM== ([[Random Access Memory]]) rather than on disk storage like a hard drive or SSD. This approach is used to optimize performance, as accessing data in RAM is significantly faster than accessing data on disk.

In-memory formats are often used in applications that require high-speed data processing, such as real-time analytics, caching systems, and certain types of databases (e.g., in-memory databases like Redis or SAP HANA). By keeping data in memory, these systems can reduce latency and improve throughput, enabling faster data retrieval and processing.

In-memory formats may involve ==specific data structures== or serialization methods that are optimized for quick access and manipulation in RAM. These formats are designed to make efficient use of memory resources while ensuring that data can be quickly read and written by the application.

In-memory formats are optimized to:
- hit fast instruction sets 
- be cache friendly 
- be parallelizable

Formats:
- [Apache Arrow](term/apache%20arrow.md) 
- [Apache Spark](Apache%20Spark.md)
- [NumPy](term/numpy.md)
- [Pandas](term/pandas.md)

The opposed to in-memory formats are [Data Lake File Formats](Data%20Lake%20File%20Formats) which save space, be cross-language and serve as long-term storage. 


