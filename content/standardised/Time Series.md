---
aliases: []
category:
date modified: 1-08-2025
tags: [modeling]
---
Time series data is a sequence of data points collected or recorded at successive points in time, typically at uniform intervals. It captures the temporal ordering of data, which is crucial for analyzing trends, patterns, and changes over time.

Time series data is widely used across various domains, including:
- Finance: Stock prices, interest rates, and economic indicators.
- Weather Forecasting: Temperature, precipitation, and wind speed data.

In [[ML_Tools]] see: TimeSeries folder
- https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries"
## What Can You Do with Time Series Data?

With time series data, you can:

- [[Time Series Forecasting]]
- [[Time Series Identify Trends and Patterns]]
- [[Anomaly Detection]]

```python
# We set the 'day' column as the index to facilitate time-series operations.
df.set_index('day', inplace=True)
print(df)
```

## Notes from Linkedin Course | Advanced SQL for Data Science: Time Series

Use of [[SQL]] adnd [[PostgreSQL]]

analysis patterns

[[Views]], [[SQL Joins]]

times series have timestamps, with measurments
differnt types use differnt frequencies
What is the unit of measurements of a field (cm,$,ect)
Metric types: counter monotonically increase, Guage (goes up ofr down), summarycalculation over a period

types of timestamps
event time; when it occured
ingestion time: recieved

Focus on times series in [[Relational Database]]

Examples monitoring, stocks ect 

timeseries data is long column, need to partition the data set be period i.e month.
We do that is we want to query periods aggregates. looking at the most recent data

query pattens 
- compare periods 
- sumamrise a given window

[[granularity]]

For older data we may want tlarger [[granularity]]. Longer range problems

use EXPALIN or ANALYZE for [[SQL]] quesries

why cant i oven the browser in pgadmin ?

[[Querying|Query]]: 

SELECT (can apply aggregate functions)
FROM
WHERE (BETWENN)
ORDER

Sliding windows: a set of continous rows [[granularity]] that slides by a row, when monitoring change over time, with overlap in windows. Tumbling window: donw slide one , but move by the windows width so no overlap used when there is a logical grouping of period.

Can join timeseries by timestampl getting more metrics, or appends to longer time period. [[granularity]] matters when joining.
Clock Skew?
solved by truncating the time to remove precision
Want one row per time period

pgadmin form

[pgAdmin Tutorial - How to Use pgAdmin](https://www.youtube.com/@DatabaseStar)

You can generate [[ER Diagrams]] in [[PostgreSQL]] / pgadmin 
These are different

combining reference data with time data. Demonramlising, doing a join once, then can query it, like a view. faster querying



Windows changing permissions of folders for pgadmin access

If you are using Windows, the following steps should set the permissions:


1. Right click the folder containing the file and select Properties
2. Select the Security tab
3. Click the Edit button
4. Click Add...
5. Enter everyone in the text box
6. Click Check names (the word Everyone should now be underlined)
7. Click OK
8. With the Everyone item selected in the Group or user names box, select all the checkboxes in the Allow column
9. Click Apply
10. Click Apply again
