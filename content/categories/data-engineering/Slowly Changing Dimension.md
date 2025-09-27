---
aliases:
- SCD
category: DE
date modified: 27-09-2025
tags:
- database
---
A Slowly Changing Dimension (SCD) is **a dimension that stores and manages both current and historical data over time in a [Data Warehouse](Data%20Warehouse.md)**.

It is considered and implemented as one of the most critical [[ETL]] tasks in tracking the history of dimension records.
## How do you track slowly changing dimensions in a [[Database]]

Take a customer dimension in a retail database.

Consider a retail company that tracks customer information, including attributes such as name, address, and membership status. Over time, customers may change their addresses or upgrade their membership levels. 
#### Implementation of SCD

- The original record for John Doe is retained with an end date to indicate that it is no longer current.
- A new record is created for the updated information, allowing the company to maintain a history of changes over time.
- This approach allows analysts to query the data and understand customer behavior and trends over time, which is essential for reporting and decision-making.

1. **Current Data**: The current state of the customer dimension might look like this:

| Customer ID | Name       | Address               | Membership Status |
|-------------|------------|-----------------------|--------------------|
| 1           | John Doe  | 123 Elm St, City A    | Gold               |
| 2           | Jane Smith | 456 Oak St, City B    | Silver             

1. **Change Occurs**: If John Doe moves to a new address and upgrades his membership to Platinum, the company needs to track this change.

2. **Historical Data**: Using the SCD approach, the [[Dimension Table]] might be updated as follows:

| Customer ID | Name       | Address               | Membership Status | Effective Date | End Date   |
|-------------|------------|-----------------------|--------------------|----------------|------------|
| 1           | John Doe  | 123 Elm St, City A    | Gold               | 2022-01-01     | 2023-10-01 |
| 1           | John Doe  | 789 Pine St, City A   | Platinum           | 2023-10-01     | NULL       |
| 2           | Jane Smith | 456 Oak St, City B    | Silver             | 2022-01-01     | NULL       |
