Large scale data processing

Written in Rust

Similar to Pandas

Polars API is strict

Polars uses slice instead of loc and iloc in pandas

Polars vs Pandas:

- **Pandas**: Mature tool with a large community, wide range of features, and seamless integration with other Python libraries. However, it can be slow and memory-intensive with large datasets.
- **Polars**: Designed for speed and memory efficiency, especially with large datasets. It uses Rust for performance and supports lazy evaluation for optimized query execution. It has a modern API similar to Pandas but is still growing in terms of features and library integration.
- **Usage Recommendations**: Use Pandas for smaller datasets and when you need extensive functionality and integration. Opt for Polars when working with large datasets and performance is crucial. Both libraries can be used together in different parts of your data science workflows.