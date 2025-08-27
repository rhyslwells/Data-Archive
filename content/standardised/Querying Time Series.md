

[[Querying|Query]] patterns for time series data often use SQL constructs:

```
SELECT ...      -- Can include aggregate functions (e.g., SUM, AVG)
FROM ...
WHERE ...       -- Often uses BETWEEN for time ranges
ORDER BY ...
```

Common Query Patterns
* Compare periods: Analyze changes between two time ranges.
* Summarize windows: Compute aggregates for defined intervals (e.g., hourly, daily).
* [[granularity]] plays an important role in both.

Windowing Concepts

Sliding Window:
  * A continuous set of rows grouped by a specific [[granularity]].
  * The window slides by one row, creating overlapping windows.
  * Useful for monitoring changes over time. Think moving averages.

Tumbling Window:
  * Moves forward by the full window size (no overlap).
  * Often used for logical groupings of time (e.g., full days, weeks).

Performance & Optimization
* For older data or longer-range queries, use coarser granularity to improve performance.
* Use `EXPLAIN` or `ANALYZE` to optimize [[SQL]] queries.
