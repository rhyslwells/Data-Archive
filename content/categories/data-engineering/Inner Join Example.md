---
aliases: []
category: DE
date modified: 11-03-2026
tags:
  - data_modeling
  - joins
  - relational_model
  - sql
---

Consider a canonical one-to-many relationship:

* `customers` (one)
* `orders` (many)

Each customer can have multiple orders. The foreign key sits on the “many” side.

### Schema

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

Here:

* `customers.customer_id` is the primary key.
* `orders.customer_id` is a foreign key.
* Cardinality: one customer → many orders.

---

## Basic INNER JOIN

Return all customers who have at least one order, with their orders:

```sql
SELECT
    c.customer_id,
    c.name,
    o.order_id,
    o.order_date,
    o.amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;
```

### Behaviour

* Only customers with matching rows in `orders` are returned.
* Each customer appears once per order.
* If a customer has 3 orders, they appear in 3 rows.

---

## Example Result Shape

If: `customers`

| customer_id | name  |
| ----------- | ----- |
| 1           | Alice |
| 2           | Bob   |

`orders`

| order_id | customer_id | amount |
| -------- | ----------- | ------ |
| 101      | 1           | 50.00  |
| 102      | 1           | 75.00  |

Result:

| customer_id | name  | order_id | amount |
| ----------- | ----- | -------- | ------ |
| 1           | Alice | 101      | 50.00  |
| 1           | Alice | 102      | 75.00  |

Bob does not appear because `INNER JOIN` enforces matching rows on both sides.

## Aggregated Variant (Typical in Analytics)

If you want one row per customer:

```sql
SELECT
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS order_count,
    SUM(o.amount) AS total_spent
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.name;
```

This collapses the one-to-many join into a one-to-one result using aggregation.
